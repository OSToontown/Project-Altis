from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClub(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClub')
    
    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

        self.members = []

    def d_requestStats(self):
        self.sendUpdate('requestStats', [])

    def addMember(self, avId):
        self.sendUpdate('addMember', [avId])

    def removeMember(self, avId):
        self.sendUpdate('removeMember', [avId])

    def setMembers(self, members):
        self.members = members

    def getMemebers(self):
        return self.members