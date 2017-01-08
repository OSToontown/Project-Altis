from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedPhaseEventMgrAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPhaseEventMgrAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.numPhases = 0
        self.dates = []
        self.curPhase = 0
        self.isRunning = False

    def setNumPhases(self, numPhases):
        self.numPhases = numPhases

    def getNumPhases(self):
        return self.numPhases

    def setDates(self, dates):
        self.dates = dates

    def getDates(self):
        return self.dates

    def setCurPhase(self, curPhase):
        self.curPhase = curPhase

    def d_setCurPhase(self, curPhase):
        self.sendUpdate('setCurPhase', [curPhase])

    def b_setCurPhase(self, curPhase):
        self.setCurPhase(curPhase)
        self.d_setCurPhase(curPhase)

    def getCurPhase(self):
        return self.curPhase

    def setIsRunning(self, isRunning):
        self.isRunning = isRunning

    def d_setIsRunning(self, isRunning):
        self.sendUpdate('setIsRunning', [isRunning])

    def b_setIsRunning(self, isRunning):
        self.setIsRunning(isRunning)
        self.d_setIsRunning(isRunning)

    def getIsRunning(self):
        return self.isRunning