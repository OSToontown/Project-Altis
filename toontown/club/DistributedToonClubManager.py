from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClub(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClub')
    
    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

    def requestStatus(self):
        self.sendUpdate('requestStatus', [])

    def requestStatusResponse(self, clubFound, clubDoId):
        pass