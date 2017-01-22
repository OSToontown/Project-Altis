from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedLightSwitchAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedLightSwitchAI')

    def __init__(self, air, interiorDoId):
        DistributedObjectAI.__init__(self, air)

        self.interiorDoId = interiorDoId
        self.lightState = True

    def delete(self):
        self.interiorDoId = 0
        self.lightState = False

        DistributedObjectAI.delete(self)

    def getInteriorDoId(self):
        return self.interiorDoId

    def toggleLight(self):
        if self.lightState:
            self.lightState = False
        else:
            self.lightState = True

        self.d_setLightState(self.lightState)

    def d_setLightState(self, lightState):
        self.sendUpdate('setLightState', [lightState])