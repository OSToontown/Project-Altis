from direct.directnotify import DirectNotifyGlobal
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
import random
from toontown.coghq import FactoryEntityCreator
from toontown.coghq.boardbothq import BoardOfficeRoomBase, BoardOfficeRoom
from toontown.coghq.boardbothq import BoardOfficeRoomSpecs
from otp.level import DistributedLevel
from otp.level import LevelSpec, LevelConstants
from toontown.nametag.NametagGlobals import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase.ToontownGlobals import *
from toontown.chat.ChatGlobals import CFThought, CFTimeout

if __dev__:
    from otp.level import EditorGlobals

def getBoardOfficeRoomReadyPostName(doId):
    return 'boardofficeRoomReady-%s' % doId

class DistributedBoardOfficeRoom(DistributedLevel.DistributedLevel, BoardOfficeRoomBase.BoardOfficeRoomBase, BoardOfficeRoom.BoardOfficeRoom):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeRoom')
    EmulateEntrancePoint = False

    def __init__(self, cr):
        DistributedLevel.DistributedLevel.__init__(self, cr)
        BoardOfficeRoomBase.BoardOfficeRoomBase.__init__(self)
        BoardOfficeRoom.BoardOfficeRoom.__init__(self)
        self.suitIds = []
        self.suits = []
        self.reserveSuits = []
        self.joiningReserves = []
        self.suitsInitialized = 0
        self.goonClipPlanes = {}
        self.boardoffice = None

    def createEntityCreator(self):
        return FactoryEntityCreator.FactoryEntityCreator(level=self)

    def generate(self):
        self.notify.debug('generate')
        DistributedLevel.DistributedLevel.generate(self)

    def delete(self):
        del self.boardoffice
        DistributedLevel.DistributedLevel.delete(self)
        BoardOfficeRoom.BoardOfficeRoom.delete(self)
        self.ignoreAll()

    def setBoardOfficeId(self, boardofficeId):
        self.notify.debug('boardofficeId: %s' % boardofficeId)
        BoardOfficeRoomBase.BoardOfficeRoomBase.setBoardOfficeId(self, boardofficeId)

    def setRoomId(self, roomId):
        self.notify.debug('roomId: %s' % roomId)
        BoardOfficeRoomBase.BoardOfficeRoomBase.setRoomId(self, roomId)

    def setRoomNum(self, num):
        self.notify.debug('roomNum: %s' % num)
        BoardOfficeRoom.BoardOfficeRoom.setRoomNum(self, num)

    def levelAnnounceGenerate(self):
        self.notify.debug('levelAnnounceGenerate')
        DistributedLevel.DistributedLevel.levelAnnounceGenerate(self)
        specModule = BoardOfficeRoomSpecs.getBoardOfficeRoomSpecModule(self.roomId)
        roomSpec = LevelSpec.LevelSpec(specModule)
        if __dev__:
            typeReg = self.getEntityTypeReg()
            roomSpec.setEntityTypeReg(typeReg)
        DistributedLevel.DistributedLevel.initializeLevel(self, roomSpec)

    def getReadyPostName(self):
        return getBoardOfficeRoomReadyPostName(self.doId)

    def privGotSpec(self, levelSpec):
        if __dev__:
            if not levelSpec.hasEntityTypeReg():
                typeReg = self.getEntityTypeReg()
                levelSpec.setEntityTypeReg(typeReg)
        DistributedLevel.DistributedLevel.privGotSpec(self, levelSpec)
        BoardOfficeRoom.BoardOfficeRoom.enter(self)
        self.acceptOnce('leavingBoardOffice', self.announceLeaving)
        bboard.post(self.getReadyPostName())

    def fixupLevelModel(self):
        BoardOfficeRoom.BoardOfficeRoom.setGeom(self, self.geom)
        BoardOfficeRoom.BoardOfficeRoom.initFloorCollisions(self)

    def setBoardOffice(self, boardoffice):
        self.boardoffice = boardoffice

    def setBossConfronted(self, avId):
        self.boardoffice.setBossConfronted(avId)

    def setDefeated(self):
        self.notify.info('setDefeated')
        from toontown.coghq.boardbothq import DistributedBoardOffice
        messenger.send(DistributedBoardOffice.DistributedBoardOffice.WinEvent)

    def initVisibility(self, *args, **kw):
        pass

    def shutdownVisibility(self, *args, **kw):
        pass

    def lockVisibility(self, *args, **kw):
        pass

    def unlockVisibility(self, *args, **kw):
        pass

    def enterZone(self, *args, **kw):
        pass

    def updateVisibility(self, *args, **kw):
        pass

    def setVisibility(self, *args, **kw):
        pass

    def resetVisibility(self, *args, **kw):
        pass

    def handleVisChange(self, *args, **kw):
        pass

    def forceSetZoneThisFrame(self, *args, **kw):
        pass

    def getParentTokenForEntity(self, entId):
        if __dev__:
            pass
        return 1000000 * self.roomNum + entId

    def enterLtNotPresent(self):
        BoardOfficeRoom.BoardOfficeRoom.enterLtNotPresent(self)
        if __dev__:
            bboard.removeIfEqual(EditorGlobals.EditTargetPostName, self)
        self.ignore('f2')

    def enterLtPresent(self):
        BoardOfficeRoom.BoardOfficeRoom.enterLtPresent(self)
        if __dev__:
            bboard.post(EditorGlobals.EditTargetPostName, self)
        if self.boardoffice is not None:
            self.boardoffice.currentRoomName = BoardOfficeRoomSpecs.BoardOfficeRoomId2RoomName[self.roomId]

        def printPos(self = self):
            thisZone = self.getZoneNode(LevelConstants.UberZoneEntId)
            pos = base.localAvatar.getPos(thisZone)
            h = base.localAvatar.getH(thisZone)
            roomName = BoardOfficeRoomSpecs.BoardOfficeRoomId2RoomName[self.roomId]
            print 'boardoffice pos: %s, h: %s, room: %s' % (repr(pos), h, roomName)
            if self.boardoffice is not None:
                floorNum = self.boardoffice.floorNum
            else:
                floorNum = '???'
            posStr = 'X: %.3f' % pos[0] + '\nY: %.3f' % pos[1] + '\nZ: %.3f' % pos[2] + '\nH: %.3f' % h + '\nboardofficeId: %s' % self.boardofficeId + '\nfloor: %s' % floorNum + '\nroomId: %s' % self.roomId + '\nroomName: %s' % roomName
            base.localAvatar.setChatAbsolute(posStr, CFThought | CFTimeout)
            return

        self.accept('f2', printPos)
        return

    def handleSOSPanel(self, panel):
        avIds = []
        for avId in self.avIdList:
            if base.cr.doId2do.get(avId):
                avIds.append(avId)

        panel.setFactoryToonIdList(avIds)

    def disable(self):
        self.notify.debug('disable')
        BoardOfficeRoom.BoardOfficeRoom.exit(self)
        if hasattr(self, 'suits'):
            del self.suits
        if hasattr(self, 'relatedObjectMgrRequest') and self.relatedObjectMgrRequest:
            self.cr.relatedObjectMgr.abortRequest(self.relatedObjectMgrRequest)
            del self.relatedObjectMgrRequest
        bboard.remove(self.getReadyPostName())
        DistributedLevel.DistributedLevel.disable(self)

    def setSuits(self, suitIds, reserveSuitIds):
        oldSuitIds = list(self.suitIds)
        self.suitIds = suitIds
        self.reserveSuitIds = reserveSuitIds

    def reservesJoining(self):
        pass

    def getCogSpec(self, cogId):
        cogSpecModule = BoardOfficeRoomSpecs.getCogSpecModule(self.roomId)
        return cogSpecModule.CogData[cogId]

    def getReserveCogSpec(self, cogId):
        cogSpecModule = BoardOfficeRoomSpecs.getCogSpecModule(self.roomId)
        return cogSpecModule.ReserveCogData[cogId]

    def getBattleCellSpec(self, battleCellId):
        cogSpecModule = BoardOfficeRoomSpecs.getCogSpecModule(self.roomId)
        return cogSpecModule.BattleCells[battleCellId]

    def getFloorOuchLevel(self):
        return 8

    def getTaskZoneId(self):
        return self.boardofficeId

    def getBossTaunt(self):
        return TTLocalizer.BoardOfficeBossTaunt

    def getBossBattleTaunt(self):
        return TTLocalizer.BoardOfficeBossBattleTaunt

    def __str__(self):
        if hasattr(self, 'roomId'):
            return '%s %s: %s' % (self.__class__.__name__, self.roomId, BoardOfficeRoomSpecs.BoardOfficeRoomId2RoomName[self.roomId])
        else:
            return 'DistributedBoardOfficeRoom'

    def __repr__(self):
        return str(self)

    def reportModelSpecSyncError(self, msg): #we need this cause the unit spec and model Num do match to see what i mean un hash next line
        self.notify.info('%s\n\nyour spec does not match the level model\nuse SpecUtil.updateSpec, then restart your AI and client' % msg)
        pass