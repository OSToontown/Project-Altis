from direct.directnotify import DirectNotifyGlobal
from otp.level.DistributedLevelAI import DistributedLevelAI
from toontown.cogdominium.DistCogdoGameAI import DistCogdoGameAI

class DistCogdoLevelGameAI(DistributedLevelAI, DistCogdoGameAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistCogdoLevelGameAI")

    def __init__(self, air, zoneId, entranceId, avIds):
        DistributedLevelAI.__init__(self, air, zoneId, entranceId, avIds)
        DistCogdoGameAI.__init__(self, air)