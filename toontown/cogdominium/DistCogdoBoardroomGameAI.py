from direct.directnotify import DirectNotifyGlobal
from toontown.cogdominium.DistCogdoLevelGameAI import DistCogdoLevelGameAI
from toontown.cogdominium.CogdoBoardroomGameBase import CogdoBoardroomGameBase
from otp.level.LevelSpec import LevelSpec
from toontown.cogdominium.DistributedCogdoBarrelAI import DistributedCogdoBarrelAI

class DistCogdoBoardroomGameAI(DistCogdoLevelGameAI, CogdoBoardroomGameBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistCogdoBoardroomGameAI")

    def __init__(self, air, zoneId, entranceId, avIds):
        DistCogdoLevelGameAI.__init__(self, air, zoneId, entranceId, avIds)

        self.levelSpec = LevelSpec(self.getSpec())

    def announceGenerate(self):
        DistCogdoLevelGameAI.announceGenerate(self)

        self.finishEvent = self.uniqueName('CogdoBoardroomGameDone')
        self.gameOverEvent = self.uniqueName('CogdoBoardroomGameLose')

    def delete(self):
        DistCogdoLevelGameAI.delete(self)