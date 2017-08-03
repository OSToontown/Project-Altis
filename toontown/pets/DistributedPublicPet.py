from toontown.pets import DistributedPet, Pet, PetBase, PetManager
from direct.directnotify import DirectNotifyGlobal
from toontown.distributed.DelayDeletable import DelayDeletable
from otp.otpbase import OTPGlobals
from panda3d.core import *
from panda3d.direct import *

class DistributedPublicPet(DistributedPet.DistributedPet):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPet')

    def __init__(self, cr):
        DistributedPet.DistributedPet.__init__(self, cr)
        self.proxyDo = 0
        self.proxy = None

    def beginPublicDisplay(self):
        DistributedPublicPet.notify.info("Received begin for public display")

    def announceGenerate(self):
        DistributedPublicPet.notify.info("Generated %d" % self.doId)
        DistributedPet.DistributedPet.announceGenerate(self)

