from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClubAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubAI')
    
    def __init__(self, air, clubManager):
        DistributedObjectAI.__init__(self, air)

        self.clubManager = clubManager
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
        pass

    def removeMember(self, avId):
        pass