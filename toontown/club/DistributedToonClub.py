from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClub(DistributedObjectGlobal):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClub')
    
    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)

        self.ownerDoId = 0
        self.members = []
        self.status = False

    def requestStatus(self):
        self.sendUpdate('requestStatus', [])

    def setOwner(self, ownerDoId):
        self.ownerDoId = ownerDoId

    def getOwner(self):
        return self.ownerDoId

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setMembers(self, members):
        self.members = members

    def getMembers(self):
        return self.members

    def addMember(self, avId):
        self.sendUpdate('addMember', [avId])

    def removeMember(self, avId):
        self.sendUpdate('removeMember', [avId])