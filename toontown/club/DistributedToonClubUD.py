from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClubUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubUD')
    
    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

        self.ownerDoId = 0
        self.members = []
        self.status = False

    def requestStatus(self):
        avId = self.air.getAvatarIdFromSender()

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

    def getMemebers(self):
        return self.members

    def addMember(self, avId):
        pass

    def removeMember(self, avId):
        pass