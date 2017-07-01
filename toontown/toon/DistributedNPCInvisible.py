from pandac.PandaModules import *
from toontown.toon.DistributedNPCToon import *

class DistributedNPCInvisible(DistributedNPCToon):

    def __init__(self, cr):
        DistributedNPCToon.__init__(self, cr)
        self.npcType = "Vanished Shopkeeper"

    def initPos(self):
        self.setCheesyEffect(11, 0, 0)