from direct.directnotify import DirectNotifyGlobal
import DistributedBoardOfficeAI
from toontown.toonbase import ToontownGlobals
from toontown.coghq.boardbothq import BoardOfficeLayout
from direct.showbase import DirectObject
import random

class BoardOfficeManagerAI(DirectObject.DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardOfficeManagerAI')
    boardofficeId = None

    def __init__(self, air):
        DirectObject.DirectObject.__init__(self)
        self.air = air

    def getDoId(self):
        return 0

    def createBoardOffice(self, boardofficeId, players):
        for avId in players:
            if bboard.has('boardofficeId-%s' % avId):
                boardofficeId = bboard.get('boardofficeId-%s' % avId)
                break

        numFloors = ToontownGlobals.BoardOfficeNumFloors[boardofficeId]
        floor = random.randrange(numFloors)
        for avId in players:
            if bboard.has('mintFloor-%s' % avId):
                floor = bboard.get('mintFloor-%s' % avId)
                floor = max(0, floor)
                floor = min(floor, numFloors - 1)
                break

        for avId in players:
            if bboard.has('mintRoom-%s' % avId):
                roomId = bboard.get('mintRoom-%s' % avId)
                for i in xrange(numFloors):
                    layout = BoardOfficeLayout.BoardOfficeLayout(boardofficeId, i)
                    if roomId in layout.getRoomIds():
                        floor = i
                else:
                    from toontown.coghq.boardbothq import BoardOfficeRoomSpecs
                    roomName = BoardOfficeRoomSpecs.BoardOfficeRoomId2RoomName[roomId]
                    BoardOfficeManagerAI.notify.warning('room %s (%s) not found in any floor of mint %s' % (roomId, roomName, boardofficeId))

        mintZone = self.air.allocateZone()
        mint = DistributedBoardOfficeAI.DistributedBoardOfficeAI(self.air, boardofficeId, mintZone, floor, players)
        mint.generateWithRequired(mintZone)
        return mintZone
