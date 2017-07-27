from otp.otpbase import OTPGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import ToontownGlobals
from toontown.battle import SuitBattleGlobals
from toontown.coghq import CogDisguiseGlobals
import random
from toontown.toon import NPCToons
import copy, string
from toontown.hood import ZoneUtil
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToonPythonUtil as PythonUtil
import time, types, random
notify = DirectNotifyGlobal.directNotify.newCategory('Quests')
ItemDict = TTLocalizer.QuestsItemDict
CompleteString = TTLocalizer.QuestsCompleteString
NotChosenString = TTLocalizer.QuestsNotChosenString
DefaultGreeting = TTLocalizer.QuestsDefaultGreeting
DefaultIncomplete = TTLocalizer.QuestsDefaultIncomplete
DefaultIncompleteProgress = TTLocalizer.QuestsDefaultIncompleteProgress
DefaultIncompleteWrongNPC = TTLocalizer.QuestsDefaultIncompleteWrongNPC
DefaultComplete = TTLocalizer.QuestsDefaultComplete
DefaultLeaving = TTLocalizer.QuestsDefaultLeaving
DefaultReject = TTLocalizer.QuestsDefaultReject
DefaultTierNotDone = TTLocalizer.QuestsDefaultTierNotDone
DefaultQuest = TTLocalizer.QuestsDefaultQuest
DefaultVisitQuestDialog = TTLocalizer.QuestsDefaultVisitQuestDialog
GREETING = 0
QUEST = 1
INCOMPLETE = 2
INCOMPLETE_PROGRESS = 3
INCOMPLETE_WRONG_NPC = 4
COMPLETE = 5
LEAVING = 6
Any = 1
OBSOLETE = 'OBSOLETE'
Start = 1
Cont = 0
Anywhere = 1
NA = 2
Same = 3
AnyFish = 4
AnyCashbotSuitPart = 5
AnyLawbotSuitPart = 6
AnyBossbotSuitPart = 7
ToonTailor = 999
ToonHQ = 1000
QuestDictRequiredQuestsIndex = 0
QuestDictStartIndex = 1
QuestDictDescIndex = 2
QuestDictFromNpcIndex = 3
QuestDictToNpcIndex = 4
QuestDictRewardIndex = 5
QuestDictNextQuestIndex = 6
QuestDictDialogIndex = 7
QuestDictExperienceIndex = 8
QuestDictMoneyIndex = 9
VeryEasy = 100
ModeratelyEasy = 80
Easy = 75
Medium = 50
Hard = 25
VeryHard = 20
TT_TIER = 0
DD_TIER = 4
DG_TIER = 7
AA_TIER = 8
MM_TIER = 11
BR_TIER = 14
DL_TIER = 17
ELDER_TIER = 20 #For now
LOOPING_FINAL_TIER = 20 #For now
VISIT_QUEST_ID = 1000
TROLLEY_QUEST_ID = 110
FIRST_COG_QUEST_ID = 145
NEWBIE_HP = 25
SELLBOT_HQ_NEWBIE_HP = 50
CASHBOT_HQ_NEWBIE_HP = 85
from toontown.toonbase.ToontownGlobals import FT_FullSuit, FT_Leg, FT_Arm, FT_Torso
QuestRandGen = random.Random()

def seedRandomGen(npcId, avId, tier, rewardHistory):
    QuestRandGen.seed(npcId * 100 + avId + tier + len(rewardHistory))


def seededRandomChoice(seq):
    return QuestRandGen.choice(seq)


def getCompleteStatusWithNpc(questComplete, toNpcId, npc):
    if questComplete:
        if npc:
            if npcMatches(toNpcId, npc):
                return COMPLETE
            else:
                return INCOMPLETE_WRONG_NPC
        else:
            return COMPLETE
    elif npc:
        if npcMatches(toNpcId, npc):
            return INCOMPLETE_PROGRESS
        else:
            return INCOMPLETE
    else:
        return INCOMPLETE


def npcMatches(toNpcId, npc):
    return toNpcId == npc.getNpcId() or toNpcId == Any or toNpcId == ToonHQ and npc.getHq() or toNpcId == ToonTailor and npc.getTailor()


def calcRecoverChance(numberNotDone, baseChance, cap = 1):
    chance = baseChance
    avgNum2Kill = 1.0 / (chance / 100.0)
    if numberNotDone >= avgNum2Kill * 1.5 and cap:
        chance = 1000
    elif numberNotDone > avgNum2Kill * 0.5:
        diff = float(numberNotDone - avgNum2Kill * 0.5)
        luck = 1.0 + abs(diff / (avgNum2Kill * 0.5))
        chance *= luck
    return chance


def simulateRecoveryVar(numNeeded, baseChance, list = 0, cap = 1):
    numHave = 0
    numTries = 0
    greatestFailChain = 0
    currentFail = 0
    capHits = 0
    attemptList = {}
    while numHave < numNeeded:
        numTries += 1
        chance = calcRecoverChance(currentFail, baseChance, cap)
        test = random.random() * 100
        if chance == 1000:
            capHits += 1
        if test < chance:
            numHave += 1
            if currentFail > greatestFailChain:
                greatestFailChain = currentFail
            if attemptList.get(currentFail):
                attemptList[currentFail] += 1
            else:
                attemptList[currentFail] = 1
            currentFail = 0
        else:
            currentFail += 1

    print 'Test results: %s tries, %s longest failure chain, %s cap hits' % (numTries, greatestFailChain, capHits)
    if list:
        print 'failures for each succes %s' % attemptList


def simulateRecoveryFix(numNeeded, baseChance, list = 0):
    numHave = 0
    numTries = 0
    greatestFailChain = 0
    currentFail = 0
    attemptList = {}
    while numHave < numNeeded:
        numTries += 1
        chance = baseChance
        test = random.random() * 100
        if test < chance:
            numHave += 1
            if currentFail > greatestFailChain:
                greatestFailChain = currentFail
            if attemptList.get(currentFail):
                attemptList[currentFail] += 1
            else:
                attemptList[currentFail] = 1
            currentFail = 0
        else:
            currentFail += 1

    print 'Test results: %s tries, %s longest failure chain' % (numTries, greatestFailChain)
    if list:
        print 'failures for each succes %s' % attemptList


class Quest:
    _cogTracks = [Any,
     'c',
     'l',
     'm',
     's',
     'g']
    _factoryTypes = [Any,
     FT_FullSuit,
     FT_Leg,
     FT_Arm,
     FT_Torso]

    def check(self, cond, msg):
        pass

    def checkLocation(self, location):
        locations = [Anywhere] + TTLocalizer.GlobalStreetNames.keys()
        self.check(location in locations, 'invalid location: %s' % location)

    def checkNumCogs(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def checkNewbieLevel(self, level):
        self.check(1, 'invalid newbie level: %s' % level)

    def checkCogType(self, type):
        types = [Any] + SuitBattleGlobals.SuitAttributes.keys()
        self.check(type in types, 'invalid cog type: %s' % type)

    def checkCogTrack(self, track):
        self.check(track in self._cogTracks, 'invalid cog track: %s' % track)

    def checkCogLevel(self, level):
        self.check(level >= 1 and level <= 12, 'invalid cog level: %s' % level)

    def checkNumSkelecogs(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def checkSkelecogTrack(self, track):
        self.check(track in self._cogTracks, 'invalid cog track: %s' % track)

    def checkSkelecogLevel(self, level):
        self.check(level >= 1 and level <= 12, 'invalid cog level: %s' % level)

    def checkNumSkeleRevives(self, num):
        self.check(1, 'invalid number of cogs: %s' % num)

    def checkNumForemen(self, num):
        self.check(num > 0, 'invalid number of foremen: %s' % num)

    def checkNumVPs(self, num):
        self.check(num > 0, 'invalid number of VPs: %s' % num)

    def checkNumSupervisors(self, num):
        self.check(num > 0, 'invalid number of supervisors: %s' % num)

    def checkNumCFOs(self, num):
        self.check(num > 0, 'invalid number of CFOs: %s' % num)

    def checkNumCJs(self, num):
        self.check(num > 0, 'invalid number of CJs: %s' % num)

    def checkNumCEOs(self, num):
        self.check(num > 0, 'invalid number of CEOs: %s' % num)

    def checkNumBuildings(self, num):
        self.check(1, 'invalid num buildings: %s' % num)

    def checkBuildingTrack(self, track):
        self.check(track in self._cogTracks, 'invalid building track: %s' % track)

    def checkBuildingFloors(self, floors):
        self.check(floors >= 1 and floors <= 6, 'invalid num floors: %s' % floors)

    def checkNumCogdos(self, num):
        self.check(1, 'invalid num buildings: %s' % num)

    def checkCogdoTrack(self, track):
        self.check(track in self._cogTracks, 'invalid building track: %s' % track)

    def checkNumFactories(self, num):
        self.check(1, 'invalid num factories: %s' % num)

    def checkFactoryType(self, type):
        self.check(type in self._factoryTypes, 'invalid factory type: %s' % type)

    def checkNumMints(self, num):
        self.check(1, 'invalid num mints: %s' % num)

    def checkNumStages(self, num):
        self.check(1, 'invalid num mints: %s' % num)

    def checkNumClubs(self, num):
        self.check(1, 'invalid num mints: %s' % num)

    def checkNumCogParts(self, num):
        self.check(1, 'invalid num cog parts: %s' % num)

    def checkNumGags(self, num):
        self.check(1, 'invalid num gags: %s' % num)

    def checkGagTrack(self, track):
        self.check(track >= ToontownBattleGlobals.MIN_TRACK_INDEX and track <= ToontownBattleGlobals.MAX_TRACK_INDEX, 'invalid gag track: %s' % track)

    def checkExperienceAmount(self, num):
        self.check(num > 0, 'invalid track experience amount: %s' % num)

    def checkGagItem(self, item):
        self.check(item >= ToontownBattleGlobals.MIN_LEVEL_INDEX and item <= ToontownBattleGlobals.MAX_LEVEL_INDEX, 'invalid gag item: %s' % item)

    def checkDeliveryItem(self, item):
        self.check(ItemDict.has_key(item), 'invalid delivery item: %s' % item)

    def checkNumItems(self, num):
        self.check(1, 'invalid num items: %s' % num)

    def checkRecoveryItem(self, item):
        self.check(ItemDict.has_key(item), 'invalid recovery item: %s' % item)

    def checkPercentChance(self, chance):
        self.check(chance > 0 and chance <= 100, 'invalid percent chance: %s' % chance)

    def checkRecoveryItemHolderAndType(self, holder, holderType = 'type'):
        holderTypes = ['type', 'level', 'track']
        self.check(holderType in holderTypes, 'invalid recovery item holderType: %s' % holderType)
        if holderType == 'type':
            holders = [Any, AnyFish] + SuitBattleGlobals.SuitAttributes.keys()
            self.check(holder in holders, 'invalid recovery item holder: %s for holderType: %s' % (holder, holderType))
        elif holderType == 'level':
            pass
        elif holderType == 'track':
            self.check(holder in self._cogTracks, 'invalid recovery item holder: %s for holderType: %s' % (holder, holderType))

    def checkTrackChoice(self, option):
        self.check(option >= ToontownBattleGlobals.MIN_TRACK_INDEX and option <= ToontownBattleGlobals.MAX_TRACK_INDEX, 'invalid track option: %s' % option)

    def checkNumFriends(self, num):
        self.check(1, 'invalid number of friends: %s' % num)

    def checkNumMinigames(self, num):
        self.check(1, 'invalid number of minigames: %s' % num)

    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        self.id = id
        self.quest = quest

    def getId(self):
        return self.id

    def getType(self):
        return self.__class__

    def getObjectiveStrings(self):
        return ['']

    def getString(self):
        return self.getObjectiveStrings()[0]

    def getRewardString(self, progressString):
        return self.getString() + ' : ' + progressString

    def getChooseString(self):
        return self.getString()

    def getPosterString(self):
        return self.getString()

    def getHeadlineString(self):
        return self.getString()

    def getDefaultQuestDialog(self):
        return self.getString() + TTLocalizer.Period

    def getNumQuestItems(self):
        return -1

    def addArticle(self, num, oString):
        if len(oString) == 0:
            return oString
        if num == 1:
            return oString
        else:
            return '%d %s' % (num, oString)

    def __repr__(self):
        return 'Quest type: %s id: %s params: %s' % (self.__class__.__name__, self.id, self.quest[0:])

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesCFOCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesCJCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesCEOCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesFactoryCount(self, avId, location, avList):
        return 0

    def doesMintCount(self, avId, location, avList):
        return 0

    def doesCogPartCount(self, avId, location, avList):
        return 0

    def getCompletionStatus(self, av, questDesc, npc = None):
        notify.error('Pure virtual - please override me')
        return None


class LocationBasedQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkLocation(self.quest[0])

    def getLocation(self):
        return self.quest[0]

    def getLocationName(self):
        loc = self.getLocation()
        if loc == Anywhere:
            locName = ''
        elif loc in ToontownGlobals.hoodNameMap:
            locName = TTLocalizer.QuestInLocationString % {'inPhrase': ToontownGlobals.hoodNameMap[loc][1],
             'location': ToontownGlobals.hoodNameMap[loc][-1] + TTLocalizer.QuestsLocationArticle}
        elif loc in ToontownGlobals.StreetBranchZones:
            locName = TTLocalizer.QuestInLocationString % {'inPhrase': ToontownGlobals.StreetNames[loc][1],
             'location': ToontownGlobals.StreetNames[loc][-1] + TTLocalizer.QuestsLocationArticle}
        return locName

    def isLocationMatch(self, zoneId):
        loc = self.getLocation()
        if loc is Anywhere:
            return 1
        if ZoneUtil.isPlayground(loc):
            if loc == ZoneUtil.getCanonicalHoodId(zoneId):
                return 1
            else:
                return 0
        elif loc == ZoneUtil.getCanonicalBranchZone(zoneId):
            return 1
        elif loc == zoneId:
            return 1
        else:
            return 0

    def getChooseString(self):
        return TTLocalizer.QuestsLocationString % {'string': self.getString(),
         'location': self.getLocationName()}

    def getPosterString(self):
        return TTLocalizer.QuestsLocationString % {'string': self.getString(),
         'location': self.getLocationName()}

    def getDefaultQuestDialog(self):
        return (TTLocalizer.QuestsLocationString + TTLocalizer.Period) % {'string': self.getString(),
         'location': self.getLocationName()}


class NewbieQuest:
    def getNewbieLevel(self):
        notify.error('Pure virtual - please override me')

    def getString(self, newStr = TTLocalizer.QuestsCogNewNewbieQuestObjective, oldStr = TTLocalizer.QuestsCogOldNewbieQuestObjective):
        laff = self.getNewbieLevel()
        if laff <= NEWBIE_HP:
            return newStr % self.getObjectiveStrings()[0]
        else:
            return oldStr % {'laffPoints': laff,
             'objective': self.getObjectiveStrings()[0]}

    def getCaption(self):
        laff = self.getNewbieLevel()
        if laff <= NEWBIE_HP:
            return TTLocalizer.QuestsCogNewNewbieQuestCaption % laff
        else:
            return TTLocalizer.QuestsCogOldNewbieQuestCaption % laff

    def getNumNewbies(self, avId, avList):
        newbieHp = self.getNewbieLevel()
        num = 0
        for av in avList:
            if av != avId and av.getMaxHp() <= newbieHp:
                num += 1

        return num


class CogQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        if self.__class__ == CogQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogType(self.quest[2])

    def getCogType(self):
        return self.quest[2]

    def getNumQuestItems(self):
        return self.getNumCogs()

    def getNumCogs(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumCogs()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        cogType = self.getCogType()
        if numCogs == 1:
            if cogType == Any:
                return TTLocalizer.Cog
            else:
                return SuitBattleGlobals.SuitAttributes[cogType]['singularname']
        elif cogType == Any:
            return TTLocalizer.Cogs
        else:
            return SuitBattleGlobals.SuitAttributes[cogType]['pluralname']

    def getObjectiveStrings(self):
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = cogName
        else:
            text = TTLocalizer.QuestsCogQuestDefeatDesc % {'numCogs': numCogs,
             'cogName': cogName}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = TTLocalizer.QuestsCogQuestSCStringS
        else:
            text = TTLocalizer.QuestsCogQuestSCStringP
        cogLoc = self.getLocationName()
        return text % {'cogName': cogName,
         'cogLoc': cogLoc}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogType = self.getCogType()
        return (questCogType is Any or questCogType is cogDict['type']) and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)
		
class EliteCogQBase:
    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict['isElite'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)
        
class EliteCogQuest(CogQuest, EliteCogQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])

    def getCogType(self):
        return Any
		
    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getObjectiveStrings(self):
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = cogName
        else:
            text = TTLocalizer.QuestsEliteCogQuestDefeatDesc % {'numCogs': numCogs,
             'cogName': cogName}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsEliteCogQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        cogName = self.getCogNameString()
        numCogs = self.getNumCogs()
        if numCogs == 1:
            text = TTLocalizer.QuestsEliteCogQuestSCStringS
        else:
            text = TTLocalizer.QuestsEliteCogQuestSCStringP
        cogLoc = self.getLocationName()
        return text % {'cogName': cogName,
         'cogLoc': cogLoc}

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return EliteCogQBase.doesCogCount(self, avId, cogDict, zoneId, avList)

class CogNewbieQuest(CogQuest, NewbieQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        if self.__class__ == CogNewbieQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogType(self.quest[2])
            self.checkNewbieLevel(self.quest[3])

    def getNewbieLevel(self):
        return self.quest[3]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if CogQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0

class TrackExpQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        if self.__class__ == TrackExpQuest:
            self.checkGagTrack(self.quest[1])
            self.checkExperienceAmount(self.quest[2])

    def getTrackType(self):
        return self.quest[1]

    def getNumQuestItems(self):
        return self.getNumExp()

    def getNumExp(self):
        return self.quest[2]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumExp()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumExp() == 1:
            return ''
        else:
            return TTLocalizer.QuestsExpQuestProgress % {'progress': questDesc[4],
             'numExp': self.getNumExp()}

    def getObjectiveStrings(self):
        trackName = self.getTrackType()
        numExp = self.getNumExp()
        if numExp == 1:
            text = trackName
        else:
            text = TTLocalizer.QuestsExpQuestCollectDesc % {'track': TTLocalizer.BattleGlobalTracks[trackName],
             'experience': numExp}
        return (text,)

    def getString(self):
        trackName = self.getTrackType()
        numExp = self.getNumExp()
        return TTLocalizer.QuestsExpQuestCollect % {'experience': numExp,
             'track': TTLocalizer.BattleGlobalTracks[trackName]}

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumExp():
            return getFinishToonTaskSCStrings(toNpcId)
        trackName = self.getTrackType()
        numExp = self.getNumExp()
        if numExp == 1:
            text = TTLocalizer.QuestsExpQuestSCStringS
        else:
            text = TTLocalizer.QuestsExpQuestSCStringP
        return text % {'track': TTLocalizer.BattleGlobalTracks[trackName],
         'experience': numExp}

    def getHeadlineString(self):
        return TTLocalizer.QuestsExpQuestHeadline

    def doesExpCount(self, avId, expArray):
        trackType = self.getTrackType()
        return (expArray[trackType] > 0)



class CogTrackQuest(CogQuest):
    trackCodes = ['c',
     'l',
     'm',
     's',
     'g']
    trackNamesS = [TTLocalizer.BossbotS,
     TTLocalizer.LawbotS,
     TTLocalizer.CashbotS,
     TTLocalizer.SellbotS,
     TTLocalizer.BoardbotS]
    trackNamesP = [TTLocalizer.BossbotP,
     TTLocalizer.LawbotP,
     TTLocalizer.CashbotP,
     TTLocalizer.SellbotP,
     TTLocalizer.BoardbotP]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        if self.__class__ == CogTrackQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogTrack(self.quest[2])

    def getCogTrack(self):
        return self.quest[2]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogTrackQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getObjectiveStrings(self):
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            text = self.trackNamesS[track]
        else:
            text = TTLocalizer.QuestsCogTrackDefeatDesc % {'numCogs': numCogs,
             'trackName': self.trackNamesP[track]}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogTrackQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        numCogs = self.getNumCogs()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            cogText = self.trackNamesS[track]
            text = TTLocalizer.QuestsCogTrackQuestSCStringS
        else:
            cogText = self.trackNamesP[track]
            text = TTLocalizer.QuestsCogTrackQuestSCStringP
        cogLocName = self.getLocationName()
        return text % {'cogText': cogText,
         'cogLoc': cogLocName}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogTrackQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogTrack = self.getCogTrack()
        return questCogTrack == cogDict['track'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class CogLevelQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogs(self.quest[1])
        self.checkCogLevel(self.quest[2])

    def getCogType(self):
        try:
           return self.quest[3] # This is just here so I don't have to waste time retroactively replacing EVERY CogLevelQuest, Barks, you can remove this after you redo quests. Be sure to use "Any" for instances that actually need Any
        except:
           return Any

    def getCogLevel(self):
        return self.quest[2]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogLevelQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getObjectiveStrings(self):
        count = self.getNumCogs()
        level = self.getCogLevel()
        name = self.getCogNameString()
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescC
        return (text % {'count': count,
          'level': level,
          'name': name},)

    def getString(self):
        return TTLocalizer.QuestsCogLevelQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumCogs()
        level = self.getCogLevel()
        name = self.getCogNameString()
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescI
        objective = text % {'level': level,
         'name': name}
        location = self.getLocationName()
        return TTLocalizer.QuestsCogLevelQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogLevelQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogLevel = self.getCogLevel()
        return questCogLevel <= cogDict['level'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)

class CogTrackLevelQuest(CogQuest):
    trackCodes = ['c',
     'l',
     'm',
     's',
     'g']
    trackNamesS = [TTLocalizer.BossbotS,
     TTLocalizer.LawbotS,
     TTLocalizer.CashbotS,
     TTLocalizer.SellbotS,
     TTLocalizer.BoardbotS]
    trackNamesP = [TTLocalizer.BossbotP,
     TTLocalizer.LawbotP,
     TTLocalizer.CashbotP,
     TTLocalizer.SellbotP,
     TTLocalizer.BoardbotP]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        if self.__class__ == CogTrackQuest:
            self.checkNumCogs(self.quest[1])
            self.checkCogTrack(self.quest[2])
            self.checkCogLevel(self.quest[3])

    def getCogTrack(self):
        return self.quest[2]

    def getCogLevel(self):
        return self.quest[3]

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogTrackQuestProgress % {'progress': questDesc[4],
             'numCogs': self.getNumCogs()}

    def getObjectiveStrings(self):
        numCogs = self.getNumCogs()
        level = self.getCogLevel()
        track = self.trackCodes.index(self.getCogTrack())
        if numCogs == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc % {'level': level, 'name': self.trackNamesS[track]}
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescC % {'count': numCogs, 'level': level, 'name': self.trackNamesP[track]}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsCogLevelQuestDefeat % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogs():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumCogs()
        level = self.getCogLevel()
        track = self.trackCodes.index(self.getCogTrack())
        if count == 1:
            text = TTLocalizer.QuestsCogLevelQuestDesc
        else:
            text = TTLocalizer.QuestsCogLevelQuestDescI
        objective = text % {'level': level,
         'name': self.trackNamesP[track]}
        location = self.getLocationName()
        return TTLocalizer.QuestsCogLevelQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogTrackQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        questCogTrack = self.getCogTrack()
        questCogLevel = self.getCogLevel()
        return questCogTrack == cogDict['track'] and questCogLevel <= cogDict['level'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class SkelecogQBase:
    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ASkeleton
        else:
            return TTLocalizer.SkeletonP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict['isSkelecog'] and avId in cogDict['activeToons'] and self.isLocationMatch(zoneId)


class SkelecogQuest(CogQuest, SkelecogQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId, avList)


class SkelecogNewbieQuest(SkelecogQuest, NewbieQuest):
    def __init__(self, id, quest):
        SkelecogQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if SkelecogQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class SkelecogTrackQuest(CogTrackQuest, SkelecogQBase):
    trackNamesS = [TTLocalizer.BossbotSkelS,
     TTLocalizer.LawbotSkelS,
     TTLocalizer.CashbotSkelS,
     TTLocalizer.SellbotSkelS,
     TTLocalizer.BoardbotSkelS]
    trackNamesP = [TTLocalizer.BossbotSkelP,
     TTLocalizer.LawbotSkelP,
     TTLocalizer.CashbotSkelP,
     TTLocalizer.SellbotSkelP,
     TTLocalizer.BoardbotSkelP]

    def __init__(self, id, quest):
        CogTrackQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])
        self.checkSkelecogTrack(self.quest[2])

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId, avList) and self.getCogTrack() == cogDict['track']


class SkelecogLevelQuest(CogLevelQuest, SkelecogQBase):
    def __init__(self, id, quest):
        CogLevelQuest.__init__(self, id, quest)
        self.checkNumSkelecogs(self.quest[1])
        self.checkSkelecogLevel(self.quest[2])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkelecogQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return SkelecogQBase.doesCogCount(self, avId, cogDict, zoneId, avList) and self.getCogLevel() <= cogDict['level']


class SkeleReviveQBase:
    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.Av2Cog
        else:
            return TTLocalizer.v2CogP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict.get('hasRevives', False) and avId in cogDict.get('activeToons', []) and self.isLocationMatch(zoneId)


class SkeleReviveQuest(CogQuest, SkeleReviveQBase):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSkeleRevives(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        return SkeleReviveQBase.getCogNameString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return SkeleReviveQBase.doesCogCount(self, avId, cogDict, zoneId, avList)


class ForemanQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumForemen(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.AForeman
        else:
            return TTLocalizer.ForemanP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return bool(CogQuest.doesCogCount(self, avId, cogDict, zoneId, avList) and cogDict['isForeman'])


class ForemanNewbieQuest(ForemanQuest, NewbieQuest):
    def __init__(self, id, quest):
        ForemanQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if ForemanQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class VPQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumVPs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ACogVP
        else:
            return TTLocalizer.CogVPs

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict['isBoss'] > 0 and self.isLocationMatch(zoneId)

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        return self.doesCogCount(avId, cogDict, zoneId, avList)


class VPNewbieQuest(VPQuest, NewbieQuest):
    def __init__(self, id, quest):
        VPQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        if VPQuest.doesVPCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class SupervisorQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumSupervisors(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ASupervisor
        else:
            return TTLocalizer.SupervisorP

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return bool(CogQuest.doesCogCount(self, avId, cogDict, zoneId, avList) and cogDict['isSupervisor'])


class SupervisorNewbieQuest(SupervisorQuest, NewbieQuest):
    def __init__(self, id, quest):
        SupervisorQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        if SupervisorQuest.doesCogCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class CFOQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCFOs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ACogCFO
        else:
            return TTLocalizer.CogCFOs

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict['isBoss'] > 0 and self.isLocationMatch(zoneId)

    def doesCFOCount(self, avId, cogDict, zoneId, avList):
        return self.doesCogCount(avId, cogDict, zoneId, avList)


class CFONewbieQuest(CFOQuest, NewbieQuest):
    def __init__(self, id, quest):
        CFOQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCFOCount(self, avId, cogDict, zoneId, avList):
        if CFOQuest.doesCFOCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0

class CJQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCJs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ACogCJ
        else:
            return TTLocalizer.CogCJs

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict['isBoss'] > 0 and self.isLocationMatch(zoneId)

    def doesCJCount(self, avId, cogDict, zoneId, avList):
        return self.doesCogCount(avId, cogDict, zoneId, avList)


class CJNewbieQuest(CJQuest, NewbieQuest):
    def __init__(self, id, quest):
        CJQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCJCount(self, avId, cogDict, zoneId, avList):
        if CJQuest.doesCJCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0

class CEOQuest(CogQuest):
    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCEOs(self.quest[1])

    def getCogType(self):
        return Any

    def getCogNameString(self):
        numCogs = self.getNumCogs()
        if numCogs == 1:
            return TTLocalizer.ACogCEO
        else:
            return TTLocalizer.CogCEOs

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return cogDict['isBoss'] > 0 and self.isLocationMatch(zoneId)

    def doesCEOCount(self, avId, cogDict, zoneId, avList):
        return self.doesCogCount(avId, cogDict, zoneId, avList)


class CEONewbieQuest(CEOQuest, NewbieQuest):
    def __init__(self, id, quest):
        CEOQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def doesCEOCount(self, avId, cogDict, zoneId, avList):
        if CEOQuest.doesCEOCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0

class RescueQuest(VPQuest):
    def __init__(self, id, quest):
        VPQuest.__init__(self, id, quest)

    def getNumToons(self):
        return self.getNumCogs()

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumToons() == 1:
            return ''
        else:
            return TTLocalizer.QuestsRescueQuestProgress % {'progress': questDesc[4],
             'numToons': self.getNumToons()}

    def getObjectiveStrings(self):
        numToons = self.getNumCogs()
        if numToons == 1:
            text = TTLocalizer.QuestsRescueQuestToonS
        else:
            text = TTLocalizer.QuestsRescueQuestRescueDesc % {'numToons': numToons}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsRescueQuestRescue % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumToons():
            return getFinishToonTaskSCStrings(toNpcId)
        numToons = self.getNumToons()
        if numToons == 1:
            text = TTLocalizer.QuestsRescueQuestSCStringS
        else:
            text = TTLocalizer.QuestsRescueQuestSCStringP
        toonLoc = self.getLocationName()
        return text % {'toonLoc': toonLoc}

    def getHeadlineString(self):
        return TTLocalizer.QuestsRescueQuestHeadline


class RescueNewbieQuest(RescueQuest, NewbieQuest):
    def __init__(self, id, quest):
        RescueQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self, newStr=TTLocalizer.QuestsRescueNewNewbieQuestObjective, oldStr=TTLocalizer.QuestsRescueOldNewbieQuestObjective)

    def doesVPCount(self, avId, cogDict, zoneId, avList):
        if RescueQuest.doesVPCount(self, avId, cogDict, zoneId, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return 0


class BuildingQuest(CogQuest):
    trackCodes = ['c',
     'l',
     'm',
     's',
     'g']
    trackNames = [TTLocalizer.Bossbot,
     TTLocalizer.Lawbot,
     TTLocalizer.Cashbot,
     TTLocalizer.Sellbot,
     TTLocalizer.Boardbot]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumBuildings(self.quest[1])
        self.checkBuildingTrack(self.quest[2])
        self.checkBuildingFloors(self.quest[3])

    def getNumFloors(self):
        return self.quest[3]

    def getBuildingTrack(self):
        return self.quest[2]

    def getNumQuestItems(self):
        return self.getNumBuildings()

    def getNumBuildings(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumBuildings()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumBuildings() == 1:
            return ''
        else:
            return TTLocalizer.QuestsBuildingQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumBuildings()}

    def getObjectiveStrings(self):
        count = self.getNumBuildings()
        floors = TTLocalizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            if floors == '':
                text = TTLocalizer.QuestsBuildingQuestDesc
            else:
                text = TTLocalizer.QuestsBuildingQuestDescF
        elif floors == '':
            text = TTLocalizer.QuestsBuildingQuestDescC
        else:
            text = TTLocalizer.QuestsBuildingQuestDescCF
        return (text % {'count': count,
          'floors': floors,
          'type': type},)

    def getString(self):
        return TTLocalizer.QuestsBuildingQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumBuildings():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumBuildings()
        floors = TTLocalizer.QuestsBuildingQuestFloorNumbers[self.getNumFloors() - 1]
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            if floors == '':
                text = TTLocalizer.QuestsBuildingQuestDesc
            else:
                text = TTLocalizer.QuestsBuildingQuestDescF
        elif floors == '':
            text = TTLocalizer.QuestsBuildingQuestDescI
        else:
            text = TTLocalizer.QuestsBuildingQuestDescIF
        objective = text % {'floors': floors,
         'type': type}
        location = self.getLocationName()
        return TTLocalizer.QuestsBuildingQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsBuildingQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesBuildingTypeCount(self, type):
        buildingTrack = self.getBuildingTrack()
        if buildingTrack == Any or buildingTrack == type:
            return True
        return False

    def doesBuildingCount(self, avId, avList):
        return 1


class BuildingNewbieQuest(BuildingQuest, NewbieQuest):
    def __init__(self, id, quest):
        BuildingQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[4])

    def getNewbieLevel(self):
        return self.quest[4]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesBuildingCount(self, avId, avList):
        return self.getNumNewbies(avId, avList)

class CogdoQuest(CogQuest):
    trackCodes = ['c',
     'l',
     'm',
     's',
     'g']
    trackNames = [TTLocalizer.Bossbot,
     TTLocalizer.Lawbot,
     TTLocalizer.Cashbot,
     TTLocalizer.Sellbot,
     TTLocalizer.Boardbot]

    def __init__(self, id, quest):
        CogQuest.__init__(self, id, quest)
        self.checkNumCogdos(self.quest[1])
        self.checkCogdoTrack(self.quest[2])

    def getCogdoTrack(self):
        return self.quest[2]

    def getNumQuestItems(self):
        return self.getNumCogdos()

    def getNumCogdos(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumCogdos()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumCogdos() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogdoQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumCogdos()}

    def getObjectiveStrings(self):
        count = self.getNumCogdos()
        buildingTrack = self.getCogdoTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            text = TTLocalizer.QuestsCogdoQuestDesc
        else:
            text = TTLocalizer.QuestsCogdoQuestDescC
        return (text % {'count': count,
          'type': type},)

    def getString(self):
        return TTLocalizer.QuestsCogdoQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumCogdos():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumCogdos()
        buildingTrack = self.getCogdoTrack()
        if buildingTrack == Any:
            type = TTLocalizer.Cog
        else:
            type = self.trackNames[self.trackCodes.index(buildingTrack)]
        if count == 1:
            text = TTLocalizer.QuestsCogdoQuestDesc
        else:
            text = TTLocalizer.QuestsCogdoQuestDescI
        objective = text % {'type': type,}
        location = self.getLocationName()
        return TTLocalizer.QuestsCogdoQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogdoQuestHeadline

    def doesCogCount(self, avId, cogDict, zoneId, avList):
        return 0

    def doesCogdoCount(self, avId, avList):
        return 1

    def doesCogdoTypeCount(self, type):
        CogdoTrack = self.getCogdoTrack()
        if CogdoTrack == Any or CogdoTrack == type:
            return True
        return False


class CogdoNewbieQuest(CogdoQuest, NewbieQuest):
    def __init__(self, id, quest):
        CogdoQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[3])

    def getNewbieLevel(self):
        return self.quest[3]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesCogdoCount(self, avId, avList):
        return self.getNumNewbies(avId, avList)


class FactoryQuest(LocationBasedQuest):
    factoryTypeNames = {FT_FullSuit: TTLocalizer.Cog,
     FT_Leg: TTLocalizer.FactoryTypeLeg,
     FT_Arm: TTLocalizer.FactoryTypeArm,
     FT_Torso: TTLocalizer.FactoryTypeTorso}

    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumFactories(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumFactories()

    def getNumFactories(self):
        return self.quest[1]

    def getFactoryType(self):
        loc = self.getLocation()
        type = Any
        if loc in ToontownGlobals.factoryId2factoryType:
            type = ToontownGlobals.factoryId2factoryType[loc]
        return type

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumFactories()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumFactories() == 1:
            return ''
        else:
            return TTLocalizer.QuestsFactoryQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumFactories()}

    def getObjectiveStrings(self):
        count = self.getNumFactories()
        factoryType = self.getFactoryType()
        if factoryType == Any:
            type = TTLocalizer.Cog
        else:
            type = FactoryQuest.factoryTypeNames[factoryType]
        if count == 1:
            text = TTLocalizer.QuestsFactoryQuestDesc
        else:
            text = TTLocalizer.QuestsFactoryQuestDescC
        return (text % {'count': count,
          'type': type},)

    def getString(self):
        return TTLocalizer.QuestsFactoryQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumFactories():
            return getFinishToonTaskSCStrings(toNpcId)
        factoryType = self.getFactoryType()
        if factoryType == Any:
            type = TTLocalizer.Cog
        else:
            type = FactoryQuest.factoryTypeNames[factoryType]
        count = self.getNumFactories()
        if count == 1:
            text = TTLocalizer.QuestsFactoryQuestDesc
        else:
            text = TTLocalizer.QuestsFactoryQuestDescI
        objective = text % {'type': type}
        location = self.getLocationName()
        return TTLocalizer.QuestsFactoryQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsFactoryQuestHeadline

    def doesFactoryCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class FactoryNewbieQuest(FactoryQuest, NewbieQuest):
    def __init__(self, id, quest):
        FactoryQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesFactoryCount(self, avId, location, avList):
        if FactoryQuest.doesFactoryCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num


class MintQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumMints(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumMints()

    def getNumMints(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumMints()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumMints() == 1:
            return ''
        else:
            return TTLocalizer.QuestsMintQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumMints()}

    def getObjectiveStrings(self):
        count = self.getNumMints()
        if count == 1:
            text = TTLocalizer.QuestsMintQuestDesc
        else:
            text = TTLocalizer.QuestsMintQuestDescC % {'count': count}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsMintQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumMints():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumMints()
        if count == 1:
            objective = TTLocalizer.QuestsMintQuestDesc
        else:
            objective = TTLocalizer.QuestsMintQuestDescI
        location = self.getLocationName()
        return TTLocalizer.QuestsMintQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsMintQuestHeadline

    def doesMintCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class MintNewbieQuest(MintQuest, NewbieQuest):
    def __init__(self, id, quest):
        MintQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesMintCount(self, avId, location, avList):
        if MintQuest.doesMintCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num

class StageQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumStages(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumStages()

    def getNumStages(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumStages()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumStages() == 1:
            return ''
        else:
            return TTLocalizer.QuestsStageQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumStages()}

    def getObjectiveStrings(self):
        count = self.getNumStages()
        if count == 1:
            text = TTLocalizer.QuestsStageQuestDesc
        else:
            text = TTLocalizer.QuestsStageQuestDescC % {'count': count}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsStageQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumStages():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumStages()
        if count == 1:
            objective = TTLocalizer.QuestsStageQuestDesc
        else:
            objective = TTLocalizer.QuestsStageQuestDescI
        location = self.getLocationName()
        return TTLocalizer.QuestsStageQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsStageQuestHeadline

    def doesStageCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class StageNewbieQuest(StageQuest, NewbieQuest):
    def __init__(self, id, quest):
        StageQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesStageCount(self, avId, location, avList):
        if StageQuest.doesStageCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num

class ClubQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumClubs(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumClubs()

    def getNumClubs(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumClubs()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumClubs() == 1:
            return ''
        else:
            return TTLocalizer.QuestsClubQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumClubs()}

    def getObjectiveStrings(self):
        count = self.getNumClubs()
        if count == 1:
            text = TTLocalizer.QuestsClubQuestDesc
        else:
            text = TTLocalizer.QuestsClubQuestDescC % {'count': count}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsClubQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumClubs():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumClubs()
        if count == 1:
            objective = TTLocalizer.QuestsClubQuestDesc
        else:
            objective = TTLocalizer.QuestsClubQuestDescI
        location = self.getLocationName()
        return TTLocalizer.QuestsClubQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsClubQuestHeadline

    def doesClubCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class ClubNewbieQuest(ClubQuest, NewbieQuest):
    def __init__(self, id, quest):
        ClubQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesClubCount(self, avId, location, avList):
        if ClubQuest.doesClubCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num


class CogPartQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumCogParts(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumParts()

    def getNumParts(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumParts()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumParts() == 1:
            return ''
        else:
            return TTLocalizer.QuestsCogPartQuestProgressString % {'progress': questDesc[4],
             'num': self.getNumParts()}

    def getObjectiveStrings(self):
        count = self.getNumParts()
        if count == 1:
            text = TTLocalizer.QuestsCogPartQuestDesc
        else:
            text = TTLocalizer.QuestsCogPartQuestDescC
        return (text % {'count': count},)

    def getString(self):
        return TTLocalizer.QuestsCogPartQuestString % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumParts():
            return getFinishToonTaskSCStrings(toNpcId)
        count = self.getNumParts()
        if count == 1:
            text = TTLocalizer.QuestsCogPartQuestDesc
        else:
            text = TTLocalizer.QuestsCogPartQuestDescI
        objective = text
        location = self.getLocationName()
        return TTLocalizer.QuestsCogPartQuestSCString % {'objective': objective,
         'location': location}

    def getHeadlineString(self):
        return TTLocalizer.QuestsCogPartQuestHeadline

    def doesCogPartCount(self, avId, location, avList):
        return self.isLocationMatch(location)


class CogPartNewbieQuest(CogPartQuest, NewbieQuest):
    def __init__(self, id, quest):
        CogPartQuest.__init__(self, id, quest)
        self.checkNewbieLevel(self.quest[2])

    def getNewbieLevel(self):
        return self.quest[2]

    def getString(self):
        return NewbieQuest.getString(self, newStr=TTLocalizer.QuestsCogPartNewNewbieQuestObjective, oldStr=TTLocalizer.QuestsCogPartOldNewbieQuestObjective)

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def doesCogPartCount(self, avId, location, avList):
        if CogPartQuest.doesCogPartCount(self, avId, location, avList):
            return self.getNumNewbies(avId, avList)
        else:
            return num


class DeliverGagQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumGags(self.quest[0])
        self.checkGagTrack(self.quest[1])
        self.checkGagItem(self.quest[2])

    def getGagType(self):
        return (self.quest[1], self.quest[2])

    def getNumQuestItems(self):
        return self.getNumGags()

    def getNumGags(self):
        return self.quest[0]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        gag = self.getGagType()
        num = self.getNumGags()
        track = gag[0]
        level = gag[1]
        questComplete = npc and av.inventory and av.inventory.numItem(track, level) >= num
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumGags() == 1:
            return ''
        else:
            return TTLocalizer.QuestsDeliverGagQuestProgress % {'progress': questDesc[4],
             'numGags': self.getNumGags()}

    def getObjectiveStrings(self):
        track, item = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
            text = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
             'name': gagName}
        return (text,)

    def getString(self):
        return TTLocalizer.QuestsDeliverGagQuestString % self.getObjectiveStrings()[0]

    def getRewardString(self, progress):
        return TTLocalizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0]

    def getDefaultQuestDialog(self):
        return TTLocalizer.QuestsDeliverGagQuestStringLong % self.getObjectiveStrings()[0] + '\x07' + TTLocalizer.QuestsDeliverGagQuestInstructions

    def getSCStrings(self, toNpcId, progress):
        if progress >= self.getNumGags():
            return getFinishToonTaskSCStrings(toNpcId)
        track, item = self.getGagType()
        num = self.getNumGags()
        if num == 1:
            text = TTLocalizer.QuestsDeliverGagQuestToSCStringS
            gagName = ToontownBattleGlobals.AvPropStringsSingular[track][item]
        else:
            text = TTLocalizer.QuestsDeliverGagQuestToSCStringP
            gagName = ToontownBattleGlobals.AvPropStringsPlural[track][item]
        return [text % {'gagName': gagName}, TTLocalizer.QuestsDeliverGagQuestSCString] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsDeliverGagQuestHeadline


class DeliverItemQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkDeliveryItem(self.quest[0])

    def getItem(self):
        return self.quest[0]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        return TTLocalizer.QuestsDeliverItemQuestProgress

    def getObjectiveStrings(self):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [article + itemName]

    def getString(self):
        return TTLocalizer.QuestsDeliverItemQuestString % self.getObjectiveStrings()[0]

    def getRewardString(self, progress):
        return TTLocalizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]

    def getDefaultQuestDialog(self):
        return TTLocalizer.QuestsDeliverItemQuestStringLong % self.getObjectiveStrings()[0]

    def getSCStrings(self, toNpcId, progress):
        iDict = ItemDict[self.getItem()]
        article = iDict[2]
        itemName = iDict[0]
        return [TTLocalizer.QuestsDeliverItemQuestSCString % {'article': article,
          'itemName': itemName}] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsDeliverItemQuestHeadline


class VisitQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        return TTLocalizer.QuestsVisitQuestProgress

    def getObjectiveStrings(self):
        return ['']

    def getString(self):
        return TTLocalizer.QuestsVisitQuestStringShort

    def getChooseString(self):
        return TTLocalizer.QuestsVisitQuestStringLong

    def getRewardString(self, progress):
        return TTLocalizer.QuestsVisitQuestStringLong

    def getDefaultQuestDialog(self):
        return random.choice(DefaultVisitQuestDialog)

    def getSCStrings(self, toNpcId, progress):
        return getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsVisitQuestHeadline


class RecoverItemQuest(LocationBasedQuest):
    def __init__(self, id, quest):
        LocationBasedQuest.__init__(self, id, quest)
        self.checkNumItems(self.quest[1])
        self.checkRecoveryItem(self.quest[2])
        self.checkPercentChance(self.quest[3])
        if len(self.quest) > 5:
            self.checkRecoveryItemHolderAndType(self.quest[4], self.quest[5])
        else:
            self.checkRecoveryItemHolderAndType(self.quest[4])

    def testRecover(self, progress):
        test = random.random() * 100
        chance = self.getPercentChance()
        numberDone = progress & pow(2, 16) - 1
        numberNotDone = progress >> 16
        returnTest = None
        avgNum2Kill = 1.0 / (chance / 100.0)
        if numberNotDone >= avgNum2Kill * 1.5:
            chance = 100
        elif numberNotDone > avgNum2Kill * 0.5:
            diff = float(numberNotDone - avgNum2Kill * 0.5)
            luck = 1.0 + abs(diff / (avgNum2Kill * 0.5))
            chance *= luck
        if test <= chance:
            returnTest = 1
            numberNotDone = 0
            numberDone += 1
        else:
            returnTest = 0
            numberNotDone += 1
            numberDone += 0
        returnCount = numberNotDone << 16
        returnCount += numberDone
        return (returnTest, returnCount)

    def testDone(self, progress):
        numberDone = progress & pow(2, 16) - 1
        print 'Quest number done %s' % numberDone
        if numberDone >= self.getNumItems():
            return 1
        else:
            return 0

    def getNumQuestItems(self):
        return self.getNumItems()

    def getNumItems(self):
        return self.quest[1]

    def getItem(self):
        return self.quest[2]

    def getPercentChance(self):
        return self.quest[3]

    def getHolder(self):
        return self.quest[4]

    def getHolderType(self):
        if len(self.quest) == 5:
            return 'type'
        else:
            return self.quest[5]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        forwardProgress = toonProgress & pow(2, 16) - 1
        questComplete = forwardProgress >= self.getNumItems()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumItems() == 1:
            return ''
        else:
            progress = questDesc[4] & pow(2, 16) - 1
            return TTLocalizer.QuestsRecoverItemQuestProgress % {'progress': progress,
             'numItems': self.getNumItems()}

    def getObjectiveStrings(self):
        holder = self.getHolder()
        holderType = self.getHolderType()
        if holder == Any:
            holderName = TTLocalizer.TheCogs
        elif holder == AnyFish:
            holderName = TTLocalizer.AFish
        elif holderType == 'type':
            holderName = SuitBattleGlobals.SuitAttributes[holder]['pluralname']
        elif holderType == 'level':
            holderName = TTLocalizer.QuestsRecoverItemQuestHolderString % {'level': TTLocalizer.Level,
             'holder': holder,
             'cogs': TTLocalizer.Cogs}
        elif holderType == 'track':
            if holder == 'c':
                holderName = TTLocalizer.BossbotP
            elif holder == 's':
                holderName = TTLocalizer.SellbotP
            elif holder == 'm':
                holderName = TTLocalizer.CashbotP
            elif holder == 'l':
                holderName = TTLocalizer.LawbotP
            elif holder == 'g':
                holderName = TTLocalizer.BoardbotP
        elif not holder:
            print("WHY THE HELL IS THERE NO HOLDER BARKS")
            return [itemName, "BARKS FRICKING FIX"]
        item = self.getItem()
        num = self.getNumItems()
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
             'name': ItemDict[item][1]}
        if not holderName:
            holderName = 'Unknown holderName!'
        return [itemName, holderName]

    def getString(self):
        return TTLocalizer.QuestsRecoverItemQuestString % {'item': self.getObjectiveStrings()[0],
         'holder': self.getObjectiveStrings()[1]}

    def getSCStrings(self, toNpcId, progress):
        item = self.getItem()
        num = self.getNumItems()
        forwardProgress = progress & pow(2, 16) - 1
        if forwardProgress >= self.getNumItems():
            if num == 1:
                itemName = ItemDict[item][2] + ItemDict[item][0]
            else:
                itemName = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
                 'name': ItemDict[item][1]}
            if toNpcId == ToonHQ:
                strings = [TTLocalizer.QuestsRecoverItemQuestReturnToHQSCString % itemName, TTLocalizer.QuestsRecoverItemQuestGoToHQSCString]
            elif toNpcId:
                npcName, hoodName, buildingArticle, buildingName, toStreet, streetName, isInPlayground = getNpcInfo(toNpcId)
                strings = [TTLocalizer.QuestsRecoverItemQuestReturnToSCString % {'item': itemName,
                  'npcName': npcName}]
                if isInPlayground:
                    strings.append(TTLocalizer.QuestsRecoverItemQuestGoToPlaygroundSCString % hoodName)
                else:
                    strings.append(TTLocalizer.QuestsRecoverItemQuestGoToStreetSCString % {'to': toStreet,
                     'street': streetName,
                     'hood': hoodName})
                strings.extend([TTLocalizer.QuestsRecoverItemQuestVisitBuildingSCString % (buildingArticle, buildingName), TTLocalizer.QuestsRecoverItemQuestWhereIsBuildingSCString % (buildingArticle, buildingName)])
            return strings
        holder = self.getHolder()
        holderType = self.getHolderType()
        locName = self.getLocationName()
        if holder == Any:
            holderName = TTLocalizer.TheCogs
        elif holder == AnyFish:
            holderName = TTLocalizer.TheFish
        elif holderType == 'type':
            holderName = SuitBattleGlobals.SuitAttributes[holder]['pluralname']
        elif holderType == 'level':
            holderName = TTLocalizer.QuestsRecoverItemQuestHolderString % {'level': TTLocalizer.Level,
             'holder': holder,
             'cogs': TTLocalizer.Cogs}
        elif holderType == 'track':
            if holder == 'c':
                holderName = TTLocalizer.BossbotP
            elif holder == 's':
                holderName = TTLocalizer.SellbotP
            elif holder == 'm':
                holderName = TTLocalizer.CashbotP
            elif holder == 'l':
                holderName = TTLocalizer.LawbotP
            elif holder == 'g':
                holderName = TTLocalizer.BoardbotP
        if num == 1:
            itemName = ItemDict[item][2] + ItemDict[item][0]
        else:
            itemName = TTLocalizer.QuestsItemNameAndNum % {'num': TTLocalizer.getLocalNum(num),
             'name': ItemDict[item][1]}
        return TTLocalizer.QuestsRecoverItemQuestRecoverFromSCString % {'item': itemName,
         'holder': holderName,
         'loc': locName}

    def getHeadlineString(self):
        return TTLocalizer.QuestsRecoverItemQuestHeadline


class TrackChoiceQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        if npc and npcMatches(toNpcId, npc):
            return COMPLETE
        else:
            return INCOMPLETE_WRONG_NPC

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return NotChosenString

    def getString(self):
        return TTLocalizer.QuestsTrackChoiceQuestString

    def getSCStrings(self, toNpcId, progress):
        return [TTLocalizer.QuestsTrackChoiceQuestSCString] + getVisitSCStrings(toNpcId)

    def getHeadlineString(self):
        return TTLocalizer.QuestsTrackChoiceQuestHeadline


class FriendQuest(Quest):
    def filterFunc(avatar):
        if len(avatar.getFriendsList()) == 0:
            return 1
        else:
            return 0

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1 or len(av.getFriendsList()) > 0
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsFriendQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsFriendQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsFriendQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsFriendQuestString]

    def doesFriendCount(self, av, otherAv):
        return 1


class FriendNewbieQuest(FriendQuest, NewbieQuest):
    def filterFunc(avatar):
        return 1

    filterFunc = staticmethod(filterFunc)

    def __init__(self, id, quest):
        FriendQuest.__init__(self, id, quest)
        self.checkNumFriends(self.quest[0])
        self.checkNewbieLevel(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumFriends()

    def getNumFriends(self):
        return self.quest[0]

    def getNewbieLevel(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumFriends()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumFriends() == 1:
            return ''
        else:
            return TTLocalizer.QuestsFriendNewbieQuestProgress % {'progress': questDesc[4],
             'numFriends': self.getNumFriends()}

    def getString(self):
        return TTLocalizer.QuestsFriendNewbieQuestObjective % self.getNumFriends()

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsFriendNewbieQuestString % (self.getNumFriends(), self.getNewbieLevel())]

    def doesFriendCount(self, av, otherAv):
        if otherAv != None and otherAv.getMaxHp() <= self.getNewbieLevel():
            return 1
        return 0


class TrolleyQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsFriendQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsTrolleyQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsTrolleyQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsTrolleyQuestString]


class MailboxQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsMailboxQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsMailboxQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsMailboxQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsMailboxQuestString]


class PhoneQuest(Quest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= 1
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        else:
            return ''

    def getString(self):
        return TTLocalizer.QuestsPhoneQuestString

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsPhoneQuestSCString

    def getHeadlineString(self):
        return TTLocalizer.QuestsPhoneQuestHeadline

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsPhoneQuestString]

class MinigameNewbieQuest(Quest, NewbieQuest):
    def __init__(self, id, quest):
        Quest.__init__(self, id, quest)
        self.checkNumMinigames(self.quest[0])
        self.checkNewbieLevel(self.quest[1])

    def getNumQuestItems(self):
        return self.getNumMinigames()

    def getNumMinigames(self):
        return self.quest[0]

    def getNewbieLevel(self):
        return self.quest[1]

    def getCompletionStatus(self, av, questDesc, npc = None):
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        questComplete = toonProgress >= self.getNumMinigames()
        return getCompleteStatusWithNpc(questComplete, toNpcId, npc)

    def getProgressString(self, avatar, questDesc):
        if self.getCompletionStatus(avatar, questDesc) == COMPLETE:
            return CompleteString
        elif self.getNumMinigames() == 1:
            return ''
        else:
            return TTLocalizer.QuestsMinigameNewbieQuestProgress % {'progress': questDesc[4],
             'numMinigames': self.getNumMinigames()}

    def getString(self):
        return TTLocalizer.QuestsMinigameNewbieQuestObjective % self.getNumMinigames()

    def getObjectiveStrings(self):
        return [TTLocalizer.QuestsMinigameNewbieQuestString % self.getNumMinigames()]

    def getHeadlineString(self):
        return TTLocalizer.QuestsNewbieQuestHeadline

    def getSCStrings(self, toNpcId, progress):
        if progress:
            return getFinishToonTaskSCStrings(toNpcId)
        return TTLocalizer.QuestsTrolleyQuestSCString

    def doesMinigameCount(self, av, avList):
        newbieHp = self.getNewbieLevel()
        points = 0
        for toon in avList:
            if toon != av and toon.getMaxHp() <= newbieHp:
                points += 1

        return points


DefaultDialog = {GREETING: DefaultGreeting,
 QUEST: DefaultQuest,
 INCOMPLETE: DefaultIncomplete,
 INCOMPLETE_PROGRESS: DefaultIncompleteProgress,
 INCOMPLETE_WRONG_NPC: DefaultIncompleteWrongNPC,
 COMPLETE: DefaultComplete,
 LEAVING: DefaultLeaving}

def getQuestFromNpcId(id):
    return QuestDict.get(id)[QuestDictFromNpcIndex]


def getQuestToNpcId(id):
    return QuestDict.get(id)[QuestDictToNpcIndex]


def getQuestDialog(id):
    return QuestDict.get(id)[QuestDictDialogIndex]


def getQuestReward(id, av):
    baseRewardId = QuestDict.get(id)[QuestDictRewardIndex]
    return transformReward(baseRewardId, av)


def isQuestJustForFun(questId, rewardId):
    return False


NoRewardTierZeroQuests = (101,
 110,
 121,
 131,
 141,
 160,
 161,
 162,
 163)
RewardTierZeroQuests = ()
PreClarabelleQuestIds = NoRewardTierZeroQuests + RewardTierZeroQuests
'''
FORMAT:
Index 0: Required quests, goes by FIRST QUEST IN CHAIN, so if you have a 3 part task chain, 1>2>3, put 1 in here, that is the one that gets recorded.
Index 1: Start or Cont goes here, Start indicates first task in chain
Index 2: The Quest class, simple stuff
Index 3: Starting NPC, used to determine who is going where
Index 4: To NPC, used to determine which npc the task gets handed to
Index 5: The reward, set this to 0 or NA unless it is a teleportation or special reward, we won't be using this often
Index 6: Next quest in chain
Index 7: Dialog
Index 8: Amount of EXP rewarded from completion of quest, this MUST BE DECLARED ON EACH PART OF CHAIN
Index 9: Amount of JBs rewarded from completion of quest, this MUST BE DECLARED ON EACH PART OF CHAIN
'''
# BEGIN OF TASKLINE
QuestDict = {
# Tutorial Quest
 101: ([], Start, (CogQuest, Anywhere, 1, Any), 20000, 20002, NA, 102, TTLocalizer.QuestDialogDict[164], 10, 5),
 102: ([], Cont, (VisitQuest,), 20002, 2001, NA, NA, TTLocalizer.QuestDialogDict[164], 10, 5),
 
# Task Zero
 2000: ([], Start, (VisitQuest,), 2001, 2112, NA, 2001, TTLocalizer.QuestDialogDict[2000], 300, 35),
 2001: ([], Cont, (RecoverItemQuest, Anywhere, 5, 2001, Easy, Any, 'type'), 2112, 2112, NA, 2002, TTLocalizer.QuestDialogDict[2001], 300, 35),
 2002: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2002, Easy, Any, 'type'), 2112, 2112, NA, 2003, TTLocalizer.QuestDialogDict[2002], 300, 35),
 2003: ([], Cont, (VisitQuest,), 2112, 2301, NA, 2004, TTLocalizer.QuestDialogDict[2003], 300, 35),
 2004: ([], Cont, (VisitQuest,), 2301, 2112, NA, NA, TTLocalizer.QuestDialogDict[2004], 300, 35),
 
 
# Task One
 2010: ([], Start, (VisitQuest, ), 2001, 2405, NA, 2011, TTLocalizer.QuestDialogDict[2010], 300, 10),
 2011: ([], Cont, (RecoverItemQuest, Anywhere, 4, 2003, 30, AnyFish), 2405, 2405, NA, 2012, TTLocalizer.QuestDialogDict[2011], 300, 10),
 2012: ([], Cont, (RecoverItemQuest, Anywhere, 4, 2004, 30, AnyFish), 2405, 2405, NA, 2013, TTLocalizer.QuestDialogDict[2012], 300, 10),
 2013: ([], Cont, (RecoverItemQuest, Anywhere, 4, 2005, 30, AnyFish), 2405, 2405, NA, 2014, TTLocalizer.QuestDialogDict[2013], 300, 10),
 2014: ([], Cont, (DeliverGagQuest, 5, 5, 1), 2405, 2405, NA, 2015, TTLocalizer.QuestDialogDict[2014], 300, 10),
 2015: ([], Cont, (DeliverGagQuest, 5, 4, 1), 2405, 2405, NA, 2016, TTLocalizer.QuestDialogDict[2015], 300, 10),
 2016: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2006, 20, Any, 'type'), 2405, 2405, NA, 2017, TTLocalizer.QuestDialogDict[2016], 300, 10),
 2017: ([], Cont, (RecoverItemQuest, Anywhere, 3, 2007, 30, 'cc', 'type'), 2405, 2405, NA, 2018, TTLocalizer.QuestDialogDict[2017], 300, 10),
 2018: ([], Cont, (DeliverItemQuest, 2008), 2405, 2001, NA, NA, TTLocalizer.QuestDialogDict[2018], 300, 10),

 # Task Two
 2020: ([], Start, (VisitQuest,), 2001, 2136, NA, 2021, TTLocalizer.QuestDialogDict[2020], 300, 35),
 2021: ([], Cont, (RecoverItemQuest, Anywhere, 3, 2009, Easy, 'pp', 'type'), 2136, 2136, NA, 2022, TTLocalizer.QuestDialogDict[2021], 300, 35),
 2022: ([], Cont, (RecoverItemQuest, Anywhere, 3, 2010, Easy, 'p', 'type'), 2136, 2136, NA, 2023, TTLocalizer.QuestDialogDict[2022], 300, 35), 
 2023: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2011, Easy, 'b', 'type'), 2136, 2136, NA, 2024, TTLocalizer.QuestDialogDict[2023], 300, 35),
 2024: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2012, Easy, 'ca', 'type'), 2136, 2136, NA, 2025, TTLocalizer.QuestDialogDict[2024], 300, 35),
 2025: ([], Cont, (RecoverItemQuest, Anywhere, 3, 2013, Easy, 'tm', 'type'), 2136, 2136, NA, 2026, TTLocalizer.QuestDialogDict[2025], 300, 35),
 2026: ([], Cont, (DeliverItemQuest, 2014), 2136, 2002, NA, 2027, TTLocalizer.QuestDialogDict[2026], 300, 35),
 2027: ([], Cont, (DeliverItemQuest, 2015), 2002, 2136, NA, 2028, TTLocalizer.QuestDialogDict[2027], 300, 35),
 2028: ([], Cont, (CogTrackQuest, Anywhere, 10, 'm'), 2136, 2136, NA, 2029, TTLocalizer.QuestDialogDict[2028], 300, 35),
 2029: ([], Cont, (DeliverItemQuest, 2014), 2136, 2001, NA, NA, TTLocalizer.QuestDialogDict[2029], 300, 35),
 
 # Task Three
 2030: ([], Start, (VisitQuest,), 2001, 2003, NA, (2031, 2032, 2033, 2034), TTLocalizer.QuestDialogDict[2030], 300, 35),
 2031: ([], Cont, (CogTrackQuest, Anywhere, 5, 's'), 2003, Same, NA, 2035, TTLocalizer.QuestDialogDict[2031], 300, 35),
 2032: ([], Cont, (CogTrackQuest, Anywhere, 5, 'm'), Same, Same, NA, 2035, TTLocalizer.QuestDialogDict[2032], 300, 35),
 2033: ([], Cont, (CogTrackQuest, Anywhere, 5, 'l'), Same, Same, NA, 2035, TTLocalizer.QuestDialogDict[2033], 300, 35),
 2034: ([], Cont, (CogTrackQuest, Anywhere, 5, 'c'), Same, Same, NA, 2035, TTLocalizer.QuestDialogDict[2034], 300, 35),
 2035: ([], Cont, (CogTrackQuest, Anywhere, 5, 'g'), Same, Same, NA, 2036, TTLocalizer.QuestDialogDict[2035], 300, 35),
 2036: ([], Cont, (CogLevelQuest, Anywhere, 5, 2), Same, Same, NA, 2037, TTLocalizer.QuestDialogDict[2036], 300, 35),
 2037: ([], Cont, (EliteCogQuest, Anywhere, 5), Same, Same, NA, 2038, TTLocalizer.QuestDialogDict[2037], 300, 35),
 2038: ([], Cont, (CogLevelQuest, Anywhere, 2, 4), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[2038], 300, 35),
 
 # Task Four
 2040: ([], Start, (VisitQuest,), 2001, 2201, NA, 2041, TTLocalizer.QuestDialogDict[2040], 370, 70),
 2041: ([], Cont, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 5, 2016, Medium, 3, 'level'), 2201, 2201, NA, 2042, TTLocalizer.QuestDialogDict[2041], 370, 70),
 2042: ([], Cont, (DeliverItemQuest, 2016), 2201, 2404, NA, 2043, TTLocalizer.QuestDialogDict[2042], 370, 70),
 2043: ([], Cont, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 7, 2017, Easy, 'g', 'track'), 2404, 2404, NA, 2044, TTLocalizer.QuestDialogDict[2043], 370, 70),
 2044: ([], Cont, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 3, 2018, Easy, 'c', 'track'), 2404, 2404, NA, 2045, TTLocalizer.QuestDialogDict[2044], 370, 70),
 2045: ([], Cont, (RecoverItemQuest, ToontownGlobals.ToontownCentral, 1, 2019, Easy, 'cn', 'type'), 2404, 2404, NA, 2046, TTLocalizer.QuestDialogDict[2045], 370, 70),
 2046: ([], Cont, (DeliverItemQuest, 2016), 2404, 2209, NA, NA, TTLocalizer.QuestDialogDict[2046], 370, 70),

 # Task Five
 2050: ([], Start, (DeliverItemQuest, 2016), 2001, 2416, NA, 2051, TTLocalizer.QuestDialogDict[2050], 385, 20),
 2051: ([], Cont, (DeliverItemQuest, 2016), 2416, 2415, NA, 2052, TTLocalizer.QuestDialogDict[2051], 385, 20),
 2052: ([], Cont, (DeliverItemQuest, 2016), 2415, 2416, NA, 2053, TTLocalizer.QuestDialogDict[2052], 385, 20),
 2053: ([], Cont, (DeliverItemQuest, 2016), 2416, 2201, NA, 2054, TTLocalizer.QuestDialogDict[2053], 385, 20),
 2054: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2020, Easy, 'g', 'track'), 2416, 2201, NA, 2055, TTLocalizer.QuestDialogDict[2054], 385, 20),
 2055: ([], Cont, (DeliverItemQuest, 2016), 2201, 2415, NA, 2056, TTLocalizer.QuestDialogDict[2055], 385, 20),
 2056: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2021, Easy, 'f', 'type'), 2416, 2201, NA, 2057, TTLocalizer.QuestDialogDict[2056], 385, 20),
 2057: ([], Cont, (DeliverItemQuest, 2022), 2415, 2416, NA, 2058, TTLocalizer.QuestDialogDict[2057], 385, 20),
 2058: ([], Cont, (CogLevelQuest, 2400, 5, 2), 2416, 2416, NA, 2059, TTLocalizer.QuestDialogDict[2058], 385, 20),
 2059: ([], Cont, (CogLevelQuest, ToontownGlobals.ToontownCentral, 4, 4), 2416, 2416, NA, NA, TTLocalizer.QuestDialogDict[2059], 385, 20),

 # Task Six
 2060: ([], Start, (VisitQuest,), 2001, 2318, NA, 2061, TTLocalizer.QuestDialogDict[2060], 350, 35),
 2061: ([], Cont, (CogTrackLevelQuest, Anywhere, 5, 'c', 3), 2318, 2318, NA, 2062, TTLocalizer.QuestDialogDict[2061], 350, 35),
 2062: ([], Cont, (CogTrackQuest, Anywhere, 10, 'l'), 2318, 2318, NA, 2063, TTLocalizer.QuestDialogDict[2062], 350, 35),
 2063: ([], Cont, (CogLevelQuest, Anywhere, 6, 2), 2318, 2318, NA, NA, TTLocalizer.QuestDialogDict[2063], 350, 35),

 # Task Seven
 2070: ([], Start, (VisitQuest,), 2001, 2402, NA, (2071, 2072, 2073, 2074), TTLocalizer.QuestDialogDict[2070], 375, 50),
 2071: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2016, Medium, 's', 'track'), 2402, 2402, NA, (2075, 2076), TTLocalizer.QuestDialogDict[2071], 375, 50),
 2072: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2016, Medium, 'm', 'track'), 2402, 2402, NA, (2075, 2076), TTLocalizer.QuestDialogDict[2072], 375, 50),
 2073: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2016, Medium, 'l', 'track'), 2402, 2402, NA, (2075, 2076), TTLocalizer.QuestDialogDict[2073], 375, 50),
 2074: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2016, Medium, 'c', 'track'), 2402, 2402, NA, (2075, 2076), TTLocalizer.QuestDialogDict[2074], 375, 50),
 2075: ([], Cont, (CogTrackQuest, Anywhere, 5, 'g'), 2402, 2402, NA, (2077, 2078), TTLocalizer.QuestDialogDict[2075], 375, 50),
 2076: ([], Cont, (CogTrackQuest, Anywhere, 5, 's'), 2402, 2402, NA, (2077, 2078), TTLocalizer.QuestDialogDict[2076], 375, 50),
 2077: ([], Cont, (CogQuest, Anywhere, 2, 'mdm'), 2402, 2402, NA, 2079, TTLocalizer.QuestDialogDict[2077], 375, 50),
 2078: ([], Cont, (CogQuest, Anywhere, 2, 'gh'), 2402, 2402, NA, 2079, TTLocalizer.QuestDialogDict[2078], 375, 50),
 2079: ([], Cont, (DeliverItemQuest, 2027), 2402, 2128, NA, NA, TTLocalizer.QuestDialogDict[2079], 375, 50),

 # Task Eight
 2080: ([], Start, (TrackExpQuest, Anywhere, 4, 20), 2001, 2001, NA, 2081, TTLocalizer.QuestDialogDict[2080], 350, 50),
 2081: ([], Cont, (TrackExpQuest, Anywhere, 5, 20), 2001, 2001, NA, 2082, TTLocalizer.QuestDialogDict[2081], 350, 50),
 2082: ([], Cont, (DeliverGagQuest, 1, 4, 2), 2001, 2117, NA, 2083, TTLocalizer.QuestDialogDict[2082], 350, 50),
 2083: ([], Cont, (DeliverGagQuest, 1, 5, 2), 2117, 2123, NA, 2084, TTLocalizer.QuestDialogDict[2083], 350, 50),
 2084: ([], Cont, (VisitQuest,), 2123, 2001, NA, 2085, TTLocalizer.QuestDialogDict[2084], 350, 50),
 2085: ([], Cont, (CogQuest, Anywhere, 5, Any), 2001, 2001, NA, 2086, TTLocalizer.QuestDialogDict[2085], 350, 50),
 2086: ([], Cont, (CogLevelQuest, Anywhere, 3, 4), 2001, 2001, NA, NA, TTLocalizer.QuestDialogDict[2086], 350, 50),
 
 # Task Nine
 2090: ([], Start, (VisitQuest,), 2001, 2208, NA, 2091, TTLocalizer.QuestDialogDict[2090], 375, 25),
 2091: ([], Cont, (CogQuest, ToontownGlobals.ToontownCentral, 30, Any), 2208, 2208, NA, 2092, TTLocalizer.QuestDialogDict[2091], 375, 25),
 2092: ([], Cont, (CogLevelQuest, 2400, 4, 2), 2208, 2208, NA, 2093, TTLocalizer.QuestDialogDict[2092], 375, 25),
 2093: ([], Cont, (CogLevelQuest, 2300, 3, 3), 2208, 2208, NA, 2094, TTLocalizer.QuestDialogDict[2093], 375, 25),
 2094: ([], Cont, (CogLevelQuest, 2100, 2, 4), 2208, 2208, NA, 2095, TTLocalizer.QuestDialogDict[2094], 375, 25),
 2095: ([], Cont, (CogLevelQuest, 2200, 2, 4), 2208, 2208, NA, 2096, TTLocalizer.QuestDialogDict[2095], 375, 25),
 2096: ([], Cont, (RecoverItemQuest, 2200, 1, 2028, Medium, 4, 'level'), 2208, 2208, NA, NA, TTLocalizer.QuestDialogDict[2096], 375, 25),

 # Task Ten
 2100: ([], Start, (VisitQuest,), 2001, 2222, NA, 2101, TTLocalizer.QuestDialogDict[2100], 375, 35),
 2101: ([], Cont, (CogLevelQuest, ToontownGlobals.ToontownCentral, 5, 3), 2222, 2222, NA, (2102, 2103, 2104), TTLocalizer.QuestDialogDict[2101], 375, 35),
 2102: ([], Cont, (CogTrackQuest, ToontownGlobals.ToontownCentral, 10, 'l'), 2222, 2222, NA, (2105, 2106), TTLocalizer.QuestDialogDict[2102], 375, 35),
 2103: ([], Cont, (CogTrackQuest, ToontownGlobals.ToontownCentral, 10, 'c'), 2222, 2222, NA, (2105, 2106), TTLocalizer.QuestDialogDict[2103], 375, 35),
 2104: ([], Cont, (CogTrackQuest, ToontownGlobals.ToontownCentral, 10, 'g'), 2222, 2222, NA, (2105, 2106), TTLocalizer.QuestDialogDict[2104], 375, 35),
 2105: ([], Cont, (CogTrackLevelQuest, Anywhere, 3, 's', 4), 2222, 2222, NA, 2107, TTLocalizer.QuestDialogDict[2105], 375, 35),
 2106: ([], Cont, (CogTrackLevelQuest, Anywhere, 3, 'm', 4), 2222, 2222, NA, 2107, TTLocalizer.QuestDialogDict[2106], 375, 35),
 2107: ([], Cont, (CogQuest, ToontownGlobals.ToontownCentral, 10, Any), 2222, 2222, NA, NA, TTLocalizer.QuestDialogDict[2107], 375, 35),
 
 # Task Eleven
 2110: ([], Start, (VisitQuest,), 2001, 2413, NA, 2111, TTLocalizer.QuestDialogDict[2110], 325, 50),
 2111: ([], Cont, (RecoverItemQuest, Anywhere, 10, 2029, Easy, Any, 'type'),2413, 2413, NA, 2112, TTLocalizer.QuestDialogDict[2111], 325, 50),
 2112: ([], Cont, (DeliverItemQuest, 2030), 2413, 2312, NA, 2113, TTLocalizer.QuestDialogDict[2112], 325, 50),
 2113: ([], Cont, (VisitQuest,), 2413, 2303, NA, 2114, TTLocalizer.QuestDialogDict[2113], 325, 50),
 2114: ([], Cont, (CogQuest, Anywhere, 5, 'ac'), 2303, 2303, NA, 2115, TTLocalizer.QuestDialogDict[2114], 325, 50),
 2115: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2031, Medium, 'ac', 'type'), 2303, 2303, NA, 2116, TTLocalizer.QuestDialogDict[2115], 325, 50),
 2116: ([], Cont, (VisitQuest,), 2303, 2128, NA, 2117, TTLocalizer.QuestDialogDict[2116], 325, 50),
 2117: ([], Cont, (RecoverItemQuest, Anywhere, 4, 2032, Easy, AnyFish), 2128, 2128, NA, 2118, TTLocalizer.QuestDialogDict[2117], 325, 50),
 2118: ([], Cont, (RecoverItemQuest, Anywhere, 1, 2033, Medium, 4, 'level'), 2128, 2128, NA, NA, TTLocalizer.QuestDialogDict[2118], 325, 50),
 
 # Task Twelve, MEGATASK OF ZONE
 2120: ([2118, 2096, 2086, 2079, 2063, 2059, 2046, 2038, 2029, 2018, 2004], Start, (VisitQuest,), 2001, 2216, NA, 2121, TTLocalizer.QuestDialogDict[2120], 500, 75),
 2121: ([], Cont, (RecoverItemQuest, Anywhere, 4, 2034, Medium, AnyFish), 2216, 2216, NA, 2122, TTLocalizer.QuestDialogDict[2121], 500, 75),
 2122: ([], Cont, (RecoverItemQuest, Anywhere, 4, 2035, VeryEasy, 'gh', 'type'), 2216, 2216, NA, 2123, TTLocalizer.QuestDialogDict[2122], 500, 75),
 2123: ([], Cont, (DeliverItemQuest, Anywhere, 2035), 2216, 2001, NA, 2124, TTLocalizer.QuestDialogDict[2123], 500, 75),
 2124: ([], Cont, (VisitQuest,), 2001, 2216, NA, 2125, TTLocalizer.QuestDialogDict[2124], 500, 75),
 2125: ([], Cont, (DeliverItemQuest, 2035), 2216, 2226, NA, 2126, TTLocalizer.QuestDialogDict[2125], 500, 75),
 2126: ([], Cont, (CogLevelQuest, ToontownGlobals.ToontownCentral, 8, 4), 2226, 2226, NA, 2127, TTLocalizer.QuestDialogDict[2126], 500, 75),
 2127: ([], Cont, (EliteCogQuest, ToontownGlobals.ToontownCentral, 10), 2226, 2226, NA, 2128, TTLocalizer.QuestDialogDict[2127], 500, 75),
 2128: ([], Cont, (BuildingQuest, Anywhere, 1, Any, 1), 2226, 2226, NA, 2129, TTLocalizer.QuestDialogDict[2128], 500, 75),
 2129: ([], Cont, (VisitQuest,), 2226, 2216, NA, 2130, TTLocalizer.QuestDialogDict[2129], 500, 75),
 2130: ([], Cont, (DeliverItemQuest, Anywhere, 2035), 2216, 2201, NA, 2131, TTLocalizer.QuestDialogDict[2130], 500, 75),
 2131: ([], Cont, (RecoverItemQuest, Anywhere, 15, 2036, VeryEasy, AnyFish), 2201, 2201, NA, 2132, TTLocalizer.QuestDialogDict[2131], 500, 75),
 2132: ([], Cont, (VisitQuest,), 2201, 2216, NA, 2133, TTLocalizer.QuestDialogDict[2132], 500, 75),
 2133: ([], Cont, (DeliverItemQuest, Anywhere, 2035), 2216, 2201, NA, 2134, TTLocalizer.QuestDialogDict[2133], 500, 75),
 2134: ([], Cont, (RecoverItemQuest, Anywhere, 10, 2016, Easy, 4, 'level'), 2201, 2201, NA, 2135, TTLocalizer.QuestDialogDict[2134], 500, 75),
 2135: ([], Cont, (VisitQuest,), 2201, 2216, NA, 2136, TTLocalizer.QuestDialogDict[2135], 500, 75),
 2136: ([], Cont, (BuildingQuest, Anywhere, 1, Any, 2), 2216, 2216, 300, NA, TTLocalizer.QuestDialogDict[2136], 500, 75),
 
 #AA Task One
 3000: ([2136], Start, (VisitQuest,), 6006, 6114, NA, 3001, TTLocalizer.QuestDialogDict[3000], 3210, 100),
 3001: ([], Cont, (DeliverItemQuest, 6001), 6114, 6111, NA, 3002, TTLocalizer.QuestDialogDict[3001], 3210, 100),
 3002: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 10, 6002, Easy, Any), 6111, Same, NA, 3003, TTLocalizer.QuestDialogDict[3002], 3210, 100),
 3003: ([], Cont, (VisitQuest,), Same, 6114, NA, 3004, TTLocalizer.QuestDialogDict[3003], 3210, 100),
 3004: ([], Cont, (VisitQuest,), 6114, 6414, NA, 3005, TTLocalizer.QuestDialogDict[3004], 3210, 100),
 3005: ([], Cont, (CogTrackQuest, ToontownGlobals.OutdoorZone, 13, 'm'), 6414, Same, NA, 3006, TTLocalizer.QuestDialogDict[3005], 3210, 100),
 3006: ([], Cont, (CogLevelQuest, 6400, 12, 4), Same, Same, NA, 3007, TTLocalizer.QuestDialogDict[3006], 3210, 100),
 3007: ([], Cont, (VisitQuest,), Same, 6114, NA, NA, TTLocalizer.QuestDialogDict[3007], 3210, 100),
 
 #AA Task Two
 3010: ([2136], Start, (VisitQuest,), 6005, 6403, NA, 3011, TTLocalizer.QuestDialogDict[3010], 3220, 100),
 3011: ([], Cont, (CogQuest, Anywhere, 5, 'sw'), 6403, Same, NA, 3012, TTLocalizer.QuestDialogDict[3011], 3220, 100),
 3012: ([], Cont, (CogTrackQuest, Anywhere, 10, 'g'), Same, Same, NA, (3013, 3015), TTLocalizer.QuestDialogDict[3012], 3220, 100),
 3013: ([], Cont, (CogQuest, Anywhere, 5, 'b'), Same, Same, NA, 3014, TTLocalizer.QuestDialogDict[3013], 3220, 100),
 3014: ([], Cont, (CogTrackLevelQuest, Anywhere, 5, 'l', 5), Same, Same, NA, 3017, TTLocalizer.QuestDialogDict[3014], 3220, 100),
 3015: ([], Cont, (CogQuest, Anywhere, 5, 'pp'), Same, Same, NA, 3016, TTLocalizer.QuestDialogDict[3015], 3220, 100),
 3016: ([], Cont, (CogTrackLevelQuest, Anywhere, 5, 'm', 5), Same, Same, NA, 3017, TTLocalizer.QuestDialogDict[3016], 3220, 100),
 3017: ([], Cont, (CogQuest, Anywhere, 20), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[3017], 3220, 100),
 
 #AA Task Three
 3020: ([2136], Start, (VisitQuest,), 6004, 6211, NA, 3021, TTLocalizer.QuestDialogDict[3020], 3200, 100),
 3021: ([], Cont, (RecoverItemQuest, Anywhere, 1, 6003, 25, 'tw', 'type'), 6211, Same, NA, 3022, TTLocalizer.QuestDialogDict[3021], 3200, 100),
 3022: ([], Cont, (EliteCogQuest, ToontownGlobals.OutdoorZone, 8), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[3022], 3200, 100),
 
 #AA Task Four
 3030: ([2136], Start, (VisitQuest,), 6007, 6401, NA, 3031, TTLocalizer.QuestDialogDict[3030], 3230, 110),
 3031: ([], Cont, (CogQuest, Anywhere, 8, 'ac'), 6401, Same, NA, 3032, TTLocalizer.QuestDialogDict[3031], 3230, 110),
 3032: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 1, 6004, 25, 'l', 'track'), Same, Same, NA, 3033, TTLocalizer.QuestDialogDict[3032], 3230, 110),
 3033: ([], Cont, (DeliverItemQuest, 6004), Same, 6409, NA, 3034, TTLocalizer.QuestDialogDict[3033], 3230, 110),
 3034: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 10, 6005, Easy, Any), 6409, Same, NA, 3035, TTLocalizer.QuestDialogDict[3034], 3230, 110),
 3035: ([], Cont, (VisitQuest,), Same, 6401, NA, 3036, TTLocalizer.QuestDialogDict[3035], 3230, 110),
 3036: ([], Cont, (CogTrackLevelQuest, Anywhere, 9, 'l', 5), 6401, Same, NA, NA, TTLocalizer.QuestDialogDict[3036], 3230, 110),
 
 #AA Task Five
 3040: ([2136], Start, (VisitQuest,), 6006, 6110, NA, 3041, TTLocalizer.QuestDialogDict[3040], 3210, 100),
 3041: ([], Cont, (VisitQuest,), 6110, 6215, NA, 3042, TTLocalizer.QuestDialogDict[3041], 3210, 100),
 3042: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 10, 6006, Easy, 's', 'track'), 6215, Same, NA, 3043, TTLocalizer.QuestDialogDict[3042], 3210, 100),
 3043: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 8, 6007, Easy, 'l', 'track'), Same, Same, NA, 3044, TTLocalizer.QuestDialogDict[3043], 3210, 100),
 3044: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 5, 6008, Medium, 5, 'level'), Same, Same, NA, 3045, TTLocalizer.QuestDialogDict[3044], 3210, 100),
 3045: ([], Cont, (DeliverItemQuest, 6009), Same, 6110, NA, NA, TTLocalizer.QuestDialogDict[3045], 3210, 100),
 
 #AA Task Six
 3050: ([2136], Start, (VisitQuest,), 6005, 6101, NA, 3051, TTLocalizer.QuestDialogDict[3050], 3220, 110),
 3051: ([], Cont, (VisitQuest,), 6101, 6103, NA, 3052, TTLocalizer.QuestDialogDict[3051], 3220, 110),
 3052: ([], Cont, (CogLevelQuest, 6100, 9, 6), 6103, Same, NA, 3053, TTLocalizer.QuestDialogDict[3052], 3220, 110),
 3053: ([], Cont, (VisitQuest,), Same, 6101, NA, 3054, TTLocalizer.QuestDialogDict[3053], 3220, 110),
 3054: ([], Cont, (VisitQuest,), 6101, 6105, NA, 3055, TTLocalizer.QuestDialogDict[3054], 3220, 110),
 3055: ([], Cont, (CogTrackQuest, 6100, 10, 'g'), 6105, Same, NA, 3056, TTLocalizer.QuestDialogDict[3055], 3220, 110),
 3056: ([], Cont, (VisitQuest,), Same, 6101, NA, 3057, TTLocalizer.QuestDialogDict[3056], 3220, 110),
 3057: ([], Cont, (VisitQuest,), 6101, 6108, NA, 3058, TTLocalizer.QuestDialogDict[3057], 3220, 110),
 3058: ([], Cont, (BuildingQuest, ToontownGlobals.OutdoorZone, 1, Any, 3), 6108, Same, NA, 3059, TTLocalizer.QuestDialogDict[3058], 3220, 110),
 3059: ([], Cont, (VisitQuest,), Same, 6101, NA, NA, TTLocalizer.QuestDialogDict[3059], 3220, 110),
 
 #AA Task Seven
 3060: ([2136], Start, (VisitQuest,), 6004, 6212, NA, 3061, TTLocalizer.QuestDialogDict[3060], 3200, 100),
 3061: ([], Cont, (RecoverItemQuest, ToontownGlobals.OutdoorZone, 15, 6010, Easy, Any), 6212, Same, NA, NA, TTLocalizer.QuestDialogDict[3061], 3200, 100),
 
 #AA Task Eight
 3070: ([2136], Start, (VisitQuest,), 6007, 6408, NA, 3071, TTLocalizer.QuestDialogDict[3070], 3230, 120),
 3071: ([], Cont, (CogQuest, Anywhere, 7, 'ds'), 6408, Same, NA, 3072, TTLocalizer.QuestDialogDict[3071], 3230, 120),
 3072: ([], Cont, (CogQuest, Anywhere, 7, 'txm'), Same, Same, NA, 3073, TTLocalizer.QuestDialogDict[3072], 3230, 120),
 3073: ([], Cont, (BuildingQuest, Anywhere, 3, Any, 2), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[3073], 3230, 120),
 
 #AA Task Nine
 3080: ([2136], Start, (VisitQuest,), 6006, 6406, NA, 3081, TTLocalizer.QuestDialogDict[3080], 3210, 110),
 3081: ([], Cont, (CogQuest, Anywhere, 9, 'cc'), 6406, Same, NA, 3082, TTLocalizer.QuestDialogDict[3081], 3210, 110),
 3082: ([], Cont, (CogQuest, Anywhere, 8, 'tw'), Same, Same, NA, 3083, TTLocalizer.QuestDialogDict[3082], 3210, 110),
 3083: ([], Cont, (CogLevelQuest, Anywhere, 10, 6), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[3083], 3210, 110),
 
 #AA Task Ten
 3090: ([2136], Start, (VisitQuest,), 6005, 6404, NA, (3091, 3092, 3093, 3094, 3095), TTLocalizer.QuestDialogDict[3090], 3220, 130),
 3091: ([], Cont, (CogTrackLevelQuest, Anywhere, 10, 'c', 5), 6404, Same, NA, 3096, TTLocalizer.QuestDialogDict[3091], 3220, 130),
 3092: ([], Cont, (CogTrackLevelQuest, Anywhere, 10, 'l', 5), 6404, Same, NA, 3096, TTLocalizer.QuestDialogDict[3092], 3220, 130),
 3093: ([], Cont, (CogTrackLevelQuest, Anywhere, 10, 'm', 5), 6404, Same, NA, 3096, TTLocalizer.QuestDialogDict[3093], 3220, 130),
 3094: ([], Cont, (CogTrackLevelQuest, Anywhere, 10, 's', 5), 6404, Same, NA, 3096, TTLocalizer.QuestDialogDict[3094], 3220, 130),
 3095: ([], Cont, (CogTrackLevelQuest, Anywhere, 10, 'g', 5), 6404, Same, NA, 3096, TTLocalizer.QuestDialogDict[3095], 3220, 130),
 3096: ([], Cont, (BuildingQuest, Anywhere, 2, Any, 3), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[3096], 3220, 130),
 
 #AA Task Eleven
 3100: ([2136], Start, (VisitQuest,), 6004, 6102, NA, 3101, TTLocalizer.QuestDialogDict[3100], 3200, 140),
 3101: ([], Cont, (CogLevelQuest, Anywhere, 12, 6), 6102, Same, NA, NA, TTLocalizer.QuestDialogDict[3101], 3200, 140),
 
 #AA Task Twelve
 3110: ([2136], Start, (VisitQuest,), 6007, 6309, NA, 3111, TTLocalizer.QuestDialogDict[3110], 3230, 175),
 3111: ([], Cont, (TrackExpQuest, Anywhere, 4, 100), 6309, Same, NA, 3112, TTLocalizer.QuestDialogDict[3111], 3230, 175),
 3112: ([], Cont, (TrackExpQuest, Anywhere, 5, 100), Same, Same, NA, 3113, TTLocalizer.QuestDialogDict[3112], 3230, 175),
 3113: ([], Cont, (DeliverGagQuest, 1, 4, 3), Same, Same, NA, 3114, TTLocalizer.QuestDialogDict[3113], 3230, 175),
 3114: ([], Cont, (DeliverGagQuest, 1, 5, 3), Same, Same, NA, NA, TTLocalizer.QuestDialogDict[3114], 3230, 175)
 }

Quest2RewardDict = {}
Tier2Reward2QuestsDict = {}
Quest2RemainingStepsDict = {}

def getAllRewardIdsForReward(rewardId):
    if rewardId is AnyCashbotSuitPart:
        return range(4000, 4011 + 1)
    if rewardId is AnyLawbotSuitPart:
        return range(4100, 4113 + 1)
    if rewardId is AnyBossbotSuitPart:
        return range(4200, 4216 + 1)
    return (rewardId,)


def findFinalRewardId(questId):
    finalRewardId = Quest2RewardDict.get(questId)
    if finalRewardId:
        remainingSteps = Quest2RemainingStepsDict.get(questId)
    else:
        try:
            questDesc = QuestDict[questId]
        except KeyError:
            print 'findFinalRewardId: Quest ID: %d not found' % questId
            return -1

        nextQuestId = questDesc[QuestDictNextQuestIndex]
        if nextQuestId == NA:
            finalRewardId = questDesc[QuestDictRewardIndex]
            remainingSteps = 1
        else:
            if type(nextQuestId) == type(()):
                finalRewardId, remainingSteps = findFinalRewardId(nextQuestId[0])
                for id in nextQuestId[1:]:
                    findFinalRewardId(id)

            else:
                finalRewardId, remainingSteps = findFinalRewardId(nextQuestId)
            remainingSteps += 1
        Quest2RewardDict[questId] = finalRewardId
        Quest2RemainingStepsDict[questId] = remainingSteps
    return (finalRewardId, remainingSteps)


for questId in QuestDict.keys():
    findFinalRewardId(questId)

def getStartingQuests(tier = None):
    startingQuests = []
    return startingQuests


def getFinalRewardId(questId, fAll = 0):
    if fAll or isStartingQuest(questId):
        return Quest2RewardDict.get(questId)
    else:
        return None
    return None


def isStartingQuest(questId):
    try:
        return QuestDict[questId][QuestDictStartIndex] == Start
    except KeyError:
        return None

    return None


def getNumChoices(tier):
    if tier in (0,):
        return 0
    if tier in (1,):
        return 2
    else:
        return 3


def getAvatarRewardId(av, questId):
    for quest in av.quests:
        if questId == quest[0]:
            return quest[3]

    notify.warning('getAvatarRewardId(): quest not found on avatar')
    return None


def getNextQuest(id, currentNpc, av):
    nextQuest = QuestDict[id][QuestDictNextQuestIndex]
    if nextQuest == NA:
        return (NA, NA)
    elif type(nextQuest) == type(()):
        nextReward = QuestDict[nextQuest[0]][QuestDictRewardIndex]
        nextNextQuest, nextNextToNpcId = getNextQuest(nextQuest[0], currentNpc, av)
        nextQuest = random.choice(nextQuest)
    if not getQuestClass(nextQuest).filterFunc(av):
        return getNextQuest(nextQuest, currentNpc, av)
    nextToNpcId = getQuestToNpcId(nextQuest)
    if nextToNpcId == Any:
        nextToNpcId = 2004
    elif nextToNpcId == Same:
        if currentNpc.getHq():
            nextToNpcId = ToonHQ
        else:
            nextToNpcId = currentNpc.getNpcId()
    elif nextToNpcId == ToonHQ:
        nextToNpcId = ToonHQ
    return (nextQuest, nextToNpcId)


def filterQuests(entireQuestPool, currentNpc, av):
    if notify.getDebug():
        notify.debug('filterQuests: entireQuestPool: %s' % entireQuestPool)
    validQuestPool = dict([ (questId, 1) for questId in entireQuestPool ])
    if isLoopingFinalTier(av.getRewardTier()):
        history = map(lambda questDesc: questDesc[0], av.quests)
    else:
        history = av.getQuestHistory()
    if notify.getDebug():
        notify.debug('filterQuests: av quest history: %s' % history)
    currentQuests = av.quests
    for questId in entireQuestPool:
        if questId in history:
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s because in history' % questId)
            validQuestPool[questId] = 0
            continue
        potentialFromNpc = getQuestFromNpcId(questId)
        if not npcMatches(potentialFromNpc, currentNpc):
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s: potentialFromNpc does not match currentNpc' % questId)
            validQuestPool[questId] = 0
            continue
        potentialToNpc = getQuestToNpcId(questId)
        if currentNpc.getNpcId() == potentialToNpc:
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s because potentialToNpc is currentNpc' % questId)
            validQuestPool[questId] = 0
            continue
        if not getQuestClass(questId).filterFunc(av):
            if notify.getDebug():
                notify.debug('filterQuests: Removed %s because of filterFunc' % questId)
            validQuestPool[questId] = 0
            continue
        if getQuestClass(questId) == TrackExpQuest:
            quest = QuestDict.get(questId)
            track = quest[1]
            trackAccess = av.getTrackAccess()
            if trackAccess[track] == 0:
                validQuestPool[questId] = 0
            continue
        for quest in currentQuests:
            fromNpcId = quest[1]
            toNpcId = quest[2]
            if potentialToNpc == toNpcId and toNpcId != ToonHQ:
                validQuestPool[questId] = 0
                if notify.getDebug():
                    notify.debug('filterQuests: Removed %s because npc involved' % questId)
                break

    finalQuestPool = filter(lambda key: validQuestPool[key], validQuestPool.keys())
    if notify.getDebug():
        notify.debug('filterQuests: finalQuestPool: %s' % finalQuestPool)
    return finalQuestPool

def chooseTrackChoiceQuest(tier, av, fixed = 0):

    def fixAndCallAgain():
        if not fixed and av.fixTrackAccess():
            notify.info('av %s trackAccess fixed: %s' % (av.getDoId(), trackAccess))
            return chooseTrackChoiceQuest(tier, av, fixed=1)
        else:
            return None
        return None

    bestQuest = None
    trackAccess = av.getTrackAccess()
    if tier == DG_TIER:
        if trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 1:
            bestQuest = 4002
        elif trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 1:
            bestQuest = 4001
        else:
            notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
            return fixAndCallAgain()
    elif tier == BR_TIER:
        if trackAccess[ToontownBattleGlobals.TRAP_TRACK] == 1:
            if trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 1:
                if trackAccess[ToontownBattleGlobals.DROP_TRACK] == 1:
                    bestQuest = 5004
                elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 1:
                    bestQuest = 5003
                else:
                    notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
                    return fixAndCallAgain()
            elif trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 1:
                if trackAccess[ToontownBattleGlobals.DROP_TRACK] == 1:
                    bestQuest = 5002
                elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 1:
                    bestQuest = 5001
                else:
                    notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
                    return fixAndCallAgain()
        elif trackAccess[ToontownBattleGlobals.SOUND_TRACK] == 0:
            bestQuest = 5005
        elif trackAccess[ToontownBattleGlobals.HEAL_TRACK] == 0:
            bestQuest = 5006
        elif trackAccess[ToontownBattleGlobals.DROP_TRACK] == 0:
            bestQuest = 5007
        elif trackAccess[ToontownBattleGlobals.LURE_TRACK] == 0:
            bestQuest = 5008
        else:
            notify.warning('av %s has bogus trackAccess: %s' % (av.getDoId(), trackAccess))
            return fixAndCallAgain()
    else:
        if notify.getDebug():
            notify.debug('questPool for reward 400 had no dynamic choice, tier: %s' % tier)
        bestQuest = seededRandomChoice(Tier2Reward2QuestsDict[tier][400])
    if notify.getDebug():
        notify.debug('chooseTrackChoiceQuest: avId: %s trackAccess: %s tier: %s bestQuest: %s' % (av.getDoId(),
         trackAccess,
         tier,
         bestQuest))
    return bestQuest


def chooseMatchingQuest(tier, validQuestPool, rewardId, npc, av):
    questsMatchingReward = Tier2Reward2QuestsDict[tier].get(rewardId, [])
    if notify.getDebug():
        notify.debug('questsMatchingReward: %s tier: %s = %s' % (rewardId, tier, questsMatchingReward))
    else:
        validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
        if notify.getDebug():
            notify.debug('validQuestsMatchingReward: %s tier: %s = %s' % (rewardId, tier, validQuestsMatchingReward))
        if validQuestsMatchingReward:
            bestQuest = seededRandomChoice(validQuestsMatchingReward)
        else:
            questsMatchingReward = Tier2Reward2QuestsDict[tier].get(AnyCashbotSuitPart, [])
            if notify.getDebug():
                notify.debug('questsMatchingReward: AnyCashbotSuitPart tier: %s = %s' % (tier, questsMatchingReward))
            validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
            if validQuestsMatchingReward:
                if notify.getDebug():
                    notify.debug('validQuestsMatchingReward: AnyCashbotSuitPart tier: %s = %s' % (tier, validQuestsMatchingReward))
                bestQuest = seededRandomChoice(validQuestsMatchingReward)
            else:
                questsMatchingReward = Tier2Reward2QuestsDict[tier].get(AnyLawbotSuitPart, [])
                if notify.getDebug():
                    notify.debug('questsMatchingReward: AnyLawbotSuitPart tier: %s = %s' % (tier, questsMatchingReward))
                validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
                if validQuestsMatchingReward:
                    if notify.getDebug():
                        notify.debug('validQuestsMatchingReward: AnyLawbotSuitPart tier: %s = %s' % (tier, validQuestsMatchingReward))
                    bestQuest = seededRandomChoice(validQuestsMatchingReward)
                else:
                    questsMatchingReward = Tier2Reward2QuestsDict[tier].get(Any, [])
                    if notify.getDebug():
                        notify.debug('questsMatchingReward: Any tier: %s = %s' % (tier, questsMatchingReward))
                    if not questsMatchingReward:
                        notify.warning('chooseMatchingQuests, no questsMatchingReward')
                        return None
                    validQuestsMatchingReward = PythonUtil.intersection(questsMatchingReward, validQuestPool)
                    if not validQuestsMatchingReward:
                        notify.warning('chooseMatchingQuests, no validQuestsMatchingReward')
                        return None
                    if notify.getDebug():
                        notify.debug('validQuestsMatchingReward: Any tier: %s = %s' % (tier, validQuestsMatchingReward))
                    bestQuest = seededRandomChoice(validQuestsMatchingReward)
    return bestQuest


def transformReward(baseRewardId, av):
    if baseRewardId == 900:
        trackId, progress = av.getTrackProgress()
        if trackId == -1:
            notify.warning('transformReward: asked to transform 900 but av is not training')
            actualRewardId = baseRewardId
        else:
            actualRewardId = 900 + 1 + trackId
        return actualRewardId
    elif baseRewardId > 800 and baseRewardId < 900:
        trackId, progress = av.getTrackProgress()
        if trackId < 0:
            notify.warning('transformReward: av: %s is training a track with none chosen!' % av.getDoId())
            return 601
        else:
            actualRewardId = baseRewardId + 200 + trackId * 100
            return actualRewardId
    else:
        return baseRewardId


def chooseBestQuests(currentNpc, av):
    currentQuests = av.quests
    completedQuests = av.getQuestHistory()
    completedIds = []
    currentIds = []
    for entry in completedQuests:
        completedIds.append(getFirstQuestIdInChain(entry))
    for entry in currentQuests:
        currentIds.append(getFirstQuestIdInChain(entry[0]))
    bestQuests = []
    for questId in QuestDict.keys():
        if len(bestQuests) >= 3:
            break
        questEntry = QuestDict.get(questId)
        if questEntry[QuestDictFromNpcIndex] == currentNpc.npcId:
            if questId not in completedIds + currentIds:
                # Filter out any mid-quests
                if questEntry[QuestDictStartIndex] != Start:
                    continue
                bestQuestToNpcId = getQuestToNpcId(questId)
                if bestQuestToNpcId == Any:
                    bestQuestToNpcId = 2003
                elif bestQuestToNpcId == Same:
                    if currentNpc.getHq():
                        bestQuestToNpcId = ToonHQ
                    else:
                        bestQuestToNpcId = currentNpc.getNpcId()
                elif bestQuestToNpcId == ToonHQ:
                    bestQuestToNpcId = ToonHQ
                bestQuests.append([questId, 0, bestQuestToNpcId])
            else:
                continue
        else:
            continue

    return bestQuests
	
def getFirstQuestIdInChain(questId):
    while True:
        questEntry = QuestDict.get(questId)
        if not questEntry:
            return questId
        if questEntry[QuestDictStartIndex] != Start:
            # This isn't a starting quest, so subtract one and check THAT quest
            questId -= 1
        else:
            # This IS a starting quest, return this quest id!
            return questId

def questExists(id):
    return QuestDict.has_key(id)


def getQuest(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        questDesc = questEntry[QuestDictDescIndex]
        questClass = questDesc[0]
        return questClass(id, questDesc[1:])
    else:
        return None
    return None

def getQuestExp(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        try:
            questExp = questEntry[QuestDictExperienceIndex]
            return questExp
        except:
                return 100
    else:
        return None
    return None
	
def getQuestRewardId(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        try:
            rewardId = questEntry[QuestDictRewardIndex]
            return rewardId
        except:
                return None
    else:
        return None
    return None

def getQuestMoney(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        try:
            questMoney = questEntry[QuestDictMoneyIndex]
            return questMoney
        except:
                return 100
    else:
        return 0
    return 0

def getQuestClass(id):
    questEntry = QuestDict.get(id)
    if questEntry:
        return questEntry[QuestDictDescIndex][0]
    else:
        return None
    return None


def getVisitSCStrings(npcId):
    if npcId == ToonHQ:
        strings = [TTLocalizer.QuestsRecoverItemQuestSeeHQSCString, TTLocalizer.QuestsRecoverItemQuestGoToHQSCString]
    elif npcId == ToonTailor:
        strings = [TTLocalizer.QuestsTailorQuestSCString]
    elif npcId:
        npcName, hoodName, buildingArticle, buildingName, toStreet, streetName, isInPlayground = getNpcInfo(npcId)
        strings = [TTLocalizer.QuestsVisitQuestSeeSCString % npcName]
        if isInPlayground:
            strings.append(TTLocalizer.QuestsRecoverItemQuestGoToPlaygroundSCString % hoodName)
        else:
            strings.append(TTLocalizer.QuestsRecoverItemQuestGoToStreetSCString % {'to': toStreet,
             'street': streetName,
             'hood': hoodName})
        strings.extend([TTLocalizer.QuestsRecoverItemQuestVisitBuildingSCString % (buildingArticle, buildingName), TTLocalizer.QuestsRecoverItemQuestWhereIsBuildingSCString % (buildingArticle, buildingName)])
    return strings


def getFinishToonTaskSCStrings(npcId):
    return [TTLocalizer.QuestsGenericFinishSCString] + getVisitSCStrings(npcId)


def chooseQuestDialog(id, status):
    questDialog = getQuestDialog(id).get(status)
    if questDialog == None:
        if status == QUEST:
            quest = getQuest(id)
            questDialog = quest.getDefaultQuestDialog()
        else:
            questDialog = DefaultDialog[status]
    if type(questDialog) == type(()):
        return random.choice(questDialog)
    else:
        return questDialog
    return


def chooseQuestDialogReject():
    return random.choice(DefaultReject)


def chooseQuestDialogTierNotDone():
    return random.choice(DefaultTierNotDone)


def getNpcInfo(npcId):
    npcName = NPCToons.getNPCName(npcId)
    npcZone = NPCToons.getNPCZone(npcId)
    hoodId = ZoneUtil.getCanonicalHoodId(npcZone)
    hoodName = base.cr.hoodMgr.getFullnameFromId(hoodId)
    buildingArticle = NPCToons.getBuildingArticle(npcZone)
    buildingName = NPCToons.getBuildingTitle(npcZone)
    branchId = ZoneUtil.getCanonicalBranchZone(npcZone)
    toStreet = ToontownGlobals.StreetNames[branchId][0]
    streetName = ToontownGlobals.StreetNames[branchId][-1]
    isInPlayground = ZoneUtil.isPlayground(branchId)
    return (npcName,
     hoodName,
     buildingArticle,
     buildingName,
     toStreet,
     streetName,
     isInPlayground)


def getNpcLocationDialog(fromNpcId, toNpcId):
    if not toNpcId:
        return (None, None, None)
    fromNpcZone = None
    fromBranchId = None
    if fromNpcId:
        fromNpcZone = NPCToons.getNPCZone(fromNpcId)
        fromBranchId = ZoneUtil.getCanonicalBranchZone(fromNpcZone)
    toNpcZone = NPCToons.getNPCZone(toNpcId)
    toBranchId = ZoneUtil.getCanonicalBranchZone(toNpcZone)
    toNpcName, toHoodName, toBuildingArticle, toBuildingName, toStreetTo, toStreetName, isInPlayground = getNpcInfo(toNpcId)
    if fromBranchId == toBranchId:
        if isInPlayground:
            streetDesc = TTLocalizer.QuestsStreetLocationThisPlayground
        else:
            streetDesc = TTLocalizer.QuestsStreetLocationThisStreet
    elif isInPlayground:
        streetDesc = TTLocalizer.QuestsStreetLocationNamedPlayground % toHoodName
    else:
        streetDesc = TTLocalizer.QuestsStreetLocationNamedStreet % {'toStreetName': toStreetName,
         'toHoodName': toHoodName}
    paragraph = TTLocalizer.QuestsLocationParagraph % {'building': TTLocalizer.QuestsLocationBuilding % toNpcName,
     'buildingName': toBuildingName,
     'buildingVerb': TTLocalizer.QuestsLocationBuildingVerb,
     'street': streetDesc}
    return (paragraph, toBuildingName, streetDesc)


def fillInQuestNames(text, avName = None, fromNpcId = None, toNpcId = None):
    text = copy.deepcopy(text)
    toNpcName = ''
    fromNpcName = ''
    where = ''
    buildingName = ''
    streetDesc = ''
    if avName != None:
        text = text.replace('_avName_', avName)
    if toNpcId:
        if toNpcId == ToonHQ:
            toNpcName = TTLocalizer.QuestsHQOfficerFillin
            where = TTLocalizer.QuestsHQWhereFillin
            buildingName = TTLocalizer.QuestsHQBuildingNameFillin
            streetDesc = TTLocalizer.QuestsHQLocationNameFillin
        elif toNpcId == ToonTailor:
            toNpcName = TTLocalizer.QuestsTailorFillin
            where = TTLocalizer.QuestsTailorWhereFillin
            buildingName = TTLocalizer.QuestsTailorBuildingNameFillin
            streetDesc = TTLocalizer.QuestsTailorLocationNameFillin
        else:
            toNpcName = str(NPCToons.getNPCName(toNpcId))
            where, buildingName, streetDesc = getNpcLocationDialog(fromNpcId, toNpcId)
    if fromNpcId:
        fromNpcName = str(NPCToons.getNPCName(fromNpcId))

    text = text.replace('_toNpcName_', toNpcName)
    text = text.replace('_fromNpcName_', fromNpcName)
    text = text.replace('_where_', where)
    text = text.replace('_buildingName_', buildingName)
    text = text.replace('_streetDesc_', streetDesc)
    return text


def getVisitingQuest():
    return VisitQuest(VISIT_QUEST_ID)


class Reward:
    def __init__(self, id, reward):
        self.id = id
        self.reward = reward

    def getId(self):
        return self.id

    def getType(self):
        return self.__class__

    def getAmount(self):
        return None

    def sendRewardAI(self, av):
        raise 'not implemented'

    def countReward(self, qrc):
        raise 'not implemented'

    def getString(self):
        return 'undefined'

    def getPosterString(self):
        return 'base class'


class MaxHpReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        maxHp = av.getMaxHp()
        maxHp = min(ToontownGlobals.MaxHpLimit, maxHp + self.getAmount())
        av.b_setMaxHp(maxHp)
        av.toonUp(maxHp)

    def countReward(self, qrc):
        qrc.maxHp += self.getAmount()

    def getString(self):
        return TTLocalizer.QuestsMaxHpReward % self.getAmount()

    def getPosterString(self):
        return TTLocalizer.QuestsMaxHpRewardPoster % self.getAmount()


class MoneyReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        money = av.getMoney()
        maxMoney = av.getMaxMoney()
        av.addMoney(self.getAmount())

    def countReward(self, qrc):
        qrc.money += self.getAmount()

    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMoneyRewardSingular
        else:
            return TTLocalizer.QuestsMoneyRewardPlural % amt

    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMoneyRewardPosterSingular
        else:
            return TTLocalizer.QuestsMoneyRewardPosterPlural % amt


class MaxMoneyReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.b_setMaxMoney(av.getMaxMoney() + self.getAmount())

    def countReward(self, qrc):
        qrc.maxMoney = self.getAmount()

    def getString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMaxMoneyRewardSingular
        else:
            return TTLocalizer.QuestsMaxMoneyRewardPlural % amt

    def getPosterString(self):
        amt = self.getAmount()
        if amt == 1:
            return TTLocalizer.QuestsMaxMoneyRewardPosterSingular
        else:
            return TTLocalizer.QuestsMaxMoneyRewardPosterPlural % amt


class MaxGagCarryReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.b_setMaxCarry(av.getMaxCarry() + self.getAmount())

    def countReward(self, qrc):
        qrc.maxCarry = self.getAmount()

    def getString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxGagCarryReward % amt

    def getPosterString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxGagCarryRewardPoster % amt


class MaxQuestCarryReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getAmount(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.b_setQuestCarryLimit(self.getAmount())

    def countReward(self, qrc):
        qrc.questCarryLimit = self.getAmount()

    def getString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxQuestCarryReward % amt

    def getPosterString(self):
        amt = self.getAmount()
        return TTLocalizer.QuestsMaxQuestCarryRewardPoster % amt


class TeleportReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getZone(self):
        return self.reward[0]

    def sendRewardAI(self, av):
        av.addTeleportAccess(self.getZone())

    def countReward(self, qrc):
        pass

    def getString(self):
        hoodName = ToontownGlobals.hoodNameMap[self.getZone()][-1]
        return TTLocalizer.QuestsTeleportReward % hoodName

    def getPosterString(self):
        hoodName = ToontownGlobals.hoodNameMap[self.getZone()][-1]
        return TTLocalizer.QuestsTeleportRewardPoster % hoodName


TrackTrainingQuotas = {ToontownBattleGlobals.HEAL_TRACK: 15,
 ToontownBattleGlobals.TRAP_TRACK: 15,
 ToontownBattleGlobals.LURE_TRACK: 15,
 ToontownBattleGlobals.SOUND_TRACK: 15,
 ToontownBattleGlobals.THROW_TRACK: 15,
 ToontownBattleGlobals.SQUIRT_TRACK: 15,
 ToontownBattleGlobals.ZAP_TRACK: 15,
 ToontownBattleGlobals.DROP_TRACK: 15}

class TrackTrainingReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def sendRewardAI(self, av):
        av.b_setTrackProgress(self.getTrack(), 0)

    def countReward(self, qrc):
        qrc.trackProgressId = self.getTrack()
        qrc.trackProgress = 0

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackTrainingReward % trackName

    def getPosterString(self):
        return TTLocalizer.QuestsTrackTrainingRewardPoster


class TrackProgressReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def getProgressIndex(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        av.addTrackProgress(self.getTrack(), self.getProgressIndex())

    def countReward(self, qrc):
        qrc.addTrackProgress(self.getTrack(), self.getProgressIndex())

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackProgressReward % {'frameNum': self.getProgressIndex(),
         'trackName': trackName}

    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackProgressRewardPoster % {'trackName': trackName,
         'frameNum': self.getProgressIndex()}


class TrackCompleteReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getTrack(self):
        track = self.reward[0]
        if track == None:
            track = 0
        return track

    def sendRewardAI(self, av):
        av.addTrackAccess(self.getTrack())
        av.clearTrackProgress()

    def countReward(self, qrc):
        qrc.addTrackAccess(self.getTrack())
        qrc.clearTrackProgress()

    def getString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackCompleteReward % trackName

    def getPosterString(self):
        trackName = ToontownBattleGlobals.Tracks[self.getTrack()].capitalize()
        return TTLocalizer.QuestsTrackCompleteRewardPoster % trackName


class ClothingTicketReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def sendRewardAI(self, av):
        pass

    def countReward(self, qrc):
        pass

    def getString(self):
        return TTLocalizer.QuestsClothingTicketReward

    def getPosterString(self):
        return TTLocalizer.QuestsClothingTicketRewardPoster


class TIPClothingTicketReward(ClothingTicketReward):
    def __init__(self, id, reward):
        ClothingTicketReward.__init__(self, id, reward)

    def getString(self):
        return TTLocalizer.TIPQuestsClothingTicketReward

    def getPosterString(self):
        return TTLocalizer.TIPQuestsClothingTicketRewardPoster


class CheesyEffectReward(Reward):
    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getEffect(self):
        return self.reward[0]

    def getHoodId(self):
        return self.reward[1]

    def getDurationMinutes(self):
        return self.reward[2]

    def sendRewardAI(self, av):
        expireTime = time.time() + int(self.getDurationMinutes()*60)
        if not self.getEffect() in av.getCheesyEffects():
            av.cheesyEffects.append(self.getEffect())
            av.b_setCheesyEffects(av.getCheesyEffects())

    def countReward(self, qrc):
        pass

    def getString(self):
        effect = self.getEffect()
        hoodId = self.getHoodId()
        duration = self.getDurationMinutes()
        string = TTLocalizer.CheesyEffectMinutes
        if duration > 90:
            duration = int((duration + 30) / 60)
            string = TTLocalizer.CheesyEffectHours
            if duration > 36:
                duration = int((duration + 12) / 24)
                string = TTLocalizer.CheesyEffectDays
        if effect == 77:
            effect = 12
        desc = TTLocalizer.CheesyEffectDescriptions[effect][1]
        return TTLocalizer.CheesyEffectIndefinite % {'effectName': desc}

    def getPosterString(self):
        effect = self.getEffect()
        if effect == 77:
            effect = 12
        desc = TTLocalizer.CheesyEffectDescriptions[effect][0]
        return TTLocalizer.QuestsCheesyEffectRewardPoster % desc


class CogSuitPartReward(Reward):
    trackNames = [TTLocalizer.Bossbot,
     TTLocalizer.Lawbot,
     TTLocalizer.Cashbot,
     TTLocalizer.Sellbot]

    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getCogTrack(self):
        return self.reward[0]

    def getCogPart(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        dept = self.getCogTrack()
        part = self.getCogPart()
        av.giveCogPart(part, dept)

    def countReward(self, qrc):
        pass

    def getCogTrackName(self):
        index = ToontownGlobals.cogDept2index[self.getCogTrack()]
        return CogSuitPartReward.trackNames[index]

    def getCogPartName(self):
        index = ToontownGlobals.cogDept2index[self.getCogTrack()]
        return CogDisguiseGlobals.PartsQueryNames[index][self.getCogPart()]

    def getString(self):
        return TTLocalizer.QuestsCogSuitPartReward % {'cogTrack': self.getCogTrackName(),
         'part': self.getCogPartName()}

    def getPosterString(self):
        return TTLocalizer.QuestsCogSuitPartRewardPoster % {'cogTrack': self.getCogTrackName(),
         'part': self.getCogPartName()}

class CogMeritReward(Reward):
    meritNames = TTLocalizer.RewardPanelMeritBarLabels

    def __init__(self, id, reward):
        Reward.__init__(self, id, reward)

    def getMeritType(self):
        return self.reward[0]

    def getNumMerits(self):
        return self.reward[1]

    def sendRewardAI(self, av):
        dept = self.getMeritType()
        num = self.getNumMerits()
        av.addMerits(dept, num)

    def countReward(self, qrc):
        pass

    def getMeritName(self):
        return CogMeritReward.meritNames[self.getMeritType()]

    def getString(self):
        return TTLocalizer.QuestsCogSuitMeritReward % {'numMerits': self.getNumMerits(),
         'meritType': self.getMeritName()}

    def getPosterString(self):
        return TTLocalizer.QuestsCogSuitMeritRewardPoster % {'numMerits': self.getNumMerits(),
         'meritType': self.getMeritName()}

def getRewardClass(id):
    reward = RewardDict.get(id)
    if reward:
        return reward[0]
    else:
        return None
    return None


def getReward(id):
    reward = RewardDict.get(id)
    if reward:
        rewardClass = reward[0]
        return rewardClass(id, reward[1:])
    else:
        notify.warning('getReward(): id %s not found.' % id)
        return None


def getNextRewards(numChoices, tier, av):
    rewardTier = list(getRewardsInTier(tier))
    optRewards = list(getOptionalRewardsInTier(tier))
    if av.getGameAccess() == OTPGlobals.AccessFull and tier == TT_TIER + 3:
        optRewards = []
    if isLoopingFinalTier(tier):
        rewardHistory = map(lambda questDesc: questDesc[3], av.quests)
        if notify.getDebug():
            notify.debug('getNextRewards: current rewards (history): %s' % rewardHistory)
    else:
        rewardHistory = av.getRewardHistory()[1]
        if notify.getDebug():
            notify.debug('getNextRewards: rewardHistory: %s' % rewardHistory)
    if notify.getDebug():
        notify.debug('getNextRewards: rewardTier: %s' % rewardTier)
        notify.debug('getNextRewards: numChoices: %s' % numChoices)
    for rewardId in getRewardsInTier(tier):
        if getRewardClass(rewardId) == CogSuitPartReward:
            deptStr = RewardDict.get(rewardId)[1]
            cogPart = RewardDict.get(rewardId)[2]
            dept = ToontownGlobals.cogDept2index[deptStr]
            if av.hasCogPart(cogPart, dept):
                notify.debug('getNextRewards: already has cog part: %s dept: %s' % (cogPart, dept))
                rewardTier.remove(rewardId)
            else:
                notify.debug('getNextRewards: keeping quest for cog part: %s dept: %s' % (cogPart, dept))

    for rewardId in rewardHistory:
        if rewardId in rewardTier:
            rewardTier.remove(rewardId)
        elif rewardId in optRewards:
            optRewards.remove(rewardId)
        elif rewardId in (901, 902, 903, 904, 905, 906, 907, 908):
            genericRewardId = 900
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)
        elif rewardId > 1000 and rewardId < 1799:
            index = rewardId % 100
            genericRewardId = 800 + index
            if genericRewardId in rewardTier:
                rewardTier.remove(genericRewardId)

    if numChoices == 0:
        if len(rewardTier) == 0:
            return []
        else:
            return [rewardTier[0]]
    rewardPool = rewardTier[:numChoices]
    for i in range(len(rewardPool), numChoices * 2):
        if optRewards:
            optionalReward = seededRandomChoice(optRewards)
            optRewards.remove(optionalReward)
            rewardPool.append(optionalReward)
        else:
            break

    if notify.getDebug():
        notify.debug('getNextRewards: starting reward pool: %s' % rewardPool)
    if len(rewardPool) == 0:
        if notify.getDebug():
            notify.debug('getNextRewards: no rewards left at all')
        return []
    finalRewardPool = [rewardPool.pop(0)]
    for i in range(numChoices - 1):
        if len(rewardPool) == 0:
            break
        selectedReward = seededRandomChoice(rewardPool)
        rewardPool.remove(selectedReward)
        finalRewardPool.append(selectedReward)

    if notify.getDebug():
        notify.debug('getNextRewards: final reward pool: %s' % finalRewardPool)
    return finalRewardPool


RewardDict = {100: (MaxHpReward, 1),
 101: (MaxHpReward, 2),
 102: (MaxHpReward, 3),
 103: (MaxHpReward, 4),
 104: (MaxHpReward, 5),
 105: (MaxHpReward, 6),
 106: (MaxHpReward, 7),
 107: (MaxHpReward, 8),
 108: (MaxHpReward, 9),
 109: (MaxHpReward, 10),
 200: (MaxGagCarryReward, 1),
 201: (MaxGagCarryReward, 2),
 202: (MaxGagCarryReward, 3),
 203: (MaxGagCarryReward, 4),
 204: (MaxGagCarryReward, 5),
 205: (MaxGagCarryReward, 6),
 206: (MaxGagCarryReward, 7),
 207: (MaxGagCarryReward, 8),
 208: (MaxGagCarryReward, 9),
 209: (MaxGagCarryReward, 10),
 300: (TeleportReward, ToontownGlobals.ToontownCentral),
 301: (TeleportReward, ToontownGlobals.DonaldsDock),
 302: (TeleportReward, ToontownGlobals.DaisyGardens),
 303: (TeleportReward, ToontownGlobals.MinniesMelodyland),
 304: (TeleportReward, ToontownGlobals.TheBrrrgh),
 305: (TeleportReward, ToontownGlobals.DonaldsDreamland),
 306: (TeleportReward, ToontownGlobals.SellbotHQ),
 307: (TeleportReward, ToontownGlobals.CashbotHQ),
 308: (TeleportReward, ToontownGlobals.LawbotHQ),
 309: (TeleportReward, ToontownGlobals.BossbotHQ),
 310: (TeleportReward, ToontownGlobals.OutdoorZone),
 400: (TrackTrainingReward, None),
 401: (TrackTrainingReward, ToontownBattleGlobals.HEAL_TRACK),
 402: (TrackTrainingReward, ToontownBattleGlobals.TRAP_TRACK),
 403: (TrackTrainingReward, ToontownBattleGlobals.LURE_TRACK),
 404: (TrackTrainingReward, ToontownBattleGlobals.SOUND_TRACK),
 405: (TrackTrainingReward, ToontownBattleGlobals.THROW_TRACK),
 406: (TrackTrainingReward, ToontownBattleGlobals.SQUIRT_TRACK),
 407: (TrackTrainingReward, ToontownBattleGlobals.ZAP_TRACK),
 408: (TrackTrainingReward, ToontownBattleGlobals.DROP_TRACK),
 500: (MaxQuestCarryReward, 2),
 501: (MaxQuestCarryReward, 3),
 502: (MaxQuestCarryReward, 4),
 600: (MoneyReward, 10),
 601: (MoneyReward, 20),
 602: (MoneyReward, 40),
 603: (MoneyReward, 60),
 604: (MoneyReward, 100),
 605: (MoneyReward, 150),
 606: (MoneyReward, 200),
 607: (MoneyReward, 250),
 608: (MoneyReward, 300),
 609: (MoneyReward, 400),
 610: (MoneyReward, 500),
 611: (MoneyReward, 600),
 612: (MoneyReward, 700),
 613: (MoneyReward, 800),
 614: (MoneyReward, 900),
 615: (MoneyReward, 1000),
 616: (MoneyReward, 1100),
 617: (MoneyReward, 1200),
 618: (MoneyReward, 1300),
 619: (MoneyReward, 1400),
 620: (MoneyReward, 1500),
 621: (MoneyReward, 1750),
 622: (MoneyReward, 2000),
 623: (MoneyReward, 2500),
 700: (MaxMoneyReward, 25),
 701: (MaxMoneyReward, 50),
 702: (MaxMoneyReward, 75),
 703: (MaxMoneyReward, 100),
 704: (MaxMoneyReward, 125),
 705: (MaxMoneyReward, 150),
 706: (MaxMoneyReward, 175),
 707: (MaxMoneyReward, 200),
 801: (TrackProgressReward, None, 1),
 802: (TrackProgressReward, None, 2),
 803: (TrackProgressReward, None, 3),
 804: (TrackProgressReward, None, 4),
 805: (TrackProgressReward, None, 5),
 806: (TrackProgressReward, None, 6),
 807: (TrackProgressReward, None, 7),
 808: (TrackProgressReward, None, 8),
 809: (TrackProgressReward, None, 9),
 810: (TrackProgressReward, None, 10),
 811: (TrackProgressReward, None, 11),
 812: (TrackProgressReward, None, 12),
 813: (TrackProgressReward, None, 13),
 814: (TrackProgressReward, None, 14),
 815: (TrackProgressReward, None, 15),
 110: (TIPClothingTicketReward,),
 1000: (ClothingTicketReward,),
 1001: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 1),
 1002: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 2),
 1003: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 3),
 1004: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 4),
 1005: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 5),
 1006: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 6),
 1007: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 7),
 1008: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 8),
 1009: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 9),
 1010: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 10),
 1011: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 11),
 1012: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 12),
 1013: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 13),
 1014: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 14),
 1015: (TrackProgressReward, ToontownBattleGlobals.HEAL_TRACK, 15),
 1101: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 1),
 1102: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 2),
 1103: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 3),
 1104: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 4),
 1105: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 5),
 1106: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 6),
 1107: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 7),
 1108: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 8),
 1109: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 9),
 1110: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 10),
 1111: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 11),
 1112: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 12),
 1113: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 13),
 1114: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 14),
 1115: (TrackProgressReward, ToontownBattleGlobals.TRAP_TRACK, 15),
 1201: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 1),
 1202: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 2),
 1203: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 3),
 1204: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 4),
 1205: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 5),
 1206: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 6),
 1207: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 7),
 1208: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 8),
 1209: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 9),
 1210: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 10),
 1211: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 11),
 1212: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 12),
 1213: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 13),
 1214: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 14),
 1215: (TrackProgressReward, ToontownBattleGlobals.LURE_TRACK, 15),
 1301: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 1),
 1302: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 2),
 1303: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 3),
 1304: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 4),
 1305: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 5),
 1306: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 6),
 1307: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 7),
 1308: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 8),
 1309: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 9),
 1310: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 10),
 1311: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 11),
 1312: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 12),
 1313: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 13),
 1314: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 14),
 1315: (TrackProgressReward, ToontownBattleGlobals.SOUND_TRACK, 15),
 1601: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 1),
 1602: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 2),
 1603: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 3),
 1604: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 4),
 1605: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 5),
 1606: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 6),
 1607: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 7),
 1608: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 8),
 1609: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 9),
 1610: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 10),
 1611: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 11),
 1612: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 12),
 1613: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 13),
 1614: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 14),
 1615: (TrackProgressReward, ToontownBattleGlobals.ZAP_TRACK, 15),
 1701: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 1),
 1702: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 2),
 1703: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 3),
 1704: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 4),
 1705: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 5),
 1706: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 6),
 1707: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 7),
 1708: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 8),
 1709: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 9),
 1710: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 10),
 1711: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 11),
 1712: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 12),
 1713: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 13),
 1714: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 14),
 1715: (TrackProgressReward, ToontownBattleGlobals.DROP_TRACK, 15),
 900: (TrackCompleteReward, None),
 901: (TrackCompleteReward, ToontownBattleGlobals.HEAL_TRACK),
 902: (TrackCompleteReward, ToontownBattleGlobals.TRAP_TRACK),
 903: (TrackCompleteReward, ToontownBattleGlobals.LURE_TRACK),
 904: (TrackCompleteReward, ToontownBattleGlobals.SOUND_TRACK),
 905: (TrackCompleteReward, ToontownBattleGlobals.THROW_TRACK),
 906: (TrackCompleteReward, ToontownBattleGlobals.SQUIRT_TRACK),
 907: (TrackCompleteReward, ToontownBattleGlobals.ZAP_TRACK),
 908: (TrackCompleteReward, ToontownBattleGlobals.DROP_TRACK),
 2205: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        2000,
        10),
 2206: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        2000,
        10),
 2101: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1000,
        10),
 2102: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1000,
        10),
 2103: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        1000,
        10),
 2105: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        20),
 2106: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        20),
 2107: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        0,
        20),
 2501: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        5000,
        60),
 2502: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        5000,
        60),
 2503: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        5000,
        20),
 2504: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        5000,
        20),
 2505: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        60),
 2506: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        60),
 2507: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        0,
        60),
 2401: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1,
        120),
 2402: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1,
        120),
 2403: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        4000,
        60),
 2404: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        4000,
        60),
 2405: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        120),
 2406: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        120),
 2407: (CheesyEffectReward,
        ToontownGlobals.CEFlatPortrait,
        4000,
        30),
 2408: (CheesyEffectReward,
        ToontownGlobals.CEFlatProfile,
        4000,
        30),
 2409: (CheesyEffectReward,
        ToontownGlobals.CETransparent,
        4000,
        30),
 2410: (CheesyEffectReward,
        ToontownGlobals.CENoColor,
        4000,
        30),
 2411: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        4000,
        30),
 2301: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1,
        360),
 2302: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1,
        360),
 2303: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        1,
        360),
 2304: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        1,
        360),
 2305: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        1440),
 2306: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        1440),
 2307: (CheesyEffectReward,
        ToontownGlobals.CEFlatPortrait,
        3000,
        240),
 2308: (CheesyEffectReward,
        ToontownGlobals.CEFlatProfile,
        3000,
        240),
 2309: (CheesyEffectReward,
        ToontownGlobals.CETransparent,
        1,
        120),
 2310: (CheesyEffectReward,
        ToontownGlobals.CENoColor,
        1,
        120),
 2311: (CheesyEffectReward,
        ToontownGlobals.CEInvisible,
        3000,
        120),
 2312: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        3000,
        120),
 2900: (CheesyEffectReward,
        ToontownGlobals.CENormal,
        0,
        0),
 2901: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1,
        1440),
 2902: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1,
        1440),
 2903: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        1,
        1440),
 2904: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        1,
        1440),
 2905: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        1440),
 2906: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        1440),
 2907: (CheesyEffectReward,
        ToontownGlobals.CEFlatPortrait,
        1,
        1440),
 2908: (CheesyEffectReward,
        ToontownGlobals.CEFlatProfile,
        1,
        1440),
 2909: (CheesyEffectReward,
        ToontownGlobals.CETransparent,
        1,
        1440),
 2910: (CheesyEffectReward,
        ToontownGlobals.CENoColor,
        1,
        1440),
 2911: (CheesyEffectReward,
        ToontownGlobals.CEInvisible,
        1,
        1440),
 2911: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        1,
        1440),
 2920: (CheesyEffectReward,
        ToontownGlobals.CENormal,
        0,
        0),
 2921: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1,
        2880),
 2922: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1,
        2880),
 2923: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        1,
        2880),
 2924: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        1,
        2880),
 2925: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        2880),
 2926: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        2880),
 2927: (CheesyEffectReward,
        ToontownGlobals.CEFlatPortrait,
        1,
        2880),
 2928: (CheesyEffectReward,
        ToontownGlobals.CEFlatProfile,
        1,
        2880),
 2929: (CheesyEffectReward,
        ToontownGlobals.CETransparent,
        1,
        2880),
 2930: (CheesyEffectReward,
        ToontownGlobals.CENoColor,
        1,
        2880),
 2931: (CheesyEffectReward,
        ToontownGlobals.CEInvisible,
        1,
        2880),
 2932: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        1,
        2880),
 2940: (CheesyEffectReward,
        ToontownGlobals.CENormal,
        0,
        0),
 2941: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1,
        10080),
 2942: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1,
        10080),
 2943: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        1,
        10080),
 2944: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        1,
        10080),
 2945: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        10080),
 2946: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        10080),
 2947: (CheesyEffectReward,
        ToontownGlobals.CEFlatPortrait,
        1,
        10080),
 2948: (CheesyEffectReward,
        ToontownGlobals.CEFlatProfile,
        1,
        10080),
 2949: (CheesyEffectReward,
        ToontownGlobals.CETransparent,
        1,
        10080),
 2950: (CheesyEffectReward,
        ToontownGlobals.CENoColor,
        1,
        10080),
 2951: (CheesyEffectReward,
        ToontownGlobals.CEInvisible,
        1,
        10080),
 2952: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        1,
        10080),
 2960: (CheesyEffectReward,
        ToontownGlobals.CENormal,
        0,
        0),
 2961: (CheesyEffectReward,
        ToontownGlobals.CEBigHead,
        1,
        43200),
 2962: (CheesyEffectReward,
        ToontownGlobals.CESmallHead,
        1,
        43200),
 2963: (CheesyEffectReward,
        ToontownGlobals.CEBigLegs,
        1,
        43200),
 2964: (CheesyEffectReward,
        ToontownGlobals.CESmallLegs,
        1,
        43200),
 2965: (CheesyEffectReward,
        ToontownGlobals.CEBigToon,
        0,
        43200),
 2966: (CheesyEffectReward,
        ToontownGlobals.CESmallToon,
        0,
        43200),
 2967: (CheesyEffectReward,
        ToontownGlobals.CEFlatPortrait,
        1,
        43200),
 2968: (CheesyEffectReward,
        ToontownGlobals.CEFlatProfile,
        1,
        43200),
 2969: (CheesyEffectReward,
        ToontownGlobals.CETransparent,
        1,
        43200),
 2970: (CheesyEffectReward,
        ToontownGlobals.CENoColor,
        1,
        43200),
 2971: (CheesyEffectReward,
        ToontownGlobals.CEInvisible,
        1,
        43200),
 2972: (CheesyEffectReward,
        ToontownGlobals.CEWire,
        1,
        43200),
 4000: (CogSuitPartReward, 'm', CogDisguiseGlobals.leftLegUpper),
 4001: (CogSuitPartReward, 'm', CogDisguiseGlobals.leftLegLower),
 4002: (CogSuitPartReward, 'm', CogDisguiseGlobals.leftLegFoot),
 4003: (CogSuitPartReward, 'm', CogDisguiseGlobals.rightLegUpper),
 4004: (CogSuitPartReward, 'm', CogDisguiseGlobals.rightLegLower),
 4005: (CogSuitPartReward, 'm', CogDisguiseGlobals.rightLegFoot),
 4006: (CogSuitPartReward, 'm', CogDisguiseGlobals.upperTorso),
 4007: (CogSuitPartReward, 'm', CogDisguiseGlobals.torsoPelvis),
 4008: (CogSuitPartReward, 'm', CogDisguiseGlobals.leftArmUpper),
 4009: (CogSuitPartReward, 'm', CogDisguiseGlobals.leftArmLower),
 4010: (CogSuitPartReward, 'm', CogDisguiseGlobals.rightArmUpper),
 4011: (CogSuitPartReward, 'm', CogDisguiseGlobals.rightArmLower),
 4100: (CogSuitPartReward, 'l', CogDisguiseGlobals.leftLegUpper),
 4101: (CogSuitPartReward, 'l', CogDisguiseGlobals.leftLegLower),
 4102: (CogSuitPartReward, 'l', CogDisguiseGlobals.leftLegFoot),
 4103: (CogSuitPartReward, 'l', CogDisguiseGlobals.rightLegUpper),
 4104: (CogSuitPartReward, 'l', CogDisguiseGlobals.rightLegLower),
 4105: (CogSuitPartReward, 'l', CogDisguiseGlobals.rightLegFoot),
 4106: (CogSuitPartReward, 'l', CogDisguiseGlobals.upperTorso),
 4107: (CogSuitPartReward, 'l', CogDisguiseGlobals.torsoPelvis),
 4108: (CogSuitPartReward, 'l', CogDisguiseGlobals.leftArmUpper),
 4109: (CogSuitPartReward, 'l', CogDisguiseGlobals.leftArmLower),
 4110: (CogSuitPartReward, 'l', CogDisguiseGlobals.leftArmHand),
 4111: (CogSuitPartReward, 'l', CogDisguiseGlobals.rightArmUpper),
 4112: (CogSuitPartReward, 'l', CogDisguiseGlobals.rightArmLower),
 4113: (CogSuitPartReward, 'l', CogDisguiseGlobals.rightArmHand),
 4200: (CogSuitPartReward, 'c', CogDisguiseGlobals.leftLegUpper),
 4201: (CogSuitPartReward, 'c', CogDisguiseGlobals.leftLegLower),
 4202: (CogSuitPartReward, 'c', CogDisguiseGlobals.leftLegFoot),
 4203: (CogSuitPartReward, 'c', CogDisguiseGlobals.rightLegUpper),
 4204: (CogSuitPartReward, 'c', CogDisguiseGlobals.rightLegLower),
 4205: (CogSuitPartReward, 'c', CogDisguiseGlobals.rightLegFoot),
 4206: (CogSuitPartReward, 'c', CogDisguiseGlobals.torsoLeftShoulder),
 4207: (CogSuitPartReward, 'c', CogDisguiseGlobals.torsoRightShoulder),
 4208: (CogSuitPartReward, 'c', CogDisguiseGlobals.torsoChest),
 4209: (CogSuitPartReward, 'c', CogDisguiseGlobals.torsoHealthMeter),
 4210: (CogSuitPartReward, 'c', CogDisguiseGlobals.torsoPelvis),
 4211: (CogSuitPartReward, 'c', CogDisguiseGlobals.leftArmUpper),
 4212: (CogSuitPartReward, 'c', CogDisguiseGlobals.leftArmLower),
 4213: (CogSuitPartReward, 'c', CogDisguiseGlobals.leftArmHand),
 4214: (CogSuitPartReward, 'c', CogDisguiseGlobals.rightArmUpper),
 4215: (CogSuitPartReward, 'c', CogDisguiseGlobals.rightArmLower),
 4216: (CogSuitPartReward, 'c', CogDisguiseGlobals.rightArmHand),
 4300: (CogMeritReward, 0, 100),
 4301: (CogMeritReward, 0, 200),
 4302: (CogMeritReward, 0, 300),
 4303: (CogMeritReward, 0, 400),
 4304: (CogMeritReward, 0, 500),
 4305: (CogMeritReward, 0, 600),
 4306: (CogMeritReward, 0, 700),
 4307: (CogMeritReward, 0, 800),
 4308: (CogMeritReward, 0, 900),
 4309: (CogMeritReward, 0, 1000),
 4310: (CogMeritReward, 1, 100),
 4311: (CogMeritReward, 1, 200),
 4312: (CogMeritReward, 1, 300),
 4313: (CogMeritReward, 1, 400),
 4314: (CogMeritReward, 1, 500),
 4315: (CogMeritReward, 1, 600),
 4316: (CogMeritReward, 1, 700),
 4317: (CogMeritReward, 1, 800),
 4318: (CogMeritReward, 1, 900),
 4319: (CogMeritReward, 1, 1000),
 4320: (CogMeritReward, 2, 100),
 4321: (CogMeritReward, 2, 200),
 4322: (CogMeritReward, 2, 300),
 4323: (CogMeritReward, 2, 400),
 4324: (CogMeritReward, 2, 500),
 4325: (CogMeritReward, 2, 600),
 4326: (CogMeritReward, 2, 700),
 4327: (CogMeritReward, 2, 800),
 4328: (CogMeritReward, 2, 900),
 4329: (CogMeritReward, 2, 1000),
 4330: (CogMeritReward, 3, 100),
 4331: (CogMeritReward, 3, 200),
 4332: (CogMeritReward, 3, 300),
 4333: (CogMeritReward, 3, 400),
 4334: (CogMeritReward, 3, 500),
 4335: (CogMeritReward, 3, 600),
 4336: (CogMeritReward, 3, 700),
 4337: (CogMeritReward, 3, 800),
 4338: (CogMeritReward, 3, 900),
 4339: (CogMeritReward, 3, 1000),
 4340: (CogMeritReward, 4, 100),
 4341: (CogMeritReward, 4, 200),
 4342: (CogMeritReward, 4, 300),
 4343: (CogMeritReward, 4, 400),
 4344: (CogMeritReward, 4, 500),
 4345: (CogMeritReward, 4, 600),
 4346: (CogMeritReward, 4, 700),
 4347: (CogMeritReward, 4, 800),
 4348: (CogMeritReward, 4, 900),
 4349: (CogMeritReward, 4, 1000)}

def getNumTiers():
    return len(RequiredRewardTrackDict) - 1


def isLoopingFinalTier(tier):
    return tier == LOOPING_FINAL_TIER


def getRewardsInTier(tier):
    return RequiredRewardTrackDict.get(tier, [])


def getNumRewardsInTier(tier):
    return len(RequiredRewardTrackDict.get(tier, []))


def rewardTierExists(tier):
    return RequiredRewardTrackDict.has_key(tier)


def getOptionalRewardsInTier(tier):
    return OptionalRewardTrackDict.get(tier, [])


def getRewardIdFromTrackId(trackId):
    return 401 + trackId


RequiredRewardTrackDict = {TT_TIER: (100,),
 TT_TIER + 1: (400,),
 TT_TIER + 2: (100,
               801,
               204,
               802,
               803,
               101,
               804,
               805,
               102,
               806,
               807,
               100,
               808,
               809,
               101,
               810,
               811,
               500,
               812,
               813,
               700,
               814,
               815,
               300),
 TT_TIER + 3: (900,),
 DD_TIER: (400,),
 DD_TIER + 1: (101,
               801,
               802,
               204,
               803,
               804,
               100,
               805,
               806,
               102,
               807,
               808,
               100,
               809,
               810,
               101,
               811,
               812,
               701,
               813,
               814,
               815,
               301),
 DD_TIER + 2: (900,),
 AA_TIER: (400,),
 AA_TIER + 1: (100,
               801,
               802,
               209,
               803,
               804,
               102,
               101,
               805,
               806,
               100,
               501,
               807,
               808,
               101,
               809,
               810,
               811,
               812,
               813,
               702,
               814,
               815,
               310),
 AA_TIER + 2: (900,),
 DG_TIER: (100,
           209,
           102,
           100,
           101,
           703,
           101,
           302),
 MM_TIER: (400,),
 MM_TIER + 1: (801,
           802,
           100,
           803,
           101,
           804,
           102,
           209,
           805,
           806,
           807,
           100,
           502,
           808,
           809,
           810,
           811,
           812,
           303,
           101,
           813,
           704,
           814,
           815),
 MM_TIER + 2: (900,),
 BR_TIER: (400,),
 BR_TIER + 1: (100,
               801,
               802,
               209,
               803,
               804,
               101,
               805,
               806,
               807,
               808,
               102,
               809,
               810,
               705,
               811,
               812,
               100,
               813,
               814,
               101,
               815,
               304),
 BR_TIER + 2: (900,),
 DL_TIER: (100,
           209,
           102,
           103,
           101,
           706,
           305),
 DL_TIER + 1: (100,
               209,
               101,
               102,
               707,
               103),
 DL_TIER + 2: (100,
               101,
               102,
               103,
               209),
 DL_TIER + 3: (102,
               101,
               100,
               209,
               707,
               102),
 ELDER_TIER: ()}
OptionalRewardTrackDict = {TT_TIER: (),
 TT_TIER + 1: (),
 TT_TIER + 2: (1000,
               601,
               601,
               602,
               602,
               2205,
               2206,
               2205,
               2206),
 TT_TIER + 3: (601,
               601,
               602,
               602,
               2205,
               2206,
               2205,
               2206),
 DD_TIER: (1000,
           601,
           602,
           603,
           603,
           2101,
           2102,
           2105,
           2106),
 DD_TIER + 1: (1000,
               602,
               602,
               603,
               603,
               2101,
               2102,
               2105,
               2106),
 DD_TIER + 2: (1000,
               602,
               602,
               603,
               603,
               2101,
               2102,
               2105,
               2106),
 AA_TIER: (1000,
           602,
           602,
           603,
           603,
           2101,
           2102,
           2105,
           2106),
 AA_TIER + 1: (1000,
               602,
               602,
               603,
               603,
               2101,
               2102,
               2105,
               2106),
 AA_TIER + 2: (1000,
               602,
               602,
               603,
               603,
               2101,
               2102,
               2105,
               2106),
 DG_TIER: (1000,
           603,
           603,
           604,
           604,
           2501,
           2502,
           2503,
           2504,
           2505,
           2506,
           2411),
 MM_TIER: (1000,
           604,
           604,
           605,
           605,
           2403,
           2404,
           2405,
           2406,
           2407,
           2408,
           2409,
           2411),
 MM_TIER + 1: (1000,
               604,
               604,
               605,
               605,
               2403,
               2404,
               2405,
               2406,
               2407,
               2408,
               2409,
               2411),
 MM_TIER + 2: (1000,
               604,
               604,
               605,
               605,
               2403,
               2404,
               2405,
               2406,
               2407,
               2408,
               2409,
               2411),
 BR_TIER: (1000,
           606,
           606,
           606,
           606,
           606,
           607,
           607,
           607,
           607,
           607,
           2305,
           2306,
           2307,
           2308,
           2309,
           2310,
           2311,
           2312,
           4330,
           4331),
 BR_TIER + 1: (1000,
               606,
               606,
               606,
               606,
               606,
               607,
               607,
               607,
               607,
               607,
               2305,
               2306,
               2307,
               2308,
               2309,
               2310,
               2311,
               2312,
               4330,
               4331),
 BR_TIER + 2: (1000,
               606,
               606,
               606,
               606,
               606,
               607,
               607,
               607,
               607,
               607,
               2305,
               2306,
               2307,
               2308,
               2309,
               2310,
               2311,
               2312,
               4330,
               4331),
 DL_TIER: (607,
           607,
           607,
           607,
           608,
           608,
           608,
           608,
           2901,
           2902,
           2907,
           2908,
           2909,
           2910,
           2911,
           2912,
           4331,
           4330,
           4321,
           4320),
 DL_TIER + 1: (1000,
               607,
               607,
               607,
               607,
               608,
               608,
               608,
               608,
               2923,
               2924,
               2927,
               2928,
               2929,
               2930,
               2931,
               2932,
               4330,
               4331,
               4320,
               4321),
 DL_TIER + 2: (608,
               608,
               608,
               608,
               609,
               609,
               609,
               609,
               2941,
               2942,
               2943,
               2944,
               2947,
               2948,
               2949,
               2950,
               2951,
               2952,
               4330,
               4331,
               4320,
               4321,
               4310,
               4311),
 DL_TIER + 3: (1000,
               609,
               609,
               609,
               609,
               609,
               609,
               2961,
               2962,
               2963,
               2964,
               2965,
               2966,
               2967,
               2968,
               2969,
               2970,
               2971,
               2972,
               4330,
               4331,
               4320,
               4321,
               4310,
               4311,
               4300,
               4301),
 ELDER_TIER: (1000,
              1000,
              610,
              611,
              612,
              613,
              614,
              615,
              616,
              617,
              618,
              2961,
              2962,
              2963,
              2964,
              2965,
              2966,
              2967,
              2968,
              2969,
              2970,
              2971,
              2972,
              4334,
              4335,
              4336,
              4324,
              4325,
              4326,
              4314,
              4315,
              4316,
              4304,
              4305,
              4306)}

def isRewardOptional(tier, rewardId):
    return OptionalRewardTrackDict.has_key(tier) and rewardId in OptionalRewardTrackDict[tier]


def getItemName(itemId):
    return ItemDict[itemId][0]


def getPluralItemName(itemId):
    return ItemDict[itemId][1]


def avatarHasTrolleyQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == TROLLEY_QUEST_ID


def avatarHasCompletedTrolleyQuest(av):
    return av.quests[0][4] > 0


def avatarHasFirstCogQuest(av):
    return len(av.quests) == 1 and av.quests[0][0] == FIRST_COG_QUEST_ID


def avatarHasCompletedFirstCogQuest(av):
    return av.quests[0][4] > 0


def avatarHasFriendQuest(av):
    return False


def avatarHasCompletedFriendQuest(av):
    return True


def avatarHasPhoneQuest(av):
    return False


def avatarHasCompletedPhoneQuest(av):
    return True


def avatarWorkingOnRequiredRewards(av):
    tier = av.getRewardTier()
    rewardList = list(getRewardsInTier(tier))
    for i in range(len(rewardList)):
        actualRewardId = transformReward(rewardList[i], av)
        rewardList[i] = actualRewardId

    for questDesc in av.quests:
        questId = questDesc[0]
        rewardId = questDesc[3]
        if rewardId in rewardList:
            return 1
        elif rewardId == NA:
            rewardId = transformReward(getFinalRewardId(questId, fAll=1), av)
            if rewardId in rewardList:
                return 1

    return 0


def avatarHasAllRequiredRewards(av, tier):
    # Get the reward history.
    rewardHistory = list(av.getRewardHistory()[1])

    # Delete quests we're working on from the reward History.
    avQuests = av.getQuests()

    # Iterate through the current quests.
    for i in xrange(0, len(avQuests), 5):
        questDesc = avQuests[i:i + 5]
        questId, fromNpcId, toNpcId, rewardId, toonProgress = questDesc
        transformedRewardId = transformReward(rewardId, av)

        if rewardId in rewardHistory:
            rewardHistory.remove(rewardId)

        if transformedRewardId in rewardHistory:
            rewardHistory.remove(transformedRewardId)

    rewardList = getRewardsInTier(tier)
    notify.debug('checking avatarHasAllRequiredRewards: history: %s, tier: %s' % (rewardHistory, rewardList))
    for rewardId in rewardList:
        if rewardId == 900:
            found = 0
            for actualRewardId in (901, 902, 903, 904, 905, 906, 907, 908):
                if actualRewardId in rewardHistory:
                    found = 1
                    rewardHistory.remove(actualRewardId)
                    if notify.getDebug():
                        notify.debug('avatarHasAllRequiredRewards: rewardId 900 found as: %s' % actualRewardId)
                    break

            if not found:
                if notify.getDebug():
                    notify.debug('avatarHasAllRequiredRewards: rewardId 900 not found')
                return 0
        else:
            actualRewardId = transformReward(rewardId, av)
            if actualRewardId in rewardHistory:
                rewardHistory.remove(actualRewardId)
            else:
                if notify.getDebug():
                    notify.debug('avatarHasAllRequiredRewards: rewardId %s not found' % actualRewardId)
                return 0

    if notify.getDebug():
        notify.debug('avatarHasAllRequiredRewards: remaining rewards: %s' % rewardHistory)
        for rewardId in rewardHistory:
            if not isRewardOptional(tier, rewardId):
                notify.warning('required reward found, expected only optional: %s' % rewardId)

    return 1


def nextQuestList(nextQuest):
    if nextQuest == NA:
        return None
    seqTypes = (types.ListType, types.TupleType)
    if type(nextQuest) in seqTypes:
        return nextQuest
    else:
        return (nextQuest,)
    return None


def checkReward(questId, forked = 0):
    quest = QuestDict[questId]
    reward = quest[5]
    nextQuests = nextQuestList(quest[6])
    if nextQuests is None:
        validRewards = RewardDict.keys() + [Any,
         AnyCashbotSuitPart,
         AnyLawbotSuitPart,
         OBSOLETE]
        if reward is OBSOLETE:
            print 'warning: quest %s is obsolete' % questId
        return reward
    else:
        forked = forked or len(nextQuests) > 1
        firstReward = checkReward(nextQuests[0], forked)
        for qId in nextQuests[1:]:
            thisReward = checkReward(qId, forked)

        return firstReward
    return


def assertAllQuestsValid():
    print 'checking quests...'
    for questId in QuestDict.keys():
        try:
            quest = getQuest(questId)
        except AssertionError, e:
            err = 'invalid quest: %s' % questId
            print err
            raise

    for questId in QuestDict.keys():
        quest = QuestDict[questId]
        tier, start, questDesc, fromNpc, toNpc, reward, nextQuest, dialog = quest
        if start:
            checkReward(questId)
