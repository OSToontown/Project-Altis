from panda3d.core import Vec4
from direct.gui.DirectGui import DirectFrame, DirectLabel, DirectWaitBar, DGG, DirectLabel
from direct.gui.OnscreenText import OnscreenText
from direct.interval.LerpInterval import *
from toontown.toonbase import ToontownIntervals
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownIntervals
from toontown.quest import Quests
import ToonExperience

class ExperienceBar(DirectFrame):

    def __init__(self, exp, level, avdna):
        DirectFrame.__init__(self, relief=None, sortOrder=50)
        self.av = None
        self.style = avdna
        if self.style.type == 't':
            self.isToon = 1
        else:
            self.isToon = 0
        self.exp = exp
        self.level = level
        self.maxExp = ToonExperience.ToonExperience().getLevelMaxExp(self.level)
        self.expBar = None
        self.__obscured = 0
        self.levelUpSfx = loader.loadSfx('phase_3.5/audio/sfx/AV_levelup.ogg')
        self.load()
        return

    def load(self):
        if self.isToon:
            self.barGeom = loader.loadModel('phase_3.5/models/gui/exp_bar')
            if self.level == ToontownGlobals.MaxToonLevel:
                pass
            else:
                self.color = self.style.getHeadColor()
                self.bgBar = DirectFrame(relief=None, geom=self.barGeom, pos=(0.0, 0, -.95), geom_scale=(0.3,0.25,0.1), geom_color=self.color)
                self.expBar = DirectWaitBar(parent=self.bgBar, guiId='expBar', pos=(0.0, 0, 0), relief=DGG.SUNKEN, frameSize=(-2.0, 2.0, -0.1, 0.1), borderWidth=(0.01, 0.01), scale=0.25, range=self.maxExp, sortOrder=50, frameColor=(0.5, 0.5, 0.5, 0.5), barColor=(0.0, 1.0, 0.0, 0.5), text=str(self.exp)+'/'+str(self.maxExp), text_scale=0.2, text_fg=(1, 1, 1, 1), text_align=TextNode.ACenter, text_pos=(0, -0.05))
                self.expBar['value'] = self.exp
                self.levelLabel = OnscreenText(text = TTLocalizer.ExpBarLevel + str(self.level+1), pos = (0.0, -0.9), scale = 0.05, font=ToontownGlobals.getBuildingNametagFont(), fg = (1, 1, 1, 1))
                self.levelLabel.hide()
            return

    def destroy(self):
        if self.av:
            self.ignore(self.av.uniqueName('toonExpChange'))
        del self.av
        del self.exp
        del self.maxExp
        if self.bgBar:
           self.bgBar.destroy()
           del self.bgBar
        if self.expBar:
           self.expBar.destroy()
        if self.levelLabel:
           self.levelLabel.destroy()
        DirectFrame.destroy(self)
		
    def updateBar(self, exp, level):
        if level >= ToontownGlobals.MaxToonLevel:
           self.hide()
           return
        currExp = self.exp
        self.exp = exp
        currMax = self.maxExp
        currLevel = self.level
        self.level = level
        self.maxExp = ToonExperience.ToonExperience().getLevelMaxExp(self.level)
        name = self.av.uniqueName('laffMeterBoing') + '-' + str(self.this)
        if currLevel != self.level:
           self.levelLabel['text'] = TTLocalizer.ExpBarLevel + str(self.level+1)
           ToontownIntervals.start(ToontownIntervals.getPulseLargerIval(self.levelLabel, name))
        if currMax != self.maxExp:
           self.expBar['range'] = self.maxExp
           base.playSfx(self.levelUpSfx)
        self.expBar['range'] = self.maxExp
        self.expBar['value'] = exp
        self.expBar['text'] = str(exp)+'/'+str(self.maxExp)
        ToontownIntervals.start(ToontownIntervals.getPulseLargerIval(self.bgBar, name))
		

    def start(self):
        if self.isToon:
            self.bgBar.show()
            self.levelLabel.show()
            if self.av:
                self.accept(self.av.uniqueName('toonExpChange'), self.updateBar)

    def stop(self):
        if self.isToon:
            self.bgBar.hide()
            self.levelLabel.hide()
            if self.av:
                self.ignore(self.av.uniqueName('toonExpChange'))

    def setAvatar(self, av):
        if self.av:
            self.ignore(self.av.uniqueName('toonExpChange'))
        self.av = av
		
    def hide(self):
        self.bgBar.hide()
        self.levelLabel.hide()
		
    def show(self):
        self.bgBar.show()
        self.levelLabel.show()
