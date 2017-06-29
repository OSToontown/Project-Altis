import time
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from direct.fsm.FSM import FSM

class DistributedSofieListenerMgrAI(DistributedObjectAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedSofieListenerMgrAI")
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        FSM.__init__(self, 'ResistanceFSM')
        self.air = air
        
    def enterOff(self):
        self.requestDelete()

    def addAchievement(self):
        avId = self.air.getAvatarIdFromSender()
        self.air.achievementsManager.sofie(avId)

