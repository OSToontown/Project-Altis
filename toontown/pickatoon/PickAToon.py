'''
Created on Sep 12, 2016

@author: Drew
'''

from direct.actor import Actor
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM, State
from direct.fsm import State
from direct.fsm import StateData
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import *
from direct.task import Task
from panda3d.core import *
import random

from toontown.hood import SkyUtil
from toontown.launcher import DownloadForceAcknowledge
from toontown.toon import ToonDNA, Toon, ToonHead
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toontowngui import TTDialog
from toontown.toontowngui.TTGui import btnDn, btnRlvr, btnUp
from toontown.toontowngui.TTDialog import *
import PickAToonOptions
from toontown.pickatoon import ShardPicker
from toontown.toontowngui import FeatureComingSoonDialog

COLORS = (Vec4(0.917, 0.164, 0.164, 1),
 Vec4(0.152, 0.75, 0.258, 1),
 Vec4(0.598, 0.402, 0.875, 1),
 Vec4(0.133, 0.59, 0.977, 1),
 Vec4(0.895, 0.348, 0.602, 1),
 Vec4(0.977, 0.816, 0.133, 1))
 
BUTTONPOSITIONS = ((-1, 0, 0.5),
            (-.6, 0, 0.5),
            (-.2, 0, 0.5),
            (.2, 0, 0.5),
            (0.6, 0, 0.5),
            (1, 0, 0.5))
 
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

class PickAToon:
    
    def __init__(self, avatarList, parentFSM, doneEvent):
        self.toonList = {i: (i in [x.position for x in avatarList]) for i in xrange(6)}
        self.avatarList = avatarList
        self.selectedToon = 0
        self.doneEvent = doneEvent
        self.jumpIn = None
        if base.showDisclaimer:
            FeatureComingSoonDialog.FeatureComingSoonDialog(text="\1textShadow\1Disclaimer:\2\nThis is an ALPHA build of Project Altis! There may be many bugs and crashes! If you encounter any, PLEASE report them to the developers!\nThanks, and enjoy Project Altis!")
        #self.optionsMgr = PickAToonOptions.PickAToonOptions()
        self.optionsMgr = PickAToonOptions.NewPickAToonOptions() # This is for the revamped options screen
        self.shardPicker = ShardPicker.ShardPicker()
        self.buttonList = []
        return

    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)
        
    def enter(self):
        base.disableMouse()
        if base.showDisclaimer:
            settings['show-disclaimer'] = False
        self.title.reparentTo(aspect2d)
        self.quitButton.show()
        self.deleteButton.show()
        self.patNode.unstash()
        self.checkPlayButton()
        self.updateFunc()
                
    def exit(self):
        base.cam.iPosHpr()
        self.title.reparentTo(hidden)
        self.quitButton.hide()
        self.deleteButton.hide()
        return None

    def load(self):
        self.patNode = render.attachNewNode('patNode')
        self.patNode2d = aspect2d.attachNewNode('patNode2d')
        gui = asyncloader.loadModel('phase_3/models/gui/pick_a_toon_gui')
        gui2 = asyncloader.loadModel('phase_3/models/gui/quit_button')
        newGui = asyncloader.loadModel('phase_3/models/gui/tt_m_gui_pat_mainGui')
        

        self.title = OnscreenText(TTLocalizer.AvatarChooserPickAToon, scale=TTLocalizer.ACtitle, parent=hidden, fg=(1, 0.9, 0.1, 1), pos=(0.0, 0.82))

        # Quit Button
        quitHover = gui.find('**/QuitBtn_RLVR')
        self.quitHover = quitHover
        self.quitButton = DirectButton(image=(quitHover, quitHover, quitHover), relief=None, text=TTLocalizer.AvatarChooserQuit, text_font=ToontownGlobals.getSignFont(), text_fg=(0.977, 0.816, 0.133, 1), text_pos=TTLocalizer.ACquitButtonPos, text_scale=TTLocalizer.ACquitButton, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.05, pos=(1.08, 0, -0.907), command=self.__handleQuit)
        self.quitButton.reparentTo(base.a2dBottomLeft)
        self.quitButton.setPos(0.25, 0, 0.075)
        
        # Options Button
        self.optionsButton = DirectButton(image=(quitHover, quitHover, quitHover), relief=None, text="Options", text_font=ToontownGlobals.getSignFont(), text_fg=(0.977, 0.816, 0.133, 1), text_pos=TTLocalizer.ACquitButtonPos, text_scale=TTLocalizer.ACquitButton, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.05, pos=(1.08, 0, -0.907), command=self.openOptions)
        self.optionsButton.reparentTo(base.a2dBottomRight)
        self.optionsButton.setPos(-0.25, 0, 0.075)
        
        # Shard Selector Button
        self.shardsButton = DirectButton(image=(quitHover, quitHover, quitHover), relief=None, text="Districts", text_font=ToontownGlobals.getSignFont(), text_fg=(0.977, 0.816, 0.133, 1), text_pos=TTLocalizer.ACquitButtonPos, text_scale=0.08, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.05, pos=(1.08, 0, -0.907), command=self.openShardPicker)
        self.shardsButton.reparentTo(base.a2dBottomLeft)
        self.shardsButton.setPos(0.25, 0, 0.2)
        
        gui.removeNode()
        gui2.removeNode()
        newGui.removeNode()

        # Area toon is in
        self.area = OnscreenText(parent=self.patNode2d, font=ToontownGlobals.getToonFont(),
                                 pos=(-.1, -.1), scale=.075, text='', shadow=(0, 0, 0, 1), fg=COLORS[self.selectedToon])

        # DMENU Pat Screen Stuff
        self.play = DirectButton(relief = None, image = (quitHover, quitHover, quitHover), text = 'PLAY THIS TOON', text_font=ToontownGlobals.getSignFont(), text_fg=(0.977, 0.816, 0.133, 1), text_pos=(0, -.016), text_scale = 0.045, image_scale=1, image1_scale=1.05, image2_scale=1.05, scale=1.4, pos=(0, 0, -0.90), command=self.playGame, parent=self.patNode2d)
        
        self.toon = Toon.Toon()
        self.toon.setPosHpr(-46, 0, 8.1, 90, 0, 0)
        self.toon.reparentTo(self.patNode)
        self.toon.stopLookAroundNow()
        
        def spawnToonButtons(*args):
            self.pickAToonGui = args[0]
            self.buttonBgs = []
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareRed'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareGreen'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squarePurple'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareBlue'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squarePink'))
            self.buttonBgs.append(self.pickAToonGui.find('**/tt_t_gui_pat_squareYellow'))
            buttonIndex = []
            for av in self.avatarList:
                self.setupButtons(av, position=av.position)
                buttonIndex.append(av.position)
                
            for pos in xrange(0, 6):
                if pos not in buttonIndex:
                    button = self.setupButtons(position=pos)
            
        asyncloader.loadModel('phase_3/models/gui/tt_m_gui_pat_mainGui', callback = spawnToonButtons)

        # Delete Toon button
        trashcanGui = loader.loadModel('phase_3/models/gui/trashcan_gui.bam')
        self.deleteButton = DirectButton(parent=base.a2dBottomRight,
                                         geom=(trashcanGui.find('**/TrashCan_CLSD'),
                                               trashcanGui.find('**/TrashCan_OPEN'),
                                               trashcanGui.find('**/TrashCan_RLVR')),
                                         text=('', TTLocalizer.AvatarChoiceDelete,
                                                   TTLocalizer.AvatarChoiceDelete, ''),
                                         text_fg=(1, 1, 1, 1), text_shadow=(0, 0, 0, 1),
                                         text_scale=0.15, text_pos=(0, -0.1), relief=None,
                                         scale=.5, command=self.__handleDelete, pos=(-.2, 0, .25))

    def selectToon(self, slot):
        self.selectedToon = slot
        self.updateFunc()
        
    def updateFunc(self):
        self.haveToon = self.toonList[self.selectedToon]
        self.area['fg'] = COLORS[self.selectedToon]
        if self.jumpIn:
            self.jumpIn.finish()
        if self.haveToon:
            self.showToon()
            taskMgr.add(self.turnHead, "turnHead")
            camZ = self.toon.getHeight()
            base.camera.setPos(-60, 0, 8 + camZ)
            self.deleteButton.show()
        else:
            self.toon.hide()
            base.camera.setPos(-60, 0, 11)
            taskMgr.remove("turnHead")
            self.deleteButton.hide()
        self.checkPlayButton()
        self.area['text'] = ''
            
    def showToon(self):
        av = [x for x in self.avatarList if x.position == self.selectedToon][0]
        dna = av.dna
        
        self.toon.setDNAString(dna)
        #self.jumpIn = Sequence(
        #         Func(self.toon.animFSM.request, 'PATTeleportIn'),
        #         Wait(2),
        #         Func(self.toon.animFSM.request, 'neutral'))
        #self.jumpIn.start() # ALTIS: TODO: Add the states to Toon.py
        self.toon.animFSM.request('neutral')
        self.toon.setName(av.name)
        self.toon.show()
        lastAreaName = ToontownGlobals.hoodNameMap.get(av.lastHood, [''])[-1]
        self.area.setText(lastAreaName)

    def turnHead(self, task):
        def clamprotation(i, mn = -1, mx = 1):
            return min(max(i, mn), mx)
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            self.toon.getGeomNode().find('**/__Actor_head').setP(clamprotation(mpos.getY()) * 25)
            self.toon.getGeomNode().find('**/__Actor_head').setH(clamprotation(mpos.getX()) * 40)

        return Task.cont
        
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
        doneStatus = {"mode": "chose", "choice": self.selectedToon}
        #Sequence (
        #          Func(self.toon.animFSM.request, 'PATTeleportOut'),
        #          Wait(4),
        #          Func(messenger.send, self.doneEvent, [doneStatus]))#.start() # ALTIS: TODO: Add the states to toon.py
        messenger.send(self.doneEvent, [doneStatus])

    def makeToon(self):
        doneStatus = {"mode": "create", "choice": self.selectedToon}
        messenger.send(self.doneEvent, [doneStatus])
                
    def setupButtons(self, av = None, position = 0):
        button = DirectButton(text = ' ', relief = None, command=self.selectToon, extraArgs = [position], image = self.buttonBgs[position])
        button.reparentTo(self.patNode2d)
        button.setPos(BUTTONPOSITIONS[position])
        button.setScale(.5)
        
        if av:
            head = hidden.attachNewNode('head')
            head.setPosHprScale(0, 5, -0.1, 180, 0, 0, 0.24, 0.24, 0.24)
            head.reparentTo(button)
            headmod = ToonHead.ToonHead()
            headmod.setupHead(ToonDNA.ToonDNA(av.dna), forGui=1)
            headmod.reparentTo(head)
        self.buttonList.append(button)

    def unload(self):
        taskMgr.remove("turnHead")
        cleanupDialog('globalDialog')
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
        base.cr.DMENU_SCREEN.murder()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        base.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        return None

    def getChoice(self):
        return self.selectedToon

    def __handleDelete(self):
        av = [x for x in self.avatarList if x.position == self.selectedToon][0]

        def diagDone():
            mode = delDialog.doneStatus
            delDialog.cleanup()
            base.transitions.noFade()
            if mode == 'ok':
                messenger.send(self.doneEvent, [{'mode': 'delete'}])
        
        base.acceptOnce('pat-del-diag-done', diagDone)
        delDialog = TTGlobalDialog(message=DEL % av.name, style=YesNo,
                                   doneEvent='pat-del-diag-done')
        base.transitions.fadeScreen(.5)

    def __handleQuit(self):
        cleanupDialog('globalDialog')
        self.doneStatus = {'mode': 'exit'}
        messenger.send(self.doneEvent, [self.doneStatus])

    def openOptions(self):
        self.optionsMgr.showOptions()
        self.optionsButton["text"] = "Back"
        self.optionsButton["command"] = self.hideOptions
        self.shardsButton.hide()
        self.patNode2d.hide()
        self.patNode.hide()
        if self.haveToon:
            self.deleteButton.hide()

    def hideOptions(self):
        self.optionsMgr.hideOptions()
        self.optionsButton["text"] = "Options"
        self.optionsButton["command"] = self.openOptions
        self.shardsButton.show()
        self.patNode2d.show()
        self.patNode.show()
        if self.haveToon:
            self.deleteButton.show()
            
    def openShardPicker(self):
        self.shardPicker.showPicker()
        self.shardsButton["text"] = "Back"
        self.shardsButton["command"] = self.hideShardPicker

    def hideShardPicker(self):
        self.shardPicker.hidePicker()
        self.shardsButton["text"] = "Districts"
        self.shardsButton["command"] = self.openShardPicker