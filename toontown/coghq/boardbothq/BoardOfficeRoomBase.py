from toontown.toonbase import ToontownGlobals

class BoardOfficeRoomBase:

    def __init__(self):
        pass

    def setBoardOfficeId(self, boardofficeId):
        self.boardofficeId = boardofficeId
        self.cogTrack = ToontownGlobals.cogHQZoneId2dept(boardofficeId)

    def setRoomId(self, roomId):
        self.roomId = roomId

    def getCogTrack(self):
        return self.cogTrack

    if __dev__:

        def getEntityTypeReg(self):
            from toontown.coghq import FactoryEntityTypes
            from otp.level import EntityTypeRegistry
            typeReg = EntityTypeRegistry.EntityTypeRegistry(FactoryEntityTypes)
            return typeReg
