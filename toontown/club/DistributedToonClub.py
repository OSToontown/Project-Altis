from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClub(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClub')
    
    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

        self.ownerDoId = 0
        self.status = False # is publically joinable or not
        self.members = []
        self.inviteCode = ''

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

    def setInviteCode(self, inviteCode):
        self.inviteCode = inviteCode

    def getInviteCode(self):
        return self.inviteCode

    def addMember(self, avId):
        self.sendUpdate('addMember', [avId])

    def removeMember(self, avId):
        self.sendUpdate('removeMember', [avId])