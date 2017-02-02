from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClubManager(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubManager')
    
    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

        self._callback = None

    def requestStatus(self, callback):
        self._callback = callback
        self.sendUpdate('requestStatus', [])

    def requestStatusResponse(self, clubFound, clubDoId):
        if not callable(self._callback):
            return

        self._callback(clubFound, clubDoId)