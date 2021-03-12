from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.gui.DirectGui import *
from toontown.toonbase import ToonPythonUtil as PythonUtil
from direct.task import Task
from panda3d.core import *
from toontown.shtiker import DisplaySettingsDialog
from toontown.shtiker import ShtikerPage
from otp.speedchat import SCColorScheme
from otp.speedchat import SCStaticTextTerminal
from otp.speedchat import SpeedChat
from toontown.toonbase import TTLocalizer, ToontownGlobals
from toontown.toon import Toon
from toontown.toontowngui import TTDialog
from toontown.shtiker import ControlRemapDialog
from toontown.toontowngui import FeatureComingSoonDialog
from decimal import Decimal
from toontown.dmenu import DMenuQuit
from direct.showbase.DirectObject import DirectObject
disabledImageColor = Vec4(0.6, 0.6, 0.6, 1)
speedChatStyles = (
    (
        2000,
        (200 / 255.0, 60 / 255.0, 229 / 255.0),
        (200 / 255.0, 135 / 255.0, 255 / 255.0),
        (220 / 255.0, 195 / 255.0, 229 / 255.0)
    ),
    (
        2012,
        (142 / 255.0, 151 / 255.0, 230 / 255.0),
        (173 / 255.0, 180 / 255.0, 237 / 255.0),
        (220 / 255.0, 195 / 255.0, 229 / 255.0)
    ),
    (
        2001,
        (0 / 255.0, 0 / 255.0, 255 / 255.0),
        (140 / 255.0, 150 / 255.0, 235 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2010,
        (0 / 255.0, 119 / 255.0, 190 / 255.0),
        (53 / 255.0, 180 / 255.0, 255 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2014,
        (0 / 255.0, 64 / 255.0, 128 / 255.0),
        (0 / 255.0, 64 / 255.0, 128 / 255.0),
        (201 / 255.0, 215 / 255.0, 255 / 255.0)
    ),
    (
        2002,
        (90 / 255.0, 175 / 255.0, 225 / 255.0),
        (120 / 255.0, 215 / 255.0, 255 / 255.0),
        (208 / 255.0, 230 / 255.0, 250 / 255.0)
    ),
    (
        2003,
        (130 / 255.0, 235 / 255.0, 235 / 255.0),
        (120 / 255.0, 225 / 255.0, 225 / 255.0),
        (234 / 255.0, 255 / 255.0, 255 / 255.0)
    ),
    (
        2004,
        (0 / 255.0, 200 / 255.0, 70 / 255.0),
        (0 / 255.0, 200 / 255.0, 80 / 255.0),
        (204 / 255.0, 255 / 255.0, 204 / 255.0)
    ),
    (
        2015,
        (13 / 255.0, 255 / 255.0, 100 / 255.0),
        (64 / 255.0, 255 / 255.0, 131 / 255.0),
        (204 / 255.0, 255 / 255.0, 204 / 255.0)
    ),
    (
        2005,
        (235 / 255.0, 230 / 255.0, 0 / 255.0),
        (255 / 255.0, 250 / 255.0, 100 / 255.0),
        (255 / 255.0, 250 / 255.0, 204 / 255.0)
    ),
    (
        2006,
        (255 / 255.0, 153 / 255.0, 0 / 255.0),
        (229 / 255.0, 147 / 255.0, 0 / 255.0),
        (255 / 255.0, 234 / 255.0, 204 / 255.0)
    ),
    (
        2011,
        (255 / 255.0, 177 / 255.0, 62 / 255.0),
        (255 / 255.0, 200 / 255.0, 117 / 255.0),
        (255 / 255.0, 234 / 255.0, 204 / 255.0)
    ),
    (
        2007,
        (255 / 255.0, 0 / 255.0, 50 / 255.0),
        (229 / 255.0, 0 / 255.0, 50 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2013,
        (130 / 255.0, 0 / 255.0, 26 / 255.0),
        (179 / 255.0, 0 / 255.0, 50 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2016,
        (176 / 255.0, 35 / 255.0, 0 / 255.0),
        (240 / 255.0, 48 / 255.0, 0 / 255.0),
        (255 / 255.0, 204 / 255.0, 204 / 255.0)
    ),
    (
        2008,
        (255 / 255.0, 153 / 255.0, 193 / 255.0),
        (240 / 255.0, 157 / 255.0, 192 / 255.0),
        (255 / 255.0, 215 / 255.0, 238 / 255.0)
    ),
    (
        2009,
        (170 / 255.0, 120 / 255.0, 20 / 255.0),
        (165 / 255.0, 120 / 255.0, 50 / 255.0),
        (210 / 255.0, 200 / 255.0, 180 / 255.0)
    )
)
PageMode = PythonUtil.Enum('Options, Codes')


class OptionsPage(ShtikerPage.ShtikerPage, DirectObject):
    notify = directNotify.newCategory('OptionsPage')

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        DirectObject.__init__(self)
        self.optionsTabPage = None
        self.codesTabPage = None
        self.title = None
        self.optionsTab = None
        self.codesTab = None

    def load(self):
        ShtikerPage.ShtikerPage.load(self)

        self.optionsTabPage = OptionsTabPage(self)
        self.optionsTabPage.hide()
        self.codesTabPage = CodesTabPage(self)
        self.codesTabPage.hide()

        self.title = DirectLabel(
            parent = self, relief = None, text = TTLocalizer.OptionsPageTitle,
            text_scale = 0.05, pos = (0, 0, 0.65))

        gui = loader.loadModel('phase_3.5/models/gui/fishingBook.bam')
        normalColor = (1, 1, 1, 1)
        clickColor = (0.8, 0.8, 0, 1)
        rolloverColor = (0.15, 0.82, 1.0, 1)
        diabledColor = (1.0, 0.98, 0.15, 1)
        self.optionsTab = DirectButton(
            parent = self, relief = None, text = TTLocalizer.OptionsPageTitle,
            text_scale = TTLocalizer.OPoptionsTab, text_align = TextNode.ALeft,
            text_pos = (0.01, 0.0, 0.0), image = gui.find('**/tabs/polySurface1'),
            image_pos = (0.55, 1, -0.91), image_hpr = (0, 0, -90),
            image_scale = (0.033, 0.033, 0.035), image_color = normalColor,
            image1_color = clickColor, image2_color = rolloverColor,
            image3_color = diabledColor, text_fg = Vec4(0.2, 0.1, 0, 1),
            command = self.setMode, extraArgs = [PageMode.Options],
            pos = (-0.64, 0, 0.77))
        gui.removeNode()

    def enter(self):
        self.setMode(PageMode.Options, updateAnyways = 1)

        ShtikerPage.ShtikerPage.enter(self)

    def exit(self):
        self.optionsTabPage.exit()
        self.codesTabPage.exit()

        ShtikerPage.ShtikerPage.exit(self)

    def unload(self):
        if self.optionsTabPage is not None:
            self.optionsTabPage.unload()
            self.optionsTabPage = None

        if self.codesTabPage is not None:
            self.codesTabPage.unload()
            self.codesTabPage = None

        if self.title is not None:
            self.title.destroy()
            self.title = None

        if self.optionsTab is not None:
            self.optionsTab.destroy()
            self.optionsTab = None

        ShtikerPage.ShtikerPage.unload(self)

    def setMode(self, mode, updateAnyways = 0):
        messenger.send('wakeup')

        if not updateAnyways:
            if self.mode == mode:
                return

        self.mode = mode

        if mode == PageMode.Options:
            self.title['text'] = TTLocalizer.OptionsPageTitle
            self.optionsTab['state'] = DGG.DISABLED
            self.optionsTabPage.enter()
            self.codesTabPage.exit()
        elif mode == PageMode.Codes:
            self.title['text'] = TTLocalizer.CdrPageTitle
            self.optionsTab['state'] = DGG.NORMAL
            self.optionsTabPage.exit()
            self.codesTabPage.enter()

class OptionsTabPage(DirectFrame):
    notify = directNotify.newCategory('OptionsTabPage')
    DisplaySettingsTaskName = 'save-display-settings'
    DisplaySettingsDelay = 60
    ChangeDisplaySettings = base.config.GetBool('change-display-settings', 1)
    ChangeDisplayAPI = base.config.GetBool('change-display-api', 0)

    def __init__(self, parent = aspect2d):
        self._parent = parent
        self.currentSizeIndex = None

        DirectFrame.__init__(self, parent = self._parent, relief = None, pos = (0.0, 0.0, 0.0), scale = (1.0, 1.0, 1.0))

        self.soundNode = self.attachNewNode('soundNode')
        self.privacyNode = self.attachNewNode('privacyNode')
        self.displayNode = self.attachNewNode('displayNode')
        self.controlsNode = self.attachNewNode('controlsNode')
        self.load()

    def destroy(self):
        self._parent = None

        DirectFrame.destroy(self)

    def load(self):
        self.displaySettings = None
        self.displaySettingsChanged = 0
        self.displaySettingsSize = (None, None)
        self.displaySettingsFullscreen = None
        self.displaySettingsBorderless = None
        self.displaySettingsApi = None
        self.displaySettingsApiChanged = 0
        guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        circleModel = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_nameShop')
        titleHeight = 0.61
        textStartHeight = 0.45
        textRowHeight = 0.145
        leftMargin = -0.72
        buttonbase_xcoord = 0.35
        buttonbase_ycoord = 0.45
        button_image_scale = (0.7, 1, 1)
        button_textpos = (0, -0.02)
        options_text_scale = 0.052
        disabled_arrow_color = Vec4(0.6, 0.6, 0.6, 1.0)
        self.speed_chat_scale = 0.055
        gui2 = base.matGui
        shuffleUp = gui2.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = gui2.find('**/tt_t_gui_mat_shuffleDown')
        self.soundButton = DirectButton(relief = None, text_style = 3, image3_color=disabledImageColor, image = (shuffleUp, shuffleDown, shuffleUp), text_pos = (0, -0.02), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = 'Sound', text_scale = .1, scale = 0.6, command = self.displaySoundOptions)
        self.soundButton.reparentTo(self)
        self.soundButton.setPos(-.6, 0, .6)
        self.soundButton.show()

        self.privacyButton = DirectButton(relief = None, text_style = 3, image3_color=disabledImageColor, image = (shuffleUp, shuffleDown, shuffleUp), text_pos = (0, -0.02), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = 'Privacy', text_scale = .1, scale = 0.6, command = self.displayPrivacyOptions)
        self.privacyButton.reparentTo(self)
        self.privacyButton.setPos(-.2, 0, .6)
        self.privacyButton.show()
        
        self.displayButton = DirectButton(relief = None, text_style = 3, image3_color=disabledImageColor, image = (shuffleUp, shuffleDown, shuffleUp), text_pos = (0, -0.02), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = 'Video', text_scale = .1, scale = 0.6, command = self.displayDisplayOptions)
        self.displayButton.reparentTo(self)
        self.displayButton.setPos(.2, 0, .6)
        self.displayButton.show()
        
        self.controlsButton = DirectButton(relief = None, text_style = 3, image3_color=disabledImageColor, image = (shuffleUp, shuffleDown, shuffleUp), text_pos = (0, -0.02), image_scale = (0.8, 0.7, 0.7), image1_scale = (0.83, 0.7, 0.7), image2_scale = (0.83, 0.7, 0.7), text_fg = (1, 1, 1, 1), text = 'Controls', text_scale = .1, scale = 0.6, command = self.displayControlsOptions)
        self.controlsButton.reparentTo(self)
        self.controlsButton.setPos(.6, 0, .6)
        self.controlsButton.show()

        self.quitConfirmation = DMenuQuit.DMenuQuit()
        self.exitButton = DirectButton(self, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = 1.15, text = TTLocalizer.OptionsPageExitToontown, text_scale = options_text_scale, text_pos = button_textpos, textMayChange = 0, pos = (0, 0, -.6), command = self.showQuitConfirmation)
        self.accept('doQuitGame', self.doQuitFunc)
        self.accept('doCancelQuitGame', self.doCancelQuitFunc)
        
        # Sound
        self.Music_Label = DirectLabel(self.soundNode, relief = None, text = TTLocalizer.OptionsPageMusic, text_align = TextNode.ALeft, text_scale = options_text_scale, pos = (leftMargin, 0, textStartHeight))
        self.SoundFX_Label = DirectLabel(self.soundNode, relief = None, text = TTLocalizer.OptionsPageSFX, text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight - textRowHeight))
                
        self.Music_toggleSlider = DirectSlider(self.soundNode, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord),
                                               value = settings['musicVol'] * 100, pageSize = 5, range = (0, 100), command = self.__doMusicLevel,
                                               thumb_geom = (guiButton.find('**/QuitBtn_UP')), thumb_relief = None, thumb_geom_scale = 1)
        self.Music_toggleSlider.setScale(0.25)
        self.SoundFX_toggleSlider = DirectSlider(self.soundNode, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight),
                                               value = settings['sfxVol'] * 100, pageSize = 5, range = (0, 100), command = self.__doSfxLevel,
                                               thumb_geom = (guiButton.find('**/QuitBtn_UP')), thumb_relief = None, thumb_geom_scale = 1)
        self.SoundFX_toggleSlider.setScale(0.25)
        self.ToonChatSounds_Label = DirectLabel(self.soundNode, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 15, pos = (leftMargin, 0, textStartHeight - 2 * textRowHeight))
        self.ToonChatSounds_Label.setScale(0.9)
        
        self.ToonChatSounds_toggleButton = DirectButton(self.soundNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'),
         guiButton.find('**/QuitBtn_DN'),
         guiButton.find('**/QuitBtn_RLVR'),
         guiButton.find('**/QuitBtn_UP')), image3_color = Vec4(0.5, 0.5, 0.5, 0.5), image_scale = button_image_scale, text = '', text3_fg = (0.5, 0.5, 0.5, 0.75), text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight * 2), command = self.__doToggleToonChatSounds)
        self.ToonChatSounds_toggleButton.setScale(0.8)


        # Privacy
        self.Friends_Label = DirectLabel(self.privacyNode, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight))
        self.Whispers_Label = DirectLabel(self.privacyNode, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight - textRowHeight))
        self.Friends_toggleButton = DirectButton(self.privacyNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord), command = self.__doToggleAcceptFriends)
        self.Whispers_toggleButton = DirectButton(self.privacyNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - textRowHeight), command = self.__doToggleAcceptWhispers)

        self.tpMessages_Label = DirectLabel(parent = self.privacyNode, relief = None, text = '', text_align = TextNode.ALeft,
                                      text_scale = options_text_scale, text_wordwrap = 16,
                                      pos = (leftMargin, 0, textStartHeight - 2 * textRowHeight))
        self.tpMessages_toggleButton = DirectButton(parent = self.privacyNode, relief = None, image = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = button_image_scale, text = '', text_scale = options_text_scale,
                                              text_pos = button_textpos,
                                              pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 2* textRowHeight),
                                              command = self.__doToggleTpMessages)

        self.friendMessages_Label = DirectLabel(parent = self.privacyNode, relief = None, text = '', text_align = TextNode.ALeft,
                                      text_scale = options_text_scale, text_wordwrap = 16,
                                      pos = (leftMargin, 0, textStartHeight - 3* textRowHeight))
        self.friendMessages_toggleButton = DirectButton(parent = self.privacyNode, relief = None, image = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = button_image_scale, text = '', text_scale = options_text_scale,
                                              text_pos = button_textpos,
                                              pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 3* textRowHeight),
                                              command = self.__doToggleFriendMessages)
        # Display
        self.DisplaySettings_Label = DirectLabel(self.displayNode, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 10, pos = (leftMargin, 0, textStartHeight))

        self.DisplaySettingsButton = DirectButton(self.displayNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image3_color = Vec4(0.5, 0.5, 0.5, 0.5), image_scale = button_image_scale, text = TTLocalizer.OptionsPageChange, text3_fg = (0.5, 0.5, 0.5, 0.75), text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord), command = self.__doDisplaySettings)
        self.SpeedChatStyle_Label = DirectLabel(self.displayNode, relief = None, text = TTLocalizer.OptionsPageSpeedChatStyleLabel, text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 10, pos = (leftMargin, 0, textStartHeight - textRowHeight))

        self.speedChatStyleLeftArrow = DirectButton(self.displayNode, relief = None, image = (gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(1, 1, 1, 0.5), scale = (-1.0, 1.0, 1.0), pos = (.25, 0, buttonbase_ycoord - textRowHeight), command = self.__doSpeedChatStyleLeft)
        self.speedChatStyleRightArrow = DirectButton(self.displayNode, relief = None, image = (gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), image3_color = Vec4(1, 1, 1, 0.5), pos = (.65, 0, buttonbase_ycoord - textRowHeight), command = self.__doSpeedChatStyleRight)
        self.speedChatStyleText = SpeedChat.SpeedChat(name = 'OptionsPageStyleText', structure = [2000], backgroundModelName = 'phase_3/models/gui/ChatPanel', guiModelName = 'phase_3.5/models/gui/speedChatGui')
        self.speedChatStyleText.setScale(self.speed_chat_scale)
        self.speedChatStyleText.reparentTo(self.displayNode, DGG.FOREGROUND_SORT_INDEX)
        self.speedChatStyleText.setPos(buttonbase_xcoord, 0, buttonbase_ycoord - textRowHeight + .03)
        self.newGui_Label = DirectLabel(parent = self.displayNode, relief = None, text = '', text_align = TextNode.ALeft,
                                      text_scale = options_text_scale, text_wordwrap = 16,
                                      pos = (leftMargin, 0, textStartHeight - 2 * textRowHeight))
        self.newGui_toggleButton = DirectButton(parent = self.displayNode, relief = None, image = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = button_image_scale, text = '', text_scale = options_text_scale,
                                              text_pos = button_textpos,
                                              pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 2 * textRowHeight),
                                              command = self.__doToggleNewGui)
        self.fov_Label = DirectLabel(parent = self.displayNode, relief = None, text = 'Field of view', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight - 3 * textRowHeight))

        self.fov_toggleSlider = DirectSlider(parent = self.displayNode, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 3 * textRowHeight),
                                               value = settings['fieldofview'], pageSize = 5, range = (30, 120), command = self.__doFovLevel,
                                               thumb_geom = (guiButton.find('**/QuitBtn_UP')), thumb_relief = None, thumb_geom_scale = 1)
        self.fov_toggleSlider.setScale(0.25)
        self.fov_resetButton = DirectButton(parent = self.displayNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = 'Reset FOV', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 4* textRowHeight), command = self.__resetFov)
        self.fovsliderText = OnscreenText("0.0", scale = .3, pos = (0, .1), fg = (1, 1, 1, 1), style = 3)
        self.fovsliderText.reparentTo(self.fov_toggleSlider.thumb)

        self.meterMode_Label = DirectLabel(parent = self.displayNode, relief = None, text = 'Nametag Laff Display Mode', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight - 5* textRowHeight))
        self.meterMode_preview = DirectLabel(parent = self.displayNode, relief=None, text='x', scale=0.06, text_align = TextNode.ACenter, text_wordwrap=9, pos=(buttonbase_xcoord, 0, textStartHeight - 5* textRowHeight))
        self.meterMode_leftButton = DirectButton(parent = self.displayNode, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale= -0.6, pos=(0.15, 0.0, buttonbase_ycoord - 5* textRowHeight), command=self.__doMeterMode, extraArgs=[-1])
        self.meterMode_rightButton = DirectButton(parent = self.displayNode, relief=None, image=(gui.find('**/Horiz_Arrow_UP'),
         gui.find('**/Horiz_Arrow_DN'),
         gui.find('**/Horiz_Arrow_Rllvr'),
         gui.find('**/Horiz_Arrow_UP')), scale = 0.6, pos = (0.55, 0.0, buttonbase_ycoord - 5* textRowHeight), command = self.__doMeterMode, extraArgs = [1])
        self.__doMeterMode()
        self.meterMode_index = 2
        self.animations_Label = DirectLabel(parent = self.displayNode, relief = None, text = '', text_align = TextNode.ALeft,
                                      text_scale = options_text_scale, text_wordwrap = 16,
                                      pos = (leftMargin, 0, textStartHeight - 6* textRowHeight))
        self.animations_toggleButton = DirectButton(parent = self.displayNode, relief = None, image = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = button_image_scale, text = '', text_scale = options_text_scale,
                                              text_pos = button_textpos,
                                              pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 6* textRowHeight),
                                              command = self.__doToggleAnimations)
        # Controls

        self.WASD_Label = DirectLabel(parent = self.controlsNode, relief = None, text = '', text_align = TextNode.ALeft, text_scale = options_text_scale, text_wordwrap = 16, pos = (leftMargin, 0, textStartHeight))
        self.WASD_toggleButton = DirectButton(parent = self.controlsNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = '', text_scale = options_text_scale, text_pos = button_textpos, pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord), command = self.__doToggleWASD)
        self.keymapDialogButton = DirectButton(parent = self.controlsNode, relief = None, image = (guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')), image_scale = button_image_scale, text = 'Change Keybinds', text_scale = (0.03, 0.05, 1), text_pos = button_textpos, pos = (buttonbase_xcoord + 0.0, 0.0, buttonbase_ycoord - textRowHeight), command = self.__openKeyRemapDialog)
        self.keymapDialogButton.setScale(1.55 * .9, .9, .9)
        self.interactKey_Label = DirectLabel(self.controlsNode, relief = None, text = '', text_align = TextNode.ALeft,
                                      text_scale = options_text_scale, text_wordwrap = 16,
                                      pos = (leftMargin, 0, textStartHeight - 2* textRowHeight))

        self.interactKey_toggleButton = DirectButton(self.controlsNode, relief = None, image = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = button_image_scale, text = '', text_scale = options_text_scale,
                                              text_pos = button_textpos,
                                              pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 2* textRowHeight),
                                              command = self.__doToggleInteractKey)

        self.doorKey_Label = DirectLabel(self.controlsNode, relief = None, text = '', text_align = TextNode.ALeft,
                                      text_scale = options_text_scale, text_wordwrap = 16,
                                      pos = (leftMargin, 0, textStartHeight - 3* textRowHeight))

        self.doorKey_toggleButton = DirectButton(self.controlsNode, relief = None, image = (
        guiButton.find('**/QuitBtn_UP'), guiButton.find('**/QuitBtn_DN'), guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = button_image_scale, text = '', text_scale = options_text_scale,
                                              text_pos = button_textpos,
                                              pos = (buttonbase_xcoord, 0.0, buttonbase_ycoord - 3*textRowHeight),
                                              command = self.__doToggleDoorKey)



        guiButton.removeNode()
        circleModel.removeNode()
        guiButton.removeNode()
        gui.removeNode()

    def displaySoundOptions(self):
        self.soundNode.show()
        self.privacyNode.hide()
        self.displayNode.hide()
        self.controlsNode.hide()
        
        self.soundButton['state'] = DGG.DISABLED
        self.privacyButton['state'] = DGG.NORMAL
        self.displayButton['state'] = DGG.NORMAL
        self.controlsButton['state'] = DGG.NORMAL
        
    def displayPrivacyOptions(self):
        self.soundNode.hide()
        self.privacyNode.show()
        self.displayNode.hide()
        self.controlsNode.hide()
                
        self.soundButton['state'] = DGG.NORMAL
        self.privacyButton['state'] = DGG.DISABLED
        self.displayButton['state'] = DGG.NORMAL
        self.controlsButton['state'] = DGG.NORMAL
                        
        self.soundButton['state'] = DGG.NORMAL
        self.privacyButton['state'] = DGG.DISABLED
        self.displayButton['state'] = DGG.NORMAL
        self.controlsButton['state'] = DGG.NORMAL
        
    def displayDisplayOptions(self):
        self.soundNode.hide()
        self.privacyNode.hide()
        self.displayNode.show()
        self.controlsNode.hide()
                        
        self.soundButton['state'] = DGG.NORMAL
        self.privacyButton['state'] = DGG.NORMAL
        self.displayButton['state'] = DGG.DISABLED
        self.controlsButton['state'] = DGG.NORMAL
        
    def displayControlsOptions(self):
        self.soundNode.hide()
        self.privacyNode.hide()
        self.displayNode.hide()
        self.controlsNode.show()
            
        self.soundButton['state'] = DGG.NORMAL
        self.privacyButton['state'] = DGG.NORMAL
        self.displayButton['state'] = DGG.NORMAL
        self.controlsButton['state'] = DGG.DISABLED
        
    def enter(self):
        self.show()
        taskMgr.remove(self.DisplaySettingsTaskName)
        self.settingsChanged = 0
        self.__setAcceptFriendsButton()
        self.__setAcceptWhispersButton()
        self.__setDisplaySettings()
        self.__setToonChatSoundsButton()
        self.__setWASDButton()
        self.__setNewGuiButton()
        self.__doFovLevel()
        self.__setAnimationsButton()
        self.__setTpMessagesButton()
        self.__setFriendMessagesButton()
        self.__setInteractKey()
        self.speedChatStyleText.enter()
        self.speedChatStyleIndex = base.localAvatar.getSpeedChatStyleIndex()
        self.updateSpeedChatStyle()
        self.__setDoorKey()
        if self._parent.book.safeMode:
            self.exitButton.hide()
        else:
            self.exitButton.show()
        self.displaySoundOptions()
        
    def exit(self):
        self.ignore('confirmDone')
        self.hide()
        self.speedChatStyleText.exit()
        if self.displaySettingsChanged:
            taskMgr.doMethodLater(self.DisplaySettingsDelay, self.writeDisplaySettings, self.DisplaySettingsTaskName)

    def unload(self):
        self.ignore('doQuitGame')
        self.ignore('doCancelQuitGame')
        self.writeDisplaySettings()
        taskMgr.remove(self.DisplaySettingsTaskName)
        if self.displaySettings != None:
            self.ignore(self.displaySettings.doneEvent)
            self.displaySettings.unload()
        self.displaySettings = None
        self.exitButton.destroy()
        self.Music_toggleSlider.destroy()
        self.SoundFX_toggleSlider.destroy()
        self.Friends_toggleButton.destroy()
        self.Whispers_toggleButton.destroy()
        self.DisplaySettingsButton.destroy()
        self.speedChatStyleLeftArrow.destroy()
        self.speedChatStyleRightArrow.destroy()
        self.doorKey_Label.destroy()
        self.doorKey_toggleButton.destroy()
        del self.exitButton
        del self.SoundFX_Label
        del self.Music_Label
        del self.Friends_Label
        del self.Whispers_Label
        del self.SpeedChatStyle_Label
        del self.SoundFX_toggleSlider
        del self.Music_toggleSlider
        del self.Friends_toggleButton
        del self.Whispers_toggleButton
        del self.speedChatStyleLeftArrow
        del self.speedChatStyleRightArrow
        del self.doorKey_Label
        del self.doorKey_toggleButton
        self.WASD_Label.destroy()
        del self.WASD_Label
        self.WASD_toggleButton.destroy()
        del self.WASD_toggleButton
        self.keymapDialogButton.destroy()
        del self.keymapDialogButton
        self.fov_toggleSlider.destroy()
        del self.fov_toggleSlider
        self.fov_resetButton.destroy()
        del self.fov_resetButton
        self.fov_Label.destroy()
        del self.fov_Label
        self.animations_Label.destroy()
        del self.animations_Label
        self.animations_toggleButton.destroy()
        del self.animations_toggleButton
        self.speedChatStyleText.exit()
        self.speedChatStyleText.destroy()
        del self.speedChatStyleText
        self.interactKey_toggleButton.destroy()
        self.interactKey_Label.destroy()
        del self.interactKey_toggleButton
        del self.interactKey_Label

        self.soundNode.removeNode()
        self.privacyNode.removeNode()
        self.displayNode.removeNode()
        self.controlsNode.removeNode()
        del self.soundNode
        del self.privacyNode
        del self.displayNode
        del self.controlsNode
        
        self.soundButton.destroy()
        self.privacyButton.destroy()
        self.displayButton.destroy()
        self.controlsButton.destroy()
        
        self.currentSizeIndex = None

    def __doMusicLevel(self):
        vol = self.Music_toggleSlider['value']
        vol = float(vol) / 100
        settings['musicVol'] = vol
        base.musicManager.setVolume(vol)
        base.musicActive = vol > 0.0

    def __doSfxLevel(self):
        vol = self.SoundFX_toggleSlider['value']
        vol = float(vol) / 100
        settings['sfxVol'] = vol
        for sfm in base.sfxManagerList:
            sfm.setVolume(vol)
        base.sfxActive = vol > 0.0
        self.__setToonChatSoundsButton()

    def __doToggleToonChatSounds(self):
        messenger.send('wakeup')
        if base.toonChatSounds:
            base.toonChatSounds = 0
            settings['toonChatSounds'] = False
        else:
            base.toonChatSounds = 1
            settings['toonChatSounds'] = True
        self.settingsChanged = 1
        self.__setToonChatSoundsButton()

    def __setToonChatSoundsButton(self):
        if base.toonChatSounds:
            self.ToonChatSounds_Label['text'] = TTLocalizer.OptionsPageToonChatSoundsOnLabel
            self.ToonChatSounds_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.ToonChatSounds_Label['text'] = TTLocalizer.OptionsPageToonChatSoundsOffLabel
            self.ToonChatSounds_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn
        if base.sfxActive:
            self.ToonChatSounds_Label.setColorScale(1.0, 1.0, 1.0, 1.0)
            self.ToonChatSounds_toggleButton['state'] = DGG.NORMAL
        else:
            self.ToonChatSounds_Label.setColorScale(0.5, 0.5, 0.5, 0.5)
            self.ToonChatSounds_toggleButton['state'] = DGG.DISABLED

    def __doToggleAcceptFriends(self):
        messenger.send('wakeup')
        acceptingNewFriends = settings.get('acceptingNewFriends', {})
        if base.localAvatar.acceptingNewFriends:
            base.localAvatar.acceptingNewFriends = 0
            acceptingNewFriends[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingNewFriends = 1
            acceptingNewFriends[str(base.localAvatar.doId)] = True
        settings['acceptingNewFriends'] = acceptingNewFriends
        self.settingsChanged = 1
        self.__setAcceptFriendsButton()

    def __doToggleAcceptWhispers(self):
        messenger.send('wakeup')
        acceptingNonFriendWhispers = settings.get('acceptingNonFriendWhispers', {})
        if base.localAvatar.acceptingNonFriendWhispers:
            base.localAvatar.acceptingNonFriendWhispers = 0
            acceptingNonFriendWhispers[str(base.localAvatar.doId)] = False
        else:
            base.localAvatar.acceptingNonFriendWhispers = 1
            acceptingNonFriendWhispers[str(base.localAvatar.doId)] = True
        settings['acceptingNonFriendWhispers'] = acceptingNonFriendWhispers
        self.settingsChanged = 1
        self.__setAcceptWhispersButton()

    def __setAcceptFriendsButton(self):
        if base.localAvatar.acceptingNewFriends:
            self.Friends_Label['text'] = TTLocalizer.OptionsPageFriendsEnabledLabel
            self.Friends_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.Friends_Label['text'] = TTLocalizer.OptionsPageFriendsDisabledLabel
            self.Friends_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn

    def __setAcceptWhispersButton(self):
        if base.localAvatar.acceptingNonFriendWhispers:
            self.Whispers_Label['text'] = TTLocalizer.OptionsPageWhisperEnabledLabel
            self.Whispers_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
        else:
            self.Whispers_Label['text'] = TTLocalizer.OptionsPageWhisperDisabledLabel
            self.Whispers_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn

    def __doDisplaySettings(self):
        if self.displaySettings == None:
            self.displaySettings = DisplaySettingsDialog.DisplaySettingsDialog()
            self.displaySettings.load()
            self.accept(self.displaySettings.doneEvent, self.__doneDisplaySettings)
        self.displaySettings.enter(self.ChangeDisplaySettings, self.ChangeDisplayAPI)

    def __doneDisplaySettings(self, anyChanged, apiChanged):
        if anyChanged:
            self.__setDisplaySettings()
            properties = base.win.getProperties()
            self.displaySettingsChanged = 1
            self.displaySettingsSize = (properties.getXSize(), properties.getYSize())
            self.displaySettingsFullscreen = properties.getFullscreen()
            self.displaySettingsBorderless = properties.getUndecorated()
            self.displaySettingsApi = base.pipe.getInterfaceName()
            self.displaySettingsApiChanged = apiChanged

    def __setDisplaySettings(self):
        properties = base.win.getProperties()
        if properties.getFullscreen():
            screensize = 'Fullscreen | %s x %s' % (properties.getXSize(), properties.getYSize())
        elif properties.getUndecorated():
            screensize = 'Borderless Windowed | %s x %s' % (properties.getXSize(), properties.getYSize())
        else:
            screensize = 'Windowed'
        api = base.pipe.getInterfaceName()
        settings = {'screensize': screensize, 'api': api}
        text = TTLocalizer.OptionsPageDisplaySettings % settings
        self.DisplaySettings_Label['text'] = text

    def __doSpeedChatStyleLeft(self):
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleIndex = self.speedChatStyleIndex - 1
            self.updateSpeedChatStyle()

    def __doSpeedChatStyleRight(self):
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleIndex = self.speedChatStyleIndex + 1
            self.updateSpeedChatStyle()

    def updateSpeedChatStyle(self):
        nameKey, arrowColor, rolloverColor, frameColor = speedChatStyles[self.speedChatStyleIndex]
        newSCColorScheme = SCColorScheme.SCColorScheme(arrowColor = arrowColor, rolloverColor = rolloverColor, frameColor = frameColor)
        self.speedChatStyleText.setColorScheme(newSCColorScheme)
        self.speedChatStyleText.clearMenu()
        colorName = SCStaticTextTerminal.SCStaticTextTerminal(nameKey)
        self.speedChatStyleText.append(colorName)
        self.speedChatStyleText.finalize()
        self.speedChatStyleText.setPos(0.445 - self.speedChatStyleText.getWidth() * self.speed_chat_scale / 2, 0, self.speedChatStyleText.getPos()[2])
        if self.speedChatStyleIndex > 0:
            self.speedChatStyleLeftArrow['state'] = DGG.NORMAL
        else:
            self.speedChatStyleLeftArrow['state'] = DGG.DISABLED
        if self.speedChatStyleIndex < len(speedChatStyles) - 1:
            self.speedChatStyleRightArrow['state'] = DGG.NORMAL
        else:
            self.speedChatStyleRightArrow['state'] = DGG.DISABLED
        base.localAvatar.b_setSpeedChatStyleIndex(self.speedChatStyleIndex)

    def writeDisplaySettings(self, task = None):
        if not self.displaySettingsChanged:
            return
        taskMgr.remove(self.DisplaySettingsTaskName)
        settings['res'] = (self.displaySettingsSize[0], self.displaySettingsSize[1])
        settings['fullscreen'] = self.displaySettingsFullscreen
        return Task.done

    def __handleExitShowWithConfirm(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent = 'confirmDone', message = TTLocalizer.OptionsPageExitConfirm, style = TTDialog.TwoChoice)
        self.confirm.show()
        self._parent.doneStatus = {'mode': 'exit',
         'exitTo': 'closeShard'}
        self.accept('confirmDone', self.__handleConfirm)

    def __handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            base.cr._userLoggingOut = True
            messenger.send(self._parent.doneEvent)
            
    def showQuitConfirmation(self):
        self.quitConfirmation.showConf()
        
    def doQuitFunc(self):
        self.quitConfirmation.hideConf()
        self._parent.doneStatus = {'mode': 'exit',
         'exitTo': 'closeShard'}
        messenger.send(self._parent.doneEvent)
        
    def doCancelQuitFunc(self):
        self.quitConfirmation.hideConf()
        
    def __doToggleDoorKey(self):
        if settings['doorkey'] == True:
            settings['doorkey'] = False
            base.localAvatar.setSystemMessage(0, 'Door Entering Hotkey is DISABLED!')
        else:
            settings['doorkey'] = True
            base.localAvatar.setSystemMessage(0, 'Door Entering Hotkey is ENABLED!')
        self.settingsChanged = 1
        self.__setDoorKey()
        base.toggleDoorKey()

    def __setDoorKey(self):
        if settings['doorkey'] == True:
            self.doorKey_Label['text'] = 'Door Entering Hotkey is ENABLED'
            self.doorKey_toggleButton['text'] = 'Turn Off'
        else:
            self.doorKey_Label['text'] = 'Door Entering Hotkey is DISABLED'
            self.doorKey_toggleButton['text'] = 'Turn On'

    def __doToggleNewGui(self):
         if settings['newGui'] == True:
           settings['newGui'] = False
           base.localAvatar.setSystemMessage(0, 'Classic Battle GUI is now active!')
         else:
            settings['newGui'] = True
            base.localAvatar.setSystemMessage(0, 'New Battle GUI is now active!')
         self.settingsChanged = 1
         self.__setNewGuiButton()

    def __setNewGuiButton(self):
        if settings['newGui'] == True:
            self.newGui_Label['text'] = 'Using the New Battle GUI.'
            self.newGui_toggleButton['text'] = 'Toggle'
        else:
            self.newGui_Label['text'] = 'Using the Classic Battle GUI.'
            self.newGui_toggleButton['text'] = 'Toggle'

    def __doToggleWASD(self):
        messenger.send('wakeup')
        if base.wantCustomControls:
            base.wantCustomControls = False
            settings['want-Custom-Controls'] = False
        else:
            base.wantCustomControls = True
            settings['want-Custom-Controls'] = True
        base.reloadControls()
        base.localAvatar.controlManager.reload()
        base.localAvatar.chatMgr.reloadWASD()
        base.localAvatar.controlManager.disable()
        self.settingsChanged = 1
        self.__setWASDButton()

    def __setWASDButton(self):
        if base.wantCustomControls:
            self.WASD_Label['text'] = 'Custom Keymapping is enabled.'
            self.WASD_toggleButton['text'] = TTLocalizer.OptionsPageToggleOff
            self.keymapDialogButton.show()
        else:
            self.WASD_Label['text'] = 'Custom Keymapping is disabled.'
            self.WASD_toggleButton['text'] = TTLocalizer.OptionsPageToggleOn
            self.keymapDialogButton.hide()

    def __openKeyRemapDialog(self):
        if base.wantCustomControls:
            self.controlDialog = ControlRemapDialog.ControlRemap()

    def __doFovLevel(self):
        fov = self.fov_toggleSlider['value']
        settings['fieldofview'] = fov
        base.camLens.setMinFov(fov / (4. / 3.))
        dec = Decimal(fov)
        self.fovsliderText['text'] = str(round(fov, 1))

    def __resetFov(self):
        self.fov_toggleSlider['value'] = 52
        settings['fieldofview'] = 52
        base.camLens.setMinFov(52 / (4. / 3.))
        self.fovsliderText['text'] = str(52)

    def __doMeterMode(self, val = 0):
        mode2name = {
        0: "Disabled",
        1: "Always On",
        2: "Hide only if full laff"}
        mode = settings['health-meter-mode'] + val
        settings['health-meter-mode'] = mode
        base.meterMode = mode
        self.meterMode_preview['text'] = mode2name.get(mode)
        self.meterMode_index = mode
        if self.meterMode_index == 0:
            self.meterMode_leftButton.hide()
            self.meterMode_rightButton.show()
        elif self.meterMode_index == 1:
            self.meterMode_leftButton.show()
            self.meterMode_rightButton.show()
        elif self.meterMode_index == 2:
            self.meterMode_leftButton.show()
            self.meterMode_rightButton.hide()

    def __doToggleAnimations(self):
        if settings['smoothanimations'] == True:
            settings['smoothanimations'] = False
            base.localAvatar.setSystemMessage(0, 'Disabled smooth animations! Restart the game to see changes!')
        else:
            settings['smoothanimations'] = True
            base.localAvatar.setSystemMessage(0, 'Enabled smooth animations! Restart the game to see changes!')
        self.settingsChanged = 1
        self.__setAnimationsButton()
        # base.toggleSmoothAnimations() TODO:

    def __setAnimationsButton(self):
        if settings['smoothanimations'] == True:
            self.animations_Label['text'] = 'Smooth Animations ON'
            self.animations_toggleButton['text'] = 'Turn Off'
        else:
            self.animations_Label['text'] = 'Smooth Animations OFF'
            self.animations_toggleButton['text'] = 'Turn On'

    def __doToggleTpMessages(self):
        if settings['tpmsgs'] == True:
            settings['tpmsgs'] = False
            base.localAvatar.setSystemMessage(0, 'Disabled Teleport messages!')
        else:
            settings['tpmsgs'] = True
            base.localAvatar.setSystemMessage(0, 'Enabled Teleport messages!')
        self.settingsChanged = 1
        self.__setTpMessagesButton()
        base.toggleTpMsgs()

    def __setTpMessagesButton(self):
        if settings['tpmsgs'] == True:
            self.tpMessages_Label['text'] = 'Teleport messages are enabled!'
            self.tpMessages_toggleButton['text'] = 'Turn Off'
        else:
            self.tpMessages_Label['text'] = 'Teleport messages are disabled!'
            self.tpMessages_toggleButton['text'] = 'Turn On'

    def __doToggleFriendMessages(self):
        if settings['friendstatusmsgs'] == True:
            settings['friendstatusmsgs'] = False
            base.localAvatar.setSystemMessage(0, 'Disabled Friend status messages!')
        else:
            settings['friendstatusmsgs'] = True
            base.localAvatar.setSystemMessage(0, 'Enabled Friend status messages!')
        self.settingsChanged = 1
        self.__setFriendMessagesButton()
        base.toggleTpMsgs()

    def __setFriendMessagesButton(self):
        if settings['friendstatusmsgs'] == True:
            self.friendMessages_Label['text'] = 'Friend status messages are enabled!'
            self.friendMessages_toggleButton['text'] = 'Turn Off'
        else:
            self.friendMessages_Label['text'] = 'Friend status messages are disabled!'
            self.friendMessages_toggleButton['text'] = 'Turn On'

    def __doToggleInteractKey(self):
        if settings['interactkey'] == True:
            settings['interactkey'] = False
            base.localAvatar.setSystemMessage(0, 'NPC Interact Hotkey is DISABLED!')
        else:
            settings['interactkey'] = True
            base.localAvatar.setSystemMessage(0, 'NPC Interact Hotkey is ENABLED!')
        self.settingsChanged = 1
        self.__setInteractKey()
        base.toggleDoorKey()

    def __setInteractKey(self):
        if settings['interactkey'] == True:
            self.interactKey_Label['text'] = 'NPC Interact Hotkey is ENABLED'
            self.interactKey_toggleButton['text'] = 'Turn Off'
        else:
            self.interactKey_Label['text'] = 'NPC Interact Hotkey is DISABLED'
            self.interactKey_toggleButton['text'] = 'Turn On'

class CodesTabPage(DirectFrame):
    notify = directNotify.newCategory('CodesTabPage')

    def __init__(self, parent = aspect2d):
        self._parent = parent
        DirectFrame.__init__(self, parent = self._parent, relief = None, pos = (0.0, 0.0, 0.0), scale = (1.0, 1.0, 1.0))
        self.load()

    def destroy(self):
        self._parent = None
        DirectFrame.destroy(self)

    def load(self):
        cdrGui = loader.loadModel('phase_3.5/models/gui/tt_m_gui_sbk_codeRedemptionGui')
        instructionGui = cdrGui.find('**/tt_t_gui_sbk_cdrPresent')
        flippyGui = cdrGui.find('**/tt_t_gui_sbk_cdrFlippy')
        codeBoxGui = cdrGui.find('**/tt_t_gui_sbk_cdrCodeBox')
        self.resultPanelSuccessGui = cdrGui.find('**/tt_t_gui_sbk_cdrResultPanel_success')
        self.resultPanelFailureGui = cdrGui.find('**/tt_t_gui_sbk_cdrResultPanel_failure')
        self.resultPanelErrorGui = cdrGui.find('**/tt_t_gui_sbk_cdrResultPanel_error')
        self.successSfx = base.loadSfx('phase_3.5/audio/sfx/tt_s_gui_sbk_cdrSuccess.ogg')
        self.failureSfx = base.loadSfx('phase_3.5/audio/sfx/tt_s_gui_sbk_cdrFailure.ogg')
        self.instructionPanel = DirectFrame(parent = self, relief = None, image = instructionGui, image_scale = 0.8, text = TTLocalizer.CdrInstructions, text_pos = TTLocalizer.OPCodesInstructionPanelTextPos, text_align = TextNode.ACenter, text_scale = TTLocalizer.OPCodesResultPanelTextScale, text_wordwrap = TTLocalizer.OPCodesInstructionPanelTextWordWrap, pos = (-0.429, 0, -0.05))
        self.codeBox = DirectFrame(parent = self, relief = None, image = codeBoxGui, pos = (0.433, 0, 0.35))
        self.flippyFrame = DirectFrame(parent = self, relief = None, image = flippyGui, pos = (0.44, 0, -0.353))
        self.codeInput = DirectEntry(parent = self.codeBox, relief = DGG.GROOVE, scale = 0.08, pos = (-0.33, 0, -0.006), borderWidth = (0.05, 0.05), frameColor = ((1, 1, 1, 1), (1, 1, 1, 1), (0.5, 0.5, 0.5, 0.5)), state = DGG.NORMAL, text_align = TextNode.ALeft, text_scale = TTLocalizer.OPCodesInputTextScale, width = 10.5, numLines = 1, focus = 1, backgroundFocus = 0, cursorKeys = 1, text_fg = (0, 0, 0, 1), suppressMouse = 1, autoCapitalize = 0, command = self.__submitCode)
        submitButtonGui = loader.loadModel('phase_3/models/gui/quit_button')
        self.submitButton = DirectButton(parent = self, relief = None, image = (submitButtonGui.find('**/QuitBtn_UP'),
         submitButtonGui.find('**/QuitBtn_DN'),
         submitButtonGui.find('**/QuitBtn_RLVR'),
         submitButtonGui.find('**/QuitBtn_UP')), image3_color = Vec4(0.5, 0.5, 0.5, 0.5), image_scale = 1.15, state = DGG.NORMAL, text = TTLocalizer.NameShopSubmitButton, text_scale = TTLocalizer.OPCodesSubmitTextScale, text_align = TextNode.ACenter, text_pos = TTLocalizer.OPCodesSubmitTextPos, text3_fg = (0.5, 0.5, 0.5, 0.75), textMayChange = 0, pos = (0.45, 0.0, 0.0896), command = self.__submitCode)
        self.resultPanel = DirectFrame(parent = self, relief = None, image = self.resultPanelSuccessGui, text = '', text_pos = TTLocalizer.OPCodesResultPanelTextPos, text_align = TextNode.ACenter, text_scale = TTLocalizer.OPCodesResultPanelTextScale, text_wordwrap = TTLocalizer.OPCodesResultPanelTextWordWrap, pos = (-0.42, 0, -0.0567))
        self.resultPanel.hide()
        closeButtonGui = loader.loadModel('phase_3/models/gui/dialog_box_buttons_gui')
        self.closeButton = DirectButton(parent = self.resultPanel, pos = (0.296, 0, -0.466), relief = None, state = DGG.NORMAL, image = (closeButtonGui.find('**/CloseBtn_UP'), closeButtonGui.find('**/CloseBtn_DN'), closeButtonGui.find('**/CloseBtn_Rllvr')), image_scale = (1, 1, 1), command = self.__hideResultPanel)
        closeButtonGui.removeNode()
        cdrGui.removeNode()
        submitButtonGui.removeNode()

    def enter(self):
        self.show()
        localAvatar.chatMgr.fsm.request('otherDialog')
        self.codeInput['focus'] = 1
        self.codeInput.enterText('')
        self.__enableCodeEntry()

    def exit(self):
        self.resultPanel.hide()
        self.hide()
        localAvatar.chatMgr.fsm.request('mainMenu')

    def unload(self):
        self.instructionPanel.destroy()
        self.instructionPanel = None
        self.codeBox.destroy()
        self.codeBox = None
        self.flippyFrame.destroy()
        self.flippyFrame = None
        self.codeInput.destroy()
        self.codeInput = None
        self.submitButton.destroy()
        self.submitButton = None
        self.resultPanel.destroy()
        self.resultPanel = None
        self.closeButton.destroy()
        self.closeButton = None
        del self.successSfx
        del self.failureSfx

    def __submitCode(self, input = None):
        if input == None:
            input = self.codeInput.get()
        self.codeInput['focus'] = 1
        if input == '':
            return
        messenger.send('wakeup')
        if base.config.GetBool('want-code-redemption', True) and hasattr(base.cr, 'codeRedemptionMgr'):
            base.cr.codeRedemptionMgr.redeemCode(input, self.__getCodeResult)
            self.codeInput.enterText('')
            self.__disableCodeEntry()
        else:
            self.__getCodeResult(6, 0)

    def __getCodeResult(self, result, awardMgrResult = 0):
        self.notify.debug('result = %s' % result)
        self.__enableCodeEntry()
        if result == 0:
            self.resultPanel['image'] = self.resultPanelSuccessGui
            self.resultPanel['text'] = TTLocalizer.CdrResultSuccess
        elif result == 1 or result == 3:
            self.resultPanel['image'] = self.resultPanelFailureGui
            self.resultPanel['text'] = TTLocalizer.CdrResultInvalidCode
        elif result == 2:
            self.resultPanel['image'] = self.resultPanelFailureGui
            self.resultPanel['text'] = TTLocalizer.CdrResultExpiredCode
        elif result == 4:
            self.resultPanel['image'] = self.resultPanelErrorGui
            if awardMgrResult == 0:
                self.resultPanel['text'] = TTLocalizer.CdrResultSuccess
            elif awardMgrResult == 1 and awardMgrResult == 2 and awardMgrResult == 15 or awardMgrResult == 16:
                self.resultPanel['text'] = TTLocalizer.CdrResultUnknownError
            elif awardMgrResult == 3 or awardMgrResult == 4:
                self.resultPanel['text'] = TTLocalizer.CdrResultMailboxFull
            elif awardMgrResult == 5 or awardMgrResult == 10:
                self.resultPanel['text'] = TTLocalizer.CdrResultAlreadyInMailbox
            elif awardMgrResult == 6 and awardMgrResult == 7 or awardMgrResult == 11:
                self.resultPanel['text'] = TTLocalizer.CdrResultAlreadyInQueue
            elif awardMgrResult == 8:
                self.resultPanel['text'] = TTLocalizer.CdrResultAlreadyInCloset
            elif awardMgrResult == 9:
                self.resultPanel['text'] = TTLocalizer.CdrResultAlreadyBeingWorn
            elif awardMgrResult == 12 and awardMgrResult == 13 or awardMgrResult == 14:
                self.resultPanel['text'] = TTLocalizer.CdrResultAlreadyReceived
            elif awardMgrResult == 16:
                self.resultPanel['text'] = TTLocalizer.CdrResultClosetFull
            elif awardMgrResult == 17:
                self.resultPanel['text'] = TTLocalizer.CdrResultTrunkFull

        elif result == 5:
            self.resultPanel['text'] = TTLocalizer.CdrResultTooManyFails
            self.__disableCodeEntry()
        elif result == 6:
            self.resultPanel['text'] = TTLocalizer.CdrResultServiceUnavailable
            self.__disableCodeEntry()

        if result == 0:
            self.successSfx.play()
        else:
            self.failureSfx.play()
        self.resultPanel.show()

    def __hideResultPanel(self):
        self.resultPanel.hide()

    def __disableCodeEntry(self):
        self.codeInput['state'] = DGG.DISABLED
        self.submitButton['state'] = DGG.DISABLED

    def __enableCodeEntry(self):
        self.codeInput['state'] = DGG.NORMAL
        self.codeInput['focus'] = 1
        self.submitButton['state'] = DGG.NORMAL
