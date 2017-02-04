import gc
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class CentralLoggerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("CentralLoggerAI")

    def logAIGarbage(self):
        if hasattr(gc, 'garbage'):
            self.notify.warning("AI Garbage Found: %s" % (str(gc.garbage)))

