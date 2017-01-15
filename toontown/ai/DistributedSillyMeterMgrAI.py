from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.ai.DistributedPhaseEventMgrAI import DistributedPhaseEventMgrAI
from otp.ai.MagicWordGlobal import *

class DistributedSillyMeterMgrAI(DistributedPhaseEventMgrAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedSillyMeterMgrAI")
    
    def __init__(self, air):
        DistributedPhaseEventMgrAI.__init__(self, air)
        
    def setCheckedPhase(self, phase):
        if phase <= -1:
           self.b_setCurPhase(-1)
           self.b_setIsRunning(False)
           return
        elif phase > 15:
           self.b_setCurPhase(-1)
           self.b_setIsRunning(False)
           return
          
        self.b_setCurPhase(phase)
        self.b_setIsRunning(True)
        messenger.send('SillyMeterPhase', [phase])

@magicWord(category=CATEGORY_PROGRAMMER, types=[int])
def setSillyMeterPhase(phase):
    '''
    Sets the Silly Meters Phase!
    '''
    if phase > 15:
        return("Phase is too high! (-1 to 15) can be used!")
    if phase < -1:
        return("Phase is too low! (-1 to 15) can be used!")
        
    if phase == -1:
        simbase.air.sillyMeterMgr.b_setCurPhase(phase)
        simbase.air.sillyMeterMgr.b_setIsRunning(False)
        messenger.send('SillyMeterPhase', [phase])
        return("Turned Off The Silly Meter!")
    
    simbase.air.sillyMeterMgr.b_setCurPhase(phase)
    simbase.air.sillyMeterMgr.b_setIsRunning(True)
    messenger.send('SillyMeterPhase', [phase])
    return "Set Silly Meters Phase!"