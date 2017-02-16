from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from panda3d.core import *
import CannonGlobals

class DistributedTargetAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedTargetAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.isActive = False
        self.position = (0, 0, 0)
        self.level = 1
        self.timeLeft = CannonGlobals.CANNON_TIMEOUT
        self.highScoreAv = None
        self.highScore = 0
        self.currentState = None
        self.playerScores = {}
        
    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        taskMgr.doMethodLater(CannonGlobals.START_DELAY, self.startGame, 'startGameTask')
    
    def delete(self):
        taskMgr.remove('startGameTask')
    
    def startGame(self, task):
        self.isActive = True
        # Reset time and stuff
        self.level = 1
        self.timeLeft = CannonGlobals.CANNON_TIMEOUT
        self.setState(self.isActive, self.level, self.timeLeft)
        self.sendUpdate("setState", self.getState())
        
        # End game after 40 seconds
        taskMgr.doMethodLater(CannonGlobals.CANNON_TIMEOUT, self.endGame, 'endGameTask')
        return task.done
        
    def endGame(self, task):
        self.isActive = False
        self.timeLeft = 0
        self.setState(self.isActive, self.level, self.timeLeft)
        self.sendUpdate("setState", self.getState())
        taskMgr.doMethodLater(10, self.startGame, self.taskName('startGameTask'))
        
        for avId in self.playerScores:
            av = self.air.doId2do.get(avId)
            if av:
                if av.zoneId != self.zoneId:
                    self.notify.warning("AVID %s was in the target scores list, but wasnt in the zone!")
                    return
                av.toonUp(self.level)
        return task.done
    
    def setPosition(self, x, y, z):
        self.sendUpdate('setPosition', [x, y, z])
        self.position = (x, y, z)
    
    def getPosition(self):
        return self.position

    def setState(self, enabled, score, time):
        self.currentState = (enabled, score, time)
    
    def getState(self):
        return self.currentState

    def setReward(self, reward):
        self.sendUpdate('setReward', [reward])

    def setResult(self, avId):
        if not avId or not self.isActive:
            return
        self.level += 1
        self.timeLeft = int(CannonGlobals.CANNON_TIMEOUT / self.level)
        taskMgr.remove('endGameTask')
        taskMgr.doMethodLater(self.timeLeft, self.endGame, 'endGameTask')
        self.sendUpdate("setState", self.getState())

    def setBonus(self, bonus):
        pass

    def setCurPinballScore(self, avId, score, multiplier):
        av = self.air.doId2do.get(avId)
        if not av:
            return
        finalScore = score * multiplier
        # Set the players score in the dict
        self.playerScores[avId] = finalScore
        # Check if the score is greater than high score
        if finalScore > self.highScore:
            # If so, set the new high score
            self.highScoreAv = av
            self.highScore = finalScore
            # Finally, send the updates
            self.setPinballHiScorer(av.getName())
            self.setPinballHiScore(finalScore)

    def setPinballHiScorer(self, name):
        self.sendUpdate("setPinballHiScorer", [name])

    def setPinballHiScore(self, score):
        self.sendUpdate("setPinballHiScore", [score])

