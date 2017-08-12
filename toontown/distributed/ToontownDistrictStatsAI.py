from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class ToontownDistrictStatsAI(DistributedObjectAI):
    notify = directNotify.newCategory('ToontownDistrictStatsAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.districtId = 0
        self.avatarCount = 0
        self.newAvatarCount = 0
        self.invasionStatus = 0
        self.invasionType = 0
        self.invasionRemaining = 0
        self.invasionTotal = 0

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        # We want to handle shard status queries so that a ShardStatusReceiver
        # being created after we're generated will know where we're at:
        self.air.netMessenger.accept('queryShardStatus', self, self.handleShardStatusQuery)

    def handleShardStatusQuery(self):
        # Send a shard status update containing our population:
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, {'population': \
            self.avatarCount}])

    def settoontownDistrictId(self, districtId):
        self.districtId = districtId

    def d_settoontownDistrictId(self, districtId):
        self.sendUpdate('settoontownDistrictId', [districtId])

    def b_settoontownDistrictId(self, districtId):
        self.settoontownDistrictId(districtId)
        self.d_settoontownDistrictId(districtId)

    def gettoontownDistrictId(self):
        return self.districtId

    def setAvatarCount(self, avatarCount):
        self.avatarCount = avatarCount

        # Send a shard status update containing our population:
        self.air.netMessenger.send('shardStatus', [self.air.ourChannel, {'population': \
            self.avatarCount}])

    def d_setAvatarCount(self, avatarCount):
        self.sendUpdate('setAvatarCount', [avatarCount])

    def b_setAvatarCount(self, avatarCount):
        self.d_setAvatarCount(avatarCount)
        self.setAvatarCount(avatarCount)

    def getAvatarCount(self):
        return self.avatarCount

    def setNewAvatarCount(self, newAvatarCount):
        self.newAvatarCount = newAvatarCount

    def d_setNewAvatarCount(self, newAvatarCount):
        self.sendUpdate('setNewAvatarCount', [newAvatarCount])

    def b_setNewAvatarCount(self, newAvatarCount):
        self.setNewAvatarCount(newAvatarCount)
        self.d_setNewAvatarCount(newAvatarCount)

    def getNewAvatarCount(self):
        return self.newAvatarCount

    def setInvasionStatus(self, invasionStatus):
        self.invasionStatus = invasionStatus

    def d_setInvasionStatus(self, invasionStatus):
        self.sendUpdate('setInvasionStatus', [invasionStatus])

    def b_setInvasionStatus(self, invasionStatus):
        self.setInvasionStatus(invasionStatus)
        self.d_setInvasionStatus(invasionStatus)

    def setInvasionType(self, invasionType):
        self.invasionType = invasionType

    def getInvasionStatus(self):
        return self.invasionStatus

    def getInvasionType(self):
        return self.invasionType

    def setInvasionCount(self, total, remaining):
        self.invasionRemaining = remaining
        self.invasionTotal = total

    def getInvasionRemaining(self):
        return self.air.suitInvasionManager.remaining

    def getInvasionTotal(self):
        return self.air.suitInvasionManager.total

    def getInvasionTimeRemaining(self):
        tasks = taskMgr.getTasksNamed('invasionTimeout')
        if len(tasks) == 0:
            return 0
        return abs(tasks[0].time)
