from toontown.coghq.BoardbotCogHQLoader import BoardbotCogHQLoader
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood.CogHood import CogHood
from toontown.hood import ZoneUtil

class BoardbotHQ(CogHood):
    notify = directNotify.newCategory('BoardbotHQ')

    ID = ToontownGlobals.BoardbotHQ
    LOADER_CLASS = BoardbotCogHQLoader
    SKY_FILE = 'phase_3.5/models/props/TT_sky'

    def enter(self, requestStatus):
        CogHood.enter(self, requestStatus)

    def spawnTitleText(self, zoneId, floorNum=None):
        CogHood.spawnTitleText(self, zoneId)
