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
        self.occupiedShards = []
        self.accept('registerShard', self.registerShard)
        self.accept('invasionEnded', self.invasionEnded)

    def invasionEnded(self, shardId):
        if shardId not in self.occupiedShards:
            return
        self.occupiedShards.remove(shardId)

    def getRandomDelay(self):
        return int(3600 * random.random())

    def startInitialInvasion(self):
        taskMgr.doMethodLater(self.getRandomDelay(), self.chooseInvasion, 'choose-task')

    def registerShard(self, shardId, online):
        if online and (shardId not in self.shards):
            self.shards.append(shardId)
        elif (not online) and (shardId in self.shards):
            self.shards.remove(shardId)

    def chooseInvasion(self, task=None):
        task.delayTime = self.getRandomDelay()
        if not len(self.shards):
            return task.again

        shardId = random.choice(self.shards)
        
        if shardId in self.occupiedShards:
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
        flags = 0
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
            # No suit index, therefore it must be a department invasion.
            invasion = INVASION_TYPE_MEGA

        self.occupiedShards.append(shardId)
        self.air.sendNetEvent('startInvasion', [shardId, [dept, suit, flags, invasion]])
        return task.again
