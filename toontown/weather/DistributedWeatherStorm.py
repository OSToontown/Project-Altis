from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal

class DistributedWeatherStorm(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedWeatherStorm')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

        self.stormType = 0
        self.duration = 0

    def announceGenerate(self):
        DistributedObject.announceGenerate(self)

    def start(self):
        pass

    def stop(self):
        pass

    def setStormType(self, stormType):
        self.stormType = stormType

    def getStormType(self):
        return self.stormType

    def setDuration(self, duration):
        self.duration = duration

    def getDuration(self):
        return self.duration