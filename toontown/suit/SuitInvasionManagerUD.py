from direct.showbase.DirectObject import DirectObject

from otp.distributed.OtpDoGlobals import MESSENGER_CHANNEL_AI

from toontown.suit.SuitDNA import suitDepts, suitsPerDept
from toontown.suit.SuitInvasionGlobals import *

import random


class SuitInvasionManagerUD(DirectObject):
    notify = directNotify.newCategory('SuitInvasionManagerUD')

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
        self.air.sendNetEvent('requestShards', channels=[MESSENGER_CHANNEL_AI])
        taskMgr.doMethodLater(self.getRandomDelay(), self.chooseInvasion, 'choose-task')

    def registerShard(self, shardId, online):
        shardId -= 1
        if online and (shardId not in self.shards):
            self.shards.append(shardId)
        elif (not online) and (shardId in self.shards):
            self.shards.remove(shardId)
            if shardId in self.occupiedShards:
                self.occupiedShards.remove(shardId)

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
        
        # Decide whether or not the invasion will have flags:
        flags = 0

        dept = random.randrange(0, len(suitDepts)-1)
        suit = random.randrange(-1, suitsPerDept)

        if suit == -1:
            # No suit index, therefore it must be a department invasion.
            invasion = INVASION_TYPE_MEGA

        self.occupiedShards.append(shardId)
        self.air.sendNetEvent('startInvasion', [shardId, dept, suit, flags, invasion], channels=[MESSENGER_CHANNEL_AI])
        return task.again
