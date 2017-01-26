from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI

class DistributedStatuaryAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedStatuaryAI")

    def __init__(self, air):
        DistributedLawnDecorAI.__init__(self, air)

        self.waterLevel = 0
        self.growthLevel = 0

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex

    def getTypeIndex(self):
        return self.typeIndex

    def setWaterLevel(self, waterLevel):
        self.waterLevel = waterLevel

    def d_setWaterLevel(self, waterLevel):
        self.sendUpdate('setWaterLevel', [waterLevel])

    def b_setWaterLevel(self, waterLevel):
        self.setWaterLevel(waterLevel)
        self.d_setWaterLevel(waterLevel)

    def getWaterLevel(self):
        return self.waterLevel

    def setGrowthLevel(self, growthLevel):
        self.growthLevel = growthLevel

    def d_setGrowthLevel(self, growthLevel):
        self.sendUpdate('setGrowthLevel', [growthLevel])

    def b_setGrowthLevel(self, growthLevel):
        self.setGrowthLevel(growthLevel)
        self.d_setGrowthLevel(growthLevel)

    def getGrowthLevel(self):
        return self.growthLevel