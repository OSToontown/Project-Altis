from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.parties import SimpleMailBase

class DistributedMailManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMailManagerAI")
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def sendSimpleMail(self, avId, msgId, contents):
        pass

    def setNumMailItems(self, todo0, todo1):
        pass

