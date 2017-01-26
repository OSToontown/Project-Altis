from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI

class DistributedGardenBoxAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGardenBoxAI")

    def __init__(self, air):
        DistributedLawnDecorAI.__init__(self, air)

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex

    def getTypeIndex(self):
        return self.typeIndex