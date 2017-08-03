from toontown.pets import Pet, PetBase
from direct.directnotify import DirectNotifyGlobal
from toontown.distributed.DelayDeletable import DelayDeletable
from direct.distributed import DistributedSmoothNode
from otp.otpbase import OTPGlobals
from panda3d.core import *
from panda3d.direct import *

class DistributedPublicPet(DistributedSmoothNode.DistributedSmoothNode, Pet.Pet, PetBase.PetBase, DelayDeletable):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPet')

    def __init__(self, cr):
        DistributedSmoothNode.DistributedSmoothNode.__init__(self, cr)
        Pet.Pet.__init__(self)
        self.proxyDo = 0
        self.proxy = None

    def beginPublicDisplay(self):
        DistributedPublicPet.notify.info("Received begin for public display")

    def announceGenerate(self):
        DistributedPublicPet.notify.info("Generated %d" % self.doId)
        DistributedSmoothNode.DistributedSmoothNode.announceGenerate(self)

    def setProxyDo(self, do):
        DistributedPublicPet.notify.info("Acquired proxy; doId %d" % do)
        self.proxyDo = do
        self.proxy = base.cr.doId2do[do]
        print(self.proxy)

    def __initCollisions(self):
        cRay = CollisionRay(0.0, 0.0, 40000.0, 0.0, 0.0, -1.0)
        cRayNode = CollisionNode('pet-cRayNode-%s' % self.doId)
        cRayNode.addSolid(cRay)
        cRayNode.setFromCollideMask(OTPGlobals.FloorBitmask)
        cRayNode.setIntoCollideMask(BitMask32.allOff())
        self.cRayNodePath = self.attachNewNode(cRayNode)
        self.lifter = CollisionHandlerFloor()
        self.lifter.setInPattern('enter%in')
        self.lifter.setOutPattern('exit%in')
        self.lifter.setOffset(OTPGlobals.FloorOffset)
        self.lifter.setReach(4.0)
        self.lifter.addCollider(self.cRayNodePath, self)
        self.cTrav = base.petManager.cTrav
        self.cTrav.addCollider(self.cRayNodePath, self.lifter)
        taskMgr.add(self._detectWater, self.getDetectWaterTaskName(), priority=32)
        self.initializeBodyCollisions('pet-%s' % self.doId)

    def __cleanupCollisions(self):
        self.disableBodyCollisions()
        taskMgr.remove(self.getDetectWaterTaskName())
        self.cTrav.removeCollider(self.cRayNodePath)
        del self.cTrav
        self.cRayNodePath.removeNode()
        del self.cRayNodePath
        del self.lifter

