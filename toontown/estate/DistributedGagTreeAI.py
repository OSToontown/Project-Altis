from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedPlantBaseAI import DistributedPlantBaseAI
from toontown.estate import GardenGlobals

class DistributedGagTreeAI(DistributedPlantBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGagTreeAI")
    
    def __init__(self, air):
        DistributedPlantBaseAI.__init__(self, air)
        self.air = air
        self.wilted = 0
        
    def announceGenerate(self):
        DistributedPlantBaseAI.announceGenerate(self)
        
    def delete(self):
        DistributedPlantBaseAI.delete(self)
        
    def disable(self):
        DistributedPlantBaseAI.disable(self)

    def setWilted(self, wilted):
        self.wilted = wilted
        
    def getWilted(self):
        return self.wilted

    def requestHarvest(self, doId):
        avatar = simbase.air.doId2do.get(doId)
        amtHarvested = 0
        track, level = GardenGlobals.getTreeTrackAndLevel(self.typeIndex)
        while amtHarvested < 10 and avatar.inventory.addItem(track, level) > 0:
            amtHarvested += 1
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_HARVEST, doId])

