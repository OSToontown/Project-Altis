from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal

class DistributedToonClubUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubUD')
    
    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

        self.members = []

    def requestStats(self):
        pass

    def addMember(self, avId):
        pass

    def removeMember(self, avId):
        pass

    def setMembers(self, members):
        self.members = members

    def getMemebers(self):
        return self.members