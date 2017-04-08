from direct.directnotify import DirectNotifyGlobal
from toontown.building.DistributedBuildingAI import DistributedBuildingAI

class DistributedAnimBuildingAI(DistributedBuildingAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedAnimBuildingAI")
	
    def __init__(self, air, blockNumber, zoneId, trophyMgr):
        DistributedBuildingAI.DistributedBuildingAI.__init__(self, air)

