from direct.directnotify import DirectNotifyGlobal
from toontown.estate.DistributedLawnDecorAI import DistributedLawnDecorAI
from toontown.estate import DistributedToonStatuaryAI, DistributedStatuaryAI,\
    GardenGlobals, DistributedFlowerAI, DistributedGagTreeAI
import datetime

class DistributedGardenPlotAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGardenPlotAI")

    def __init__(self, air):
        DistributedLawnDecorAI.__init__(self, air)
        
        self.getPlotFromSlot = {0: GardenGlobals.plots0,
                                1: GardenGlobals.plots1,
                                2: GardenGlobals.plots2,
                                3: GardenGlobals.plots3,
                                4: GardenGlobals.plots4,
                                5: GardenGlobals.plots5}
        
    def announceGenerate(self):
        DistributedLawnDecorAI.announceGenerate(self)
        
    def delete(self):
        DistributedLawnDecorAI.delete(self)
        
    def disable(self):
        DistributedLawnDecorAI.disable(self)
        
    def finishPlanting(self, avId):
        self.planted.generateWithRequired(self.zoneId)
        self.addGardenData()
        self.sendUpdate('plantedItem', [self.planted.doId])
        self.planted.sendUpdate('setMovie', [GardenGlobals.MOVIE_FINISHPLANTING, avId])
        
    def finishRemove(self, avId):
        self.deleteGardenData()
        if not self.planted:
            self.notify.warning("%d tried to remove a garden item that doesnt exist" % avId)
            return
        self.planted.removeNode()
        self.planted.delete()
        simbase.air.removeObject(self.planted.doId)
        self.planted = None
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_FINISHREMOVING, avId])
        
    def addGardenData(self):
        estate = simbase.air.doId2do.get(self.getEstate())
        plantTime = int(datetime.datetime.now().strftime('%Y%m%d%H%M'))
        if isinstance(self.planted, DistributedFlowerAI.DistributedFlowerAI):
            data = [self.getPlot(), GardenGlobals.FLOWER_TYPE, self.planted.getTypeIndex(), self.planted.getVariety(), self.planted.getWaterLevel(), self.planted.getGrowthLevel(), 0, plantTime, plantTime]
        elif isinstance(self.planted, DistributedGagTreeAI.DistributedGagTreeAI):
            data = [self.getPlot(), GardenGlobals.GAG_TREE_TYPE, self.planted.getTypeIndex(), 0, self.planted.getWaterLevel(), self.planted.getGrowthLevel(), 0, plantTime, plantTime]
        elif isinstance(self.planted, DistributedStatuaryAI.DistributedStatuaryAI):
            data = [self.getPlot(), GardenGlobals.STATUARY_TYPE, self.planted.getTypeIndex(), 0, self.planted.getWaterLevel(), self.planted.getGrowthLevel(), 0, plantTime, plantTime]
        elif isinstance(self.planted, DistributedToonStatuaryAI.DistributedToonStatuaryAI):
            data = [self.getPlot(), GardenGlobals.TOON_STATUARY_TYPE, self.planted.getTypeIndex(), 0, self.planted.getWaterLevel(), self.planted.getGrowthLevel(), self.planted.getOptional(), plantTime, plantTime]
        else:
            self.notify.warning("Tried to add garden data for an unknown object type! Uh oh!")
            return
        estate.items[self.getOwnerIndex()].appendd(tuple(data))
        estate.updateItems()

    def deleteGardenData(self):
        estate = simbase.air.doId2do.get(self.getEstate())
        dataIndex = -1
        for index, item in enumerate(estate.items[self.getOwnerIndex()]):
            if item[0] == self.getPlot():
                dataIndex = index
        if dataIndex >=0:
            del estate.items[self.getOwnerIndex()][dataIndex]
            estate.updateItems()

    def plotEntered(self):
        pass

    def removeItem(self):
        pass

    def plantFlower(self, species, variety, av):
        self.planted = DistributedFlowerAI.DistributedFlowerAI()
        self.planted.setEstate(self.getEstate())
        self.planted.setOwnerIndex(self.getOwnerIndex())
        self.planted.setOwnerPlot(self.doId)
        self.planted.setPlot(self.getPlot())
        self.planted.setPosition(*self.getPosition())
        self.planted.setHeading(self.getHeading())
        self.planted.setWaterLevel(0)
        self.planted.setGrowthLevel(0)
        self.planted.setTypeIndex(species)
        self.planted.setVariety(variety)
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_PLANT, av])

    def plantGagTree(self, track, level, av):
        self.planted = DistributedGagTreeAI.DistributedGagTreeAI()
        self.planted.setEstate(self.getEstate())
        self.planted.setOwnerIndex(self.getOwnerIndex())
        self.planted.setOwnerPlot(self.doId)
        self.planted.setPlot(self.getPlot())
        self.planted.setPosition(*self.getPosition())
        self.planted.setHeading(self.getHeading())
        self.planted.setWaterLevel(0)
        self.planted.setGrowthLevel(0)
        self.planted.setTypeIndex(GardenGlobals.getTreeTypeIndex(track, level))
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_PLANT, av])

    def plantStatuary(self, type, av):
        self.planted = DistributedStatuaryAI.DistributedStatuaryAI()
        self.planted.setEstate(self.getEstate())
        self.planted.setOwnerIndex(self.getOwnerIndex())
        self.planted.setOwnerPlot(self.doId)
        self.planted.setPlot(self.getPlot())
        self.planted.setPosition(*self.getPosition())
        self.planted.setHeading(self.getHeading())
        self.planted.setWaterLevel(0)
        self.planted.setGrowthLevel(0)
        self.planted.setTypeIndex(type)
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_PLANT, av])

    def plantToonStatuary(self, type, dna, av):
        self.planted = DistributedToonStatuaryAI.DistributedToonStatuaryAI()
        self.planted.setEstate(self.getEstate())
        self.planted.setOwnerIndex(self.getOwnerIndex())
        self.planted.setOwnerPlot(self.doId)
        self.planted.setPlot(self.getPlot())
        self.planted.setPosition(*self.getPosition())
        self.planted.setHeading(self.getHeading())
        self.planted.setWaterLevel(0)
        self.planted.setGrowthLevel(0)
        self.planted.setTypeIndex(type)
        self.planted.setOptional(dna)
        self.sendUpdate('setMovie', [GardenGlobals.MOVIE_PLANT, av])

    def plantNothing(self, beans, toon):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do[avId]
        jbs = av.getMoney()
        av.setMoney(jbs - beans)
        av.d_setMoney(jbs - beans)
        self.planted = None