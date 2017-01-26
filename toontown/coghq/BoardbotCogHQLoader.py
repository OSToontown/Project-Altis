from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from toontown.coghq import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
from toontown.coghq import FactoryExterior
from toontown.coghq import FactoryInterior
from toontown.coghq import SellbotHQExterior
from toontown.coghq import SellbotHQBossBattle
from pandac.PandaModules import DecalEffect, NodePath

aspectSF = 0.7227

class BoardbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, ['quietZone', 'factoryInterior', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')

        self.fsm.addState(State.State('factoryInterior', self.enterFactoryInterior, self.exitFactoryInterior, ['quietZone', 'factoryExterior']))
        for stateName in ['quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryInterior')

        self.musicFile = 'phase_14/audio/bgm/BD_courtyard.ogg'
        self.cogHQExteriorModelPath = 'phase_9/models/cogHQ/SellbotHQExterior'
        self.cogHQLobbyModelPath = 'phase_9/models/cogHQ/SellbotHQLobby'
        self.factoryExteriorModelPath = 'phase_9/models/cogHQ/SellbotFactoryExterior'
        self.geom = None

    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadSellbotHQAnims()

    def unloadPlaceGeom(self):
        if self.geom:
            self.geom.removeNode()
            self.geom = None
        CogHQLoader.CogHQLoader.unloadPlaceGeom(self)

    def loadPlaceGeom(self, zoneId):
        self.notify.info('loadPlaceGeom: %s' % zoneId)
        zoneId = zoneId - zoneId % 100
        if zoneId == ToontownGlobals.BoardbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            dgLinkTunnel = self.geom.find('**/Tunnel1')
            dgLinkTunnel.setName('linktunnel_dg_5316_DNARoot')
            factoryLinkTunnel = self.geom.find('**/Tunnel2')
            factoryLinkTunnel.setName('linktunnel_sellhq_11200_DNARoot')
            cogSignModel = loader.loadModel('phase_4/models/props/sign_sellBotHeadHQ')
            cogSign = cogSignModel.find('**/sign_sellBotHeadHQ').copyTo(NodePath())
            cogSign.flattenStrong()
            cogSignModel.removeNode()
            cogSignSF = 23
            dgSign = cogSign.copyTo(dgLinkTunnel)
            dgSign.setPosHprScale(0.0, -291.5, 29, 180.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            dgSign.node().setEffect(DecalEffect.make())
            dgText = DirectGui.OnscreenText(text=TTLocalizer.DaisyGardens[-1], font=ToontownGlobals.getSuitFont(), pos=(0, -0.3), scale=TTLocalizer.SCHQLdgText, mayChange=False, parent=dgSign)
            dgText.setDepthWrite(0)
            dgText.flattenStrong()
            factorySign = cogSign.copyTo(factoryLinkTunnel)
            factorySign.setPosHprScale(148.625, -155, 27, -90.0, 0.0, 0.0, cogSignSF, cogSignSF, cogSignSF * aspectSF)
            factorySign.node().setEffect(DecalEffect.make())
            factoryTypeText = DirectGui.OnscreenText(text=TTLocalizer.Sellbot, font=ToontownGlobals.getSuitFont(), pos=TTLocalizer.SellbotFactoryPosPart1, scale=TTLocalizer.SellbotFactoryScalePart1, mayChange=False, parent=factorySign)
            factoryTypeText.setDepthWrite(0)
            factoryTypeText.flattenStrong()
            factoryText = DirectGui.OnscreenText(text=TTLocalizer.Factory, font=ToontownGlobals.getSuitFont(), pos=TTLocalizer.SellbotFactoryPosPart2, scale=TTLocalizer.SellbotFactoryScalePart2, mayChange=False, parent=factorySign)
            factoryText.setDepthWrite(0)
            factoryText.flattenStrong()
            doors = self.geom.find('**/doors')
            door0 = doors.find('**/door_0')
            door1 = doors.find('**/door_1')
            door2 = doors.find('**/door_2')
            door3 = doors.find('**/door_3')
            for door in [door0, door1, door2, door3]:
                doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
                door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
                door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
                doorTrigger = door.find('**/door_trigger*')
                doorTrigger.setY(doorTrigger.getY() - 1.5)
                doorFrame.node().setEffect(DecalEffect.make())
                doorFrame.flattenStrong()
                door.flattenMedium()
            cogSign.removeNode()
            self.geom.flattenMedium()
        elif zoneId == ToontownGlobals.SellbotLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit SellbotLobby')
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            front = self.geom.find('**/frontWall')
            front.node().setEffect(DecalEffect.make())
            door = self.geom.find('**/door_0')
            parent = door.getParent()
            door.wrtReparentTo(front)
            doorFrame = door.find('**/doorDoubleFlat/+GeomNode')
            door.find('**/doorFrameHoleLeft').wrtReparentTo(doorFrame)
            door.find('**/doorFrameHoleRight').wrtReparentTo(doorFrame)
            doorFrame.node().setEffect(DecalEffect.make())
            door.find('**/leftDoor').wrtReparentTo(parent)
            door.find('**/rightDoor').wrtReparentTo(parent)
            self.geom.flattenStrong()
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadSellbotHQAnims()

    def enterFactoryExterior(self, requestStatus):
        self.placeClass = FactoryExterior.FactoryExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None

    def enterFactoryInterior(self, requestStatus):
        self.placeClass = FactoryInterior.FactoryInterior
        self.enterPlace(requestStatus)

    def exitFactoryInterior(self):
        self.exitPlace()
        self.placeClass = None

    def getExteriorPlaceClass(self):
        return SellbotHQExterior.SellbotHQExterior

    def getBossPlaceClass(self):
        return SellbotHQBossBattle.SellbotHQBossBattle