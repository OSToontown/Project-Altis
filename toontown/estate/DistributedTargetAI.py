from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from panda3d.core import *
import CannonGlobals

class DistributedTargetAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedTargetAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self.air)
        self.position = None
        
    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        taskMgr.doMethodLater(CannonGlobals.GAME_DELAY, self.startGame, 'startGameTask')
    
    def startGame(self):
        pass
        
    def endGame(self):
        pass
    
    def setPosition(self, x, y, z):
        self.sendUpdate('setPosition', [x, y, z])
        self.position = Point3(x, y, z)
    
    def getPosition(self):
        return self.position

    def setState(self, enabled, score, time):
        pass

    def setReward(self, reward):
        pass

    def setResult(self, avId):
        pass

    def setBonus(self, bonus):
        pass

    def setCurPinballScore(self, avId, score, multiplier):
        pass

    def setPinballHiScorer(self, name):
        pass

    def setPinballHiScore(self, score):
        pass

