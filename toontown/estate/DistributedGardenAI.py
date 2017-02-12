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

    def sendNewProp(self, todo0, todo1, todo2, todo3):
        pass