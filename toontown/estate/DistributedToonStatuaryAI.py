from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedStatuaryAI import DistributedStatuaryAI

class DistributedToonStatuaryAI(DistributedStatuaryAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedToonStatuaryAI")

    def __init__(self, air):
        DistributedStatuaryAI.__init__(self, air)
        self.air = air
        self.optional = 0

    def setOptional(self, optional):
        self.optional = optional

    def getOptional(self):
        return self.optional