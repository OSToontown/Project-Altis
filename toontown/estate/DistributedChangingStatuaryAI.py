from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedStatuaryAI import DistributedStatuaryAI

class DistributedChangingStatuaryAI(DistributedStatuaryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedChangingStatuaryAI")

    def __init__(self, air):
        DistributedStatuaryAI.__init__(self, air)
        self.air = air
        self.growth = -1

    def setGrowthLevel(self, growth):
        self.growth = growth

    def getGrowthLevel(self):
        return self.growth