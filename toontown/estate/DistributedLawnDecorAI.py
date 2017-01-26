from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedNodeAI import DistributedNodeAI
from toontown.estate import GardenGlobals

class DistributedLawnDecorAI(DistributedNodeAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedLawnDecorAI")

    def __init__(self, air):
        DistributedNodeAI.__init__(self, air)
        self.air = air
        self.plot = None
        self.ownerIndex = None

    def delete(self):
        DistributedNodeAI.delete(self)
        
    def disable(self):
        DistributedNodeAI.disable(self)
        
    def setEstate(self, estate):
        self.estate = estate
        
    def getEstate(self):
        return self.estate

    def setPlot(self, plot):
        self.plot = plot

    def getPlot(self):
        return self.plot

    def setHeading(self, heading):
        self.heading = heading

    def getHeading(self):
        return self.heading

    def setPosition(self, x, y, z):
        self.position = (x, y, z)

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

    def removeItem(self, avId):
        self.user = avId
        self.d_setMovie(GardenGlobals.MOVIE_REMOVE, avId)

    def d_setMovie(self, mode, avId):
        self.sendUpdate('setMovie', [mode, avId])

    def movieDone(self):
        if hasattr(self, user):
            del self.user

    def d_interactionDenied(self, avId):
        self.sendUpdate('interactionDenied', [avId])

    def delete(self):
        DistributedNodeAI.delete(self)