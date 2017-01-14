from panda3d.core import *
from toontown.toon import ToonDNA
from direct.fsm import StateData
from direct.gui.DirectGui import *
from MakeAToonGlobals import *
from toontown.toonbase import TTLocalizer, ToontownGlobals, ToontownBattleGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.task import Task

class StartShop(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('StartShop')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.index = -1
        self.gagOneIndex = None
        self.gagTwoIndex = None

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
            print 'StartShop: toon not found'

        self.hideButtons()

    def load(self):
        normalTextColor = (0.3, 0.25, 0.2, 1)
        buttonXOffset = 0.15
        buttonYOffset = 0.15
        self.buttonsOne = []
        self.buttonsTwo = []
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
        invModel = loader.loadModel('phase_3.5/models/gui/inventory_icons')
        poster = bookModel.find('**/questCard')
        self.parentFrame = self.getNewFrame()
        self.pgFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(-3, 0, -0.7), hpr=(0, 0, -3), scale=1.1, frameColor=(1, 1, 1, 1), text='', text_scale=0.046875, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.pgLButton = DirectButton(parent=self.pgFrame, relief=None, image=shuffleImage, image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapPG, extraArgs=[-1])
        self.pgRButton = DirectButton(parent=self.pgFrame, relief=None, image=shuffleImage, image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapPG, extraArgs=[1])
        self.pgInfo = DirectFrame(parent=self.pgFrame, relief=None, text='Starting Playground:', text_font=ToontownGlobals.getBuildingNametagFont(), text_scale=0.05, text_fg=(1,1,1,1), text_wordwrap=8.0, pos=(0, 0, 0.25))
        self.gagFrame = DirectFrame(parent=self.parentFrame, image=poster, image_scale=(1,1,3), relief=None, pos=(0, 0, -0.5), scale=1.1, frameColor=(1, 1, 1, 1), text='', text_scale=0.046875, text_pos=(-0.001, -0.015), text_font=ToontownGlobals.getBuildingNametagFont(), text_fg=(1, 1, 1, 1))
        for trackId in xrange(len(ToontownBattleGlobals.Tracks)):
            iconGeom = invModel.find('**/' + ToontownBattleGlobals.AvPropsNew[trackId][0])
            if trackId == 4 or trackId == 5:
                button = DirectButton(parent=self.gagFrame, image=iconGeom, relief=None, pos=(0, 0, .45-(buttonYOffset*trackId)), image_color=(0.3,0.3,0.3,1), state=DGG.DISABLED)
                button2 = DirectButton(parent=self.gagFrame, image=iconGeom, relief=None, pos=(buttonXOffset, 0, .45-(buttonYOffset*trackId)), image_color=(0.3,0.3,0.3,1), state=DGG.DISABLED)
            else:
                button = DirectButton(parent=self.gagFrame, image=iconGeom, relief=None, pos=(0, 0, .45-(buttonYOffset*trackId)), command=self.chooseGag, extraArgs=[trackId])
                button2 = DirectButton(parent=self.gagFrame, image=iconGeom, relief=None, pos=(buttonXOffset, 0, .45-(buttonYOffset*trackId)), command=self.chooseGag, extraArgs=[trackId, 1])
            self.buttonsOne.append(button)
            self.buttonsTwo.append(button2)
            
        self.__swapPG(0)
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
		
    def __swapPG(self, direction):
        self.index += direction
        if self.index <= 0:
            self.index = 0
            self.pgLButton['state'] = DGG.DISABLED
            self.pgRButton['state'] = DGG.NORMAL
        elif self.index >= 2:
            self.index = 2
            self.pgLButton['state'] = DGG.NORMAL
            self.pgRButton['state'] = DGG.DISABLED
        else:
            self.pgLButton['state'] = DGG.NORMAL
            self.pgRButton['state'] = DGG.NORMAL
        if self.toon:
            self.toon.startingPg = self.index
        if self.index == 0:
            self.pgFrame['text'] = TTLocalizer.lToontownCentral
            self.gagFrame.hide()
        elif self.index == 1:
            self.pgFrame['text'] = TTLocalizer.lDonaldsDock
            self.gagFrame.show()
            for button in self.buttonsTwo:
                button.hide()
        elif self.index == 2:
            self.pgFrame['text'] = TTLocalizer.lDaisyGardens
            self.gagFrame.show()
            for button in self.buttonsTwo:
                button.show()
        else:
            self.pgFrame['text'] = TTLocalizer.lToontownCentral
            self.gagFrame.hide()
			
    def chooseGag(self, index, type=0):
        if type == 0:
            if index == self.gagTwoIndex:
                pass
            else:
                self.gagOneIndex = index
                self.toon.choiceAlpha = index
                self.resetButtons()
                self.buttonsOne[self.gagOneIndex].setColor(0,1,0,1)
                try:
                    self.buttonsTwo[self.gagTwoIndex].setColor(0,1,0,1)
                except:
                    pass
        else:
            if index == self.gagOneIndex:
                pass
            else:
                self.gagTwoIndex = index
                self.toon.choiceBeta = index
                self.resetButtons()
                self.buttonsTwo[self.gagTwoIndex].setColor(0,1,0,1)
                try:
                    self.buttonsOne[self.gagOneIndex].setColor(0,1,0,1)
                except:
                    pass
				
    def resetButtons(self):
        for button in self.buttonsOne + self.buttonsTwo:
            button.setColor(1,1,1,1)

    def __handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    def __handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)
