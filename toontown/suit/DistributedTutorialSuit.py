from toontown.suit import DistributedSuitBase
from direct.directnotify import DirectNotifyGlobal
from direct.interval.IntervalGlobal import *
from toontown.toonbase import TTLocalizer
from direct.fsm import ClassicFSM, State
from toontown.chat.ChatGlobals import *
from direct.fsm import State
from pandac.PandaModules import *
from toontown.suit import SuitDNA
from toontown.distributed.DelayDeletable import DelayDeletable

class DistributedTutorialSuit(DistributedSuitBase.DistributedSuitBase, DelayDeletable):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTutorialSuit')

    def __init__(self, cr):
        try:
            self.DistributedSuit_initialized
            return
        except:
            self.DistributedSuit_initialized = 1
        
        DistributedSuitBase.DistributedSuitBase.__init__(self, cr)
        self.fsm = ClassicFSM.ClassicFSM('DistributedSuit', [State.State('Off', self.enterOff, self.exitOff, ['Walk', 'Battle']),
         State.State('Walk', self.enterWalk, self.exitWalk, ['WaitForBattle', 'Battle']),
         State.State('Battle', self.enterBattle, self.exitBattle, []),
         State.State('WaitForBattle', self.enterWaitForBattle, self.exitWaitForBattle, ['Battle'])], 'Off', 'Off')
        self.fsm.enterInitialState()
        self.acceptOnce('zoneChange', self.doZoneMovie)

    def generate(self):
        DistributedSuitBase.DistributedSuitBase.generate(self)

    def announceGenerate(self):
        DistributedSuitBase.DistributedSuitBase.announceGenerate(self)
        self.setState('Walk')

    def disable(self):
        self.notify.debug('DistributedSuit %d: disabling' % self.getDoId())
        self.setState('Off')
        DistributedSuitBase.DistributedSuitBase.disable(self)

    def delete(self):
        try:
            self.DistributedSuit_deleted
            return
        except:
            self.DistributedSuit_deleted = 1
        
        self.notify.debug('DistributedSuit %d: deleting' % self.getDoId())
        del self.fsm
        DistributedSuitBase.DistributedSuitBase.delete(self)

    def d_requestBattle(self, pos, hpr):
        self.cr.playGame.getPlace().setState('WaitForBattle')
        self.sendUpdate('requestBattle', [pos[0], pos[1], pos[2], hpr[0], hpr[1], hpr[2]])

    def __handleToonCollision(self, collEntry):
        pass
		
    def doZoneMovie(self, zoneId):
        if zoneId == self.zoneId:
            avHeight = max(base.localAvatar.getHeight(), 3.0)
            scaleFactor = avHeight * 0.3333333333
            track = Sequence()
            track.append(Wait(1))
            track.append(Func(self.setChatAbsolute, TTLocalizer.TutorialSuit1, CFSpeech | CFTimeout))
            track.append(Wait(3))
            track.append(Func(self.setChatAbsolute, TTLocalizer.TutorialSuitTaunt.get(SuitDNA.getSuitDept(self.dna.name)), CFSpeech | CFTimeout))
            track.append(Wait(3))
            track.append(Func(self.d_requestBattle, self.getPos(), self.getHpr()))
            track.start()

    def enterWalk(self):
        self.enableBattleDetect('walk', self.__handleToonCollision)
        self.loop('neutral', 0)
        self.setPos(30, 20, -0.5)
        self.setH(90)

    def exitWalk(self):
        self.disableBattleDetect()