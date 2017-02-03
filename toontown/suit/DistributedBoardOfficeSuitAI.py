from toontown.suit import DistributedFactorySuitAI
from direct.directnotify import DirectNotifyGlobal

class DistributedBoardOfficeSuitAI(DistributedFactorySuitAI.DistributedFactorySuitAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeSuitAI')

    def isForeman(self):
        return 0

    def isSupervisor(self):
        return self.boss

    def isVirtual(self):
        return 0
