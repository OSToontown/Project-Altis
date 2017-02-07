from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD

class AwardManagerUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("AwardManagerUD")

    def giveAwardToToon(self, rewardId, avId, rewardName, hours, seconds):
        pass

