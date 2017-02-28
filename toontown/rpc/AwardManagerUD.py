from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class AwardManagerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("AwardManagerUD")
    
    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def giveAwardToToon(self, rewardId, avId, rewardName, hours, seconds):
        pass

