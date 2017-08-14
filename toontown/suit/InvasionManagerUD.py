from direct.distributed.DistributedObjectUD import DistributedObjectUD

from toontown.suit.SuitInvasionGlobals import *

import random


class InvasionManagerUD(DistributedObjectUD):

    def __init__(self, air):
        DistributedObjectUD.__init__(self, air)
    
    def chooseInvasion(self):
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
