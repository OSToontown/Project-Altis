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
        self.cSphere = None

    def makeSphere(self):
        # Tubby said I couldn't make CollisionSpheres on the AI so it's on the client now
        self.cSphere = CollisionSphere(0.0, 0.0, 0.0, 5.0)
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

    def isOwner(self):
        return self.getOwnerId() == base.localAvatar.doId

    def beginPublicDisplay(self):
        DistributedPublicPet.notify.info("Received begin for public display for public pet %d" % self.doId)
        d = Func(self.pose, 'reappear', 0)
        e = self.getTeleportInTrack()
        g = Func(self.loop, 'neutral')
        Sequence(d, e, g).start()


    def finishPublicDisplay(self):
        DistributedPublicPet.notify.info("Finishing public display for public pet %d" % self.doId)
        Sequence(self.getTeleportOutTrack()).start()


    def announceGenerate(self):
        DistributedPet.DistributedPet.announceGenerate(self) # Hack to fix pet DNA
        self.ready = True
        if self.isOwner():
            base.localAvatar.publicPetId = self.doId
            self.makeSphere()

    def disable(self):
        if self.isOwner():
            base.localAvatar.publicPetId = 0

        self.ignoreAll()
        if self.cSphere: # Possibility that the cSphere doesn't exist because the doodle wasn't fully generated
            del self.cSphere
            del self.cSphereNode
            del self.cSphereNodePath
        DistributedPet.DistributedPet.disable(self)

