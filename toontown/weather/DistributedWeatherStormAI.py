from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedWeatherStormAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedWeatherStormAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.stormType = 0
        self.duration = 0

    def start(self):
        self.sendUpdate('start', [])

    def stop(self):
        self.sendUpdate('stop', [])

    def setStormType(self, stormType):
        self.stormType = stormType

    def d_setStormType(self, stormType):
        self.sendUpdate('setStormType', [stormType])

    def b_setStormType(self, stormType):
        self.setStormType(stormType)
        self.d_setStormType(stormType)

    def getStormType(self):
        return self.stormType

    def setDuration(self, duration):
        self.duration = duration

    def d_setDuration(self, duration):
        self.sendUpdate('setDuration', [duration])

    def b_setDuration(self, duration):
        self.setDuration(duration)
        self.d_setDuration(duration)

    def getDuration(self):
        return self.duration