from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClubAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubAI')
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

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