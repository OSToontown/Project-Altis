from direct.directnotify.DirectNotifyGlobal import *
from direct.distributed import DistributedObjectAI

class SafeZoneManagerAI(DistributedObjectAI.DistributedObjectAI):
    notify = directNotify.newCategory('SafeZoneManagerAI')

    def __init__(self, air):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.healFrequency = 20.0  # The time in seconds between each Toon-up pulse.

    def enterSafeZone(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        av.startToonUp(self.healFrequency)

    def exitSafeZone(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return
        av.stopToonUp()
