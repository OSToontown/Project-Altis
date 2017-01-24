from toontown.safezone import DistributedTreasureAI
from toontown.toonbase import ToontownGlobals

class DistributedSZTreasureAI(DistributedTreasureAI.DistributedTreasureAI):

    def __init__(self, air, treasurePlanner, treasureType, x, y, z):
        DistributedTreasureAI.DistributedTreasureAI.__init__(self, air, treasurePlanner, treasureType, x, y, z)
        self.healAmount = treasurePlanner.healAmount
