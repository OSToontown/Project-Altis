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
        self.buttons = []
        TrackYOffset = 0.35
        TrackYSpacing = -0.12
        ButtonXOffset = -0.28
        ButtonXSpacing = 0.26
        self.buttonModels = loader.loadModel('phase_3.5/models/gui/inventory_gui')
        self.upButton = self.buttonModels.find('**/InventoryButtonUp')
        self.downButton = self.buttonModels.find('**/InventoryButtonDown')
        self.rolloverButton = self.buttonModels.find('**/InventoryButtonRollover')
        self.flatButton = self.buttonModels.find('**/InventoryButtonFlat')
        self.rowModel = self.buttonModels.find('**/TrainingPointRow')
        for track in xrange(len(ToontownBattleGlobals.Tracks)):
            trackFrame = DirectFrame(parent=self, image=self.rowModel, scale=(1.05, 0.8, 1.1), pos=(0, 0.3, TrackYOffset + track * TrackYSpacing), image_color=(ToontownBattleGlobals.TrackColors[track][0],
             ToontownBattleGlobals.TrackColors[track][1],
             ToontownBattleGlobals.TrackColors[track][2],
             1), state=DGG.NORMAL, relief=None)
            self.trackRows.append(trackFrame)
            self.trackNameLabels.append(DirectLabel(text=TextEncoder.upper(ToontownBattleGlobals.Tracks[track]), parent=self.trackRows[track], pos=(-0.72 + -0.06825, -0.1, 0.01), scale=TTLocalizer.INtrackNameLabels, relief=None, text_fg=(0.2, 0.2, 0.2, 1), text_font=ToontownGlobals.getInterfaceFont(), text_align=TextNode.ALeft, textMayChange=0))
            self.trackProgressLabels.append(DirectLabel(text='', parent=self.trackRows[track], pos=(-0.72 + -0.06825, -0.1, -0.025), scale=TTLocalizer.INtrackNameLabels/2, relief=None, text_fg=(0.2, 0.2, 0.2, 1), text_font=ToontownGlobals.getInterfaceFont(), text_align=TextNode.ALeft, textMayChange=0))
            self.buttons.append([])
            for item in xrange(5):
                button = DirectButton(parent=self.trackRows[track], image=(self.upButton,
                 self.downButton,
                 self.rolloverButton,
                 self.flatButton), text='', text_scale=0.04, text_align=TextNode.ARight, geom_scale=0.7, geom_pos=(-0.01, -0.1, 0), text_fg=Vec4(1, 1, 1, 1), text_pos=(0.07, -0.04), textMayChange=1, relief=None, image_color=(0, 0.6, 1, 1), image_scale=(1.05, 1, 1), pos=(ButtonXOffset + item * ButtonXSpacing + -0.06825, -0.1, 0), command=self.upgradeMe, extraArgs=[track])
                self.buttons[track].append(button)
        self.updatePage()

    def unload(self):
        del self.title
        del self.pointDesc
        del self.pointLabel
        del self.trackRows
        del self.trackNameLabels
        del self.trackProgressLabels
        del self.buttons
        ShtikerPage.ShtikerPage.unload(self)

    def clearPage(self):
        pass

    def updatePage(self):
        self.updateButtons()
        for track in xrange(8):
            points = base.localAvatar.getSpentTrainingPoints()
            points = points[track]
            if points < 2:
                self.trackProgressLabels[track]['text'] = '%s/2 POINTS TO UNLOCK' % points
            else:
                self.trackProgressLabels[track]['text'] = 'UNLOCKED'
        self.pointLabel['text'] = str(base.localAvatar.getTrainingPoints())

    def enter(self):
        self.updatePage()
        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.clearPage()
        ShtikerPage.ShtikerPage.exit(self)
		
    def updateButtons(self):
        av = base.localAvatar
        pointArray = av.getSpentTrainingPoints()
        for buttonArray in self.buttons:
            for button in buttonArray:
                button['state'] = DGG.DISABLED
        for track in xrange(len(pointArray)):
            for button in self.buttons[track]:
                button['state'] = DGG.NORMAL
                button['text'] = '0/1'
            for iteration in xrange(pointArray[track]):
                self.buttons[track][iteration]['state'] = DGG.DISABLED
                self.buttons[track][iteration]['image_color'] = Vec4(0.4, 0.4, 0.4, 1)
                self.buttons[track][iteration]['text'] = '1/1'
            for i in xrange(3): # Temporary until we include prestiging
                self.buttons[track][i+2]['state'] = DGG.DISABLED
                self.buttons[track][i+2]['image_color'] = Vec4(0.4, 0.4, 0.4, 1)
                self.buttons[track][i+2]['text'] = '0/1'
            if av.getTrainingPoints() == 0:
                for button in self.buttons[track]:
                    button['state'] = DGG.DISABLED
				
    def upgradeMe(self, track):
        av = base.localAvatar
        av.sendUpdate('requestSkillSpend', [track])
        self.updatePage()
        
                
