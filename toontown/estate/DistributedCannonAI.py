from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import *
from toontown.minigame import CannonGameGlobals
from toontown.toonbase import ToontownGlobals
import CannonGlobals
class DistributedCannonAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedCannonAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.estateId = 0
        self.targetId = 0
        self.posHpr = (0, 0, 0, 0, 0, 0)
        self.bumperPos = ToontownGlobals.PinballCannonBumperInitialPos
        self.active = 0
        self.avId = 0
    
    def setEstateId(self, estateId):
        self.estateId = estateId
        
    def getEstateId(self):
        return self.estateId

    def setTargetId(self, targetId):
        self.targetId = targetId

    def getTargetId(self):
        return self.targetId
        
    def setPosHpr(self, x, y, z, h, p, r):
        self.posHpr = (x, y, z, h, p, r)
        
    def getPosHpr(self):
        return self.posHpr

    def setActive(self, active):
        self.active = active
        self.sendUpdate("setActiveState", [active])

    def setActiveState(self, todo0):
        pass

    def requestEnter(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if not self.avId:
            self.avId = avId
            self.setMovie(CannonGlobals.CANNON_MOVIE_LOAD, self.avId)
            self.acceptOnce(self.air.getAvatarExitEvent(avId), self.exitCannon, extraArgs = [CannonGlobals.CANNON_MOVIE_FORCE_EXIT])
        else:
            self.notify.warning("Cannon already occupied!")
            self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'requestExit', [])

    def requestExit(self):
        pass
        
    def exitCannon(self, movie):
        self.ignore(self.air.getAvatarExitEvent(self.avId))
        self.setMovie(movie, self.avId)
        self.avId = 0

    def setMovie(self, movie, avId):
        self.sendUpdate("setMovie", [movie, avId])

    def setCannonPosition(self, zRot, angle):
        self.updateCannonPosition(self.avId, zRot, angle)

    def setCannonLit(self, zRot, angle): # lit
        avId = self.air.getAvatarIdFromSender()
        if avId != self.avId:
            return
        self.setCannonWillFire(avId, CannonGameGlobals.FUSE_TIME, zRot, angle, globalClockDelta.getRealNetworkTime())

    def setFired(self):
        pass

    def setLanded(self):
        self.setCannonExit(self.avId)

    def updateCannonPosition(self, avId, zRot, angle):
        self.sendUpdate("updateCannonPosition", [avId, zRot, angle])

    def setCannonWillFire(self, avId, fuseTime, zRot, angle, gtime):
        self.sendUpdate('setCannonWillFire', [avId, fuseTime, zRot, angle, gtime])

    def setCannonExit(self, avId):
        self.exitCannon(movie = CannonGlobals.CANNON_MOVIE_CLEAR)
        self.sendUpdate('setCannonExit', [avId])

    def requestBumperMove(self, x, y, z):
        self.setCannonBumperPos(x, y, z)

    def setCannonBumperPos(self, x, y, z):
        self.bumperPos = (x, y, z)
        self.sendUpdate('setCannonBumperPos', [x, y, z])
        
    def getCannonBumperPos(self):
        return self.bumperPos

