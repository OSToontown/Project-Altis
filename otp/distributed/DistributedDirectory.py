from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObject import DistributedObject

class DistributedDirectory(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDirectory")

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)