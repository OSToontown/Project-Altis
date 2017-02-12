'''
Created on Jan 30, 2017

@author: Drew
'''
from panda3d.core import *
from toontown.shtiker import ShtikerPage
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from direct.gui.DirectGui import *
from toontown.toontowngui import TTDialog
from toontown.shtiker.OptionsPageGUI import *

class ItemsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = OptionLabel(parent=self, relief=None, text_align = TextNode.ACenter, text=TTLocalizer.ItemsPageTitle, text_scale=0.1, pos=(0, 0, 0.65))
        self.buttonModel = 'phase_3/models/gui/quit_button.bam'
        matGui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.nametagStyle_label = DirectLabel(parent=self, relief=None, text=TTLocalizer.ItemsPageNametagStyle, text_align=TextNode.ALeft, text_scale=0.054, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight * 0.145))
        self.nametagStyle_preview = DirectLabel(self, relief=None, text='Preview', scale=0.06, text_align = TextNode.ACenter text_wordwrap=9, pos=(buttonbase_xcoord, 0, textStartHeight * 0.145))
        self.nametagStyle_leftButton = DirectButton(self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale= -0.6, pos=(0.15, 0, textStartHeight * 0.145), command=self.__changeNametagStyle, extraArgs=[-1])
        self.nametagStyle_rightButton = DirectButton(self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale = 0.6, pos = (0.55, 0, textStartHeight * 0.145), command = self.__changeNametagStyle, extraArgs = [1])
        self.nametagStyle_index = 0
        
    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        if self.title:
            self.title.removeNode()
        self.nametagStyle_label.destroy()
        del self.nametagStyle_label
        self.nametagStyle_preview.destroy()
        del self.nametagStyle_preview
        self.nametagStyle_leftButton.destroy()
        del self.nametagStyle_leftButton
        self.nametagStyle_rightButton.destroy()
        del self.nametagStyle_rightButton

    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        self.__updateNametagStyle()

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)
        if self.nametagStyle_index != -1 and self.nametagStyle_index != base.localAvatar.nametagStyles.index(base.localAvatar.getNametagStyle()):
            base.localAvatar.requestNametagStyle(base.localAvatar.nametagStyles[self.nametagStyle_index])
    
    def __updateNametagStyle(self):
        self.nametagStyle_preview['text_font'] = ToontownGlobals.getNametagFont(base.localAvatar.nametagStyles[self.nametagStyle_index])
        nametagCount = len(base.localAvatar.nametagStyles)            
        if nametagCount == 0:
            self.nametagStyle_rightButton.hide()
            self.nametagStyle_leftButton.hide()
            
        if self.nametagStyle_index >= (nametagCount - 1):
            self.nametagStyle_rightButton.hide()
        else:
            self.nametagStyle_rightButton.show()
        
        if self.nametagStyle_index <= 0:
            self.nametagStyle_leftButton.hide()
        else:
            self.nametagStyle_leftButton.show()
    
    def __changeNametagStyle(self, val):
        self.nametagStyle_index += val
        self.__updateNametagStyle()
