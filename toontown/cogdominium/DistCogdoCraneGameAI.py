from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from toontown.cogdominium.DistCogdoLevelGameAI import DistCogdoLevelGameAI
from toontown.cogdominium.DistCogdoCraneAI import DistCogdoCraneAI
from toontown.cogdominium.CogdoCraneGameBase import CogdoCraneGameBase
from otp.level.LevelSpec import LevelSpec
from toontown.cogdominium.DistCogdoCraneCogAI import DistCogdoCraneCogAI
from toontown.suit.SuitDNA import SuitDNA

class DistCogdoCraneGameAI(DistCogdoLevelGameAI, CogdoCraneGameBase):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistCogdoCraneGameAI")

    def __init__(self, air, zoneId, entranceId, avIds):
        DistCogdoLevelGameAI.__init__(self, air, zoneId, entranceId, avIds)

        self.levelSpec = LevelSpec(self.getSpec())
        self.cranes = []

    def generate(self):
        DistCogdoLevelGameAI.generate(self)

    def announceGenerate(self):
        DistCogdoLevelGameAI.announceGenerate(self)

        self.finishEvent = self.uniqueName('CogdoCraneGameDone')
        self.gameOverEvent = self.uniqueName('CogdoCraneGameLose')

        for index in xrange(4):
            crane = DistCogdoCraneAI(self.air, self.doId)
            crane.setIndex(index)
            crane.generateWithRequired(self.zoneId)
            self.cranes.append(crane)

    def delete(self):
        DistCogdoLevelGameAI.delete(self)

        for crane in self.cranes:
            crane.requestDelete()