from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedPlantBaseAI import DistributedPlantBaseAI

class DistributedFlowerAI(DistributedPlantBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedFlowerAI")
    
    def __init__(self, air):
        self.air = air

        self.typeIndex = None

    def setTypeIndex(self, typeIndex):
        DistributedPlantBaseAI.setTypeIndex(self, typeIndex)
        self.typeIndex = typeIndex

    def getTypeIndex(self):
        return self.typeIndex
    
    def setVariety(self, variety):
        self.variety = variety
    
    def getVariety(self):
        return self.variety
