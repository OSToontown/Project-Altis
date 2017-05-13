from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from toontown.building.ElevatorConstants import *
from toontown.building.ElevatorUtils import *
from toontown.building import DistributedElevatorExt
from toontown.building import DistributedElevator
from toontown.toonbase import ToontownGlobals
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.gui import DirectGui
from toontown.hood import ZoneUtil
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TTDialog
from toontown.coghq import CogDisguiseGlobals

class DistributedBoardOfficeElevatorExt(DistributedElevatorExt.DistributedElevatorExt):

    def __init__(self, cr):
        DistributedElevatorExt.DistributedElevatorExt.__init__(self, cr)
        self.type = ELEVATOR_BOARD_OFFICE
        self.countdownTime = ElevatorData[self.type]['countdown']

    def generate(self):
        DistributedElevatorExt.DistributedElevatorExt.generate(self)

    def delete(self):
        self.elevatorModel.removeNode()
        del self.elevatorModel
        DistributedElevatorExt.DistributedElevatorExt.delete(self)

    def setBoardOfficeId(self, boardofficeId):
        self.boardofficeId = boardofficeId
        boardofficeId2originId = {ToontownGlobals.BoardOfficeIntA: 0,
         ToontownGlobals.BoardOfficeIntB: 1,
         ToontownGlobals.BoardOfficeIntC: 2}
        originId = boardofficeId2originId[self.boardofficeId]
        geom = self.cr.playGame.hood.loader.geom
        locator = geom.find('**/elevator_origin_%s' % originId)
        if locator:
            self.elevatorModel.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
        else:
            self.notify.error('No origin found for originId: %s' % originId)
        # locator = geom.find('**/elevator_signorigin_%s' % originId)
        # backgroundGeom = geom.find('**/ElevatorFrameFront_%d' % originId)
        # backgroundGeom.node().setEffect(DecalEffect.make())
        # signText = DirectGui.OnscreenText(text=TextEncoder.upper(TTLocalizer.GlobalStreetNames[boardofficeId][-1]), font=ToontownGlobals.getSuitFont(), scale=TTLocalizer.DMEEsignText, fg=(0.87, 0.87, 0.87, 1), mayChange=False, parent=backgroundGeom)
        # signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
        # signText.setDepthWrite(0)

    def setupElevator(self):
        self.elevatorModel = loader.loadModel('phase_11/models/lawbotHQ/LB_ElevatorScaled')
        self.elevatorModel.reparentTo(render)
        self.leftDoor = self.elevatorModel.find('**/left_door')
        self.rightDoor = self.elevatorModel.find('**/right_door')
        DistributedElevator.DistributedElevator.setupElevator(self)
        self.elevatorSphereNodePath.setY(-1.42)

    def getElevatorModel(self):
        return self.elevatorModel

    def setBldgDoId(self, bldgDoId):
        self.bldg = None
        self.setupElevator()
        return

    def getZoneId(self):
        return 0

    def __doorsClosed(self, zoneId):
        pass

    def setBoardOfficeInteriorZone(self, zoneId):
        if self.localToonOnBoard:
            hoodId = self.cr.playGame.hood.hoodId
            boardofficeId = self.boardofficeId
            if bboard.has('boardofficeIdOverride'):
                boardofficeId = bboard.get('boardofficeIdOverride')
            doneStatus = {'loader': 'cogHQLoader',
             'where': 'boardofficeInterior',
             'how': 'teleportIn',
             'zoneId': zoneId,
             'boardofficeId': self.boardofficeId,
             'hoodId': hoodId}
            self.cr.playGame.getPlace().elevator.signalDone(doneStatus)

    def setBoardOfficeInteriorZoneForce(self, zoneId):
        place = self.cr.playGame.getPlace()
        if place:
            place.fsm.request('elevator', [self, 1])
            hoodId = self.cr.playGame.hood.hoodId
            boardofficeId = self.boardofficeId
            if bboard.has('boardofficeIdOverride'):
                boardofficeId = bboard.get('boardofficeIdOverride')
            doneStatus = {'loader': 'cogHQLoader',
             'where': 'boardofficeInterior',
             'how': 'teleportIn',
             'zoneId': zoneId,
             'boardofficeId': self.boardofficeId,
             'hoodId': hoodId}
            if hasattr(place, 'elevator') and place.elevator:
                place.elevator.signalDone(doneStatus)
            else:
                self.notify.warning("setBoardOfficeInteriorZoneForce: Couldn't find playGame.getPlace().elevator, zoneId: %s" % zoneId)
        else:
            self.notify.warning("setBoardOfficeInteriorZoneForce: Couldn't find playGame.getPlace(), zoneId: %s" % zoneId)

    def rejectBoard(self, avId, reason = 0):
        DistributedElevatorExt.DistributedElevatorExt.rejectBoard(self, avId, reason)

    def __handleRejectAck(self):
        doneStatus = self.rejectDialog.doneStatus
        if doneStatus != 'ok':
            self.notify.error('Unrecognized doneStatus: ' + str(doneStatus))
        doneStatus = {'where': 'reject'}
        self.cr.playGame.getPlace().elevator.signalDone(doneStatus)
        self.rejectDialog.cleanup()
        del self.rejectDialog

    def getDestName(self):
        if self.boardofficeId == ToontownGlobals.BoardOfficeIntA:
            return "Board Office 1"
        elif self.boardofficeId == ToontownGlobals.BoardOfficeIntB:
            return "Board Office 2"
        elif self.boardofficeId == ToontownGlobals.BoardOfficeIntC:
            return "Board Office 3"
