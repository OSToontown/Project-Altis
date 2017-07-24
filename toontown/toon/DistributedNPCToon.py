from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from toontown.toon.DistributedNPCToonBase import *
from direct.task.Task import Task
from toontown.chat.ChatGlobals import *
from toontown.hood import ZoneUtil
from toontown.nametag.NametagGlobals import *
from toontown.quest import QuestChoiceGui
from toontown.quest import QuestParser
from toontown.quest import TrackChoiceGui
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TeaserPanel

ChoiceTimeout = 20
AVAILABLE_QUEST = 0
QUESTS_FULL = 1
COMPLETED_QUEST = 2
INCOMPLETE_QUEST = 3

class DistributedNPCToon(DistributedNPCToonBase):
    
    def __init__(self, cr):
        DistributedNPCToonBase.__init__(self, cr)

        self.curQuestMovie = None
        self.questChoiceGui = None
        self.trackChoiceGui = None
        self.icon = None
        self.npcType = 'Shopkeeper'
        self.questNotifyTypes = [base.loader.loadModel('phase_3/models/gui/quest_exclaim.bam'), base.loader.loadModel('phase_3/models/gui/quest_exclaim_silver.bam'), base.loader.loadModel('phase_3/models/gui/quest_question.bam'), base.loader.loadModel('phase_3/models/gui/quest_question_silver.bam')]
        for icon in self.questNotifyTypes:
            icon.setScale(4)
            icon.setZ(3)
        self.beginCheckTask()

    def allowedToTalk(self):
        return True

    def delayDelete(self):
        DistributedNPCToonBase.delayDelete(self)

        if self.curQuestMovie:
            curQuestMovie = self.curQuestMovie
            self.curQuestMovie = None
            curQuestMovie.timeout(fFinish=1)
            curQuestMovie.cleanup()

    def disable(self):
        self.cleanupMovie()
        taskMgr.remove('update-quests')

        DistributedNPCToonBase.disable(self)

    def cleanupMovie(self):
        self.clearChat()
        self.ignore('chooseQuest')
        if self.questChoiceGui:
            self.questChoiceGui.destroy()
            self.questChoiceGui = None
        self.ignore(self.uniqueName('doneChatPage'))
        if self.curQuestMovie:
            self.curQuestMovie.timeout(fFinish=1)
            self.curQuestMovie.cleanup()
            self.curQuestMovie = None
        if self.trackChoiceGui:
            self.trackChoiceGui.destroy()
            self.trackChoiceGui = None

    def handleCollisionSphereEnter(self, collEntry):
        base.cr.playGame.getPlace().fsm.request('quest', [self])
        self.sendUpdate('avatarEnter', [])
        self.nametag3d.setDepthTest(0)
        self.nametag3d.setBin('fixed', 0)

    def handleOkTeaser(self):
        self.dialog.destroy()
        del self.dialog
        place = base.cr.playGame.getPlace()
        if place:
            place.fsm.request('walk')

    def finishMovie(self, av, isLocalToon, elapsedTime):
        self.cleanupMovie()
        av.startLookAround()
        self.startLookAround()
        self.detectAvatars()
        self.initPos()
        if isLocalToon:
            self.showNametag2d()
            taskMgr.remove(self.uniqueName('lerpCamera'))
            self.returnCamera()
            self.sendUpdate('setMovieDone', [])
            self.nametag3d.clearDepthTest()
            self.nametag3d.clearBin()
            
    def returnCamera(self):
        avHeight = max(base.localAvatar.getHeight(), 3.0)
        scaleFactor = avHeight * 0.3333333333
        camera.wrtReparentTo(base.localAvatar)
        camera.posQuatInterval(1, (0, -9 * scaleFactor, avHeight), (0, 0, 0), other=base.localAvatar, blendType='easeInOut').start()
        def walk():
            base.cr.playGame.getPlace().setState('walk')
        Sequence(Wait(1), Func(walk)).start()
        
    def setupCamera(self, mode):
        camera.wrtReparentTo(render)
        if mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE or mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE:
            camera.posQuatInterval(1, (5, 9, self.getHeight() - 0.5), (155, -2, 0), other=self, blendType='easeInOut').start()
        else:
            camera.posQuatInterval(1, (-5, 9, self.getHeight() - 0.5), (-150, -2, 0), other=self, blendType='easeInOut').start()

    def setMovie(self, mode, npcId, avId, quests, timestamp):
        isLocalToon = avId == base.localAvatar.doId
        if mode == NPCToons.QUEST_MOVIE_CLEAR:
            self.cleanupMovie()
            if isLocalToon:
                self.returnCamera()
            return
        if mode == NPCToons.QUEST_MOVIE_TIMEOUT:
            self.cleanupMovie()
            if isLocalToon:
                self.returnCamera()
            self.setPageNumber(0, -1)
            self.clearChat()
            self.startLookAround()
            self.detectAvatars()
            return
        av = base.cr.doId2do.get(avId)
        if av is None:
            self.notify.warning('Avatar %d not found in doId' % avId)
            return
        if mode == NPCToons.QUEST_MOVIE_REJECT:
            rejectString = Quests.chooseQuestDialogReject()
            rejectString = Quests.fillInQuestNames(rejectString, avName=av.name)
            self.setChatAbsolute(rejectString, CFSpeech | CFTimeout)
            if isLocalToon:
                base.localAvatar.posCamera(0, 0)
                base.cr.playGame.getPlace().setState('walk')
            return
        if mode == NPCToons.QUEST_MOVIE_TIER_NOT_DONE:
            rejectString = Quests.chooseQuestDialogTierNotDone()
            rejectString = Quests.fillInQuestNames(rejectString, avName=av.name)
            self.setChatAbsolute(rejectString, CFSpeech | CFTimeout)
            if isLocalToon:
                base.localAvatar.posCamera(0, 0)
                base.cr.playGame.getPlace().setState('walk')
            return
        self.setupAvatars(av)
        fullString = ''
        toNpcId = None
        if isLocalToon:
            self.hideNametag2d()
        if mode == NPCToons.QUEST_MOVIE_COMPLETE:
            questId, rewardId, toNpcId = quests
            scriptId = 'quest_complete_' + str(questId)
            if QuestParser.questDefined(scriptId):
                self.curQuestMovie = QuestParser.NPCMoviePlayer(scriptId, av, self)
                self.curQuestMovie.play()
                return
            if isLocalToon:
                self.setupCamera(mode)
            greetingString = Quests.chooseQuestDialog(questId, Quests.GREETING)
            if greetingString:
                fullString += greetingString + '\x07'
            fullString += Quests.chooseQuestDialog(questId, Quests.COMPLETE) + '\x07'
            if rewardId > 2:
                fullString += Quests.getReward(rewardId).getString()
            quest = Quests.QuestDict.get(questId)
            experience = quest[Quests.QuestDictExperienceIndex]
            money = quest[Quests.QuestDictMoneyIndex]
            fullString += TTLocalizer.QuestMovieExpJbReward % {'exp': experience, 'money': money}
            leavingString = Quests.chooseQuestDialog(questId, Quests.LEAVING)
            if leavingString:
                fullString += '\x07' + leavingString
        elif mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE_CANCEL:
            fullString = TTLocalizer.QuestMovieQuestChoiceCancel
        elif mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE_CANCEL:
            fullString = TTLocalizer.QuestMovieTrackChoiceCancel
        elif mode == NPCToons.QUEST_MOVIE_INCOMPLETE:
            questId, completeStatus, toNpcId = quests
            scriptId = 'quest_incomplete_' + str(questId)
            if QuestParser.questDefined(scriptId):
                if self.curQuestMovie:
                    self.curQuestMovie.timeout()
                    self.curQuestMovie.cleanup()
                    self.curQuestMovie = None
                self.curQuestMovie = QuestParser.NPCMoviePlayer(scriptId, av, self)
                self.curQuestMovie.play()
                return
            if isLocalToon:
                self.setupCamera(mode)
            greetingString = Quests.chooseQuestDialog(questId, Quests.GREETING)
            if greetingString:
                fullString += greetingString + '\x07'
            fullString += Quests.chooseQuestDialog(questId, completeStatus)
            leavingString = Quests.chooseQuestDialog(questId, Quests.LEAVING)
            if leavingString:
                fullString += '\x07' + leavingString
        elif mode == NPCToons.QUEST_MOVIE_ASSIGN:
            questId, rewardId, toNpcId = quests
            scriptId = 'quest_assign_' + str(questId)
            if QuestParser.questDefined(scriptId):
                if self.curQuestMovie:
                    self.curQuestMovie.timeout()
                    self.curQuestMovie.cleanup()
                    self.curQuestMovie = None
                self.curQuestMovie = QuestParser.NPCMoviePlayer(scriptId, av, self)
                self.curQuestMovie.play()
                return
            if isLocalToon:
                self.setupCamera(mode)
            fullString += Quests.chooseQuestDialog(questId, Quests.QUEST)
            leavingString = Quests.chooseQuestDialog(questId, Quests.LEAVING)
            if leavingString:
                fullString += '\x07' + leavingString
        elif mode == NPCToons.QUEST_MOVIE_QUEST_CHOICE:
            if isLocalToon:
                self.setupCamera(mode)
            self.setChatAbsolute(TTLocalizer.QuestMovieQuestChoice, CFSpeech)
            if isLocalToon:
                self.acceptOnce('chooseQuest', self.sendChooseQuest)
                self.questChoiceGui = QuestChoiceGui.QuestChoiceGui()
                self.questChoiceGui.setQuests(quests, npcId, ChoiceTimeout)
            return
        elif mode == NPCToons.QUEST_MOVIE_TRACK_CHOICE:
            if isLocalToon:
                self.setupCamera(mode)
            tracks = quests
            self.setChatAbsolute(TTLocalizer.QuestMovieTrackChoice, CFSpeech)
            if isLocalToon:
                self.acceptOnce('chooseTrack', self.sendChooseTrack)
                self.trackChoiceGui = TrackChoiceGui.TrackChoiceGui(tracks, ChoiceTimeout)
            return
        fullString = Quests.fillInQuestNames(fullString, avName=av.name, fromNpcId=npcId, toNpcId=toNpcId)
        self.acceptOnce(self.uniqueName('doneChatPage'), self.finishMovie, extraArgs=[av, isLocalToon])
        self.clearChat()
        self.setPageChat(avId, 0, fullString, 1)

    def sendChooseQuest(self, questId):
        if self.questChoiceGui:
            self.questChoiceGui.destroy()
            self.questChoiceGui = None
        self.sendUpdate('chooseQuest', [questId])

    def sendChooseTrack(self, trackId):
        if self.trackChoiceGui:
            self.trackChoiceGui.destroy()
            self.trackChoiceGui = None
        self.sendUpdate('chooseTrack', [trackId])
		
    def checkQuestStatus(self):
        av = base.localAvatar
        retVal = self.hasQuests()
        if retVal is not None:
            self.setQuestNotify(retVal)
        elif self.checkCompletedQuests():
            self.setQuestNotify(COMPLETED_QUEST)
        elif self.checkIncompletedQuests():
            self.setQuestNotify(INCOMPLETE_QUEST)
        else:
            self.setQuestNotify(None)
			
    def setQuestNotify(self, type):
        try:
            if type is None:
                if self.icon:
                    self.icon.detachNode()
                    del self.icon
                return
            if self.icon:
                self.icon.detachNode()
                self.icon = None
            self.icon = self.questNotifyTypes[type]
            np = NodePath(self.nametag.getIcon())
            if np.isEmpty():
                return
            self.icon.reparentTo(np)
        except:
            pass
		
    def hasQuests(self):
        potentialQuests = []
        nyaQuests = []
        av = base.localAvatar
        for quest in Quests.QuestDict.keys():
            questEntry = Quests.QuestDict.get(quest)
            if NPCToons.getNPCName(questEntry[Quests.QuestDictFromNpcIndex]) == self.getName():
                if questEntry[1] == Quests.Start:
                    potentialQuests.append(quest)
        for quest in potentialQuests:
            questEntry = Quests.QuestDict.get(quest)
            if quest in av.getQuestHistory():
                if quest in potentialQuests:
                    potentialQuests.remove(quest)
            for needed in questEntry[0]:
                if not needed in av.getQuestHistory():
                    nyaQuests.append(quest)
                    if quest in potentialQuests:
                        potentialQuests.remove(quest)
        if len(potentialQuests) > 0:
            return AVAILABLE_QUEST
        elif len(nyaQuests) > 0 and len(potentialQuests) == 0:
            return QUESTS_FULL
        else:
            return None
		
    def checkCompletedQuests(self):
        av = base.localAvatar
        for quest in av.quests:
            questId, fromNpcId, toNpcId, rewardId, toonProgress = quest
            newQuest = tuple(quest)
            actualQuest = Quests.getQuest(questId)
            fComplete = actualQuest.getCompletionStatus(av, newQuest) == Quests.COMPLETE
            name = self.getName()
            if fComplete:
                questId, fromNpcId, toNpcId, rewardId, toonProgress = quest
                entry = NPCToons.NPCToonDict.get(toNpcId)
                if entry[1] == name:
                    return True
        return False
		
    def checkIncompletedQuests(self):
        av = base.localAvatar
        for quest in av.quests:
            questId, fromNpcId, toNpcId, rewardId, toonProgress = quest
            newQuest = tuple(quest)
            actualQuest = Quests.getQuest(questId)
            fIncomplete = actualQuest.getCompletionStatus(av, newQuest) == Quests.INCOMPLETE
            name = self.getName()
            if fIncomplete:
                questId, fromNpcId, toNpcId, rewardId, toonProgress = quest
                entry = NPCToons.NPCToonDict.get(toNpcId)
                if entry[1] == name:
                    return True
        return False
		
		
    def beginCheckTask(self):
        taskMgr.doMethodLater(1, self.__updateQuest, 'update-quests')
		
    def __updateQuest(self, task):
        self.checkQuestStatus()
        taskMgr.doMethodLater(1, self.__updateQuest, 'update-quests')
        return Task.done
        
