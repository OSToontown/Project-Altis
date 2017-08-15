from toontown.suit.SuitDNA import suitDepts, suitsPerDept
from toontown.suit.SuitInvasionGlobals import *

import random


class InvasionManagerUD:

    def __init__(self, air):
        self.air = air

    def chooseInvasion(self, task=None):
        # Choose the invasion type:
        invasion = INVASION_TYPE_NORMAL 
        if random.random() <= 0.05:
            invasion = INVASION_TYPE_MEGA
        
        # Decide whether or not the invasion will have flags:
        flags = None
        flagChance = random.random()
        if flagChance <= 0.1:
            flags = IFV2
        elif flagChance <= 0.03:
            flags = IFWaiter
        elif flagChance <= 0.02:
            flags = IFSkelecog

        dept = random.randrange(0, len(suitDepts))
        suit = random.randrange(-1, suitsPerDept)

        if suit == -1:
            # No index, department invasion.
            invasion = INVASION_TYPE_MEGA

        print self.air.rpcServer.handler.shardStatus.shards
