from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistCogdoCraneCogAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistCogdoCraneCogAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.gameId = 0
        self.dnaString = ''
        self.spawnInfo = [0, 0]

    def setGameId(self, gameId):
        self.gameId = gameId

    def getGameId(self):
        return self.gameId

    def setDNAString(self, dnaString):
        self.dnaString = dnaString

    def getDNAString(self):
        return self.dnaString

    def setSpawnInfo(self, entranceId, timestamp):
        self.spawnInfo = [entranceId, timestamp]

    def getSpawnInfo(self):
        return self.spawnInfo