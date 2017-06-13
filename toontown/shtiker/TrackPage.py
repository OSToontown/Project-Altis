from pandac.PandaModules import *
from toontown.shtiker import ShtikerPage
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.quest import Quests
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.toonbase import TTLocalizer
from toontown.toon import Toon

class TrackPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.TrackPageTitle, text_scale=0.1, pos=(0, 0, 0.65))
        self.pointDesc = DirectLabel(parent=self, relief=None, text=TTLocalizer.TrackPageSubtitle, text_scale=0.075, pos=(0, 0, 0.55))
        self.pointLabel = DirectLabel(parent=self, relief=None, text=str(base.localAvatar.getTrainingPoints()), text_font=ToontownGlobals.getBuildingNametagFont(), text_fg=(0, 0.75, 0.75, 1), text_scale=0.1, pos=(0, 0, 0.45))
        self.trackRows = []
        self.trackNameLabels = []
        self.trackProgressLabels = []
        TrackYOffset = 0.35
        TrackYSpacing = -0.12
        self.buttonModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        self.rowModel = self.buttonModels.find('**/TrainingPointRow')
        for track in xrange(len(ToontownBattleGlobals.Tracks)):
            trackFrame = DirectFrame(parent=self, image=self.rowModel, scale=(1.05, 0.8, 1.1), pos=(0, 0.3, TrackYOffset + track * TrackYSpacing), image_color=(ToontownBattleGlobals.TrackColors[track][0],
             ToontownBattleGlobals.TrackColors[track][1],
             ToontownBattleGlobals.TrackColors[track][2],
             1), state=DGG.NORMAL, relief=None)
            self.trackRows.append(trackFrame)
            self.trackNameLabels.append(DirectLabel(text=TextEncoder.upper(ToontownBattleGlobals.Tracks[track]), parent=self.trackRows[track], pos=(-0.72 + -0.06825, -0.1, 0.01), scale=TTLocalizer.INtrackNameLabels, relief=None, text_fg=(0.2, 0.2, 0.2, 1), text_font=ToontownGlobals.getInterfaceFont(), text_align=TextNode.ALeft, textMayChange=0))
            points = base.localAvatar.getSpentTrainingPoints()
            points = points[track]
            if points < 2:
                text = '%s/2 POINTS TO UNLOCK' % points
            else:
                text = 'UNLOCKED'
            self.trackProgressLabels.append(DirectLabel(text=text, parent=self.trackRows[track], pos=(-0.72 + -0.06825, -0.1, -0.025), scale=TTLocalizer.INtrackNameLabels/2, relief=None, text_fg=(0.2, 0.2, 0.2, 1), text_font=ToontownGlobals.getInterfaceFont(), text_align=TextNode.ALeft, textMayChange=0))

    def unload(self):
        del self.title
        del self.pointDesc
        del self.pointLabel
        del self.trackRows
        del self.trackNameLabels
        del self.trackProgressLabels
        ShtikerPage.ShtikerPage.unload(self)

    def clearPage(self):
        pass

    def updatePage(self):
        pass

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.clearPage()
        ShtikerPage.ShtikerPage.exit(self)
