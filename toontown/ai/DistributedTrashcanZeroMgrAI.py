from direct.directnotify import DirectNotifyGlobal
from toontown.ai.DistributedPhaseEventMgrAI import DistributedPhaseEventMgrAI

class DistributedTrashcanZeroMgrAI(DistributedPhaseEventMgrAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedTrashcanZeroMgrAI")
    
    def __init__(self, air):
        DistributedPhaseEventMgrAI.__init__(self, air)

