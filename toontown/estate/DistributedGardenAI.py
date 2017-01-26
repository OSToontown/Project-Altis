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
        
    def disable(self):
        DistributedObjectAI.disable(self)

    def delete(self):
        DistributedObjectAI.delete(self)

    def d_sendNewProp(self, prop, x, y, z):
        self.sendUpdate('sendNewProp', [prop, x, y, z])