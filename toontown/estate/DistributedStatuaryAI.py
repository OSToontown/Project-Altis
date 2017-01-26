from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI

class DistributedStatuaryAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedStatuaryAI")

    def __init__(self, air):
        DistributedLawnDecorAI.__init__(self, air)
        self.air = air

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex

    def getTypeIndex(self):
        return self.typeIndex

    def setOwnerPlot(self, owner):
        self.ownerPlot = owner

    def getOwnerPlot(self):
        return self.ownerPlot

    def setWaterLevel(self, waterLevel):
        self.waterLevel = waterLevel

    def getWaterLevel(self):
        return self.waterLevel

    def setGrowthLevel(self, growthLevel):
        self.growthLevel = growthLevel

    def getGrowthLevel(self):
        return self.growthLevel