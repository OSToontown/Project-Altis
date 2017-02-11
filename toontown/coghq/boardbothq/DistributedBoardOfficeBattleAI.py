from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedLevelBattleAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import State
from direct.fsm import ClassicFSM, State
from toontown.battle.BattleBase import *
from toontown.coghq import CogDisguiseGlobals
from toontown.toonbase.ToontownBattleGlobals import getBoardOfficeCreditMultiplier
from toontown.toonbase.ToonPythonUtil import addListsByValue

class DistributedBoardOfficeBattleAI(DistributedLevelBattleAI.DistributedLevelBattleAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeBattleAI')

    def __init__(self, air, battleMgr, pos, suit, toonId, zoneId, level, battleCellId, roundCallback = None, finishCallback = None, maxSuits = 4):
        DistributedLevelBattleAI.DistributedLevelBattleAI.__init__(self, air, battleMgr, pos, suit, toonId, zoneId, level, battleCellId, 'BoardOfficeReward', roundCallback, finishCallback, maxSuits)
        self.battleCalc.setSkillCreditMultiplier(1)
        if self.bossBattle:
            self.level.d_setBossConfronted(toonId)
        self.fsm.addState(State.State('BoardOfficeReward', self.enterBoardOfficeReward, self.exitBoardOfficeReward, ['Resume']))
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('BoardOfficeReward')

    def getTaskZoneId(self):
        return self.level.boardofficeId

    def handleToonsWon(self, toons):
        extraMerits = [0, 0, 0, 0, 0]
        amount = ToontownGlobals.BoardOfficeCogBuckRewards[self.level.boardofficeId]
        index = ToontownGlobals.cogHQZoneId2deptIndex(self.level.boardofficeId)
        extraMerits[index] = amount
        for toon in toons:
            recovered, notRecovered = self.air.questManager.recoverItems(toon, self.suitsKilled, self.getTaskZoneId())
            self.toonItems[toon.doId][0].extend(recovered)
            self.toonItems[toon.doId][1].extend(notRecovered)
            meritArray = self.air.promotionMgr.recoverMerits(toon, self.suitsKilled, self.getTaskZoneId(), getBoardOfficeCreditMultiplier(self.getTaskZoneId()), extraMerits=extraMerits)
            if toon.doId in self.helpfulToons:
                self.toonMerits[toon.doId] = addListsByValue(self.toonMerits[toon.doId], meritArray)
            else:
                self.notify.debug('toon %d not helpful list, skipping merits' % toon.doId)
            if self.bossBattle:
                self.toonParts[toon.doId] = self.air.cogSuitMgr.recoverPart(
                                            toon, 'fullSuit', self.suitTrack,
                                            self.getTaskZoneId(), toons)
                self.notify.debug('toonParts = %s' % self.toonParts)

    def enterBoardOfficeReward(self):
        self.joinableFsm.request('Unjoinable')
        self.runableFsm.request('Unrunable')
        self.resetResponses()
        self.assignRewards()
        self.bossDefeated = 1
        self.level.setVictors(self.activeToons[:])
        self.timer.startCallback(BUILDING_REWARD_TIMEOUT, self.serverRewardDone)

    def exitBoardOfficeReward(self):
        pass

    def enterResume(self):
        DistributedLevelBattleAI.DistributedLevelBattleAI.enterResume(self)
        if self.bossBattle and self.bossDefeated:
            self.battleMgr.level.b_setDefeated()
