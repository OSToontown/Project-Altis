from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI
from toontown.estate import GardenGlobals
import datetime

class DistributedPlantBaseAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPlantBaseAI")

    def __init__(self, air):
        DistributedLawnDecorAI.__init__(self, air)
        self.air = air
        self.growthLevel = -1

    def announceGenerate(self):
        DistributedLawnDecorAI.announceGenerate(self)

    def delete(self):
        DistributedLawnDecorAI.delete(self)

    def disable(self):
        DistributedLawnDecorAI.disable(self)

    def setOwnerPlot(self, owner):
        self.ownerPlot = owner

    def getOwnerPlot(self):
        return self.ownerPlot

    def setTypeIndex(self, typeIndex):
        self.typeIndex = typeIndex
        self.attributes = GardenGlobals.PlantAttributes[typeIndex]
        self.name = self.attributes['name']
        self.plantType = self.attributes['plantType']
        self.growthThresholds = self.attributes['growthThresholds']
        self.maxWaterLevel = self.attributes['maxWaterLevel']
        self.minWaterLevel = self.attributes['minWaterLevel']

    def getTypeIndex(self):
        return self.typeIndex

    def setWaterLevel(self, water):
        self.waterLevel = water

    def getWaterLevel(self):
        return self.waterLevel

    def setGrowthLevel(self, growth):
        self.growthLevel = growth

    def getGrowthLevel(self):
        return self.growthLevel

    def waterPlant(self, avId):
        self.lastWateredBy = avId
        newLevel = self.waterLevel + 1
        if newLevel > self.maxWaterLevel:
            self.setWaterLevel(self.maxWaterLevel)
        else:
            self.setWaterLevel(newLevel)
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_WATER, avId])
        self.sendUpdate('setWaterLevel', [self.getWaterLevel()])

    def waterPlantDone(self):
        if hasattr(self, 'lastWateredBy'):
            av = simbase.air.doId2do.get(self.lastWateredBy)
            skill = av.getWateringCanSkill()
            skill += GardenGlobals.WateringCanAttributes[av.wateringCan]['skillPts'] / 100
            av.b_setWateringCanSkill(skill)
            del self.lastWateredBy
        estate = simbase.air.doId2do.get(self.getEstate())
        dataIndex = -1
        for n, item in enumerate(estate.items[self.getOwnerIndex()]):
            if item[0] == self.getPlot():
                dataIndex = n
        if dataIndex >= 0:
            dtime = int(datetime.datetime.now().strftime('%Y%m%d%H%M'))
            data = list(estate.items[self.getOwnerIndex()][dataIndex])
            data[4] = self.getWaterLevel()
            data[8] = dtime
            estate.items[self.getOwnerIndex()][dataIndex] = tuple(data)
            estate.updateItems()