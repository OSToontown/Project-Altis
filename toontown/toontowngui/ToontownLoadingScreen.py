from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import NO_FADE_SORT_INDEX
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
from direct.interval.IntervalGlobal import Sequence, Wait
import random

class ToontownLoadingScreen:

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.gui = loader.loadModel('phase_3/models/gui/progress-background.bam')
        self.title = DirectLabel(guiId='ToontownLoadingScreenTitle', parent=self.gui, relief=None, pos=(base.a2dRight/5, 0, 0.235), text='', textMayChange=1, text_scale=0.08, text_fg=(0.03, 0.83, 0, 1), text_align=TextNode.ALeft, text_font=ToontownGlobals.getSignFont())
        self.waitBar = DirectWaitBar(guiId='ToontownLoadingScreenWaitBar', parent=self.gui, frameSize=(base.a2dLeft+(base.a2dRight/4.95), base.a2dRight-(base.a2dRight/4.95), -0.03, 0.03), pos=(0, 0, 0.15), text='')
        logoScale = 0.3625  # Scale for our locked aspect ratio (2:1).
        self.logo = OnscreenImage(image='phase_3/maps/toontown-logo.png', 
            scale=(logoScale * 2.0, 1, logoScale))
        
        self.logo.reparentTo(hidden)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        # self.logo.setPos(scale[0], 0, -scale[2])
        self.logo.setPos(0, 0, -scale[2] * 2)

    def destroy(self):
        self.title.destroy()
        self.gui.removeNode()
        self.logo.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory, zoneId):
        self.waitBar['range'] = range
        self.title['text'] = label
        self.__count = 0
        self.__expectedCount = range
        if gui:
            self.title.reparentTo(base.a2dpBottomLeft, NO_FADE_SORT_INDEX)
            self.title.setPos(0.24, 0, 0.23)
            self.gui.setPos(0, -0.1, 0)
            self.gui.reparentTo(aspect2d, NO_FADE_SORT_INDEX)
            #self.gui.setTexture(self.background, 1)
            self.logo.reparentTo(base.a2dpTopCenter, NO_FADE_SORT_INDEX)
        else:
            self.title.reparentTo(base.a2dpBottomLeft, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
            self.logo.reparentTo(hidden)
        
        self.waitBar.reparentTo(base.a2dpBottomCenter, NO_FADE_SORT_INDEX)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.logo.reparentTo(hidden)
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        self.waitBar.update(self.__count)