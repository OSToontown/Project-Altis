from direct.distributed import DistributedObjectAI
from otp.level import DistributedLevelAI
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.coghq.boardbothq import BoardOfficeLayout, DistributedBoardOfficeRoomAI
from toontown.coghq import BattleExperienceAggregatorAI

class DistributedBoardOfficeAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeAI')

    def __init__(self, air, boardofficeId, zoneId, floorNum, avIds):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.boardofficeId = boardofficeId
        self.zoneId = zoneId
        self.floorNum = floorNum
        self.avIds = avIds

    def generate(self):
        DistributedObjectAI.DistributedObjectAI.generate(self)
        self.notify.info('generate %s, id=%s, floor=%s' % (self.doId, self.boardofficeId, self.floorNum))
        self.layout = BoardOfficeLayout.BoardOfficeLayout(self.boardofficeId, self.floorNum)
        self.rooms = []
        self.battleExpAggreg = BattleExperienceAggregatorAI.BattleExperienceAggregatorAI()
        for i in xrange(self.layout.getNumRooms()):
            room = DistributedBoardOfficeRoomAI.DistributedBoardOfficeRoomAI(self.air, self.boardofficeId, self.doId, self.zoneId, self.layout.getRoomId(i), i * 2, self.avIds, self.battleExpAggreg)
            room.generateWithRequired(self.zoneId)
            self.rooms.append(room)

        roomDoIds = []
        for room in self.rooms:
            roomDoIds.append(room.doId)

        self.sendUpdate('setRoomDoIds', [roomDoIds])
        if __dev__:
            simbase.boardoffice = self
        description = '%s|%s|%s' % (self.boardofficeId, self.floorNum, self.avIds)
        for avId in self.avIds:
            self.air.writeServerEvent('boardofficeEntered', avId, description)

    def requestDelete(self):
        self.notify.info('requestDelete: %s' % self.doId)
        for room in self.rooms:
            room.requestDelete()

        DistributedObjectAI.DistributedObjectAI.requestDelete(self)

    def delete(self):
        self.notify.info('delete: %s' % self.doId)
        if __dev__:
            if hasattr(simbase, 'boardoffice') and simbase.boardoffice is self:
                del simbase.boardoffice
        del self.rooms
        del self.layout
        del self.battleExpAggreg
        DistributedObjectAI.DistributedObjectAI.delete(self)

    def getTaskZoneId(self):
        return self.boardofficeId

    def allToonsGone(self):
        self.notify.info('allToonsGone')
        self.requestDelete()

    def getZoneId(self):
        return self.zoneId

    def getBoardOfficeId(self):
        return self.boardofficeId

    def getFloorNum(self):
        return self.floorNum
