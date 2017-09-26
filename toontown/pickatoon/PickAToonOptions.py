'''
Created on Apr 2, 2016

@author: Drew
'''

from decimal import Decimal
from direct.gui.DirectGui import *
from direct.gui import DirectGuiGlobals
from direct.interval.IntervalGlobal import Wait, Func, Sequence, LerpColorScaleInterval
from direct.showbase.DirectObject import DirectObject
from panda3d.core import (TransparencyAttrib, Point3, Vec4,
                          TextNode, Vec3, VBase3)

from toontown.options import GraphicsOptions
from toontown.shtiker import ControlRemapDialog, DisplaySettingsDialog
from toontown.toonbase import TTLocalizer
from toontown.toontowngui import OptionHelp


resolution_table = [
    (800, 600),
    (1024, 768),
    (1280, 1024),
    (1600, 1200),
    (1280, 720),
    (1920, 1080)]

class NewPickAToonOptions(DirectObject):

    def __init__(self):
        self.optionsOpenSfx = None # base.loadSfx(DMenuResources.Settings_Open) # ALTIS: TODO: Add sound effects
        self.optionsCloseSfx = None # base.loadSfx(DMenuResources.Settings_Close) # ALTIS: TODO: Add sound effects

        self.Music_Label = None
        self.Music_toggleSlider = None
        self.SoundFX_Label = None
        self.SoundFX_toggleSlider = None
        self.ToonChatSounds_Label = None
        self.ToonChatSounds_toggleButton = None
        self.WASD_Label = None
        self.WASD_toggleButton = None
        self.keymapDialogButton = None
        self.Widescreen_Label = None
        self.AspectRatioList = None
        self.DisplaySettings_Label = None
        self.DisplaySettingsButton = None
        self.fov_toggleSlider = None
        self.fov_Label = None
        self.fov_resetButton = None
        self.doorKey_Label = None
        self.doorKey_toggleButton = None
        self.doorKey_helpButton = None
        self.interactKey_Label = None
        self.interactKey_toggleButton = None
        self.interactKey_helpButton = None
        self.interactKey_help = None
        self.doorKey_help = None
        
        self.displaySettings = None
        self.displaySettingsChanged = 0
        self.displaySettingsSize = (None, None)
        self.displaySettingsFullscreen = None
        self.displaySettingsBorderless = None
        self.displaySettingsApi = None
        self.displaySettingsApiChanged = 0

        self.animations_Label = None
        self.animations_toggleButton = None

    def showOptions(self, animate = True):
        # base.playSfx(self.optionsOpenSfx) # ALTIS: TODO: Add sound effects
        self.displayOptions()
        base.transitions.fadeScreen(0.5)
        if animate:
            self.optionsNode.setColorScale(1, 1, 1, 0)
            self.optionsNode.setPos(0, 0, -.15)
            self.optionsNode.posInterval(.15, Point3(0, 0, 0)).start()
            LerpColorScaleInterval(self.optionsNode, .15, Vec4(1, 1, 1, 1), Vec4(1, 1, 1, 0)).start()
 
    def hideOptions(self, animate = True):
        # base.playSfx(self.optionsCloseSfx) # ALTIS: TODO: Add sound effects
        self.ignore('window-event')
        if animate:
            self.optionsNode.setColorScale(1, 1, 1, 1)
            self.optionsNode.posInterval(.15, Point3(0, 0, -.15)).start()
            LerpColorScaleInterval(self.optionsNode, .15, Vec4(1, 1, 1, 0), Vec4(1, 1, 1, 1)).start()
            Sequence (
            Wait(.15),
            Func(self.delAllOptions)).start()
        else:
            self.delAllOptions()

    def displayOptions(self):
        self.optionsNode = aspect2d.attachNewNode('optionsNode')
        self.optionsNode.reparentTo(aspect2d, 4000)

        self.guimodel = loader.loadModel('phase_3/models/gui/pick_a_toon_gui')
        self.guiButton = loader.loadModel('phase_3/models/gui/quit_button')
        self.quitHover = self.guimodel.find('**/QuitBtn_RLVR')

        self.optionsBox = OnscreenImage(image = 'phase_3/maps/stat_board.png')
        self.optionsBox.setTransparency(TransparencyAttrib.MAlpha)
        self.optionsBox.setPos(0, 0, 0)
        self.optionsBox.setScale(render2d, VBase3(1))
        self.optionsBox.reparentTo(self.optionsNode)

        self.soundOptionsButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = 'Sound', text_scale = .1, scale = 0.95, command = self.displaySoundOptions)
        self.soundOptionsButton.reparentTo(self.optionsNode)
        self.soundOptionsButton.setPos(-.6, 0, .7)
        self.soundOptionsButton.show()

        self.controlOptionsButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = 'Controls', text_scale = .1, scale = 0.95, command = self.displayControlOptions)
        self.controlOptionsButton.reparentTo(self.optionsNode)
        self.controlOptionsButton.setPos(0, 0, .7)
        self.controlOptionsButton.show()

        self.videoOptionsButton = DirectButton(relief = None, text_style = 3, text_fg = (1, 1, 1, 1), text = 'Video', text_scale = .1, scale = 0.95, command = self.displayVideoOptions)
        self.videoOptionsButton.reparentTo(self.optionsNode)
        self.videoOptionsButton.setPos(.6, 0, .7)
        self.videoOptionsButton.show()

        self.displaySoundOptions()

    def displaySoundOptions(self):
        self.delSoundOptions()
        self.delControlOptions()
        self.delVideoOptions()

        # Music Label
        self.Music_Label = DirectLabel(parent = self.optionsNode, relief = None, text = 'Music Volume', text_align = TextNode.ACenter, text_scale = 0.052, pos = (0, 0, 0.4))
        # Music Slider
        self.Music_toggleSlider = DirectSlider(parent = self.optionsNode, pos = (0, 0, 0.3),
                                               value = settings['musicVol'] * 100, pageSize = 5, range = (0, 100), command = self.__doMusicLevel, thumb_geom = (self.guiButton.find('**/QuitBtn_UP')), thumb_relief = None, thumb_geom_scale = 1)
        self.Music_toggleSlider.setScale(0.4, 0.4, 0.4)
        self.Music_toggleSlider.show()

        # SFX Slider
        self.SoundFX_toggleSlider = DirectSlider(parent = self.optionsNode, pos = (0, 0.0, 0.1),
                                               value = settings['sfxVol'] * 100, pageSize = 5, range = (0, 100), command = self.__doSfxLevel, thumb_geom = (self.guiButton.find('**/QuitBtn_UP')), thumb_relief = None, thumb_geom_scale = 1)
        self.SoundFX_toggleSlider.setScale(0.4, 0.4, 0.4)
        # SFX Label
        self.SoundFX_Label = DirectLabel(parent = self.optionsNode, relief = None, text = 'SFX Volume', text_align = TextNode.ACenter, text_scale = 0.052, pos = (0, 0, 0.2))

        # Toon Chat Sound Effects
        self.ToonChatSounds_toggleButton = DirectButton(parent = self.optionsNode, relief = None, image = (self.guiButton.find('**/QuitBtn_UP'),
         self.guiButton.find('**/QuitBtn_DN'),
         self.guiButton.find('**/QuitBtn_RLVR'),
         self.guiButton.find('**/QuitBtn_UP')), image3_color = Vec4(0.5, 0.5, 0.5, 0.5), image_scale = (0.7, 1, 1), text = '', text3_fg = (0.5, 0.5, 0.5, 0.75), text_scale = 0.052, text_pos = (0, -.02), pos = (0, 0, -.1), command = self.__doToggleToonChatSounds)
        self.ToonChatSounds_toggleButton.setScale(0.8)
        self.ToonChatSounds_Label = DirectLabel(parent = self.optionsNode, relief = None, text = 'Toon Chat Sounds', text_align = TextNode.ACenter, text_scale = 0.052, pos = (0, 0, 0))

        # Set Button Text
        self.__setToonChatSoundsButton()

    def displayControlOptions(self):
        self.delSoundOptions()
        self.delControlOptions()
        self.delVideoOptions()

        # Key Remapping
        self.WASD_Label = DirectLabel(parent = self.optionsNode, relief = None, text = '', text_align = TextNode.ACenter, text_scale = 0.052, text_wordwrap = 16, pos = (0, 0, .4))
        self.WASD_toggleButton = DirectButton(parent = self.optionsNode, relief = None, image = (self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.7, 1, 1), text = '', text_scale = 0.052, text_pos = (0, -.02), pos = (0, 0, .3), command = self.__doToggleWASD)

        self.keymapDialogButton = DirectButton(parent = self.optionsNode, relief = None, image = (self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.7, 1, 1), text = 'Change Keybinds', text_scale = (0.03, 0.05, 1), text_pos = (0, -.02), pos = (0, 0, .2), command = self.__openKeyRemapDialog)
        self.keymapDialogButton.setScale(1.55, 1.0, 1.0)

        self.interactKey_Label = DirectLabel(self.optionsNode, relief = None, text = '', text_align = TextNode.ACenter,
                                      text_scale = .052, text_wordwrap = 16,
                                      pos = (0, 0, .1))

        self.interactKey_toggleButton = DirectButton(self.optionsNode, relief = None, image = (
        self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = (0.7, 1, 1), text = '', text_scale = .052,
                                              text_pos = (0, -.02),
                                              pos = (0, 0, 0),
                                              command = self.__doToggleInteractKey)
                                              
        self.interactKey_helpButton = DirectButton(self.interactKey_toggleButton, relief = None, image = 'phase_3/maps/dmenu/help.png', scale = .05, pos = (.3, 0, 0))
        self.interactKey_helpButton.setTransparency(1)


        self.doorKey_Label = DirectLabel(self.optionsNode, relief = None, text = '', text_align = TextNode.ACenter,
                                      text_scale = .052, text_wordwrap = 16,
                                      pos = (0, 0, -.1))

        self.doorKey_toggleButton = DirectButton(self.optionsNode, relief = None, image = (
        self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')),
                                              image_scale = (0.7, 1, 1), text = '', text_scale = .052,
                                              text_pos = (0, -.02),
                                              pos = (0, 0, -.2),
                                              command = self.__doToggleDoorKey)
        self.doorKey_helpButton = DirectButton(self.doorKey_toggleButton, relief = None, image = 'phase_3/maps/dmenu/help.png', scale = .05, pos = (.3, 0, 0))
        self.doorKey_helpButton.setTransparency(1)
        
        self.__doHelpInteractKey()
        self.__doHelpDoorKey()
        self.interactKey_help.hide()
        self.doorKey_help.hide()

        self.interactKey_helpButton.bind(DirectGuiGlobals.ENTER, self.showInteractKeyHelp)
        self.interactKey_helpButton.bind(DirectGuiGlobals.EXIT, self.hideInteractKeyHelp)
        self.doorKey_helpButton.bind(DirectGuiGlobals.ENTER, self.showDoorKeyHelp)
        self.doorKey_helpButton.bind(DirectGuiGlobals.EXIT, self.hideDoorKeyHelp)
        
        # Set Button Text
        self.__setWASDButton()
        self.__setDoorKey()
        self.__setInteractKey()

    def displayVideoOptions(self):
        self.delSoundOptions()
        self.delControlOptions()
        self.delVideoOptions()

        # Aspect Ratio Options
        self.AspectRatioList = DirectOptionMenu(relief = None, parent = self.optionsNode, text_align = TextNode.ACenter, items = GraphicsOptions.AspectRatioLabels, command = self.__doWidescreen, text_scale = .6,
        popupMarker_pos = (-1, 0, 0),
        popupMarker_relief = None,
        highlightScale = (1.1, 1.1),
        image = (self.guiButton.find('**/QuitBtn_UP'),
        self.guiButton.find('**/QuitBtn_DN'),
        self.guiButton.find('**/QuitBtn_RLVR'),
        self.guiButton.find('**/QuitBtn_UP')), image_scale = 8, image3_color = Vec4(0.5, 0.5, 0.5, 0.5), text = '', text3_fg = (0.5, 0.5, 0.5, 0.75), text_pos = (0, -.02), pos = (0, 0, .3), image_pos = (0, 0, 0), item_text_align = TextNode.ACenter, popupMenu_text_scale = .5, item_relief = None, item_pressEffect = 1)
        self.AspectRatioList.setScale(0.1)
        self.AspectRatioList.set(base.Widescreen)
        self.Widescreen_Label = DirectLabel(parent = self.optionsNode, relief = None, text = 'Aspect Ratio', text_align = TextNode.ACenter, text_scale = 0.052, pos = (0, 0, .4))

        self.DisplaySettings_Label = DirectLabel(parent = self.optionsNode, relief = None, text = '', text_align = TextNode.ACenter, text_scale = 0.052, text_wordwrap = 16, pos = (0, 0, .2))
        self.DisplaySettingsButton = DirectButton(parent = self.optionsNode, relief = None, image = (self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')), image3_color = Vec4(0.5, 0.5, 0.5, 0.5), image_scale = (0.7, 1, 1), text = TTLocalizer.OptionsPageChange, text3_fg = (0.5, 0.5, 0.5, 0.75), text_scale = 0.052, text_pos = (0, -.02), pos = (0, 0, .1), command = self.__doDisplaySettings)

        self.fov_Label = DirectLabel(parent = self.optionsNode, relief = None, text = 'Field of view', text_align = TextNode.ACenter, text_scale = 0.052, text_wordwrap = 16, pos = (0, 0, 0))

        self.fov_toggleSlider = DirectSlider(parent = self.optionsNode, pos = (0, 0, -.1),
                                               value = settings['fieldofview'], pageSize = 5, range = (30, 120), command = self.__doFovLevel, thumb_geom = (self.guiButton.find('**/QuitBtn_UP')), thumb_relief = None, thumb_geom_scale = 1)
        self.fov_toggleSlider.setScale(0.25)
        self.fov_resetButton = DirectButton(parent = self.optionsNode, relief = None, image = (self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.7, 1, 1), text = 'Reset FOV', text_scale = 0.052, text_pos = (0, -.02), pos = (0, 0, -.2), command = self.__resetFov)
        self.fovsliderText = OnscreenText('0.0', scale = .3, pos = (0, .1), fg = (1, 1, 1, 1), style = 3)
        self.fovsliderText.reparentTo(self.fov_toggleSlider.thumb)
        self.animations_Label = DirectLabel(parent = self.optionsNode, relief = None, text = '', text_align = TextNode.ACenter, text_scale = 0.052, text_wordwrap = 16, pos = (0, 0, -.3))
        self.animations_toggleButton = DirectButton(parent = self.optionsNode, relief = None, image = (self.guiButton.find('**/QuitBtn_UP'), self.guiButton.find('**/QuitBtn_DN'), self.guiButton.find('**/QuitBtn_RLVR')), image_scale = (0.7, 1, 1), text = '', text_scale = 0.052, text_pos = (0, -.02), pos = (0, 0, -.4), command = self.__doToggleAnimations)
        self.__doFovLevel()
        self.__setDisplaySettings()
        self.__setAnimationsButton()
        # TODO: Add more graphics options like Resolution, and more graphics options like in POTCO to allow changing quality of textures, etc.

    def delSoundOptions(self):
        if self.Music_Label:
            self.Music_Label.destroy()
            self.Music_Label = None

        if self.Music_toggleSlider:
            self.Music_toggleSlider.destroy()
            self.Music_toggleSlider = None

        if self.SoundFX_Label:
            self.SoundFX_Label.destroy()
            self.SoundFX_Label = None

        if self.SoundFX_toggleSlider:
            self.SoundFX_toggleSlider.destroy()
            self.SoundFX_toggleSlider = None

        if self.ToonChatSounds_Label:
            self.ToonChatSounds_Label.destroy()
            self.ToonChatSounds_Label = None

        if self.ToonChatSounds_toggleButton:
            self.ToonChatSounds_toggleButton.destroy()
            self.ToonChatSounds_toggleButton = None

    def delControlOptions(self):
        if self.WASD_Label:
            self.WASD_Label.destroy()
            self.WASD_Label = None

        if self.WASD_toggleButton:
            self.WASD_toggleButton.destroy()
            self.WASD_toggleButton = None

        if self.keymapDialogButton:
            self.keymapDialogButton.destroy()
            self.keymapDialogButton = None

        if self.doorKey_Label:
            self.doorKey_Label.destroy()
            self.doorKey_Label = None

        if self.doorKey_toggleButton:
            self.doorKey_toggleButton.destroy()
            self.doorKey_toggleButton = None

        if self.doorKey_helpButton:
            self.doorKey_helpButton.destroy()
            self.doorKey_helpButton = None
            
        if self.interactKey_Label:
            self.interactKey_Label.destroy()
            self.interactKey_Label = None

        if self.interactKey_toggleButton:
            self.interactKey_toggleButton.destroy()
            self.interactKey_toggleButton = None
            
        if self.interactKey_helpButton:
            self.interactKey_helpButton.destroy()
            self.interactKey_helpButton = None
            
        if self.interactKey_help:
            self.interactKey_help.destroy()
            self.interactKey_help = None
        if self.doorKey_help:
            self.doorKey_help.destroy()
            self.doorKey_help = None
        
    def delVideoOptions(self):
        if self.Widescreen_Label:
            self.Widescreen_Label.destroy()
            self.Widescreen_Label = None

        if self.AspectRatioList:
            self.AspectRatioList.destroy()
            self.AspectRatioList = None

        if self.DisplaySettings_Label:
            self.DisplaySettings_Label.destroy()
            self.DisplaySettings_Label = None

        if self.DisplaySettingsButton:
            self.DisplaySettingsButton.destroy()
            self.DisplaySettingsButton = None

        if self.fov_toggleSlider:
            self.fov_toggleSlider.destroy()
            self.fov_toggleSlider = None
            self.fov_Label.destroy()
            self.fov_Label = None
            self.fov_resetButton.destroy()
            self.fov_resetButton = None

        if self.animations_Label:
            self.animations_Label.destroy()
            self.animations_Label = None
            self.animations_toggleButton.destroy()
            self.animations_toggleButton = None

    def delAllOptions(self):
        base.transitions.noFade()
        self.delSoundOptions()
        self.delControlOptions()
        self.delVideoOptions()

        self.optionsBox.destroy()
        del self.optionsBox

        self.optionsNode.removeNode()
        del self.optionsNode

        # EZ copy from optionspage.py
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

    def __doWidescreen(self, ratio):
        messenger.send('wakeup')
        ratio = self.AspectRatioList.selectedIndex
        if base.Widescreen != ratio:
            base.Widescreen = ratio
            settings['Widescreen'] = ratio
            self.settingsChanged = 1
            base.updateAspectRatio()

    def __doToggleWASD(self):
        messenger.send('wakeup')
        if base.wantCustomControls:
            base.wantCustomControls = False
            settings['want-Custom-Controls'] = False
        else:
            base.wantCustomControls = True
            settings['want-Custom-Controls'] = True
        base.reloadControls()
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

    def __doDisplaySettings(self):
        if self.displaySettings == None:
            self.displaySettings = DisplaySettingsDialog.DisplaySettingsDialog()
            self.displaySettings.load()
            base.accept(self.displaySettings.doneEvent, self.__doneDisplaySettings)
        self.displaySettings.enter(True, False)

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

    def __doToggleAnimations(self):
        if settings['smoothanimations'] == True:
            settings['smoothanimations'] = False
        else:
            settings['smoothanimations'] = True
        self.settingsChanged = 1
        self.__setAnimationsButton()

    def __setAnimationsButton(self):
        if settings['smoothanimations'] == True:
            self.animations_Label['text'] = 'Smooth Animations ON'
            self.animations_toggleButton['text'] = 'Turn Off\n\n(REQUIRES RESTART)'
        else:
            self.animations_Label['text'] = 'Smooth Animations OFF'
            self.animations_toggleButton['text'] = 'Turn On\n\n(REQUIRES RESTART)'

    def __doToggleDoorKey(self):
        if settings['doorkey'] == True:
            settings['doorkey'] = False
        else:
            settings['doorkey'] = True
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

    def __doToggleInteractKey(self):
        if settings['interactkey'] == True:
            settings['interactkey'] = False
        else:
            settings['interactkey'] = True
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

    def windowEvent(self, win):
        self.optionsBox.setScale(render2d, Vec3(1))
        
    def __doHelpInteractKey(self):
        try:
            self.interactKey_help = OptionHelp.OptionHelp(parent = self.interactKey_helpButton, helpText = 'Enabling this option will require a key to be pressed before interacting with an NPC.', moviePath = 'phase_3/movies/ttpa_help_npc_interaction.mp4')
            self.interactKey_help.setScale(20)
            self.interactKey_help.setPos(1.5, 0, 0)
        except:
            pass
    
    def __doHelpDoorKey(self):
        try:
            self.doorKey_help = OptionHelp.OptionHelp(parent = self.doorKey_helpButton, helpText = 'Enabling this option will require a key to be pressed before using a door.', moviePath = 'phase_3/movies/ttpa_help_door_interaction.mp4')
            self.doorKey_help.setScale(20)
            self.doorKey_help.setPos(1.5, 0, 0)
        except:
            pass
        
    def showInteractKeyHelp(self, event):
        self.interactKey_help.show()
        
    def hideInteractKeyHelp(self, event):
        self.interactKey_help.hide()
                
    def showDoorKeyHelp(self, event):
        self.doorKey_help.show()
        
    def hideDoorKeyHelp(self, event):
        self.doorKey_help.hide()