from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
import CogHQLoader
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
import BoardbotHQExterior
import BoardbotOfficeExterior
from toontown.coghq.boardbothq import BoardOfficeInterior
from toontown.coghq import CashbotHQBossBattle

aspectSF = 0.7227

class BoardbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('BoardbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('boardofficeInterior', self.enterBoardOfficeInterior, self.exitBoardOfficeInterior, ['quietZone', 'cogHQExterior']))
        self.fsm.addState(State.State('factoryExterior', self.enterFactoryExterior, self.exitFactoryExterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('boardofficeInterior')
			
        for stateName in ['quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('factoryExterior')

        self.musicFile = 'phase_14/audio/bgm/BD_courtyard.ogg'
        self.cogHQExteriorModelPath = 'phase_14/models/boardbotHQ/boardbot_courtyard'
        self.factoryExteriorModelPath = 'phase_14/models/boardbotHQ/boardbot_factory_exterior'
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
            #ddLinkTunnel = self.geom.find('**/tunnel1')
            #ddLinkTunnel.setName('linktunnel_dl_9252_DNARoot')
            locator = self.geom.find('**/sign_origin')
            signText = DirectGui.OnscreenText(text=TTLocalizer.DonaldsDreamland[-1], font=ToontownGlobals.getSuitFont(), scale=3, fg=(0.87, 0.87, 0.87, 1), mayChange=False, parent=self.geom)
            signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
            signText.setDepthWrite(0)
            self.geom.flattenMedium()
        elif zoneId == ToontownGlobals.BoardbotOfficeLobby:
            self.geom = loader.loadModel(self.factoryExteriorModelPath)
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
		
    def enterFactoryExterior(self, requestStatus):
        self.placeClass = BoardbotOfficeExterior.BoardbotOfficeExterior
        self.enterPlace(requestStatus)
        self.hood.spawnTitleText(requestStatus['zoneId'])

    def exitFactoryExterior(self):
        taskMgr.remove('titleText')
        self.hood.hideTitleText()
        self.exitPlace()
        self.placeClass = None