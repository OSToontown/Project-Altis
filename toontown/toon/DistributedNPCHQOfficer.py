from direct.interval.IntervalGlobal import *
from pandac.PandaModules import *
from toontown.toon import DistributedNPCToon
from toontown.chat.ChatGlobals import *
from toontown.hood import ZoneUtil
from toontown.nametag.NametagGlobals import *
from toontown.quest import QuestChoiceGui
from toontown.quest import QuestParser
from toontown.quest import TrackChoiceGui
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import TeaserPanel

ChoiceTimeout = 20

class DistributedNPCHQOfficer(DistributedNPCToon.DistributedNPCToon):
    
    def __init__(self, cr):
        DistributedNPCToon.DistributedNPCToon.__init__(self, cr)

        self.npcType = 'HQ Officer'
        
    def announceGenerate(self):
        DistributedNPCToon.DistributedNPCToon.announceGenerate(self)
        if base.cr.playGame.hood.hoodId == 1000:
            if self.posIndex in [0, 3]:
                self.setHat(16, 0, 0)
            else:
                self.setHat(48, 0, 0)
            self.setGlasses(20, 0, 0)
        elif base.cr.playGame.hood.hoodId == 2000:
            self.setHat(41, 0, 0)
        elif base.cr.playGame.hood.hoodId == 4000:
            self.setHat(29, 0, 0)
            if self.posIndex == 3:
                self.setBackpack(22, 0, 0)
