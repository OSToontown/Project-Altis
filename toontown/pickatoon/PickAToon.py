'''
Created on Sep 12, 2016

@author: Drew
'''


from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.showbase.DirectObject import DirectObject
from direct.task import Task
from panda3d.core import *

from toontown.dmenu import DMenuQuit, DMenuOptions
from toontown.hood import SkyUtil
from toontown.pickatoon import ShardPicker
from toontown.toon import ToonDNA, Toon, ToonHead, LaffMeter
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toontowngui.TTDialog import *


COLORS = (Vec4(0.917, 0.164, 0.164, 1),
 Vec4(0.152, 0.75, 0.258, 1),
 Vec4(0.598, 0.402, 0.875, 1),
 Vec4(0.133, 0.59, 0.977, 1),
 Vec4(0.895, 0.348, 0.602, 1),
 Vec4(0.977, 0.816, 0.133, 1))

BUTTONPOSITIONS = (
 (-1, 0, 0.5),
 (-.6, 0, 0.5),
 (-.2, 0, 0.5),
 (-1, 0, 0),
 (-.6, 0, 0),
 (-.2,0, 0)
 )

BUTTONPOSITIONSCLASSIC = (
 Vec3(-0.840167, 0, 0.359333),
 Vec3(0.00933349, 0, 0.306533),
 Vec3(0.862, 0, 0.3293),
 Vec3(-0.863554, 0, -0.445659),
 Vec3(0.00999999, 0, -0.5181),
 Vec3(0.864907, 0, -0.445659)
 )
# The main position
MAIN_POS = (-60, 0, 11)
MAIN_HPR = (-90, -2, 0)

# To be used when entering PAT
TOON_HALL_POS = (110, 0, 8)
TOON_HALL_HPR = (-90, 0, 0)

# To be used when going to menu
HQ_POS = (14, 16, 8)
HQ_HPR = (-48, 0, 0)

DEL = TTLocalizer.PhotoPageDelete + ' %s?'
chooser_notify = DirectNotifyGlobal.directNotify.newCategory('PickAToon')

MAX_AVATARS = 6

class PickAToon(DirectObject):

    def __init__(self, avatarList, parentFSM, doneEvent):
        DirectObject.__init__(self)
        self.toonList = {i: (i in [x.position for x in avatarList]) for i in xrange(6)}
        self.avatarList = avatarList
        self.selectedToon = 0
        self.doneEvent = doneEvent
        self.jumpIn = None
        self.background2d = OnscreenImage(image = 'phase_3.5/maps/loading/toon.jpg', parent = render2d)
        self.background2d.setScale(render2d, Vec3(1))
        self.background2d.setBin('background', 2)
        self.background2d.setTransparency(1)
        self.background2d.setColorScale(.6, .1, .1, 0)
        self.backgroundClassic = None
        # self.optionsMgr = PickAToonOptions.PickAToonOptions()
        self.optionsMgr = DMenuOptions.DMenuOptions() # This is for the revamped options screen
        self.shardPicker = ShardPicker.ShardPicker()
        self.buttonList = []
        self.quitConfirmation = DMenuQuit.DMenuQuit()
        self.isClassic = False
        self.deleteButtons = []
        self.hasToons = {}

    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    def showClassic(self):
        return
        self.isClassic = True
        self.classicButton['text'] = "Altis"
        settings['patMode'] = "Classic"
        if not self.backgroundClassic:
            classicGui = loader.loadModel('phase_3/models/gui/tt_m_gui_pat_mainGui')
            classicGui.flattenMedium()
            self.backgroundClassic = classicGui.find('**/tt_t_gui_pat_background')
            self.backgroundClassic.flattenStrong()
            self.backgroundClassic.reparentTo(aspect2d)
            self.backgroundClassic.setBin('background', 1)
            self.backgroundClassic.setScale(1, 1, 1)
            self.backgroundClassic.setTransparency(1)
        LerpColorScaleInterval(self.backgroundClassic, 1, Vec4(1, 1, 1, 1), startColorScale = Vec4(1, 1, 1, 0), blendType = 'easeInOut').start()
        for button in self.buttonList:
            position = BUTTONPOSITIONSCLASSIC[button['extraArgs'][0]]
            if self.hasToons.get(button['extraArgs'][0]) == True:
                button['command'] = self.selectToonClassic
            else:
                button['command'] = self.makeToonClassic

            button.posHprScaleInterval(1, position, Vec3(0, 0, 0), Vec3(1.01, 1.01, 1.01), blendType = 'easeInOut').start()
        self.play.hide()

    def hideClassic(self):
        self.isClassic = False
        self.classicButton['text'] = "Classic"
        settings['patMode'] = "Altis"
        for button in self.buttonList:
            position = BUTTONPOSITIONS[button['extraArgs'][0]]
            button.posHprScaleInterval(1, position, Vec3(0, 0, 0), Vec3(0.5, 0.5, 0.5), blendType = 'easeInOut').start()
            button['command'] = self.selectToon
        self.play.show()
        if self.backgroundClassic:
            LerpColorScaleInterval(self.backgroundClassic, 1, Vec4(1, 1, 1, 0), startColorScale = Vec4(1, 1, 1, 1), blendType = 'easeInOut').start()

    def enter(self):
        base.disableMouse()
        if base.showDisclaimer:
            settings['show-disclaimer'] = False
        self.title.reparentTo(aspect2d)
        self.quitButton.show()
        self.patNode.unstash()
        self.checkPlayButton()
        self.updateFunc()
        self.accept('doQuitGame', self.doQuitFunc)
        self.accept('doCancelQuitGame', self.doCancelQuitFunc)

    def exit(self):
        base.cam.iPosHpr()
        self.title.reparentTo(hidden)
        self.quitButton.hide()
        if self.backgroundClassic:
            self.backgroundClassic.removeNode()
            self.backgroundClassic = None

    def load(self):
        try:
            self.patNode = render.attachNewNode('patNode')
            self.patNode2d = aspect2d.attachNewNode('patNode2d')
            self.patNode.setTransparency(1)
            self.patNode2d.setTransparency(1)
            self.patNode.setColorScale(1, 1, 1, 0)
            self.patNode2d.setColorScale(1, 1, 1, 0)
            gui = base.patgui
            gui2 = base.gui2
            newGui = base.newGui
            matGui = base.matGui
            shuffleUp = base.shuffleUp
            shuffleDown = base.shuffleDown

            self.title = OnscreenText(TTLocalizer.AvatarChooserPickAToon, font = ToontownGlobals.getSignFont(), scale = TTLocalizer.ACtitle, parent = hidden, fg = (1, 0.9, 0.1, 1), pos = (0.0, 0.82))

            # Quit Button
            quitHover = gui.find('**/QuitBtn_RLVR')
            self.quitHover = quitHover
            self.quitButton = DirectButton(image = (shuffleUp, shuffleDown, shuffleUp), relief = None, image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.73, 0.73), image2_scale = (0.83, 0.73, 0.73), text = TTLocalizer.AvatarChooserQuit, text_font = ToontownGlobals.getSignFont(), text_fg = (0.977, 0.816, 0.133, 1), text_pos = (0, -0.02), text_scale = 0.06, scale = 1, pos = (1.08, 0, -0.907), command = self.quitGame)
            self.quitButton.reparentTo(base.a2dBottomLeft)
            self.quitButton.setPos(0.25, 0, 0.075)

            # Options Button
            self.optionsButton = DirectButton(image = (shuffleUp, shuffleDown, shuffleUp), relief = None, image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.73, 0.73), image2_scale = (0.83, 0.73, 0.73), text = 'Options', text_font = ToontownGlobals.getSignFont(), text_fg = (0.977, 0.816, 0.133, 1), text_pos = (0, -0.02), text_scale = 0.06, scale = 1, pos = (1.08, 0, -0.907), command = self.openOptions)
            self.optionsButton.reparentTo(base.a2dBottomRight)
            self.optionsButton.setPos(-0.25, 0, 0.075)

            # Shard Selector Button
            self.shardsButton = DirectButton(image = (shuffleUp, shuffleDown, shuffleUp), relief = None, image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.73, 0.73), image2_scale = (0.83, 0.73, 0.73), text = 'Districts', text_font = ToontownGlobals.getSignFont(), text_fg = (0.977, 0.816, 0.133, 1), text_pos = (0, -0.02), text_scale = 0.06, scale = 1, pos = (1.08, 0, -0.907), command = self.openShardPicker)
            self.shardsButton.reparentTo(base.a2dBottomLeft)
            self.shardsButton.setPos(0.25, 0, 0.2)

            # Area toon is in
            self.area = OnscreenText(parent = self.patNode2d, font = ToontownGlobals.getToonFont(),
                                     pos = (-.1, -.1), scale = .075, text = '', shadow = (0, 0, 0, 1), fg = COLORS[self.selectedToon])

            # DMENU Pat Screen Stuff
            self.play = DirectButton(relief = None, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.73, 0.73), image2_scale = (0.83, 0.73, 0.73), text = 'PLAY THIS TOON', text_font = ToontownGlobals.getSignFont(), text_fg = (0.977, 0.816, 0.133, 1), text_pos = (0, -.016), text_scale = 0.035, scale = 1.4, pos = (0, 0, -0.90), command = self.playGame, parent = self.patNode2d)

            self.toon = Toon.Toon()
            self.toon.setPosHpr(Vec3(5, 0, 0), Vec3(150, 0, 0))
            self.toon.reparentTo(base.cr.DMENU_SCREEN.background)
            self.toon.stopLookAroundNow()

            self.pickAToonGui = newGui
            self.buttonBgs = []
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareRed'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareGreen'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squarePurple'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareBlue'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squarePink'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareYellow'))
            buttonIndex = []
            for av in self.avatarList:
                self.setupButtons(av, position = av.position)
                buttonIndex.append(av.position)

            for pos in xrange(0, 6):
                if pos not in buttonIndex:
                    button = self.setupButtons(position = pos)

            base.graphicsEngine.renderFrame()
            self.changeName = DirectButton(relief = None, image = (quitHover, quitHover, quitHover), text = 'NAME THIS TOON', text_font = ToontownGlobals.getSignFont(), text_fg = (0.977, 0.816, 0.133, 1), text_pos = (0, -.016), text_scale = 0.045, image_scale = 1, image1_scale = 1.05, image2_scale = 1.05, scale = 1.4, pos = (0, 0, -0.75), command = self.__handleNameYourToon, parent = self.patNode2d)

            LerpColorScaleInterval(self.patNode, .5, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0)).start()
            LerpColorScaleInterval(self.patNode2d, .5, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0)).start()
        except:
            pass

    def toggleClassic(self):
        if self.isClassic:
            self.hideClassic()
        else:
            self.showClassic()

    def selectToon(self, slot):
        self.selectedToon = slot
        self.updateFunc()

    def selectToonClassic(self, slot):
        self.selectedToon = slot
        doneStatus = {'mode': 'chose', 'choice': slot}
        messenger.send(self.doneEvent, [doneStatus])

    def updateFunc(self):
        self.haveToon = self.toonList[self.selectedToon]
        self.area['fg'] = COLORS[self.selectedToon]
        if self.jumpIn:
            self.jumpIn.finish()
        if hasattr(self, 'laffMeter'):
            self.laffMeter.destroy()
            del self.laffMeter
        if self.haveToon:
            self.showToon()
            camZ = self.toon.getHeight()    
        else:
            self.changeName.hide()
            self.toon.hide()

        self.checkPlayButton()
        self.area['text'] = ''

    def showToon(self):
        try:
            av = [x for x in self.avatarList if x.position == self.selectedToon][0]
            dna = av.dna
            if av.allowedName == 1:
                self.toon.setName(av.name + '\n\1textShadow\1NAME REJECTED!\2')
                self.changeName.show()
            elif av.wantName != '':
                self.toon.setName(av.name + '\n\1textShadow\1NAME PENDING!\2')
                self.changeName.hide()
            else:
                self.toon.setName(av.name)
                self.changeName.hide()
            self.toon.setDNAString(dna)
            self.laffMeter = LaffMeter.LaffMeter(ToonDNA.ToonDNA(dna), av.hp, av.maxHp)
            self.laffMeter.set_pos(-.6, 0, -.5)
            self.laffMeter.reparent_to(self.patNode2d)
            self.laffMeter.start()
            self.toon.setHat(av.hat[0], av.hat[1], av.hat[2])
            self.toon.setGlasses(av.glasses[0], av.glasses[1], av.glasses[2])
            self.toon.setBackpack(av.backpack[0], av.backpack[1], av.backpack[2])
            self.toon.setShoes(av.shoes[0], av.shoes[1], av.shoes[2])
            self.jumpIn = Sequence(
                    Func(self.toon.loop, 'wave'),
                    Wait(self.toon.getDuration('wave')),
                    Func(self.toon.animFSM.request, 'neutral'))
            self.jumpIn.start() # ALTIS: TODO: Add the states to Toon.py
            self.toon.animFSM.request('neutral')
            self.toon.show()
        except:
            pass


    def checkPlayButton(self):
        if self.toonList[self.selectedToon]:
            self.play['text'] = 'PLAY THIS TOON'
            self.play['command'] = self.playGame
        else:
            self.play['text'] = 'MAKE A TOON'
            self.play['command'] = self.makeToon

    def playGame(self):
        if self.jumpIn:
            self.jumpIn.finish()
        doneStatus = {'mode': 'chose', 'choice': self.selectedToon}
        # Sequence (
        #          Func(self.toon.animFSM.request, 'PATTeleportOut'),
        #          Wait(4),
        #          Func(messenger.send, self.doneEvent, [doneStatus]))#.start() # ALTIS: TODO: Add the states to toon.py
        messenger.send(self.doneEvent, [doneStatus])

    def makeToon(self, position = None):
        doneStatus = {'mode': 'create', 'choice': self.selectedToon}
        messenger.send(self.doneEvent, [doneStatus])

    def makeToonClassic(self, position):
        self.selectToon(position)
        doneStatus = {'mode': 'create', 'choice': self.selectedToon}
        messenger.send(self.doneEvent, [doneStatus])

    def setupButtons(self, av = None, position = 0):
        deleteButton = None
        button = DirectButton(text = ('', '', ''), text_scale = TTLocalizer.ACplayThisToon, text_fg = (1, 0.9, 0.1, 1), relief = None, text_font = ToontownGlobals.getSignFont(), command = self.selectToon, extraArgs = [position], image = self.buttonBgs[position])
        button.reparentTo(self.patNode2d)
        button.setPos(BUTTONPOSITIONS[position])
        button.setScale(.5)
        # Delete Toon button
        trashcanGui = loader.loadModel('phase_3/models/gui/trashcan_gui.bam')
        if av:
            self.hasToons[position] = True
            headmod = ToonHead.ToonHead()
            headmod.setupHead(ToonDNA.ToonDNA(av.dna), forGui = 1)
            headmod.setPosHprScale(0, -0.5, -0.1, 180, 0, 0, 0.24, 0.24, 0.24)
            headmod.startBlink()
            headmod.startLookAround()
            button['text_pos'] = (0, 0, 2)
            headmod.reparentTo(button)
            deleteButton = DirectButton(parent = button,
                                 geom = (trashcanGui.find('**/TrashCan_CLSD'),
                                       trashcanGui.find('**/TrashCan_OPEN'),
                                       trashcanGui.find('**/TrashCan_RLVR')),
                                 text = ('', TTLocalizer.AvatarChoiceDelete,
                                           TTLocalizer.AvatarChoiceDelete, ''),
                                 text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1),
                                 text_scale = 0.15, text_pos = (0, -0.1), relief = None,
                                 scale = .5, command = self.__handleDelete, extraArgs = [position], pos = (.2, 0, -.2))
        else:
            button['text'] = (TTLocalizer.AvatarChoiceMakeAToon,)
            self.hasToons[position] = False
        self.buttonList.append(button)
        if deleteButton:
            self.deleteButtons.append(deleteButton)

    def unload(self):
        cleanupDialog('globalDialog')
        self.ignoreAll()
        self.background2d.removeNode()
        del self.background2d
        self.patNode.removeNode()
        del self.patNode
        self.patNode2d.removeNode()
        del self.patNode2d
        self.title.removeNode()
        del self.title
        self.quitButton.destroy()
        del self.quitButton
        self.optionsButton.destroy()
        del self.optionsButton
        self.shardsButton.destroy()
        del self.shardsButton
        self.shardPicker.unload()
        del self.avatarList
        self.toon.removeNode()
        del self.toon
        self.hasToons = {}
        for button in self.deleteButtons:
            button.destroy()
            del button
        base.cr.DMENU_SCREEN.murder()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)

    def getChoice(self):
        return self.selectedToon

    def __handleDelete(self, position):
        self.selectToon(position)
        av = [x for x in self.avatarList if x.position == position][0]

        def dodelete(itreallywantstohaveanargumentheresoletsjustputonethatwontbeusedatall = None):
            if self.passwordEntry.get().lower() == TTLocalizer.AvatarChoiceDeleteConfirmUserTypes:
                self.deleteWithPasswordFrame.destroy()
                delDialog.cleanup()
                base.transitions.noFade()
                messenger.send(self.doneEvent, [{'mode': 'delete'}])
            else:
                self.passwordEntry.enterText('')
                
        def cancel():
            self.deleteWithPasswordFrame.destroy()
            delDialog.cleanup()
            base.transitions.noFade()
        
        def diagDone():
            mode = delDialog.doneStatus
            if mode == 'ok':
                buttons = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
                buttons.flattenMedium()
                nameBalloon = loader.loadModel('phase_3/models/props/chatbox_input')
                nameBalloon.flattenMedium()
                okButtonImage = (buttons.find('**/ChtBx_OKBtn_UP'), buttons.find('**/ChtBx_OKBtn_DN'), buttons.find('**/ChtBx_OKBtn_Rllvr'))
                cancelButtonImage = (buttons.find('**/CloseBtn_UP'), buttons.find('**/CloseBtn_DN'), buttons.find('**/CloseBtn_Rllvr'))
                deleteText = TTLocalizer.AvatarChoiceDeleteConfirmText % {
                'name': av.name,
                'confirm': TTLocalizer.AvatarChoiceDeleteConfirmUserTypes}
                self.deleteWithPasswordFrame = DirectFrame(pos=(0.0, 0.1, 0.2), parent=aspect2dp, relief=None, image=DGG.getDefaultDialogGeom(), image_color=ToontownGlobals.GlobalDialogColor, image_scale=(1.4, 1.0, 1.0), text=deleteText, text_wordwrap=19, text_scale=TTLocalizer.ACdeleteWithPasswordFrame, text_pos=(0, 0.25), textMayChange=1, sortOrder=NO_FADE_SORT_INDEX)
                self.passwordEntry = DirectEntry(parent=self.deleteWithPasswordFrame, relief=None, image=nameBalloon, image1_color=(0.8, 0.8, 0.8, 1.0), scale=0.064, pos=(-0.3, 0.0, -0.2), width=10, numLines=1, focus=1, cursorKeys=1, command=dodelete)
                self.passwordEntry.flattenMedium()
                DirectButton(parent=self.deleteWithPasswordFrame, image=okButtonImage, relief=None, text=TTLocalizer.AvatarChoiceDeletePasswordOK, text_scale=0.05, text_pos=(0.0, -0.1), textMayChange=0, pos=(-0.22, 0.0, -0.35), command=dodelete)
                DirectButton(parent=self.deleteWithPasswordFrame, image=cancelButtonImage, relief=None, text=TTLocalizer.AvatarChoiceDeletePasswordCancel, text_scale=0.05, text_pos=(0.0, -0.1), textMayChange=1, pos=(0.2, 0.0, -0.35), command=cancel)
            else:
                delDialog.cleanup()
                base.transitions.noFade()
                
        base.acceptOnce('pat-del-diag-done', diagDone)
        delDialog = TTGlobalDialog(message = DEL % av.name, style = YesNo,
                                   doneEvent = 'pat-del-diag-done')

        base.transitions.fadeScreen(.5)

    def __handleNameYourToon(self):
        doneStatus = {"mode": "nameIt", "choice": self.selectedToon}
        messenger.send(self.doneEvent, [doneStatus])

    def __handleQuit(self):
        messenger.send('showQuitDialog')

    def openOptions(self):
        self.optionsMgr.showOptions()
        self.optionsButton.reparent_to(self.optionsMgr.optionsNode)
        self.optionsButton.setPos(0, 1, -.75)
        self.optionsButton['text'] = 'Back'
        self.optionsButton['command'] = self.hideOptions
        self.shardsButton.hide()
        self.patNode2d.hide()
        self.patNode.hide()

    def hideOptions(self):
        self.optionsMgr.hideOptions()
        self.optionsButton.wrt_reparent_to(base.a2dBottomRight)
        self.optionsButton.setPos(-0.25, 0, 0.075)
        self.optionsButton['text'] = 'Options'
        self.optionsButton['command'] = self.openOptions
        self.shardsButton.show()
        self.patNode2d.show()
        self.patNode.show()

    def openShardPicker(self):
        self.shardPicker.showPicker()
        self.shardsButton['text'] = 'Back'
        self.shardsButton['command'] = self.hideShardPicker
        for button in self.buttonList:
            button.hide()
        if hasattr(self, 'laffMeter'):
            self.laffMeter.hide()

    def hideShardPicker(self):
        self.shardPicker.hidePicker()
        self.shardsButton['text'] = 'Districts'
        self.shardsButton['command'] = self.openShardPicker
        for button in self.buttonList:
            button.show()
        if hasattr(self, 'laffMeter'):
            self.laffMeter.show()

    def quitGame(self):
        self.showQuitConfirmation()
        self.optionsButton.hide()
        self.shardsButton.hide()
        self.quitButton.hide()
        LerpColorScaleInterval(self.patNode, .5, Vec4(1, 1, 1, 0), Vec4(1, 1, 1, 1)).start()
        LerpColorScaleInterval(self.patNode2d, .5, Vec4(1, 1, 1, 0), Vec4(1, 1, 1, 1)).start()

    def showQuitConfirmation(self):
        LerpColorScaleInterval(self.background2d, .5, Vec4(.6, .1, .1, .5), startColorScale = Vec4(.6, .1, .1, 0)).start()
        self.quitConfirmation.showConf()

    def doQuitFunc(self):
        base.exitFunc()

    def doCancelQuitFunc(self):
        LerpColorScaleInterval(self.background2d, .5, Vec4(.6, .1, .1, 0), startColorScale = Vec4(.6, .1, .1, .5)).start()
        self.quitConfirmation.hideConf()
        self.optionsButton.show()
        self.shardsButton.show()
        self.quitButton.show()
        LerpColorScaleInterval(self.patNode, .5, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0)).start()
        LerpColorScaleInterval(self.patNode2d, .5, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0)).start()
