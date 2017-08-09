from pandac.PandaModules import *
from toontown.toon import ToonDNA
from direct.fsm import StateData
from direct.gui.DirectGui import *
from toontown.makeatoon.MakeAToonGlobals import *
import random
from toontown.toonbase import TTLocalizer
from direct.directnotify import DirectNotifyGlobal
from toontown.toontowngui import TeaserPanel
from toontown.makeatoon import ShuffleButton

class BodyShop(StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('BodyShop')

    def __init__(self, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.toon = None
        self.torsoChoice = 0
        self.legChoice = 0
        self.headChoice = 0
        self.speciesChoice = 0
        self.speciesButtons = []

    def enter(self, toon, shopsVisited = []):
        base.disableMouse()
        self.toon = toon
        self.dna = self.toon.getStyle()
        gender = self.toon.style.getGender()
        self.speciesStart = self.getSpeciesStart()
        self.speciesChoice = self.speciesStart
        self.headStart = 0
        self.headChoice = ToonDNA.toonHeadTypes.index(self.dna.head) - ToonDNA.getHeadStartIndex(self.species)
        self.torsoStart = 0
        self.torsoChoice = ToonDNA.toonTorsoTypes.index(self.dna.torso) % 3
        self.legStart = 0
        self.legChoice = ToonDNA.toonLegTypes.index(self.dna.legs)
        if CLOTHESSHOP in shopsVisited:
            self.clothesPicked = 1
        else:
            self.clothesPicked = 0
        self.clothesPicked = 1
        if gender == 'm' or ToonDNA.GirlBottoms[self.dna.botTex][1] == ToonDNA.SHORTS:
            torsoStyle = 's'
            torsoPool = ToonDNA.toonTorsoTypes[:3]
        else:
            torsoStyle = 'd'
            torsoPool = ToonDNA.toonTorsoTypes[3:6]
        self.__setSpecies(self.speciesStart)
        self.__swapHead(0)
        self.__swapTorso(0)
        self.__swapLegs(0)
        choicePool = [ToonDNA.toonHeadTypes, torsoPool, ToonDNA.toonLegTypes]
        self.shuffleButton.setChoicePool(choicePool)
        self.accept(self.shuffleFetchMsg, self.changeBody)
        self.acceptOnce('last', self.__handleBackward)
        self.accept('next', self.__handleForward)
        self.acceptOnce('MAT-newToonCreated', self.shuffleButton.cleanHistory)
        self.restrictHeadType(self.dna.head)

    def getSpeciesStart(self):
        for species in ToonDNA.toonSpeciesTypes:
            if species == self.dna.head[0]:
                self.species = species
                return ToonDNA.toonSpeciesTypes.index(species)

    def showButtons(self):
        self.parentFrame.show()
        for btn in self.speciesButtons:
            btn.show()

    def hideButtons(self):
        self.parentFrame.hide()
        self.memberButton.hide()
        for btn in self.speciesButtons:
            btn.hide()

    def exit(self):
        try:
            del self.toon
        except:
            self.notify.warning('BodyShop: toon not found')

        self.hideButtons()
        self.ignore('last')
        self.ignore('next')
        self.ignore('enter')
        self.ignore(self.shuffleFetchMsg)

    def load(self):
        self.gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        guiRArrowUp = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDown = self.gui.find('**/tt_t_gui_mat_arrowDown')
        guiRArrowRollover = self.gui.find('**/tt_t_gui_mat_arrowUp')
        guiRArrowDisabled = self.gui.find('**/tt_t_gui_mat_arrowDisabled')
        shuffleFrame = self.gui.find('**/tt_t_gui_mat_shuffleFrame')
        shuffleArrowUp = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDown = self.gui.find('**/tt_t_gui_mat_shuffleArrowDown')
        shuffleArrowRollover = self.gui.find('**/tt_t_gui_mat_shuffleArrowUp')
        shuffleArrowDisabled = self.gui.find('**/tt_t_gui_mat_shuffleArrowDisabled')
        self.upsellModel = loader.loadModel('phase_3/models/gui/tt_m_gui_ups_mainGui')
        upsellTex = self.upsellModel.find('**/tt_t_gui_ups_banner')
        self.parentFrame = DirectFrame(relief=DGG.RAISED, pos=(0.98, 0, 0.416), frameColor=(1, 0, 0, 0))
        self.parentFrame.setPos(-0.36, 0, -0.5)
        self.parentFrame.reparentTo(base.a2dTopRight)
        self.createSpeciesButtons()
        self.headFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.3), hpr=(0, 0, 2), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.BodyShopHead, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.headLButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapHead, extraArgs=[-1])
        self.headRButton = DirectButton(parent=self.headFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapHead, extraArgs=[1])
        self.bodyFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonScale, relief=None, pos=(0, 0, -0.5), hpr=(0, 0, -2), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.BodyShopBody, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.torsoLButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapTorso, extraArgs=[-1])
        self.torsoRButton = DirectButton(parent=self.bodyFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapTorso, extraArgs=[1])
        self.legsFrame = DirectFrame(parent=self.parentFrame, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, -0.7), hpr=(0, 0, 3), scale=0.9, frameColor=(1, 1, 1, 1), text=TTLocalizer.BodyShopLegs, text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.legLButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.__swapLegs, extraArgs=[-1])
        self.legRButton = DirectButton(parent=self.legsFrame, relief=None, image=(shuffleArrowUp,
         shuffleArrowDown,
         shuffleArrowRollover,
         shuffleArrowDisabled), image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.__swapLegs, extraArgs=[1])
        self.memberButton = DirectButton(relief=None, image=(upsellTex,
         upsellTex,
         upsellTex,
         upsellTex), image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, scale=0.9, pos=(0, 0, -0.84), command=self.__restrictForward)
        self.parentFrame.hide()
        self.memberButton.hide()
        self.shuffleFetchMsg = 'BodyShopShuffle'
        self.shuffleButton = ShuffleButton.ShuffleButton(self, self.shuffleFetchMsg)
        return

    def unload(self):
        self.gui.removeNode()
        del self.gui
        self.upsellModel.removeNode()
        del self.upsellModel
        self.parentFrame.destroy()
        self.headFrame.destroy()
        self.bodyFrame.destroy()
        self.legsFrame.destroy()
        self.headLButton.destroy()
        self.headRButton.destroy()
        self.torsoLButton.destroy()
        self.torsoRButton.destroy()
        self.legLButton.destroy()
        self.legRButton.destroy()
        self.memberButton.destroy()
        del self.parentFrame
        del self.headFrame
        del self.bodyFrame
        del self.legsFrame
        del self.headLButton
        del self.headRButton
        del self.torsoLButton
        del self.torsoRButton
        del self.legLButton
        del self.legRButton
        del self.memberButton
        for button in self.speciesButtons:
            button.destroy()
            del button
        self.speciesButtons = []
        self.shuffleButton.unload()
        self.ignore('MAT-newToonCreated')

    def __swapTorso(self, offset):
        gender = self.toon.style.getGender()
        if not self.clothesPicked:
            length = len(ToonDNA.toonTorsoTypes[6:])
            torsoOffset = 6
        elif gender == 'm':
            length = len(ToonDNA.toonTorsoTypes[:3])
            torsoOffset = 0
            if self.toon.style.topTex not in ToonDNA.MakeAToonBoyShirts:
                randomShirt = ToonDNA.getRandomTop(gender, ToonDNA.MAKE_A_TOON)
                shirtTex, shirtColor, sleeveTex, sleeveColor = randomShirt
                self.toon.style.topTex = shirtTex
                self.toon.style.topTexColor = shirtColor
                self.toon.style.sleeveTex = sleeveTex
                self.toon.style.sleeveTexColor = sleeveColor
            if self.toon.style.botTex not in ToonDNA.MakeAToonBoyBottoms:
                botTex, botTexColor = ToonDNA.getRandomBottom(gender, ToonDNA.MAKE_A_TOON)
                self.toon.style.botTex = botTex
                self.toon.style.botTexColor = botTexColor
        else:
            length = len(ToonDNA.toonTorsoTypes[3:6])
            if self.toon.style.torso[1] == 'd':
                torsoOffset = 3
            else:
                torsoOffset = 0
            if self.toon.style.topTex not in ToonDNA.MakeAToonGirlShirts:
                randomShirt = ToonDNA.getRandomTop(gender, ToonDNA.MAKE_A_TOON)
                shirtTex, shirtColor, sleeveTex, sleeveColor = randomShirt
                self.toon.style.topTex = shirtTex
                self.toon.style.topTexColor = shirtColor
                self.toon.style.sleeveTex = sleeveTex
                self.toon.style.sleeveTexColor = sleeveColor
            if self.toon.style.botTex not in ToonDNA.MakeAToonGirlBottoms:
                if self.toon.style.torso[1] == 'd':
                    botTex, botTexColor = ToonDNA.getRandomBottom(gender, ToonDNA.MAKE_A_TOON, girlBottomType=ToonDNA.SKIRT)
                    self.toon.style.botTex = botTex
                    self.toon.style.botTexColor = botTexColor
                    torsoOffset = 3
                else:
                    botTex, botTexColor = ToonDNA.getRandomBottom(gender, ToonDNA.MAKE_A_TOON, girlBottomType=ToonDNA.SHORTS)
                    self.toon.style.botTex = botTex
                    self.toon.style.botTexColor = botTexColor
                    torsoOffset = 0
        self.torsoChoice = (self.torsoChoice + offset) % length
        self.__updateScrollButtons(self.torsoChoice, length, self.torsoStart, self.torsoLButton, self.torsoRButton)
        torso = ToonDNA.toonTorsoTypes[torsoOffset + self.torsoChoice]
        self.dna.torso = torso
        self.toon.swapToonTorso(torso)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    def __swapLegs(self, offset):
        length = len(ToonDNA.toonLegTypes)
        self.legChoice = (self.legChoice + offset) % length
        self.notify.debug('self.legChoice=%d, length=%d, self.legStart=%d' % (self.legChoice, length, self.legStart))
        self.__updateScrollButtons(self.legChoice, length, self.legStart, self.legLButton, self.legRButton)
        newLeg = ToonDNA.toonLegTypes[self.legChoice]
        self.dna.legs = newLeg
        self.toon.swapToonLegs(newLeg)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)

    def __swapHead(self, offset):
        self.headList = ToonDNA.getHeadList(self.species)
        length = len(self.headList)
        self.headChoice = (self.headChoice + offset) % length
        self.__updateHead()

    def __swapSpecies(self, offset):
        length = len(ToonDNA.toonSpeciesTypes)
        self.speciesChoice = (self.speciesChoice + offset) % length
        self.__updateScrollButtons(self.speciesChoice, length, self.speciesStart, self.speciesLButton, self.speciesRButton)
        self.species = ToonDNA.toonSpeciesTypes[self.speciesChoice]
        self.headList = ToonDNA.getHeadList(self.species)
        maxHeadChoice = len(self.headList) - 1
        if self.headChoice > maxHeadChoice:
            self.headChoice = maxHeadChoice
        self.__updateHead()
        
    def createSpeciesButtons(self):
        gui = base.matGui
        shuffleUp = gui.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = gui.find('**/tt_t_gui_mat_shuffleDown')
        pos = ((.3, 0, .3),  (.6, 0, .3),  (.9, 0, .3),
               (.3, 0, .1),  (.6, 0, .1),  (.9, 0, .1),
               (.3, 0, -.1), (.6, 0, -.1), (.9, 0, -.1),
               (.3, 0, -.3), (.6, 0, -.3), (.9, 0, -.3),
               (.3, 0, -.5), (.6, 0, -.5), (.9, 0, -.5)
              )
        
        for x in xrange(len(ToonDNA.toonSpeciesTypes)):
            name = TTLocalizer.AllSpecies[x]
            btn = DirectButton(relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp, shuffleDown), 
            image_scale = (0.6, 0.7, 0.7), image1_scale = (0.63, 0.7, 0.7), image2_scale = (0.63, 0.7, 0.7),
            text_fg = (1, 1, 1, 1), text = name, text_pos = (0, -0.02), text_scale = .08,
            scale = 0.95, command = self.__setSpecies, extraArgs = [x])
            btn.reparentTo(base.a2dLeftCenter)
            btn.setPos(pos[x])
            btn.hide()
            self.speciesButtons.append(btn)
        
    def __setSpecies(self, offset):
        for btn in self.speciesButtons:
            btn['state'] = DGG.NORMAL
            
        self.speciesButtons[offset]['state'] = DGG.DISABLED
        
        length = len(ToonDNA.toonSpeciesTypes)
        self.speciesChoice = (offset) % length
        self.species = ToonDNA.toonSpeciesTypes[self.speciesChoice]
        self.headList = ToonDNA.getHeadList(self.species)
        maxHeadChoice = len(self.headList) - 1
        if self.headChoice > maxHeadChoice:
            self.headChoice = maxHeadChoice
        self.__updateHead()

    def __updateHead(self):
        self.__updateScrollButtons(self.headChoice, len(self.headList), self.headStart, self.headLButton, self.headRButton)
        headIndex = ToonDNA.getHeadStartIndex(self.species) + self.headChoice
        newHead = ToonDNA.toonHeadTypes[headIndex]
        self.dna.head = newHead
        self.toon.swapToonHead(newHead)
        self.toon.loop('neutral', 0)
        self.toon.swapToonColor(self.dna)
        self.restrictHeadType(newHead)

    def __updateScrollButtons(self, choice, length, start, lButton, rButton):
        if choice == (start - 1) % length:
            rButton['state'] = DGG.DISABLED
        elif choice != (start - 1) % length:
            rButton['state'] = DGG.NORMAL
        if choice == start % length:
            lButton['state'] = DGG.DISABLED
        elif choice != start % length:
            lButton['state'] = DGG.NORMAL
        if lButton['state'] == DGG.DISABLED and rButton['state'] == DGG.DISABLED:
            self.notify.info('Both buttons got disabled! Doing fallback code. choice%d, length=%d, start=%d, lButton=%s, rButton=%s' % (choice,
             length,
             start,
             lButton,
             rButton))
            if choice == start % length:
                lButton['state'] = DGG.DISABLED
                rButton['state'] = DGG.NORMAL
            elif choice == (start - 1) % length:
                lButton['state'] = DGG.NORMAL
                rButton['state'] = DGG.DISABLED
            else:
                lButton['state'] = DGG.NORMAL
                rButton['state'] = DGG.NORMAL

    def __handleForward(self):
        self.doneStatus = 'next'
        messenger.send(self.doneEvent)

    def __handleBackward(self):
        self.doneStatus = 'last'
        messenger.send(self.doneEvent)

    def restrictHeadType(self, head):
        if not base.cr.isPaid():
            if head[0] in ('h', 'p', 'b'):
                self.accept('next', self.__restrictForward)
            else:
                self.accept('next', self.__handleForward)

    def __restrictForward(self):
        TeaserPanel.TeaserPanel(pageName='species')

    def changeBody(self):
        newChoice = self.shuffleButton.getCurrChoice()
        newHead = newChoice[0]
        newSpeciesIndex = ToonDNA.toonSpeciesTypes.index(ToonDNA.getSpecies(newHead))
        newHeadIndex = ToonDNA.toonHeadTypes.index(newHead) - ToonDNA.getHeadStartIndex(ToonDNA.getSpecies(newHead))
        newTorsoIndex = ToonDNA.toonTorsoTypes.index(newChoice[1])
        newLegsIndex = ToonDNA.toonLegTypes.index(newChoice[2])
        oldHead = self.toon.style.head
        oldSpeciesIndex = ToonDNA.toonSpeciesTypes.index(ToonDNA.getSpecies(oldHead))
        oldHeadIndex = ToonDNA.toonHeadTypes.index(oldHead) - ToonDNA.getHeadStartIndex(ToonDNA.getSpecies(oldHead))
        oldTorsoIndex = ToonDNA.toonTorsoTypes.index(self.toon.style.torso)
        oldLegsIndex = ToonDNA.toonLegTypes.index(self.toon.style.legs)
        self.__setSpecies(random.randrange(0, 9))
        self.__swapHead(newHeadIndex - oldHeadIndex)
        self.__swapTorso(newTorsoIndex - oldTorsoIndex)
        self.__swapLegs(newLegsIndex - oldLegsIndex)

    def getCurrToonSetting(self):
        return [self.toon.style.head, self.toon.style.torso, self.toon.style.legs]

