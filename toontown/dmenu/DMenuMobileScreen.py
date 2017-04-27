# DMENU VERSION 1.0

from direct.actor import Actor
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from direct.interval.IntervalGlobal import Wait, Func, Sequence, LerpColorScaleInterval, Parallel, ActorInterval
from direct.showbase import Audio3DManager
from direct.showbase.DirectObject import DirectObject
from panda3d.core import TransparencyAttrib, Point3, VBase3, Vec4, Vec3, \
    TextNode
import random
import webbrowser

from toontown.dmenu import DMenuCredits
from toontown.dmenu import DMenuQuit
from toontown.dmenu.DMenuGlobals import *
from toontown.dmenu.DMenuResources import *
from toontown.dmenu import DMenuNewsManager
from toontown.hood import SkyUtil
from toontown.nametag.NametagGlobals import *
from toontown.nametag.NametagGroup import *
from toontown.pickatoon import PickAToonOptions, PickAToon
from toontown.toon import Toon, ToonDNA
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toontowngui import FeatureComingSoonDialog
from toontown.toontowngui.TTGui import btnDn, btnRlvr, btnUp


# The camera's initial position when first entering main menu
INIT_POS = (-62, 0, 11)
INIT_HPR = (-90, -2, 0)

# The main position
MAIN_POS = (-60, 0, 11)
MAIN_HPR = (-90, -2, 0)

# To be used when entering PAT
TOON_HALL_POS = (110, 0, 8)
TOON_HALL_HPR = (-90, 0, 0)

# To be used when going to menu
HQ_POS = (14, 16, 8)
HQ_HPR = (-48, 0, 0)

class DMenuMobileScreen(DirectObject):
    notify = directNotify.newCategory('DMenuScreen')

    def __init__(self):
        DirectObject.__init__(self)
        base.cr.DMENU_SCREEN = self
        self.seq = None
        base.cr.avChoice = None
        self.allButtons = []
        base.transitions.fadeOut(0)
        base.camera.setPosHpr(Point3(MAIN_POS), VBase3(MAIN_HPR))
        base.transitions.getFadeInIval(1).start()
        if base.showDisclaimer:
            FeatureComingSoonDialog.FeatureComingSoonDialog(text = TTLocalizer.PopupAlphaDisclaimer)
        self.background2d = OnscreenImage(image = 'phase_3.5/maps/loading/toon.jpg', parent = render2d)
        self.background2d.setScale(render2d, Vec3(1))
        self.background2d.setBin('background', 1)
        self.background2d.setTransparency(1)
        self.background2d.setColorScale(1, 1, 1, 1)
        self.background = loader.loadModel('phase_3.5/models/modules/tt_m_ara_int_toonhall')
        self.background.reparentTo(render)
        self.background.setPosHpr(-25, 0, 8.1, -95, 0, 0)

        self.surlee = Toon.Toon()
        self.surlee.setName('Doctor Surlee')
        self.surlee.setPickable(0)
        self.surlee.setPlayerType(CCNonPlayer)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties('pls', 'ls', 'l', 'm', 9, 0, 9, 9, 98, 27, 86, 27, 38, 27)
        self.surlee.setDNA(dna)
        self.surlee.loop('scientistGame')
        self.surlee.reparentTo(self.background)
        self.surlee.setPosHpr(13, 24, 0.025, -180, 0, 0)

        self.dimm = Toon.Toon()
        self.dimm.setName('Doctor Dimm')
        self.dimm.setPickable(0)
        self.dimm.setPlayerType(CCNonPlayer)
        dna = ToonDNA.ToonDNA()
        dna.newToonFromProperties('fll', 'ss', 's', 'm', 15, 0, 15, 15, 99, 27, 86, 27, 39, 27)
        self.dimm.setDNA(dna)
        self.dimm.loop('scientistGame')
        self.dimm.reparentTo(self.background)
        self.dimm.setPosHpr(16, 24, 0.025, -180, 0, 0)

        surleeHand = self.surlee.find('**/def_joint_right_hold')
        clipBoard = loader.loadModel('phase_4/models/props/tt_m_prp_acs_clipboard')
        surleeHandNode = surleeHand.attachNewNode('ClipBoard')
        clipBoard.instanceTo(surleeHandNode)
        surleeHandNode.setH(180)
        surleeHandNode.setScale(render, 1.0)
        surleeHandNode.setPos(0, 0, 0.1)

        dimmHand = self.dimm.find('**/def_joint_right_hold')
        sillyReader = loader.loadModel('phase_4/models/props/tt_m_prp_acs_sillyReader')
        dimHandNode = dimmHand.attachNewNode('SillyReader')
        sillyReader.instanceTo(dimHandNode)
        dimHandNode.setH(180)
        dimHandNode.setScale(render, 1.0)
        dimHandNode.setPos(0, 0, 0.1)

        self.sky = loader.loadModel('phase_3.5/models/props/TT_sky')
        SkyUtil.startCloudSky(self)
        base.camera.setPosHpr(MAIN_POS, MAIN_HPR)

        self.logo = OnscreenImage(image = GameLogo, scale = (.5, .5, .25))
        self.logo.reparentTo(aspect2d)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        self.logo.setPos(0, 0, .6)
        self.logo.setColorScale(Vec4(0, 0, 0, 0))
        fadeInLogo = (LerpColorScaleInterval(self.logo, 1, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0))).start()
        self.releaseNotesBox = None
        self.releaseNotesText = None
        self.createButtons()

        self.fadeOut = None
        self.optionsMgr = PickAToonOptions.NewPickAToonOptions()
        self.quitConfirmation = DMenuQuit.DMenuQuit()
        self.newsMgr = DMenuNewsManager.DMenuNewsManager()

        self.accept('doQuitGame', self.doQuitFunc)
        self.accept('doCancelQuitGame', self.doCancelQuitFunc)
        self.patNode = None

        # TT: We need these to run the Pick A Toon screen
        self.patAvList = base.cr.PAT_AVLIST
        self.patFSM = base.cr.PAT_LOGINFSM
        self.patDoneEvent = base.cr.PAT_DONEEVENT

    def enterReleaseNotes(self):
        if not self.releaseNotesBox:
            # Release Notes Box
            self.releaseNotesBox = OnscreenImage(image = 'phase_3/maps/stat_board.png')
            self.releaseNotesBox.set_transparency(TransparencyAttrib.MAlpha)
            self.releaseNotesBox.reparent_to(render2d)
            self.releaseNotesBox.set_pos(0, 0, 0)
            self.releaseNotesBox.set_scale(render2d, VBase3(1))

            # Release Notes Text
            self.releaseNotesText = OnscreenText(text = 'Fetching Release Notes...', align = TextNode.ALeft, scale = .05, wordwrap = 50)
            self.releaseNotesText.reparent_to(base.a2dTopLeft)
            self.releaseNotesText.set_pos(.4, 0, -.4)
            callAsync(self.getReleaseNotes).start()

        for button in self.allButtons:
            button.hide()
        self.logo.hide()
        self.releaseNotesBox.show()
        self.releaseNotesText.show()
        if not hasattr(self, 'closeReleaseNotesButton'):
            self.closeReleaseNotesButton = DirectButton(relief = None, image = (btnUp, btnDn, btnRlvr), text = 'Back', text_font = ToontownGlobals.getSignFont(), text_fg = (0.977, 0.816, 0.133, 1), text_scale = TTLocalizer.AClogoutButton, text_pos = (0, -0.035), image_scale = 1, image1_scale = 1.05, image2_scale = 1.05, scale = 0.7, command = self.exitReleaseNotes)
        self.closeReleaseNotesButton.reparent_to(aspect2d)
        self.closeReleaseNotesButton.setPos(0, 1, -.75)
        self.closeReleaseNotesButton.show()

    def getReleaseNotes(self):
        # TODO: Make this threaded so it doesnt freeze
        releaseNotes = self.newsMgr.fetchReleaseNotes()
        self.releaseNotesText['text'] = 'Release Notes:\n' + self.newsMgr.fetchReleaseNotes()
        
    def exitReleaseNotes(self):
        self.releaseNotesBox.hide()
        self.releaseNotesText.hide()
        self.closeReleaseNotesButton.hide()
        for button in self.allButtons:
            button.show()
        self.logo.show()


    def skyTrack(self, task):
        return SkyUtil.cloudSkyTrack(task)

    def createButtons(self):
        buttonImage = GuiModel.find('**/QuitBtn_RLVR')
        gui = base.matGui
        shuffleUp = gui.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = gui.find('**/tt_t_gui_mat_shuffleDown')

        mPlay = 'phase_3/maps/dmenu/dm_play.png'
        mOptions = 'phase_3/maps/dmenu/dm_settings.png'
        mQuit = 'phase_3/maps/dmenu/dm_quit.png'

        self.PlayButton = DirectButton(relief = None, text_style = 3, image = mPlay, image_scale = (.35), image1_scale = (.34), image2_scale = (.36), text_fg = (1, 1, 1, 1), text_pos = (0, -0.02), text_scale = .07, scale = 1.2, command = self.playGame)
        self.PlayButton.reparentTo(aspect2d)
        self.PlayButton.setPos(MPlayBtnPos)
        self.PlayButton.setTransparency(1)
        self.PlayButton.show()

        self.OptionsButton = DirectButton(relief = None, text_style = 3, image = mOptions, image_scale = (.3), image1_scale = (.29), image2_scale = (.31), text_fg = (1, 1, 1, 1), text_pos = (0, -0.02), text_scale = .08, scale = 0.95, command = self.openOptions)
        self.OptionsButton.reparentTo(base.a2dBottomLeft)
        self.OptionsButton.setPos(MOptionsBtnPos)
        self.OptionsButton.setTransparency(1)
        self.OptionsButton.show()

        self.QuitButton = DirectButton(relief = None, text_style = 3, image = mQuit, image_scale = (.3), image1_scale = (.29), image2_scale = (.31), text_fg = (1, 1, 1, 1), text_pos = (0, -0.02), text_scale = .08, scale = 0.95, command = self.quitGame)
        self.QuitButton.reparentTo(base.a2dBottomRight)
        self.QuitButton.setPos(MQuitBtnPos)
        self.QuitButton.setTransparency(1)
        self.QuitButton.show()

        self.CreditsButton = DirectButton(relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = "Credits", text_pos = (0, -0.02), text_scale = .07, scale = 0.95, command = self.startCredits)
        self.CreditsButton.reparentTo(base.a2dTopRight)
        self.CreditsButton.setPos(MCreditsBtnPos)
        self.CreditsButton.show()

        self.NewsButton = DirectButton(relief = None, text_style = 3, image = (shuffleUp, shuffleDown, shuffleUp), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = TTLocalizer.DiscordButton, text_pos = (0, -0.02), text_scale = .07, scale = 0.95, command = self.enterReleaseNotes)
        self.NewsButton.reparentTo(base.a2dTopLeft)
        self.NewsButton.setPos(MDiscordBtnPos)
        self.NewsButton.show()

        self.allButtons.append(self.PlayButton)
        self.allButtons.append(self.OptionsButton)
        self.allButtons.append(self.QuitButton)
        self.allButtons.append(self.CreditsButton)
        self.allButtons.append(self.NewsButton)

    def murder(self):
        if self.logo is not None:
            self.logo.destroy()
            self.logo = None

        if self.background is not None:
            self.background.hide()
            self.background.reparentTo(hidden)
            self.background.removeNode()
            self.background = None

        if self.background2d:
            self.background2d.reparentTo(hidden)
            self.background2d.removeNode()
            self.background2d = None

        if self.PlayButton is not None:
            self.PlayButton.destroy()
            self.PlayButton = None

        if self.OptionsButton is not None:
            self.OptionsButton.destroy()
            self.OptionsButton = None

        if self.QuitButton is not None:
            self.QuitButton.destroy()
            self.QuitButton = None

        if self.NewsButton:
            self.NewsButton.destroy()
            self.NewsButton = None

        if self.CreditsButton:
            self.CreditsButton.destroy()
            self.CreditsButton = None
            
        if self.surlee:
            self.surlee.delete()
        if self.dimm:
            self.dimm.delete()

        if self.releaseNotesBox:
            self.releaseNotesBox.remove_node()
            self.releaseNotesText.destroy()
            self.releaseNotesBox = None
            self.releaseNotesText = None

        self.ignoreAll()

        taskMgr.remove('skyTrack')
        self.sky.reparentTo(hidden)

    def openOptions(self):
        self.optionsMgr.showOptions(False)
        if not hasattr(self, 'closeOptionsButton'):
            self.closeOptionsButton = DirectButton(relief = None, image = (btnUp, btnDn, btnRlvr), text = 'Back', text_fg = (0, 0, 0, 1), text_scale = TTLocalizer.AClogoutButton, text_pos = (0, -0.035), image_scale = 1, image1_scale = 1.05, image2_scale = 1.05, scale = 0.7, command = self.hideOptions)
        self.closeOptionsButton.reparent_to(self.optionsMgr.optionsNode)
        self.closeOptionsButton.setPos(0, 1, -.75)
        self.closeOptionsButton.show()
        for button in self.allButtons:
            LerpColorScaleInterval(button, .15, Vec4(1, 1, 1, 0), Vec4(1, 1, 1, 1)).start()

    def hideOptions(self):
        self.optionsMgr.hideOptions(False)
        self.closeOptionsButton.hide()
        for button in self.allButtons:
            LerpColorScaleInterval(button, .15, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0)).start()

    def playGame(self):
        self.ignore('doQuitGame')
        self.ignore('doCancelQuitGame')
        if self.fadeOut is not None:
            self.fadeOut.finish()
            self.fadeOut = None
        Sequence(
            Func(self.doPlayButton),
            LerpColorScaleInterval(self.background2d, .5, Vec4(1, 1, 1, 0), startColorScale = Vec4(1, 1, 1, 1)),
            Func(self.enterGame)).start()

    def enterOptions(self):
        pass

    def enterGame(self):
        base.cr.avChoice = PickAToon.PickAToon(self.patAvList, self.patFSM, self.patDoneEvent)
        base.cr.avChoice.load()
        base.cr.avChoice.enter()

    def doPlayButton(self):
        self.PlayButton['state'] = DGG.DISABLED
        self.OptionsButton['state'] = DGG.DISABLED
        self.QuitButton['state'] = DGG.DISABLED
        self.NewsButton['state'] = DGG.DISABLED
        self.CreditsButton['state'] = DGG.DISABLED
        Parallel(
            self.PlayButton.posInterval(.2, Point3(MPlayBtnHidePos), blendType = 'easeInOut'),
            self.OptionsButton.posInterval(.2, Point3(MOptionsBtnHidePos), blendType = 'easeInOut'),
            self.QuitButton.posInterval(.2, Point3(MQuitBtnHidePos), blendType = 'easeInOut'),
            self.NewsButton.posInterval(.2, Point3(MDiscordBtnHidePos), blendType = 'easeInOut'),
            self.CreditsButton.posInterval(.2, Point3(MCreditsBtnHidePos), blendType = 'easeInOut'),
            self.logo.posInterval(0.5, Point3(0, 0, 2.5), blendType = 'easeInOut')).start()

    def quitGame(self):
        self.showQuitConfirmation()
        Parallel(
            self.PlayButton.posInterval(.2, Point3(MPlayBtnHidePos), blendType = 'easeInOut'),
            self.OptionsButton.posInterval(.2, Point3(MOptionsBtnHidePos), blendType = 'easeInOut'),
            self.QuitButton.posInterval(.2, Point3(MQuitBtnHidePos), blendType = 'easeInOut'),
            self.NewsButton.posInterval(.2, Point3(MDiscordBtnHidePos), blendType = 'easeInOut'),
            self.CreditsButton.posInterval(.2, Point3(MCreditsBtnHidePos), blendType = 'easeInOut'),
            self.logo.posInterval(0.5, Point3(0, 0, 2.5), blendType = 'easeInOut')).start()

    def showQuitConfirmation(self):
        LerpColorScaleInterval(self.background2d, .5, Vec4(.6, .1, .1, 1), startColorScale = Vec4(1, 1, 1, 1)).start()
        self.quitConfirmation.showConf()

    def doQuitFunc(self):
        base.exitFunc()

    def doCancelQuitFunc(self):
        LerpColorScaleInterval(self.background2d, .5, Vec4(1, 1, 1, 1), startColorScale = Vec4(.6, .1, .1, 1)).start()
        self.buttonInAnimation()
        self.quitConfirmation.hideConf()

    def buttonInAnimation(self):
        logo = self.logo.posInterval(.5, Point3(0, 0, .5), blendType = 'easeInOut')
        play = self.PlayButton.posInterval(.5, Point3(MPlayBtnPos), blendType = 'easeInOut')
        opt = self.OptionsButton.posInterval(.5, Point3(MOptionsBtnPos), blendType = 'easeInOut')
        quit = self.QuitButton.posInterval(.5, Point3(MQuitBtnPos), blendType = 'easeInOut')
        discord = self.NewsButton.posInterval(.5, Point3(MDiscordBtnPos), blendType = 'easeInOut')
        credits = self.CreditsButton.posInterval(.5, Point3(MCreditsBtnPos), blendType = 'easeInOut')

        Sequence(
                 Func(logo.start),
                 Wait(0.1),
                 Func(play.start),
                 Wait(0.1),
                 Func(opt.start),
                 Func(discord.start),
                 Func(credits.start),
                 Func(quit.start)).start()

    def openDiscord(self):
        webbrowser.open_new_tab('https://discord.me/ttprojectaltis')

    def startCredits(self):
        DMenuCredits.DMenuCredits()