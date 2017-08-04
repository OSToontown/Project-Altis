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

    def beginPublicDisplay(self):
        DistributedPublicPet.notify.info("Received begin for public display")
        DistributedPet.DistributedPet.announceGenerate(self) # Hack to fix pet DNA
        base.localAvatar.publicPetId = self.doId
        self.ready = True

        d = Func(self.pose, 'reappear', 0)
        e = self.getTeleportInTrack()
        g = Func(self.loop, 'neutral')
        Sequence(d, e, g).start()

    def announceGenerate(self):
        DistributedPublicPet.notify.info("Waiting on announceGenerate for %d" % self.doId)

    def disable(self):
        base.localAvatar.publicPetId = 0
        DistributedPet.DistributedPet.disable(self)

