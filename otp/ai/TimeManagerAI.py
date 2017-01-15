import time
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.ClockDelta import globalClockDelta

class TimeManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("TimeManagerAI")

    def requestServerTime(self, context):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'serverTime', [context, 
            globalClockDelta.getRealNetworkTime(bits=32), int(time.time())])

    def setDisconnectReason(self, reason):
        self.air.writeServerEvent('disconnect-reason', self.air.getAvatarIdFromSender(), reason)

    def setExceptionInfo(self, exception):
        self.air.writeServerEvent('client-exception', self.air.getAvatarIdFromSender(), exception)

    def setSignature(self, todo0, todo1, todo2):
        pass

    def setFrameRate(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8, todo9, todo10, todo11, todo12, todo13, todo14, todo15, todo16, todo17):
        pass

    def setCpuInfo(self, todo0, todo1):
        pass

    def checkForGarbageLeaks(self, todo0):
        pass

    def setNumAIGarbageLeaks(self, todo0):
        pass

    def setClientGarbageLeak(self, todo0, todo1):
        pass

    def checkAvOnDistrict(self, todo0, todo1):
        pass