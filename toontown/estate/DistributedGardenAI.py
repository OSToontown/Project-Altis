import random
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.estate import GardenGlobals
from toontown.estate import HouseGlobals
from toontown.toonbase import TTLocalizer
from toontown.estate.DistributedGardenBoxAI import DistributedGardenBoxAI
from toontown.estate.DistributedGardenPlotAI import DistributedGardenPlotAI
from toontown.estate.DistributedToonStatuaryAI import DistributedToonStatuaryAI

class DistributedGardenAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedGardenAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.gardenBoxes = []
        self.gardenPlots = []

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        self.__createGardenDrops()
        self.__createGardenBoxes()
        self.__createEstatePlots()

    def __createGardenDrops(self):
        for index in xrange(HouseGlobals.NUM_PROPS):
            self.d_sendNewProp(HouseGlobals.PROP_ICECUBE, *HouseGlobals.gardenDrops[index])

    def __createGardenBoxes(self):
        for index in xrange(len(GardenGlobals.estateBoxes)):
            flowerBoxes = GardenGlobals.estateBoxes[index]

            for flowerBox in flowerBoxes:
                x, y, heading, typeIndex = flowerBox
            
                gardenBox = DistributedGardenBoxAI(self.air)
                gardenBox.setPlot(index)
                gardenBox.setHeading(heading)
                gardenBox.setPosition((x, y, 0))
                gardenBox.setOwnerIndex(1) # TODO: get the owner index from DistributedEstate!
                gardenBox.setTypeIndex(typeIndex)
                gardenBox.generateWithRequired(self.zoneId)
                self.gardenBoxes.append(gardenBox)

    def __deleteGardenBoxes(self):
        for gardenBox in self.gardenBoxes:
            gardenBox.requestDelete()

    def __createEstatePlots(self):
        for index in xrange(len(GardenGlobals.estatePlots)):
            estatePlots = GardenGlobals.estatePlots[index]

            for estatePlot in estatePlots:
                x, y, heading, plotType = estatePlot

                gardenPlot = DistributedGardenPlotAI(self.air)
                gardenPlot.setPlot(plotType)
                gardenPlot.setHeading(heading)
                gardenPlot.setPosition((x, y, 0))
                gardenPlot.setOwnerIndex(1)
                gardenPlot.generateWithRequired(self.zoneId)
                self.gardenPlots.append(gardenPlot)

    def __deleteEstatePlots(self):
        for gardenPlot in self.gardenPlots:
            gardenPlot.requestDelete()

    def delete(self):
        DistributedObjectAI.delete(self)

        self.__deleteGardenBoxes()
        self.__deleteEstatePlots()

    def d_sendNewProp(self, prop, x, y, z):
        self.sendUpdate('sendNewProp', [prop, x, y, z])