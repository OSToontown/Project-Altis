import atexit
import math
import os
import random
import shutil
from sys import platform
import sys
import tempfile
import time
import ToontownAsyncLoader
from direct.directnotify import DirectNotifyGlobal
from direct.filter.CommonFilters import CommonFilters
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *
from toontown.toonbase.ToonPythonUtil import *
from direct.showbase.Transitions import Transitions
from direct.task import *
from pandac.PandaModules import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownLoader
from otp.otpbase import OTPBase
from otp.otpbase import OTPGlobals
from otp.otpbase import OTPLauncherGlobals
from toontown.launcher import ToontownDownloadWatcher
from toontown.margins import MarginGlobals
from toontown.margins.MarginManager import MarginManager
from toontown.nametag import NametagGlobals
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownAccess
from toontown.toonbase import ToontownBattleGlobals
from toontown.toontowngui import TTDialog
from toontown.options import GraphicsOptions
from toontown.audio.AltisAudio import AltisAudio
from direct.interval.IntervalGlobal import Sequence, Func, Wait
from direct.task.Task import Task

class ToonBase(OTPBase.OTPBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonBase')

    def __init__(self):
        OTPBase.OTPBase.__init__(self)
        # First, build a list of all possible resolutions:
        self.resList = []
        displayInfo = self.pipe.getDisplayInformation()
        for i in xrange(displayInfo.getTotalDisplayModes()):
            width = displayInfo.getDisplayModeWidth(i)
            height = displayInfo.getDisplayModeHeight(i)
            if (width, height) not in self.resList:
                self.resList.append((width, height))

        # Next, separate the resolutions by their ratio:
        self.resDict = {}
        for res in self.resList:
            ratio = int((float(res[0])/float(res[1])) * 100000) / 100000.0
            self.resDict.setdefault(ratio, []).append(res)

        # Get the native width, height and ratio:
        self.nativeWidth = self.pipe.getDisplayWidth()
        self.nativeHeight = self.pipe.getDisplayHeight()
        self.nativeRatio = int((float(self.nativeWidth)/float(self.nativeHeight)) * 100000) / 100000.0

        # Finally, choose the best resolution if we're either fullscreen, or
        # don't have one defined in our preferences:
        fullscreen = settings.get('fullscreen', False)
        if ('res' not in settings) or fullscreen:
            if fullscreen:
                # If we're fullscreen, we want to fit the entire screen:
                res = (self.nativeWidth, self.nativeHeight)
            elif self.nativeRatio not in self.resDict:
                print "base.resDict does not contain the native resolution: %r" % self.resDict
                res = (800, 600)
            elif len(self.resDict[self.nativeRatio]) > 1:
                # We have resolutions that match our native ratio and fit it!
                # Let's use one:
                res = sorted(self.resDict[self.nativeRatio])[0]
            else:
                # Okay, we don't have any resolutions that match our native
                # ratio and fit it. Let's just use one of the second largest
                # ratio's resolutions:
                ratios = sorted(self.resDict.keys(), reverse=False)
                nativeIndex = ratios.index(self.nativeRatio)
                res = sorted(self.resDict[ratios[nativeIndex - 1]])[0]

        else:
            res = settings['res']

        # Store our result:
        settings['res'] = res

        # Reload the graphics pipe:
        properties = WindowProperties()

        properties.setSize(res[0], res[1])
        properties.setFullscreen(fullscreen)
        properties.setParentWindow(0)

        # Store the window sort for later:
        sort = self.win.getSort()

        if self.win:
            currentProperties = WindowProperties(self.win.getProperties())
            gsg = self.win.getGsg()
        else:
            currentProperties = WindowProperties.getDefault()
            gsg = None
        newProperties = WindowProperties(currentProperties)
        newProperties.addProperties(properties)
        if (gsg is None) or (currentProperties.getFullscreen() != newProperties.getFullscreen()) or (currentProperties.getParentWindow() != newProperties.getParentWindow()):
            self.openMainWindow(props=properties, gsg=gsg, keepCamera=True)
            self.graphicsEngine.openWindows()
            self.disableShowbaseMouse()
        else:
            self.win.requestProperties(properties)
            self.graphicsEngine.renderFrame()

        self.win.setSort(sort)
        self.graphicsEngine.renderFrame()
        self.graphicsEngine.renderFrame()
        
        self.audioMgr = AltisAudio()
        
        self.disableShowbaseMouse()
        self.addCullBins()
        self.debugRunningMultiplier /= OTPGlobals.ToonSpeedFactor
        self.baseXpMultiplier = self.config.GetFloat('base-xp-multiplier', 1.0)
        self.toonChatSounds = self.config.GetBool('toon-chat-sounds', 1)
        self.placeBeforeObjects = self.config.GetBool('place-before-objects', 1)
        self.endlessQuietZone = False
        self.wantDynamicShadows = 0
        self.exitErrorCode = 0
        camera.setPosHpr(0, 0, 0, 0, 0, 0)
        self.camLens.setMinFov(settings['fieldofview']/(4./3.))
        self.camLens.setNearFar(ToontownGlobals.DefaultCameraNear, ToontownGlobals.DefaultCameraFar)
        self.musicManager.setVolume(settings.get("musicVol"))
        for sfm in self.sfxManagerList:
            sfm.setVolume(settings.get("sfxVol"))
        self.sfxActive = settings.get("sfxVol") > 0.0
        self.setBackgroundColor(ToontownGlobals.DefaultBackgroundColor)
        self.screenshotSfx = self.loader.loadSfx('phase_4/audio/sfx/Photo_shutter.ogg')
        tpm = TextPropertiesManager.getGlobalPtr()
        candidateActive = TextProperties()
        candidateActive.setTextColor(0, 0, 1, 1)
        tpm.setProperties('candidate_active', candidateActive)
        candidateInactive = TextProperties()
        candidateInactive.setTextColor(0.3, 0.3, 0.7, 1)
        tpm.setProperties('candidate_inactive', candidateInactive)
        self.transitions.IrisModelName = 'phase_3/models/misc/iris'
        self.transitions.FadeModelName = 'phase_3/models/misc/fade'
        self.exitFunc = self.userExit
        if 'launcher' in __builtins__ and launcher:
            launcher.setPandaErrorCode(11)
        globalClock.setMaxDt(0.2)
        if self.config.GetBool('want-particles', 1) == 1:
            self.notify.debug('Enabling particles')
            self.enableParticles()

        # OS X Specific Actions
        if platform == "darwin":
            self.acceptOnce(ToontownGlobals.QuitGameHotKeyOSX, self.exitOSX)
            self.accept(ToontownGlobals.QuitGameHotKeyRepeatOSX, self.exitOSX)
            self.acceptOnce(ToontownGlobals.HideGameHotKeyOSX, self.hideGame)
            self.accept(ToontownGlobals.HideGameHotKeyRepeatOSX, self.hideGame)
            self.acceptOnce(ToontownGlobals.MinimizeGameHotKeyOSX, self.minimizeGame)
            self.accept(ToontownGlobals.MinimizeGameHotKeyRepeatOSX, self.minimizeGame)

        self.accept('f3', self.toggleGui)
        self.accept('panda3d-render-error', self.panda3dRenderError)
        oldLoader = self.loader
        self.loader = ToontownLoader.ToontownLoader(self)
        __builtins__['loader'] = self.loader
        
        self.asyncLoader = ToontownAsyncLoader.ToontownAsyncLoader(self)
        __builtins__['asyncloader'] = self.asyncLoader
        
        self.asyncCall = ToontownAsyncLoader.AsyncCall
        __builtins__['callAsync'] = self.asyncCall
        
        __builtins__['NO_FADE_SORT_INDEX'] = 4000
        oldLoader.destroy()
        self.accept('PandaPaused', self.disableAllAudio)
        self.accept('PandaRestarted', self.enableAllAudio)
        self.friendMode = self.config.GetBool('switchboard-friends', 0)
        self.wantPets = self.config.GetBool('want-pets', 1)
        self.wantBingo = self.config.GetBool('want-fish-bingo', 1)
        self.wantKarts = self.config.GetBool('want-karts', 1)
        self.wantNewSpecies = self.config.GetBool('want-new-species', 0)
        self.wantAchievements = self.config.GetBool('want-achievements', 1)
        self.inactivityTimeout = self.config.GetFloat('inactivity-timeout', ToontownGlobals.KeyboardTimeout)
        if self.inactivityTimeout:
            self.notify.debug('Enabling Panda timeout: %s' % self.inactivityTimeout)
            self.mouseWatcherNode.setInactivityTimeout(self.inactivityTimeout)
        self.mouseWatcherNode.setEnterPattern('mouse-enter-%r')
        self.mouseWatcherNode.setLeavePattern('mouse-leave-%r')
        self.mouseWatcherNode.setButtonDownPattern('button-down-%r')
        self.mouseWatcherNode.setButtonUpPattern('button-up-%r')
        self.randomMinigameAbort = self.config.GetBool('random-minigame-abort', 0)
        self.randomMinigameDisconnect = self.config.GetBool('random-minigame-disconnect', 0)
        self.randomMinigameNetworkPlugPull = self.config.GetBool('random-minigame-netplugpull', 0)
        self.autoPlayAgain = self.config.GetBool('auto-play-again', 0)
        self.skipMinigameReward = self.config.GetBool('skip-minigame-reward', 0)
        self.wantMinigameDifficulty = self.config.GetBool('want-minigame-difficulty', 0)
        self.minigameDifficulty = self.config.GetFloat('minigame-difficulty', -1.0)
        if self.minigameDifficulty == -1.0:
            del self.minigameDifficulty
        self.minigameSafezoneId = self.config.GetInt('minigame-safezone-id', -1)
        if self.minigameSafezoneId == -1:
            del self.minigameSafezoneId
        cogdoGameSafezoneId = self.config.GetInt('cogdo-game-safezone-id', -1)
        cogdoGameDifficulty = self.config.GetFloat('cogdo-game-difficulty', -1)
        if cogdoGameDifficulty != -1:
            self.cogdoGameDifficulty = cogdoGameDifficulty
        if cogdoGameSafezoneId != -1:
            self.cogdoGameSafezoneId = cogdoGameSafezoneId
        ToontownBattleGlobals.SkipMovie = self.config.GetBool('skip-battle-movies', 0)
        self.creditCardUpFront = self.config.GetInt('credit-card-up-front', -1)
        if self.creditCardUpFront == -1:
            del self.creditCardUpFront
        else:
            self.creditCardUpFront = self.creditCardUpFront != 0
        self.housingEnabled = self.config.GetBool('want-housing', 1)
        self.cannonsEnabled = self.config.GetBool('estate-cannons', 0)
        self.fireworksEnabled = self.config.GetBool('estate-fireworks', 0)
        self.dayNightEnabled = self.config.GetBool('estate-day-night', 0)
        self.cloudPlatformsEnabled = self.config.GetBool('estate-clouds', 0)
        self.greySpacing = self.config.GetBool('allow-greyspacing', 0)
        self.goonsEnabled = self.config.GetBool('estate-goon', 0)
        self.restrictTrialers = self.config.GetBool('restrict-trialers', 1)
        self.roamingTrialers = self.config.GetBool('roaming-trialers', 1)
        self.slowQuietZone = self.config.GetBool('slow-quiet-zone', 0)
        self.slowQuietZoneDelay = self.config.GetFloat('slow-quiet-zone-delay', 5)
        self.killInterestResponse = self.config.GetBool('kill-interest-response', 0)
        self.forceSkipTutorial = self.config.GetBool('force-skip-tutorial', 0)
        tpMgr = TextPropertiesManager.getGlobalPtr()
        WLDisplay = TextProperties()
        WLDisplay.setSlant(0.3)
        WLEnter = TextProperties()
        WLEnter.setTextColor(1.0, 0.0, 0.0, 1)
        tpMgr.setProperties('WLDisplay', WLDisplay)
        tpMgr.setProperties('WLEnter', WLEnter)
        textShadow = TextProperties()
        textShadow.setShadow(.01)
        textShadow.setTextColor(0.8, 0.4, 0.0, 1)
        tpMgr.setProperties('textShadow', textShadow)
        orangeText = TextProperties()
        orangeText.setTextColor(1.0, 0.65, 0.0, 1)
        orangeText.setTextScale(1.2)
        tpMgr.setProperties('orangeText', orangeText)
        playerGreen = TextProperties()
        playerGreen.setTextColor(0.0, 1.0, 0.2, 1.0)
        playerGreen.setShadow(.01)
        tpMgr.setProperties('playerGreen', playerGreen)
        cogGray = TextProperties()
        cogGray.setTextColor(0.2, 0.2, 0.2, 1.0)
        cogGray.setShadow(.01)
        tpMgr.setProperties('cogGray', cogGray)
        del tpMgr
        self.lastScreenShotTime = globalClock.getRealTime()
        self.accept('InputState-forward', self.__walking)
        self.canScreenShot = 1
        self.glitchCount = 0
        self.walking = 0
        self.oldX = max(1, base.win.getXSize())
        self.oldY = max(1, base.win.getYSize())
        self.aspectRatio = float(self.oldX) / self.oldY
        self.localAvatarStyle = None
        self.filters = CommonFilters(self.win, self.cam)
        
        self.wantCustomControls = settings.get('want-Custom-Controls', False)

        self.MOVE_UP = 'arrow_up'   
        self.MOVE_DOWN = 'arrow_down'
        self.MOVE_LEFT = 'arrow_left'      
        self.MOVE_RIGHT = 'arrow_right'
        self.JUMP = 'control'
        self.ACTION_BUTTON = 'delete'
        self.SCREENSHOT_KEY = 'f9'
        self.INTERACT = 'shift'
        keymap = settings.get('keymap', {})
        if self.wantCustomControls:
            self.MOVE_UP = keymap.get('MOVE_UP', self.MOVE_UP)
            self.MOVE_DOWN = keymap.get('MOVE_DOWN', self.MOVE_DOWN)
            self.MOVE_LEFT = keymap.get('MOVE_LEFT', self.MOVE_LEFT)
            self.MOVE_RIGHT = keymap.get('MOVE_RIGHT', self.MOVE_RIGHT)
            self.JUMP = keymap.get('JUMP', self.JUMP)
            self.ACTION_BUTTON = keymap.get('ACTION_BUTTON', self.ACTION_BUTTON)
            self.SCREENSHOT_KEY = keymap.get('SCREENSHOT_KEY', self.SCREENSHOT_KEY)
            self.INTERACT = keymap.get('INTERACT', self.INTERACT)
            ToontownGlobals.OptionsPageHotkey = keymap.get('OPTIONS-PAGE', ToontownGlobals.OptionsPageHotkey)
        
        self.CHAT_HOTKEY = keymap.get('CHAT_HOTKEY', 't')
        
        self.accept(self.SCREENSHOT_KEY, self.takeScreenShot)

        self.Widescreen = settings.get('aspect-ratio', 0)
        self.currentScale = settings.get('texture-scale', 1.0)
        self.setTextureScale()
        self.setRatio()
        self.updateAntiAliasing()
        self.updateAnisotrophicFiltering()
        
        self.showDisclaimer = settings.get('show-disclaimer', True) # Show this the first time the user starts the game, it is set in the settings to False once they pick a toon

        self.lodMaxRange = 750
        self.lodMinRange = 20
        self.lodDelayFactor = 0.4
        
        self.meterMode = settings.get('health-meter-mode', 2)
        
        self.wantSmoothAnims = settings.get('smoothanimations', True)
        
        self.wantTpMessages = settings.get('tpmsgs', True)
        
        self.wantFriendStatusMessagse = settings.get('friendstatusmsgs', True)
        
        self.wantDoorKey = settings.get('doorkey', False)
        
        self.wantInteractKey = settings.get('interactkey', False)
        
        self.accept('f4', self.toggleNametags)
        
        if 'experimental-touch' in settings:
            self.wantMobile = settings.get('experimental-touch', False)
        else:
            self.wantMobile = False
            
        def sp1(*args):
            self.patgui = args[0]
        
        def sp2(*args):
            self.gui2 = args[0]     
            
        def sp3(*args):
            self.newGui = args[0]     
            
        def sp4(*args):
            self.matGui = args[0]
            self.shuffleUp = self.matGui.find('**/tt_t_gui_mat_shuffleUp')
            self.shuffleDown = self.matGui.find('**/tt_t_gui_mat_shuffleDown')
            
        # Speed up the pat loading abit, have these pre-load
        asyncloader.loadModel('phase_3/models/gui/pick_a_toon_gui', callback = sp1)
        self.notify.info("Pre-loading PICK A TOON GUI")
        asyncloader.loadModel('phase_3/models/gui/quit_button', callback = sp2)
        self.notify.info("Pre-loading Button UI")
        asyncloader.loadModel('phase_3/models/gui/tt_m_gui_pat_mainGui', callback = sp3)
        self.notify.info("Pre-loading PICK A TOON GUI 2")
        asyncloader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui', callback = sp4)
        self.notify.info("Pre-loading MAKE A TOON GUI")

        self.notify.info('Subscribing to window size changed event')
        self.accept(base.win.getWindowEvent(), self.onWindowEvent)
        
        self.lockedMusic = False
            
    def updateAntiAliasing(self):
        loadPrcFileData('', 'framebuffer-multisample %s' %settings.get('anti-aliasing'))
            
    def updateAspectRatio(self):
        self.setRatio()

    def updateAnisotrophicFiltering(self):
        level = ttsettings.AnistrophicOptions[settings.get('anisotropic-filtering')]
        
        loadPrcFileData('', 'texture-anisotropic-degree %d' % level)
        
    def setRatio(self): # Set the aspect ratio
        base.setAspectRatio(GraphicsOptions.AspectRatios[self.Widescreen])
            
    def setTextureScale(self): # Set the global texture scale (TODO)
        scale = settings.get('texture-scale')
        
    def toggleTpMsgs(self):
        self.wantTpMessages = settings.get('tpmsgs', True)
        self.wantFriendStatusMessagse = settings.get('friendstatusmsgs', True)
        
    def toggleDoorKey(self):
        self.wantDoorKey = settings.get('doorkey', False)
        self.wantInteractKey = settings.get('interactkey', False)

    def openMainWindow(self, *args, **kw):
        result = OTPBase.OTPBase.openMainWindow(self, *args, **kw)
        self.setCursorAndIcon()
        return result

    def windowEvent(self, win):
        OTPBase.OTPBase.windowEvent(self, win)

        MarginGlobals.updateMarginVisibles()

    def setCursorAndIcon(self):
        tempdir = tempfile.mkdtemp()
        atexit.register(shutil.rmtree, tempdir)
        vfs = VirtualFileSystem.getGlobalPtr()

        searchPath = DSearchPath()
        if __debug__:
            searchPath.appendDirectory(Filename('resources/phase_3/etc'))
        searchPath.appendDirectory(Filename('/phase_3/etc'))

        for filename in ['toonmono.cur', 'icon.ico']:
            p3filename = Filename(filename)
            found = vfs.resolveFilename(p3filename, searchPath)
            if not found:
                return # Can't do anything past this point.

            with open(os.path.join(tempdir, filename), 'wb') as f:
                f.write(vfs.readFile(p3filename, False))

        wp = WindowProperties()
        wp.setCursorFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'toonmono.cur')))
        wp.setIconFilename(Filename.fromOsSpecific(os.path.join(tempdir, 'icon.ico')))
        self.win.requestProperties(wp)

    def addCullBins(self):
        cbm = CullBinManager.getGlobalPtr()
        cbm.addBin('ground', CullBinManager.BTUnsorted, 18)
        cbm.addBin('shadow', CullBinManager.BTBackToFront, 19)
        cbm.addBin('gui-popup', CullBinManager.BTUnsorted, 60)

    def disableShowbaseMouse(self):
        self.useDrive()
        self.disableMouse()
        if self.mouseInterface: self.mouseInterface.detachNode()
        if self.mouse2cam: self.mouse2cam.detachNode()

    def __walking(self, pressed):
        self.walking = pressed

    def toggleGui(self):
        if aspect2d.isHidden():
            aspect2d.show()
        else:
            aspect2d.hide()

    def toggleNametags(self):
        nametags3d = render.findAllMatches('**/nametag3d')
        nametags2d = render2d.findAllMatches('**/Nametag2d')
        hide = False
        for nametag in nametags2d:
            if not nametag.isHidden():
                hide = True
        for nametag in nametags3d:
            if not nametag.isHidden():
                hide = True
        for nametag in nametags3d:
            if hide:
                nametag.hide()
            else:
                nametag.show()
        for nametag in nametags2d:
            if hide:
                nametag.hide()
            else:
                nametag.show()

    def takeScreenShot(self):
        if hasattr(self, 'screenShotNotice') and self.screenShotNotice:
            self.screenShotNotice.destroy()
            taskMgr.remove('clearScreenshot')
        if not os.path.exists(TTLocalizer.ScreenshotPath):
            os.mkdir(TTLocalizer.ScreenshotPath)
            self.notify.info('Made new directory to save screenshots.')
        self.screenshotSfx.play()
        namePrefix = TTLocalizer.ScreenshotPath + launcher.logPrefix + 'screenshot'
        timedif = globalClock.getRealTime() - self.lastScreenShotTime
        if self.glitchCount > 10 and self.walking:
            return
        if timedif < 1.0 and self.walking:
            self.glitchCount += 1
            return
        if not hasattr(self, 'localAvatar'):
            self.screenshot(namePrefix=namePrefix)
            self.lastScreenShotTime = globalClock.getRealTime()
            return
        coordOnScreen = self.config.GetBool('screenshot-coords', 0)
        self.localAvatar.stopThisFrame = 1
        ctext = self.localAvatar.getAvPosStr()
        self.screenshotStr = ''
        messenger.send('takingScreenshot')
        if coordOnScreen:
            coordTextLabel = DirectLabel(pos=(-0.81, 0.001, -0.87), text=ctext, text_scale=0.05, text_fg=VBase4(1.0, 1.0, 1.0, 1.0), text_bg=(0, 0, 0, 0), text_shadow=(0, 0, 0, 1), relief=None)
            coordTextLabel.setBin('gui-popup', 0)
            strTextLabel = None
            if len(self.screenshotStr):
                strTextLabel = DirectLabel(pos=(0.0, 0.001, 0.9), text=self.screenshotStr, text_scale=0.05, text_fg=VBase4(1.0, 1.0, 1.0, 1.0), text_bg=(0, 0, 0, 0), text_shadow=(0, 0, 0, 1), relief=None)
                strTextLabel.setBin('gui-popup', 0)
        self.graphicsEngine.renderFrame()
        screenshot = self.screenshot(namePrefix=namePrefix, imageComment=ctext + ' ' + self.screenshotStr)
        self.lastScreenShotTime = globalClock.getRealTime()
        pandafile = Filename(str(ExecutionEnvironment.getCwd()) + '/' + str(screenshot))
        winfile = pandafile.toOsSpecific()
        self.screenShotNotice = DirectLabel(text = "Screenshot Saved" + ':\n' + winfile, scale = 0.05, pos = (0.0, 0.0, 0.3), text_bg = (0, 0, 0, .4), text_fg = (1, 1, 1, 1), frameColor = (1, 1, 1, 0))
        self.screenShotNotice.reparentTo(base.a2dBottomCenter)
        self.screenShotNotice.setBin('gui-popup', 0)
        if coordOnScreen:
            if strTextLabel is not None:
                strTextLabel.destroy()
            coordTextLabel.destroy()
            
        def clearScreenshotMsg(task):
            self.screenShotNotice.destroy()
            return task.done

        taskMgr.doMethodLater(5.0, clearScreenshotMsg, 'clearScreenshot')

    def addScreenshotString(self, str):
        if len(self.screenshotStr):
            self.screenshotStr += '\n'
        self.screenshotStr += str

    def initNametagGlobals(self):
        NametagGlobals.setMe(base.cam)

        NametagGlobals.setCardModel('phase_3/models/props/panel.bam')
        NametagGlobals.setArrowModel('phase_3/models/props/arrow.bam')
        NametagGlobals.setChatBalloon3dModel('phase_3/models/props/chatbox.bam')
        NametagGlobals.setChatBalloon2dModel('phase_3/models/props/chatbox_noarrow.bam')
        NametagGlobals.setThoughtBalloonModel('phase_3/models/props/chatbox_thought_cutout.bam')

        chatButtonGui = loader.loadModel('phase_3/models/gui/chat_button_gui.bam')
        NametagGlobals.setPageButton(
            chatButtonGui.find('**/Horiz_Arrow_UP'), chatButtonGui.find('**/Horiz_Arrow_DN'),
            chatButtonGui.find('**/Horiz_Arrow_Rllvr'), chatButtonGui.find('**/Horiz_Arrow_UP'))
        NametagGlobals.setQuitButton(
            chatButtonGui.find('**/CloseBtn_UP'), chatButtonGui.find('**/CloseBtn_DN'),
            chatButtonGui.find('**/CloseBtn_Rllvr'), chatButtonGui.find('**/CloseBtn_UP'))
        chatButtonGui.removeNode()

        rolloverSound = DirectGuiGlobals.getDefaultRolloverSound()
        if rolloverSound is not None:
            NametagGlobals.setRolloverSound(rolloverSound)
        
        clickSound = DirectGuiGlobals.getDefaultClickSound()
        if clickSound is not None:
            NametagGlobals.setClickSound(clickSound)

        self.marginManager = MarginManager()
        self.margins = self.aspect2d.attachNewNode(
            self.marginManager, DirectGuiGlobals.MIDGROUND_SORT_INDEX + 1)
        
        self.leftCells = [
            self.marginManager.addCell(0.1, -0.6, self.a2dTopLeft, 1),
            self.marginManager.addCell(0.1, -1.0, self.a2dTopLeft, 2),
            self.marginManager.addCell(0.1, -1.4, self.a2dTopLeft, 3)
        ]
        self.bottomCells = [
            self.marginManager.addCell(0.4, 0.1, self.a2dBottomCenter, 4),
            self.marginManager.addCell(-0.4, 0.1, self.a2dBottomCenter, 5),
            self.marginManager.addCell(-1.0, 0.1, self.a2dBottomCenter, 6),
            self.marginManager.addCell(1.0, 0.1, self.a2dBottomCenter, 7)
        ]
        self.rightCells = [
            self.marginManager.addCell(-0.1, -0.6, self.a2dTopRight, 8),
            self.marginManager.addCell(-0.1, -1.0, self.a2dTopRight, 9),
            self.marginManager.addCell(-0.1, -1.4, self.a2dTopRight, 10)
        ]

    def setCellsActive(self, cells, active):
        for cell in cells:
            cell.setActive(active)
        self.marginManager.reorganize()

    def cleanupDownloadWatcher(self):
        self.downloadWatcher.cleanup()
        self.downloadWatcher = None

    def startShow(self, cr, launcherServer = None):
        self.cr = cr
        base.graphicsEngine.renderFrame()
        self.downloadWatcher = ToontownDownloadWatcher.ToontownDownloadWatcher(TTLocalizer.LauncherPhaseNames)
        if launcher.isDownloadComplete():
            self.cleanupDownloadWatcher()
        else:
            self.acceptOnce('launcherAllPhasesComplete', self.cleanupDownloadWatcher)
        gameServer = os.environ.get('TT_GAMESERVER', 'localhost')
        # Get the base port.
        serverPort = base.config.GetInt('server-port', 7198)

        # Get the number of client-agents.
        clientagents = base.config.GetInt('client-agents', 1) - 1

        # Get a new port.
        serverPort += (random.randint(0, clientagents) * 100)

        serverList = []
        for name in gameServer.split(';'):
            url = URLSpec(name, 1)
            if config.GetBool('server-force-ssl', True):
                url.setScheme('https')
            else:
                url.setScheme('http')
            if url.getServer() == "127.0.0.1":
                url.setScheme('')

            if not url.hasPort():
                url.setPort(serverPort)
            serverList.append(url)

        cr.loginFSM.request('connect', [serverList])
        self.ttAccess = ToontownAccess.ToontownAccess()
        self.ttAccess.initModuleInfo()

        # Start detecting speed hacks:
        self.lastSpeedHackCheck = time.time()
        self.lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()
        taskMgr.add(self.__speedHackCheckTick, 'speedHackCheck-tick')

    def __speedHackCheckTick(self, task):
        elapsed = time.time() - self.lastSpeedHackCheck
        tcElapsed = TrueClock.getGlobalPtr().getLongTime() - self.lastTrueClockTime

        if tcElapsed > (elapsed + 0.05):
            # The TrueClock is running faster than it should. This means the
            # player may have sped up the process. Disconnect them:
            self.cr.stopReaderPollTask()
            self.cr.lostConnection()
            return task.done

        self.lastSpeedHackCheck = time.time()
        self.lastTrueClockTime = TrueClock.getGlobalPtr().getLongTime()

        return task.cont

    def removeGlitchMessage(self):
        self.ignore('InputState-forward')

    def exitShow(self, errorCode = None):
        self.notify.info('Exiting Toontown: errorCode = %s' % errorCode)
        if errorCode:
            launcher.setPandaErrorCode(errorCode)
        else:
            launcher.setPandaErrorCode(0)
        sys.exit()

    def setExitErrorCode(self, code):
        self.exitErrorCode = code
        if os.name == 'nt':
            exitCode2exitPage = {OTPLauncherGlobals.ExitEnableChat: 'chat',
             OTPLauncherGlobals.ExitSetParentPassword: 'setparentpassword',
             OTPLauncherGlobals.ExitPurchase: 'purchase'}
            if code in exitCode2exitPage:
                launcher.setRegistry('EXIT_PAGE', exitCode2exitPage[code])

    def getExitErrorCode(self):
        return self.exitErrorCode

    def userExit(self):
        try:
            self.localAvatar.d_setAnimState('TeleportOut', 1)
        except:
            pass

        if hasattr(self, 'ttAccess'):
            self.ttAccess.delete()
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectCloseWindow)
        base.cr._userLoggingOut = False
        try:
            localAvatar
        except:
            pass
        else:
            messenger.send('clientLogout')
            self.cr.dumpAllSubShardObjects()

        self.cr.loginFSM.request('shutdown')
        self.notify.warning('Could not request shutdown; exiting anyway.')
        self.ignore(ToontownGlobals.QuitGameHotKeyOSX)
        self.ignore(ToontownGlobals.QuitGameHotKeyRepeatOSX)
        self.ignore(ToontownGlobals.HideGameHotKeyOSX)
        self.ignore(ToontownGlobals.HideGameHotKeyRepeatOSX)
        self.ignore(ToontownGlobals.MinimizeGameHotKeyOSX)
        self.ignore(ToontownGlobals.MinimizeGameHotKeyRepeatOSX)
        self.exitShow()

    def panda3dRenderError(self):
        launcher.setPandaErrorCode(14)
        if self.cr.timeManager:
            self.cr.timeManager.setDisconnectReason(ToontownGlobals.DisconnectGraphicsError)
        self.cr.sendDisconnect()
        sys.exit()

    def getShardPopLimits(self):
        return (
            config.GetInt('shard-low-pop', ToontownGlobals.LOW_POP),
            config.GetInt('shard-mid-pop', ToontownGlobals.MID_POP),
            config.GetInt('shard-high-pop', ToontownGlobals.HIGH_POP)
        )
    def lockMusic(self):
        self.lockedMusic = True

    def unlockMusic(self):
        self.lockedMusic = False
        
    def playMusic(self, *args, **kw):
        if not self.lockedMusic:
            OTPBase.OTPBase.playMusic(self, *args, **kw)
        
    def fadeMusicIn(self, musicFile, looping = 1):
        self.audioMgr.fadeInMusic(musicFile, looping)
        
    def fadeMusicOut(self, musicFile):
        self.audioMgr.fadeOutMusic(musicFile)

    def exitOSX(self):
        self.confirm = TTDialog.TTGlobalDialog(doneEvent='confirmDone', message=TTLocalizer.OptionsPageExitConfirm, 
            style=TTDialog.TwoChoice)
        
        self.confirm.show()
        self.accept('confirmDone', self.handleConfirm)

    def handleConfirm(self):
        status = self.confirm.doneStatus
        self.ignore('confirmDone')
        self.confirm.cleanup()
        del self.confirm
        if status == 'ok':
            self.userExit()

    def hideGame(self):
        # Hacky, I know, but it works
        hideCommand = """osascript -e 'tell application "System Events"
                                            set frontProcess to first process whose frontmost is true
                                            set visible of frontProcess to false
                                       end tell'"""
        os.system(hideCommand)

    def minimizeGame(self):
        wp = WindowProperties()
        wp.setMinimized(True)
        base.win.requestProperties(wp)

    def reloadControls(self):
        self.ignore(self.SCREENSHOT_KEY)
        keymap = settings.get('keymap', {})
        self.CHAT_HOTKEY = keymap.get('CHAT_HOTKEY', 'r')
        if self.wantCustomControls:
            self.MOVE_UP = keymap.get('MOVE_UP', self.MOVE_UP)
            self.MOVE_DOWN = keymap.get('MOVE_DOWN', self.MOVE_DOWN)
            self.MOVE_LEFT = keymap.get('MOVE_LEFT', self.MOVE_LEFT)
            self.MOVE_RIGHT = keymap.get('MOVE_RIGHT', self.MOVE_RIGHT)
            self.JUMP = keymap.get('JUMP', self.JUMP)
            self.ACTION_BUTTON = keymap.get('ACTION_BUTTON', self.ACTION_BUTTON)
            self.SCREENSHOT_KEY = keymap.get('SCREENSHOT_KEY', self.SCREENSHOT_KEY)
            self.INTERACT = keymap.get('INTERACT', self.INTERACT)
            ToontownGlobals.OptionsPageHotkey = keymap.get('OPTIONS-PAGE', ToontownGlobals.OptionsPageHotkey)
        else:
            self.MOVE_UP = 'arrow_up'
            self.MOVE_DOWN = 'arrow_down'
            self.MOVE_LEFT = 'arrow_left'      
            self.MOVE_RIGHT = 'arrow_right'
            self.JUMP = 'control'
            self.ACTION_BUTTON = 'delete'
            self.SCREENSHOT_KEY = 'f9'
            self.INTERACT = 'shift'
    
        self.accept(self.SCREENSHOT_KEY, self.takeScreenShot)

    def onWindowEvent(self, window):
        settings['res'] = self.getSize()
        if window.isClosed():
            sys.exit(0)

