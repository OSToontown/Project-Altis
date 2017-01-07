from panda3d.core import *
from toontown.toon import ToonDNA
from direct.fsm import StateData
from direct.gui.DirectGui import *
from MakeAToonGlobals import *
from toontown.toonbase import TTLocalizer, ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class StatusShop(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('StatusShop')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.index = 0
        return

    def enter(self, toon, shopsVisited = []):
        base.disableMouse()
        self.toon = toon
        self.dna = toon.getStyle()
        self.acceptOnce('last', self.__handleBackward)
        self.acceptOnce('next', self.__handleForward)

    def showButtons(self):
        self.parentFrame.show()

    def hideButtons(self):
        self.parentFrame.hide()

    def exit(self):
        self.ignore('last')
        self.ignore('next')
        self.ignore('enter')
        try:
            del self.toon
        except:
            print 'StatusShop: toon not found'

        self.hideButtons()

    def load(self):
        normalTextColor = (0.3, 0.25, 0.2, 1)
        self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
        guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
        shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
        shuffleUp = self.gui.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = self.gui.find('**/tt_t_gui_mat_shuffleDown')
        shuffleImage = (self.gui.find('**/tt_t_gui_mat_shuffleArrowUp'), self.gui.find('**/tt_t_gui_mat_shuffleArrowDown'), self.gui.find('**/tt_t_gui_mat_shuffleArrowUp'), self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled'))
        bookModel = loader.loadModel('phase_3.5/models/gui/stickerbook_gui')
        poster = bookModel.find('**/questCard')
        self.parentFrame = self.getNewFrame()
        self.uberFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.7), hpr=(0, 0, 3), scale=1.1, frameColor=(1, 1, 1, 1), text='', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.uberLButton = DirectButton(parent=self.uberFrame, relief=None, image=shuffleImage, image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapUberStatus, extraArgs=[-1])
        self.uberRButton = DirectButton(parent=self.uberFrame, relief=None, image=shuffleImage, image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapUberStatus, extraArgs=[1])
        self.uberInfo = DirectFrame(parent=self.uberFrame, relief=None, image=poster, image_scale=(0.5, 0.5, 0.7), image_pos=(0,0,-0.15), text='', text_font=ToontownGlobals.getInterfaceFont(), text_fg=normalTextColor, text_scale=0.05, text_wordwrap=8.0, pos=(-0.5, 0, 0.5))
        self.__swapUberStatus(0)
        self.parentFrame.hide()

    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.parentFrame.destroy()
        del self.parentFrame
        self.ignore('MAT-newToonCreated')
    
    def getNewFrame(self):
        frame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1, 0, 0, 0))
        frame.setPos(-0.36, 0, -0.5)
        frame.reparentTo(base.a2dTopRight)
        return frame
		
    def __swapUberStatus(self, direction):
        self.index += direction
        if self.index <= 0:
            self.index = 0
            self.uberLButton['state'] = DGG.DISABLED
            self.uberRButton['state'] = DGG.NORMAL
        elif self.index >= 3:
            self.index = 3
            self.uberLButton['state'] = DGG.NORMAL
            self.uberRButton['state'] = DGG.DISABLED
        else:
            self.uberLButton['state'] = DGG.NORMAL
            self.uberRButton['state'] = DGG.NORMAL
        if self.toon:
            self.toon.uberType = self.index
        self.uberFrame['text'] = TTLocalizer.UberTitles[self.index]
        self.uberInfo['text'] = TTLocalizer.UberInfos[self.index]

    def __handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    def __handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)
