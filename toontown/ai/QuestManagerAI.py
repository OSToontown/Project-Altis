from toontown.toon.DistributedNPCSpecialQuestGiverAI import DistributedNPCSpecialQuestGiverAI
from toontown.building import FADoorCodes
from otp.ai.MagicWordGlobal import *
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.quest import Quests

QuestIdIndex = 0
QuestFromNpcIdIndex = 1
QuestToNpcIdIndex = 2
QuestRewardIdIndex = 3
QuestProgressIndex = 4

class QuestManagerAI:
    notify = directNotify.newCategory('QuestManagerAI')

    def __init__(self, air):
        self.air = air

    def __toonQuestsList2Quests(self, quests):
        return [Quests.getQuest(x[0]) for x in quests]

    def __incrementQuestProgress(self, quest):
        """
        Increment the supplied quest's progress by 1.
        """
        quest[4] += 1

    def requestInteract(self, avId, npc):
        # Get the avatar.
        av = self.air.doId2do.get(avId)
        if not av:
            return

        history = av.getQuestHistory()
        avQuestPocketSize = av.getQuestCarryLimit()
        avQuests = av.getQuests()

        fakeTier = 0

        avTrackProgress = av.getTrackProgress()

        # Iterate through their quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i:i + 5]
            questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
            questClass = Quests.getQuest(questId)
            if questClass:
                completeStatus = questClass.getCompletionStatus(av, questDesc, npc)
            else:
                continue

            # If the quest is a DeliverGagQuest, add the gags.
            if isinstance(questClass, Quests.DeliverGagQuest):
                # Check if it's the required NPC.
                if npc.npcId == toNpcId:
                    track, level = questClass.getGagType()
                    currItems = av.inventory.numItem(track, level)
                    if currItems >= questClass.getNumGags():
                        av.inventory.setItem(track, level, av.inventory.numItem(track, level) - questClass.getNumGags())
                    else:
                        npc.rejectAvatar(avId)
                    av.b_setInventory(av.inventory.makeNetString())

            # If they've completed a quest.
            if completeStatus == Quests.COMPLETE:
                # ToonUp the toon to max health.
                av.toonUp(av.maxHp)

                # If it's a TrackChoiceQuest then present their track choices.
                if isinstance(questClass, Quests.TrackChoiceQuest):
                    npc.presentTrackChoice(avId, questId, [0,1,2,3,4,5,6,7])
                    break
                # If there is another part to this quest then give them that.
                if Quests.getNextQuest(questId, npc, av)[0] != Quests.NA:
                    self.nextQuest(av, npc, questId)
                    if int(avId) in self.air.tutorialManager.avId2fsm:
                        self.air.tutorialManager.avId2fsm[int(avId)].demand('Tunnel')
                    break
                else:
                    # The toon has completed this quest. Give them a reward!
                    npc.completeQuest(avId, questId, rewardId)
                    self.completeQuest(av, questId)
                break
        else:
            # They haven't completed any quests so we have to give them choices.
            # If they've got a full pouch then reject them.
            if (len(avQuests) == avQuestPocketSize*5):
                npc.rejectAvatar(avId)
                return
            elif isinstance(npc, DistributedNPCSpecialQuestGiverAI):
                # Don't display choices. Force a choice.
                self.tutorialQuestChoice(avId, npc)
                return
            else:
                #Present quest choices.
                choices = self.avatarQuestChoice(av, npc)
                if choices != []:
                    for choice in choices:
                        questClass = Quests.QuestDict.get(choice[0])
                        for required in questClass[0]:
                            if required not in history:
                                if len(choices) == 1:
                                    choices = []
                                else:
                                    if choice in choices:
                                        choices.remove(choice)
                            else:
                                continue
                    if choices != []:
                        npc.presentQuestChoice(avId, choices)
                    else:
                        npc.rejectAvatar(avId)
                else:
                    npc.rejectAvatar(avId)

    def npcGiveTrackChoice(self, av, tier):
        trackQuest = Quests.chooseTrackChoiceQuest(tier, av)
        return [(trackQuest, 400, Quests.ToonHQ)]

    def avatarQuestChoice(self, av, npc):
        # Get the best quests for an avatar/npc.
        return Quests.chooseBestQuests(npc, av)

    def avatarChoseQuest(self, avId, npc, questId, rewardId, toNpcId):
        # Get the avatar.
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if len(av.quests) > av.getQuestCarryLimit():
            return

        # Get the npcIds
        fromNpcId = npc.npcId
        if toNpcId == 0:
            toNpcId = Quests.getQuestToNpcId(questId)

        # Add the quest to the avatars list.
        transformedRewardId = Quests.transformReward(rewardId, av)
        av.addQuest([questId, fromNpcId, toNpcId, rewardId, 0], transformedRewardId)

        # Remove the tasks for timeout.
        taskMgr.remove(npc.uniqueName('clearMovie'))

        # Assign the quest.
        npc.assignQuest(avId, questId, rewardId, toNpcId)

    def avatarChoseTrack(self, avId, npc, pendingTrackQuest, trackId):
        # Get the avatar.
        av = self.air.doId2do.get(avId)
        if not av:
            return

        # Remove the tasks for timeout.
        taskMgr.remove(npc.uniqueName('clearMovie'))

        # Show the completion movie and remove the task.
        npc.completeQuest(avId, pendingTrackQuest, Quests.getRewardIdFromTrackId(trackId))
        self.completeQuest(av, pendingTrackQuest)

        # Set their track their working on.
        av.b_setTrackProgress(trackId, 0)

    def avatarCancelled(self, npcId):
        # Get the NPC.
        npc = self.air.doId2do.get(npcId)
        if not npc:
            return

        # Remove the task for timeout.
        taskMgr.remove(npc.uniqueName('clearMovie'))

    def nextQuest(self, av, npc, questId):
        # Get the next QuestId and toNpcId.
        nextQuestId, toNpcId = Quests.getNextQuest(questId, npc, av)

        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i:i + 5]

            if questDesc[QuestIdIndex] == questId:
                questDesc[QuestIdIndex] = nextQuestId
                questDesc[QuestToNpcIdIndex] = toNpcId
                questDesc[QuestProgressIndex] = 0
            questList.append(questDesc)

        # Show the quest movie and set their quests.
        npc.incompleteQuest(av.doId, nextQuestId, Quests.QUEST, toNpcId)
        av.b_setQuests(questList)

    def completeQuest(self, av, completeQuestId):
        #Get the avatars current quests.
        avQuests = av.getQuests()

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i:i + 5]
            questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
            questClass = Quests.getQuest(questId)
            questExp = Quests.getQuestExp(questId)
            questMoney = Quests.getQuestMoney(questId)
            rewardId = Quests.getQuestRewardId(questId)

            if questId == completeQuestId:
                av.removeQuest(questId)
                self.giveReward(av, questId, rewardId)
                if questExp != 0:
                    av.b_setToonExp(av.getToonExp() + questExp)
                if questMoney != 0:
                    av.addMoney(questMoney)
                av.addStat(ToontownGlobals.STATS_TASKS)
                av.addToQuestHistory(questId)

                break

    def giveReward(self, av, questId, rewardId):
        # Give the reward.
        rewardClass = Quests.getReward(rewardId)
        if rewardClass is None or rewardId < 100:
            self.notify.warning('rewardClass was None for rewardId: %s.' % rewardId)
        else:
            rewardClass.sendRewardAI(av)

    def tutorialQuestChoice(self, avId, npc):
        # Get the avatar.
        av = self.air.doId2do.get(avId)
        if not av:
            return

        # Get the possible quest choices and force the player to choose it.
        choices = self.avatarQuestChoice(av, npc)
        if len(choices) == 0:
            npc.rejectAvatar(avId)
            return
        quest = choices[0]

        self.avatarChoseQuest(avId, npc, quest[0], quest[1], 0)

        # Are we in the tutorial speaking to Tutorial Tom?
        if int(avId) in self.air.tutorialManager.avId2fsm:
            self.air.tutorialManager.avId2fsm[int(avId)].demand('Battle')

    def toonRodeTrolleyFirstTime(self, av):
        # Toon played a minigame.
        self.toonPlayedMinigame(av, [])

    def toonPlayedMinigame(self, av, toons):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.TrolleyQuest):
                questDesc[QuestProgressIndex] = 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonMadeFriend(self, avId):
        # Get the avatar.
        av = self.air.doId2do.get(avId)
        if not av:
            return

        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.FriendQuest):
                questDesc[QuestProgressIndex] = 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonUsedPhone(self, avId):
        # Get the avatar.
        av = self.air.doId2do.get(avId)
        if not av:
            return

        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.PhoneQuest):
                questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonCaughtFishingItem(self, av):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        fishingItem = -1
        questList = []

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if fishingItem != -1:
                questList.append(questDesc)
                continue
            if isinstance(questClass, Quests.RecoverItemQuest):
                if not hasattr(questClass, 'getItem'):
                    questList.append(questDesc)
                    continue
                if questClass.getHolder() == Quests.AnyFish:
                    if not questClass.getCompletionStatus(av, questDesc) == Quests.COMPLETE:
                        baseChance = questClass.getPercentChance()
                        amountRemaining = questClass.getNumItems() - questDesc[QuestProgressIndex]
                        chance = Quests.calcRecoverChance(amountRemaining, baseChance)
                        if chance >= baseChance:
                            questDesc[QuestProgressIndex] += 1
                            fishingItem = questClass.getItem()
            questList.append(questDesc)

        av.b_setQuests(questList)
        return fishingItem

    def hasTailorClothingTicket(self, av, npc):
        # Get the avatars current quests.
        avQuests = av.getQuests()

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.DeliverItemQuest):
                if questClass.getCompletionStatus(av, questDesc, npc) == Quests.COMPLETE:
                    # They have a clothing ticket.
                    return 1
        return 0

    def removeClothingTicket(self, av, npc):
        # Get the avatars current quests.
        avQuests = av.getQuests()

        # Iterate through their current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.DeliverItemQuest):
                if questClass.getCompletionStatus(av, questDesc, npc) == Quests.COMPLETE:
                    av.removeQuest(questDesc[QuestIdIndex])
                    break

    def recoverItems(self, toon, suitsKilled, zoneId):
        """
        Called in battleExperience to alert the quest system that a toon should
        test for recovered items.

        Returns a tuple of two lists:
            Index 0: a list of recovered items.
            Index 1: a list of unrecovered items.
        """
        recovered, notRecovered = ([] for i in xrange(2))
        for index, quest in enumerate(self.__toonQuestsList2Quests(toon.quests)):
            if isinstance(quest, Quests.RecoverItemQuest):
                isComplete = quest.getCompletionStatus(toon, toon.quests[index])
                if isComplete == Quests.COMPLETE:
                    # This quest is complete, skip.
                    continue
                # It's a quest where we need to recover an item!
                if quest.isLocationMatch(zoneId):
                    # We're in the correct area to recover the item, woo!
                    if quest.getHolder() == Quests.Any or quest.getHolderType() in ['type', 'track', 'level']:
                        for suit in suitsKilled:
                            if quest.getCompletionStatus(toon, toon.quests[index]) == Quests.COMPLETE:
                                # Test if the task has already been completed.
                                # If it has, we don't need to iterate through the cogs anymore.
                                break
                            # Here comes the long IF statement...
                            if (quest.getHolder() == Quests.Any) \
                            or (quest.getHolderType() == 'type' and quest.getHolder() == suit['type']) \
                            or (quest.getHolderType() == 'track' and quest.getHolder() == suit['track']) \
                            or (quest.getHolderType() == 'level' and quest.getHolder() <= suit['level']):
                                progress = toon.quests[index][4] & pow(2, 16) - 1 # This seems to be the Disne
                                completion = quest.testRecover(progress)
                                if completion[0]:
                                    # We win! We got the item from the cogs. :)
                                    recovered.append(quest.getItem())
                                    self.__incrementQuestProgress(toon.quests[index])
                                else:
                                    # Tough luck, maybe next time.
                                    notRecovered.append(quest.getItem())
        toon.d_setQuests(toon.getQuests())
        return (recovered, notRecovered)

    def toonKilledBuilding(self, av, type, difficulty, floors, zoneId, activeToons):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []
        zoneId = ZoneUtil.getBranchZone(zoneId)

        # Iterate through the avatars current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if questClass.getCompletionStatus(av, questDesc) == Quests.INCOMPLETE:
                if isinstance(questClass, Quests.BuildingQuest):
                    if questClass.isLocationMatch(zoneId):
                        if questClass.doesBuildingTypeCount(type):
                            if questClass.doesBuildingCount(av, activeToons):
                                if floors >= questClass.getNumFloors():
                                    questDesc[QuestProgressIndex] += 1

            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonKilledCogdo(self, av, type, difficulty, zoneId, activeToons):
        self.notify.debug("toonKilledCogdo(%s, '%s', %s, %d, %s)" % (str(av), type, str(difficulty), zoneId, str(activeToons)))
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []
        zoneId = ZoneUtil.getBranchZone(zoneId)

        # Iterate through the avatars current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if questClass.getCompletionStatus(av, questDesc) == Quests.INCOMPLETE:
                if isinstance(questClass, Quests.CogdoQuest):
                    if questClass.isLocationMatch(zoneId):
                        if questClass.doesCogdoTypeCount(type):
                            if questClass.doesCogdoCount(av, activeToons):
                                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonCollectedExp(self, av, expArray):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through the avatars current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.TrackExpQuest):
                if questClass.doesExpCount(av, expArray):
                    questDesc[QuestProgressIndex] += expArray[questClass.getTrackType()]
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonDefeatedFactory(self, av, factoryId, activeVictors):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through the avatars current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.FactoryQuest):
                if questClass.doesFactoryCount(av, factoryId, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonDefeatedMint(self, av, mintId, activeVictors):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []

        # Iterate through the avatars current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.MintQuest):
                if questClass.doesMintCount(av, mintId, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonDefeatedStage(self, av, stageId, activeVictors):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.StageQuest):
                if questClass.doesStageCount(av, stageId, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonDefeatedCountryClub(self, av, clubId, activeVictors):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.ClubQuest):
                if questClass.doesClubCount(av, clubId, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)
		
    def toonDefeatedBoss(self, av, zone, dept, activeVictors):
        # Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.VPQuest):
                if questClass.doesVPCount(av, dept, zone, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            elif isinstance(questClass, Quests.CFOQuest):
                if questClass.doesCFOCount(av, dept, zone, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            elif isinstance(questClass, Quests.CJQuest):
                if questClass.doesCJCount(av, dept, zone, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            elif isinstance(questClass, Quests.CEOQuest):
                if questClass.doesCEOCount(av, dept, zone, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)

    def toonDefeatedBoardOffice(self, av, clubId, activeVictors):
        '''# Get the avatars current quests.
        avQuests = av.getQuests()
        questList = []
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])
            if isinstance(questClass, Quests.ClubQuest):
                if questClass.doesClubCount(av, clubId, activeVictors):
                    questDesc[QuestProgressIndex] += 1
            questList.append(questDesc)

        av.b_setQuests(questList)'''
        pass

    def toonKilledCogs(self, av, suitsKilled, zoneId, activeToonList):
        # Get the avatar's current quests.
        avQuests = av.getQuests()
        questList = []

        # Make a list of the activeToonDoIds
        activeToonDoIds = [toon.doId for toon in activeToonList if not None]

        # Iterate through the avatar's current quests.
        for i in xrange(0, len(avQuests), 5):
            questDesc = avQuests[i : i + 5]
            questClass = Quests.getQuest(questDesc[QuestIdIndex])

            # Check if they are doing a cog quest
            if isinstance(questClass, Quests.CogQuest) and not (isinstance(questClass, Quests.VPQuest) or isinstance(questClass, Quests.CFOQuest) or isinstance(questClass, Quests.CJQuest) or isinstance(questClass, Quests.CEOQuest)):

                # Check if the cog counts...
                for suit in suitsKilled:
                    if questClass.doesCogCount(av.doId, suit, zoneId, activeToonList):

                        # Looks like the cog counts!
                        if questClass.getCompletionStatus(av, questDesc) != Quests.COMPLETE:
                            questDesc[QuestProgressIndex] += 1

            # Add the quest to the questList
            questList.append(questDesc)

        # Update the avatar's quests
        av.b_setQuests(questList)


@magicWord(category=CATEGORY_PROGRAMMER, types=[str, int, int])
def quests(command, arg0=0, arg1=0):
    invoker = spellbook.getTarget()
    currQuests = invoker.getQuests()
    currentQuestIds = []

    for i in xrange(0, len(currQuests), 5):
        currentQuestIds.append(currQuests[i])

    pocketSize = invoker.getQuestCarryLimit()
    carrying = len(currQuests) / 5
    canCarry = False

    if (carrying < pocketSize):
        canCarry = True

    if command == 'clear':
        invoker.b_setQuests([])
        return 'Cleared quests'
    elif command == 'clearHistory':
        invoker.d_setQuestHistory([])
        return 'Cleared quests history'
    elif command == 'add':
        if arg0:
            if canCarry:
                if arg0 in Quests.QuestDict.keys():
                    quest = Quests.getQuest(arg0)
                    invoker.addQuest(quest, 0)
                    return 'Added QuestID %s'%(arg0)
                else:
                    return 'Invalid QuestID %s'%(arg0)
            else:
                return 'Cannot take anymore quests'
        else:
            return 'add needs 1 argument.'
    elif command == 'remove':
        if arg0:
            if arg0 in currentQuestIds:
                invoker.removeQuest(arg0)
                return 'Removed QuestID %s'%(arg0)
            elif arg0 < pocketSize and arg0 > 0:
                if len(currentQuestIds) <= arg0:
                    questIdToRemove = currentQuestIds[arg0 - 1]
                    invoker.removeQuest(questIdToRemove)
                    return 'Removed quest from slot %s'%(arg0)
                else:
                    return 'Invalid quest slot'
            else:
                return 'Cannot remove quest %s'%(arg0)
        else:
            return 'remove needs 1 argument.'
    elif command == 'list':
        if arg0:
            if arg0 > 0 and arg0 <= pocketSize:
                start = (arg0 -1) * 5
                questDesc = currQuests[start : start + 5]
                return 'QuestDesc in slot %s: %s.'%(arg0, questDesc)
            else:
                return 'Invalid quest slot %s.'%(arg0)
        else:
            return 'CurrentQuests: %s'%(currentQuestIds)
    elif command == 'bagSize':
        if arg0 > 0 and arg0 < 5:
            invoker.b_setQuestCarryLimit(arg0)
            return 'Set carry limit to %s'%(arg0)
        else:
            return 'Argument 0 must be between 1 and 4.'
    elif command == 'progress':
        if arg0 and arg1:
            if arg0 > 0 and arg0 <= pocketSize:
                questList = []
                wantedQuestId = currentQuestIds[arg0 - 1]

                for i in xrange(0, len(currQuests), 5):
                    questDesc = currQuests[i : i + 5]

                    if questDesc[0] == wantedQuestId:
                        questDesc[4] = arg1

                    questList.append(questDesc)

                invoker.b_setQuests(questList)
                return 'Set quest slot %s progress to %s'%(arg0, arg1)
            elif arg0 in Quests.QuestDict.keys():
                if arg0 in currentQuestIds:
                    questList = []

                    for i in xrange(0, len(currQuests), 5):
                        questDesc = currQuests[i : i + 5]

                        if questDesc[0] == arg0:
                            questDesc[4] = arg1

                        questList.append(questDesc)

                    invoker.b_setQuests(questList)
                    return 'Set QuestID %s progress to %s'%(arg0, arg1)
                else:
                    return 'Cannot progress QuestID: %s.'%(arg0)
            else:
                return 'Invalid quest or slot id'
        else:
            return 'progress needs 2 arguments.'
    elif command == 'getHistory':
        return invoker.getQuestHistory()
    elif command == 'addHistory':
        history = invoker.getQuestHistory()
        history.append(arg0)
        invoker.b_setQuestHistory(history)
        return "Added %s to quest history!" % arg0
    elif command == 'getQuests':
        return invoker.getQuests()
    else:
        return 'Invalid first argument.'
