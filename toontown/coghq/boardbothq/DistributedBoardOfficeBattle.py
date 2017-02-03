from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from toontown.battle.BattleBase import *
from toontown.coghq import DistributedLevelBattle
from direct.directnotify import DirectNotifyGlobal
from toontown.toon import TTEmote
from otp.avatar import Emote
from toontown.battle import SuitBattleGlobals
import random
from toontown.suit import SuitDNA
from direct.fsm import State
from direct.fsm import ClassicFSM, State
from toontown.toonbase import ToontownGlobals
from toontown.nametag import NametagGlobals

class DistributedBoardOfficeBattle(DistributedLevelBattle.DistributedLevelBattle):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeBattle')

    def __init__(self, cr):
        DistributedLevelBattle.DistributedLevelBattle.__init__(self, cr)
        self.fsm.addState(State.State('BoardOfficeReward', self.enterBoardOfficeReward, self.exitBoardOfficeReward, ['Resume']))
        offState = self.fsm.getStateNamed('Off')
        offState.addTransition('BoardOfficeReward')
        playMovieState = self.fsm.getStateNamed('PlayMovie')
        playMovieState.addTransition('BoardOfficeReward')

    def enterBoardOfficeReward(self, ts):
        self.notify.debug('enterBoardOfficeReward()')
        self.disableCollision()
        self.delayDeleteMembers()
        if self.hasLocalToon():
            NametagGlobals.setWant2dNametags(False)
            if self.bossBattle:
                messenger.send('localToonConfrontedBoardOfficeBoss')
        self.movie.playReward(ts, self.uniqueName('building-reward'), self.__handleBoardOfficeRewardDone, noSkip=True)

    def __handleBoardOfficeRewardDone(self):
        self.notify.debug('boardoffice reward done')
        if self.hasLocalToon():
            self.d_rewardDone(base.localAvatar.doId)
        self.movie.resetReward()
        self.fsm.request('Resume')

    def exitBoardOfficeReward(self):
        self.notify.debug('exitBoardOfficeReward()')
        self.movie.resetReward(finish=1)
        self._removeMembersKeep()
        NametagGlobals.setWant2dNametags(True)
