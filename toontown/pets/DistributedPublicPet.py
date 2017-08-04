from toontown.pets import DistributedPet
from direct.directnotify import DirectNotifyGlobal
from toontown.distributed.DelayDeletable import DelayDeletable
from otp.otpbase import OTPGlobals
from panda3d.core import *
from panda3d.direct import *
from direct.interval.IntervalGlobal import *

class DistributedPublicPet(DistributedPet.DistributedPet):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPet')

    def __init__(self, cr):
        DistributedPet.DistributedPet.__init__(self, cr, ready = False)

    def makeSphere(self):
        # Tubby said I couldn't make CollisionSpheres on the AI so it's on the client now
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 3.0)
        self.cSphere.setTangible(0)
        self.cSphereNode = CollisionNode('PetSphere')
        self.cSphereNode.addSolid(self.cSphere)
        self.cSphereNodePath = self.attachNewNode(self.cSphereNode)
        self.cSphereNodePath.reparentTo(self)
        self.cSphereNode.setCollideMask(OTPGlobals.WallBitmask)

        self.accept('exit' + self.cSphereNode.getName(), self.__collisionExit)
        self.accept('enter' + self.cSphereNode.getName(), self.__collisionEnter)

    def __collisionEnter(self, collEntry):
        self.sendUpdate('sphereEntered', [])

    def __collisionExit(self, collEntry):
        self.sendUpdate('sphereLeft', [])

    def beginPublicDisplay(self):
        DistributedPublicPet.notify.info("Received begin for public display")
        DistributedPet.DistributedPet.announceGenerate(self) # Hack to fix pet DNA
        self.ready = True

        d = Func(self.pose, 'reappear', 0)
        e = self.getTeleportInTrack()
        g = Func(self.loop, 'neutral')
        Sequence(d, e, g).start()

        if self.getOwnerId() == base.localAvatar.doId:
            self.notify.info("Setting up our own pet")
            base.localAvatar.publicPetId = self.doId
            self.makeSphere()

    def announceGenerate(self):
        DistributedPublicPet.notify.info("Waiting on announceGenerate for %d" % self.doId)

    def disable(self):
        base.localAvatar.publicPetId = 0
        self.ignoreAll()
        DistributedPet.DistributedPet.disable(self)

