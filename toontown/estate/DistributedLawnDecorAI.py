from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedNodeAI import DistributedNodeAI

class DistributedLawnDecorAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedLawnDecorAI")

    def __init__(self, air):
        DistributedNodeAI.__init__(self, air)

    def setPlot(self, plot):
        self.plot = plot

    def getPlot(self):
        return self.plot

    def setHeading(self, heading):
        self.heading = heading

    def getHeading(self):
        return self.heading

    def setPosition(self, position):
        self.position = position

    def getPosition(self):
        return self.position

    def setOwnerIndex(self, ownerIndex):
        self.ownerIndex = ownerIndex

    def getOwnerIndex(self):    
        return self.ownerIndex

    def generate(self):
        DistributedNodeAI.generate(self)

    def announceGenerate(self):
        DistributedNodeAI.announceGenerate(self)

    def plotEntered(self):
        pass

    def removeItem(self):
        pass

    def d_setMovie(self, mode, avId):
        self.sendUpdate('setMovie', [mode, avId])

    def movieDone(self):
        pass

    def d_interactionDenied(self, avId):
        self.sendUpdate('interactionDenied', [avId])

    def delete(self):
        DistributedNodeAI.delete(self)