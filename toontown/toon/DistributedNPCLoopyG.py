from pandac.PandaModules import *
from toontown.toon.DistributedNPCToon import *

class DistributedNPCLoopyG(DistributedNPCToon):

    def __init__(self, cr):
        DistributedNPCToon.__init__(self, cr)
        self.npcType = "Meatball Cook"

    def initPos(self):
        self.setGlasses(17, 0, 0)
        self.setHat(26, 0, 0)
        self.setBackpack(23, 0, 0)
        self.setShoes(1, 31, 0)