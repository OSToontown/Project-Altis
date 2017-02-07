from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistCogdoCraneAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistCogdoCraneAI")

    def __init__(self, air, craneGameId):
        DistributedObjectAI.__init__(self, air)

        self.craneGameId = craneGameId
        self.index = 0

    def getCraneGameId(self):
        return self.craneGameId

    def setIndex(self, index):
        self.index = index

    def d_setIndex(self, index):
        self.sendUpdate('setIndex', [index])

    def b_setIndex(self, index):
        self.setIndex(index)
        self.d_setIndex(index)

    def getIndex(self):
        return self.index

    def d_setState(self, state, avId):
        self.sendUpdate('setState', [state, avId])

    def clearSmoothing(self, todo0):
        pass

    def d_setCablePos(self, todo0, todo1, todo2, todo3, todo4):
        pass