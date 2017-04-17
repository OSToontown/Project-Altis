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
from direct.gui import DirectGuiGlobals
from toontown.toontowngui import TTDialog
from toontown.shtiker.OptionsPageGUI import *
from toontown.fishing import FishGlobals
from direct.actor import Actor
from direct.interval.IntervalGlobal import *

class ItemsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.title = OptionLabel(parent=self, relief=None, text_align = TextNode.ACenter, text=TTLocalizer.ItemsPageTitle, text_scale=0.1, pos=(0, 0, 0.65))
        self.buttonModel = 'phase_3/models/gui/quit_button.bam'
        matGui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.nametagStyle_label = DirectLabel(parent = self, relief=None, text=TTLocalizer.ItemsPageNametagStyle, text_align=TextNode.ALeft, text_scale=0.054, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight * 0.145 + .3))
        self.nametagStyle_preview = DirectLabel(parent = self, relief=None, text='Preview', scale=0.06, text_align = TextNode.ACenter, text_wordwrap=9, pos=(buttonbase_xcoord, 0, textStartHeight * 0.145 + .3))
        self.nametagStyle_leftButton = DirectButton(parent = self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale= -0.6, pos=(0.15, 0, textStartHeight * 0.145 + .3), command=self.__changeNametagStyle, extraArgs=[-1])
        self.nametagStyle_rightButton = DirectButton(parent = self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale = 0.6, pos = (0.55, 0, textStartHeight * 0.145 + .3), command = self.__changeNametagStyle, extraArgs = [1])
        self.nametagStyle_index = 0
        
        self.fishingRods_label = DirectLabel(parent = self, relief=None, text=TTLocalizer.ItemsPageFishingRods, text_align=TextNode.ALeft, text_scale=0.054, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight * 0.145))
        # The preview is a button to enable the hover effect
        self.fishingRods_preview = DirectButton(parent = self, relief=None, text='Preview', scale=0.06, text_align = TextNode.ACenter, text_wordwrap=9, pos=(buttonbase_xcoord, 0, textStartHeight * 0.145))
        self.fishingRods_leftButton = DirectButton(parent = self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale= -0.6, pos=(0.15, 0, textStartHeight * 0.145), command=self.__changeFishingRods, extraArgs=[-1])
        self.fishingRods_rightButton = DirectButton(parent = self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale = 0.6, pos = (0.55, 0, textStartHeight * 0.145), command = self.__changeFishingRods, extraArgs = [1])
        self.fishingRods_index = 0
        self.fishingRods_previewPanel = OnscreenImage(parent = self, image = 'phase_3/maps/stat_board.png', pos = (buttonbase_xcoord, 0, textStartHeight * 0.145), scale = 0.2)
        self.fishingRods_previewPanel.setTransparency(TransparencyAttrib.MAlpha)
        self.fishingRods_previewPanel.hide()
        self.fishingRods_preview.bind(DirectGuiGlobals.ENTER, self.enterHoverFishing)
        self.fishingRods_preview.bind(DirectGuiGlobals.EXIT, self.exitHoverFishing)
        self.geom = None
        self.geomRotate = None
        
        self.cheesyEffect_label = DirectLabel(parent = self, relief=None, text=TTLocalizer.ItemsPageCheesyEffect, text_align=TextNode.ALeft, text_scale=0.054, text_wordwrap=16, pos=(leftMargin, 0, textStartHeight * 0.145 - .3))
        self.cheesyEffect_preview = DirectLabel(parent = self, relief=None, text='Preview', scale=0.06, text_align = TextNode.ACenter, text_wordwrap=9, pos=(buttonbase_xcoord, 0, textStartHeight * 0.145 - .3))
        self.cheesyEffect_leftButton = DirectButton(parent = self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale= -0.6, pos=(0.15, 0, textStartHeight * 0.145 - .3), command=self.__changeCheesyEffect, extraArgs=[-1])
        self.cheesyEffect_rightButton = DirectButton(parent = self, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale = 0.6, pos = (0.55, 0, textStartHeight * 0.145 - .3), command = self.__changeCheesyEffect, extraArgs = [1])
        self.cheesyEffect_index = 0

    def unload(self):
        ShtikerPage.ShtikerPage.unload(self)
        if self.title:
            self.title.removeNode()
        if self.geom:
            self.geom.cleanup()
            self.geom.removeNode()
        if self.geomRotate:
            self.geomRotate.finish()
        self.nametagStyle_label.destroy()
        del self.nametagStyle_label
        self.nametagStyle_preview.destroy()
        del self.nametagStyle_preview
        self.nametagStyle_leftButton.destroy()
        del self.nametagStyle_leftButton
        self.nametagStyle_rightButton.destroy()
        del self.nametagStyle_rightButton

        self.fishingRods_label.destroy()
        del self.fishingRods_label
        self.fishingRods_preview.destroy()
        del self.fishingRods_preview
        self.fishingRods_leftButton.destroy()
        del self.fishingRods_leftButton
        self.fishingRods_rightButton.destroy()
        del self.fishingRods_rightButton
        self.fishingRods_previewPanel.destroy()
        del self.fishingRods_previewPanel
        
        self.cheesyEffect_label.destroy()
        del self.cheesyEffect_label
        self.cheesyEffect_preview.destroy()
        del self.cheesyEffect_preview
        self.cheesyEffect_leftButton.destroy()
        del self.cheesyEffect_leftButton
        self.cheesyEffect_rightButton.destroy()
        del self.cheesyEffect_rightButton
        
    def enter(self):
        ShtikerPage.ShtikerPage.enter(self)
        self.nametagStyle_index = settings.get('lastNametag', {})[str(base.localAvatar.doId)]
        self.fishingRods_index = settings.get('lastRod', {})[str(base.localAvatar.doId)]
        self.cheesyEffect_index = settings.get('lastEffect', {})[str(base.localAvatar.doId)]
        
        self.__updateNametagStyle()
        self.__updateFishingRods()
        self.__updateCheesyEffect()

    def exit(self):
        ShtikerPage.ShtikerPage.exit(self)

        nametagStyle_index = settings.get('lastNametag', {})
        fishingRods_index = settings.get('lastRod', {})
        cheesyEffect_index = settings.get('lastEffect', {})
                
        nametagStyle_index[str(base.localAvatar.doId)] = self.nametagStyle_index
        settings['lastNametag'] = nametagStyle_index
        
        fishingRods_index[str(base.localAvatar.doId)] = self.fishingRods_index
        settings['lastRod'] = fishingRods_index
        
        cheesyEffect_index[str(base.localAvatar.doId)] = self.cheesyEffect_index
        settings['lastEffect'] = cheesyEffect_index
        
        if self.nametagStyle_index != -1 and self.nametagStyle_index != base.localAvatar.nametagStyles.index(base.localAvatar.getNametagStyle()):
            base.localAvatar.requestNametagStyle(base.localAvatar.nametagStyles[self.nametagStyle_index])
        if self.fishingRods_index != -1 and self.fishingRods_index != base.localAvatar.fishingRods.index(base.localAvatar.getFishingRod()):
            base.localAvatar.requestFishingRod(base.localAvatar.fishingRods[self.fishingRods_index])
        if self.cheesyEffect_index != -1 and self.cheesyEffect_index != base.localAvatar.cheesyEffects.index(base.localAvatar.savedCheesyEffect):
            base.localAvatar.requestCheesyEffects(base.localAvatar.cheesyEffects[self.cheesyEffect_index])
    
    def __updateNametagStyle(self):
        self.nametagStyle_preview['text_font'] = ToontownGlobals.getNametagFont(base.localAvatar.nametagStyles[self.nametagStyle_index])
        self.nametagStyle_preview['text'] = TTLocalizer.NametagFontNames[base.localAvatar.nametagStyles[self.nametagStyle_index]]
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
        
    def __updateFishingRods(self):
        self.fishingRods_preview['text'] = TTLocalizer.FishingRodNameDict.get(base.localAvatar.fishingRods[self.fishingRods_index])
        rodPath = FishGlobals.RodFileDict.get(base.localAvatar.fishingRods[self.fishingRods_index])
        if self.geom:
            self.geom.cleanup()
            self.geom.removeNode()
            self.geom = None
            if self.geomRotate:
                self.geomRotate.finish()
        self.geom = Actor.Actor(rodPath, {'cast': 'phase_4/models/props/fishing-pole-chan'})
        self.geom.setHpr(90, 55, -90)
        self.geom.setPos(0, 0, -.5)
        self.geom.setScale(.4)
        self.geomRotate = self.geom.hprInterval(4, Vec3(450, 55, -90)).loop()
        self.geom.reparentTo(self.fishingRods_previewPanel)
        self.geom.pose('cast', 130)
        nametagCount = len(base.localAvatar.fishingRods)            
        if nametagCount == 0:
            self.fishingRods_rightButton.hide()
            self.fishingRods_leftButton.hide()
            
        if self.fishingRods_index >= (nametagCount - 1):
            self.fishingRods_rightButton.hide()
        else:
            self.fishingRods_rightButton.show()
        
        if self.fishingRods_index <= 0:
            self.fishingRods_leftButton.hide()
        else:
            self.fishingRods_leftButton.show()
    
    def __changeFishingRods(self, val):
        self.fishingRods_index += val
        self.__updateFishingRods()

    def enterHoverFishing(self, hoverEvent):
        if hasattr(self, 'fishingRods_previewPanel'):
            self.fishingRods_previewPanel.show()
    
    def exitHoverFishing(self, hoverEvent):
        if hasattr(self, 'fishingRods_previewPanel'):
            self.fishingRods_previewPanel.hide()
            
    def __updateCheesyEffect(self):
        try:
            self.cheesyEffect_preview['text'] = TTLocalizer.CheesyEffectId2Name.get(base.localAvatar.cheesyEffects[self.cheesyEffect_index])
        except:
            self.cheesyEffect_preview['text'] = 'Unknown Effect ID: %s' % self.cheesyEffect_index
        ceCount = len(base.localAvatar.cheesyEffects)            
        if ceCount == 0:
            self.cheesyEffect_rightButton.hide()
            self.cheesyEffect_leftButton.hide()
            
        if self.cheesyEffect_index >= (ceCount - 1):
            self.cheesyEffect_rightButton.hide()
        else:
            self.cheesyEffect_rightButton.show()
        
        if self.cheesyEffect_index <= 0:
            self.cheesyEffect_leftButton.hide()
        else:
            self.cheesyEffect_leftButton.show()
    
    def __changeCheesyEffect(self, val):
        self.cheesyEffect_index += val
        self.__updateCheesyEffect()