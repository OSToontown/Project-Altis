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

    def setDates(self, dates):
        self.dates = dates

    def getDates(self):
        return self.dates
        
    def setNumPhases(self, phaseAmount):
        if phaseAmount != int(phaseAmount):
            return
        
        self.numPhases = phaseAmount

    def d_setNumPhases(self, phaseAmount):
        if phaseAmount != int(phaseAmount):
            return
        
        self.sendUpdate('setNumPhases', [phaseAmount])
        
    def b_setNumPhases(self, phaseAmount):
        if phaseAmount != int(phaseAmount):
            return
        
        self.setNumPhases(phaseAmount)
        self.d_setNumPhases(phaseAmount)
        
    def getNumPhases(self):
        return self.numPhases
        
    def setCurPhase(self, phase):
        if phase != int(phase):
            return
        
        self.curPhase = phase

    def d_setCurPhase(self, phase):
        if phase != int(phase):
            return
        
        self.sendUpdate('setCurPhase', [phase])
        
    def b_setCurPhase(self, phase):
        if phase != int(phase):
            return
        
        self.setCurPhase(phase)
        self.d_setCurPhase(phase)
        
    def getCurPhase(self):
        return self.curPhase
 
    def setIsRunning(self, bool):
        if bool not in [True, False, 0, 1]:
            return
         
        if bool == 0:
            bool = False
        
        self.isRunning = bool

    def d_setIsRunning(self, bool):
        if bool not in [True, False, 0, 1]:
            return
         
        if bool == 0:
            bool = False
        
        self.sendUpdate("setIsRunning", [bool])
        
    def b_setIsRunning(self, bool):
        if bool not in [True, False, 0, 1]:
            return
         
        if bool == 0:
            bool = False
        
        self.setIsRunning(bool)
        self.d_setIsRunning(bool)
 
    def getIsRunning(self):
        return self.isRunning 

