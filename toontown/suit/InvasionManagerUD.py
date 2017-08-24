from direct.showbase.DirectObject import DirectObject

from toontown.suit.SuitDNA import suitDepts, suitsPerDept
from toontown.suit.SuitInvasionGlobals import *

import random


class InvasionManagerUD(DirectObject):
    notify = directNotify.newCategory('InvasionManagerUD')

    def __init__(self, air):
        DirectObject.__init__(self)

        self.air = air
        self.shards = []
        self.accept('registerShard', self.registerShard)

    def registerShard(self, shardId, online):
        if online and (shardId not in self.shards):
            self.shards.append(shardId)
        elif (not online) and (shardId in self.shards):
            self.shards.remove(shardId)

    def chooseInvasion(self, task=None):
        if not len(self.shards):
            return task.again

        # 40% chance to start an invasion:
        invasionChance = random.random()
        if invasionChance >= 0.40:
            return task.again

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

        self.notify.warning([invasion, flags, flagChance, dept, suit])
        shard = random.choice(self.shards)

        task.delayTime = 3600 # TODO: Generate a random time.
        return task.again
