'''
Created on Jan 2, 2017

@author: Drew
'''

from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import Wait, Func, Sequence, LerpScaleInterval
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TransparencyAttrib, TextNode, Vec3

from toontown.toonbase import TTLocalizer
from toontown.toontowngui.TTGui import *


class DMenuQuit(DirectObject):

    def __init__(self):
        self.optionsOpenSfx = None # base.loadSfx(DMenuResources.Settings_Open) # ALTIS: TODO: Add sound effects
        self.optionsCloseSfx = None # base.loadSfx(DMenuResources.Settings_Close) # ALTIS: TODO: Add sound effects

    def showConf(self):
        # base.playSfx(self.optionsOpenSfx) # ALTIS: TODO: Add sound effects
        self.displayConfirmation()
        zoomIn = (LerpScaleInterval(self.confNode, .4, Vec3(1, 1, 1), Vec3(0, 0, 0), blendType = 'easeInOut')).start()

    def hideConf(self):
        base.transitions.noFade()
        # base.playSfx(self.optionsCloseSfx) # ALTIS: TODO: Add sound effects
        zoomOut = (LerpScaleInterval(self.confNode, .4, Vec3(0, 0, 0), Vec3(1, 1, 1), blendType = 'easeInOut')).start()
        Sequence (
        Wait(.4),
        Func(self.delConf)).start()

    def displayConfirmation(self):
        self.confNode = aspect2d.attachNewNode('confNode')
        self.confNode.reparentTo(aspect2d, 4000)
        base.transitions.fadeScreen(0.5)
        gui = base.matGui
        shuffleUp = gui.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = gui.find('**/tt_t_gui_mat_shuffleDown')

        self.confBox = OnscreenImage(image = 'phase_3/maps/stat_board.png')
        self.confBox.setTransparency(TransparencyAttrib.MAlpha)
        self.confBox.setPos(0, 0, 0)
        self.confBox.setScale(0.7, 1, 0.4)
        self.confBox.reparentTo(self.confNode)

        self.question = DirectLabel(parent = self.confNode, relief = None, text_style = 3, text = TTLocalizer.QuitConfirm, text_align = TextNode.ACenter, text_scale = 0.07, pos = (0, 0, 0.2))

        self.yesBtn = DirectButton(relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = TTLocalizer.lYes, text_pos = (0, -0.02), text_scale = .07, scale = 1.2, command = self.quitGame)
        self.yesBtn.reparentTo(self.confNode)
        self.yesBtn.setPos(-.3, 0, -.2)
        self.yesBtn.show()

        self.noBtn = DirectButton(relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = TTLocalizer.lNo, text_pos = (0, -0.02), text_scale = .07, scale = 1.2, command = self.cancelQuitGame)
        self.noBtn.reparentTo(self.confNode)
        self.noBtn.setPos(.3, 0, -.2)
        self.noBtn.show()

    def delConf(self):
        if self.confNode:
            self.confNode.removeNode()
            del self.confNode

    def quitGame(self):
        messenger.send('doQuitGame')

    def cancelQuitGame(self):
        self.yesBtn['state'] = DGG.DISABLED
        self.noBtn['state'] = DGG.DISABLED
        messenger.send('doCancelQuitGame')
