from toontown.coghq.SellbotCogHQLoader import SellbotCogHQLoader
from toontown.toonbase import ToontownGlobals
from toontown.hood.CogHood import CogHood

class BoardbotHQ(CogHood):
    notify = directNotify.newCategory('BoardbotHQ')

    ID = ToontownGlobals.BoardbotHQ
    LOADER_CLASS = BoardbotCogHQLoader

    def load(self):
        CogHood.load(self)

    def enter(self, requestStatus):
        CogHood.enter(self, requestStatus)

        base.localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CogHQCameraNear, ToontownGlobals.CogHQCameraFar)
