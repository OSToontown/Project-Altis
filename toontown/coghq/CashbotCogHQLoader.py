from direct.directnotify import DirectNotifyGlobal
from direct.fsm import StateData
from toontown.coghq import CogHQLoader, MintInterior
from toontown.toonbase import ToontownGlobals
from direct.gui import DirectGui
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon
from direct.fsm import State
from toontown.coghq import CashbotHQExterior
from toontown.coghq import CashbotHQBossBattle
from pandac.PandaModules import DecalEffect

class CashbotCogHQLoader(CogHQLoader.CogHQLoader):
    notify = DirectNotifyGlobal.directNotify.newCategory('CashbotCogHQLoader')

    def __init__(self, hood, parentFSMState, doneEvent):
        CogHQLoader.CogHQLoader.__init__(self, hood, parentFSMState, doneEvent)
        self.fsm.addState(State.State('mintInterior', self.enterMintInterior, self.exitMintInterior, ['quietZone', 'cogHQExterior']))
        for stateName in ['start', 'cogHQExterior', 'quietZone']:
            state = self.fsm.getStateNamed(stateName)
            state.addTransition('mintInterior')

        self.musicFile = 'phase_10/audio/bgm/CB_courtyard.ogg'
        self.cogHQExteriorModelPath = 'phase_10/models/cogHQ/CashBotShippingStation'
        self.cogHQLobbyModelPath = 'phase_10/models/cogHQ/VaultLobby'
        self.zoneVisDict = []
        self.geom = None

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
        if zoneId == ToontownGlobals.CashbotHQ:
            self.geom = loader.loadModel(self.cogHQExteriorModelPath)
            ddLinkTunnel = self.geom.find('**/LinkTunnel1')
            ddLinkTunnel.setName('linktunnel_mm_4410_DNARoot')
            locator = self.geom.find('**/sign_origin')
            backgroundGeom = self.geom.find('**/EntranceFrameFront')
            backgroundGeom.node().setEffect(DecalEffect.make())
            signText = DirectGui.OnscreenText(text=TTLocalizer.MinniesMelodyland[-1], font=ToontownGlobals.getSuitFont(), scale=3, fg=(0.87, 0.87, 0.87, 1), mayChange=False, parent=backgroundGeom)
            signText.setPosHpr(locator, 0, 0, 0, 0, 0, 0)
            signText.setDepthWrite(0)
            self.geom.flattenMedium()
        elif zoneId == ToontownGlobals.CashbotLobby:
            if base.config.GetBool('want-qa-regression', 0):
                self.notify.info('QA-REGRESSION: COGHQ: Visit CashbotLobby')
            self.geom = loader.loadModel(self.cogHQLobbyModelPath)
            self.geom.flattenMedium()
        else:
            self.notify.warning('loadPlaceGeom: unclassified zone %s' % zoneId)
        CogHQLoader.CogHQLoader.loadPlaceGeom(self, zoneId)

    def unload(self):
        CogHQLoader.CogHQLoader.unload(self)
        Toon.unloadCashbotHQAnims()

    def enterMintInterior(self, requestStatus):
        self.placeClass = MintInterior.MintInterior
        self.mintId = requestStatus['mintId']
        self.enterPlace(requestStatus)

    def exitMintInterior(self):
        self.exitPlace()
        self.placeClass = None
        del self.mintId
        return

    def getExteriorPlaceClass(self):
        return CashbotHQExterior.CashbotHQExterior

    def getBossPlaceClass(self):
        return CashbotHQBossBattle.CashbotHQBossBattle
		
    def enterCogHQBossBattle(self, requestStatus):
        self.notify.debug('CashbotCogHQLoader.enterCogHQBossBattle')
        CogHQLoader.CogHQLoader.enterCogHQBossBattle(self, requestStatus)
        base.cr.forbidCheesyEffects(1)

    def exitCogHQBossBattle(self):
        self.notify.debug('CashbotCogHQLoader.exitCogHQBossBattle')
        CogHQLoader.CogHQLoader.exitCogHQBossBattle(self)
        base.cr.forbidCheesyEffects(0)
