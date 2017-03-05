from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import BoardbotHQExterior
from toontown.coghq.boardbothq import BoardOfficeInterior
from toontown.coghq import CashbotHQBossBattle
aspectSF = 0.7227

class BoardbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('boardofficeInterior', self.enterBoardOfficeInterior, self.exitBoardOfficeInterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('boardofficeInterior')
        self.musicFile = 'phase_14/audio/bgm/BD_courtyard.mid'
        self.cogHQExteriorModelPath = 'phase_10/models/cogHQ/CashBotShippingStation'
        self.cogHQLobbyModelPath = 'phase_10/models/cogHQ/VaultLobby'
        self.geom = None
        return
        
    def load(self, zoneId):
        CogHQLoader.CogHQLoader.load(self, zoneId)
        Toon.loadCashbotHQAnims()

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
            ddLinkTunnel = self.geom.find('**/LinkTunnel1')
            ddLinkTunnel.setName('linktunnel_dl_9252_DNARoot')
            locator = self.geom.find('**/sign_origin')
            backgroundGeom = self.geom.find('**/EntranceFrameFront')
            backgroundGeom.node().setEffect(DecalEffect.make())
            signText = DirectGui.OnscreenText(text=TTLocalizer.DonaldsDreamland[-1], font=ToontownGlobals.getSuitFont(), scale=3, fg=(0.87, 0.87, 0.87, 1), mayChange=False, parent=backgroundGeom)
            signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
            signText.setDepthWrite(0)
            self.geom.flattenMedium()
        elif zoneId == ToontownGlobals.BoardbotLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit BoardbotLobby')
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            self.geom.flattenMedium()
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadCashbotHQAnims()

    def enterBoardOfficeInterior(self, requestStatus):
        self.placeClass = BoardOfficeInterior.BoardOfficeInterior
        self.boardofficeId = requestStatus['boardofficeId']
        self.enterPlace(requestStatus)

    def exitBoardOfficeInterior(self):
        self.exitPlace()
        self.placeClass = None
        del self.boardofficeId
        return

    def getExteriorPlaceClass(self):
        return BoardbotHQExterior.BoardbotHQExterior

    def getBossPlaceClass(self):
        return CashbotHQBossBattle.CashbotHQBossBattle