from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClubAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubAI')
    
    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)