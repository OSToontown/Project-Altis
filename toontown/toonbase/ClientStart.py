#!/usr/bin/env python2
import __builtin__

__builtin__.process = 'client'

# Temporary hack patch:
__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist=['*']).__dict__)
from direct.extensions_native import HTTPChannel_extensions
from direct.extensions_native import Mat3_extensions
from direct.extensions_native import VBase3_extensions
from direct.extensions_native import VBase4_extensions
from direct.extensions_native import NodePath_extensions
from panda3d.core import loadPrcFile

if __debug__:
    loadPrcFile('config/general.prc')
    loadPrcFile('config/release/dev.prc')

from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.settings.Settings import Settings

notify = directNotify.newCategory('ClientStart')
notify.setInfo(True)

preferencesFilename = ConfigVariableString(
    'preferences-filename', 'preferences.json').getValue()
notify.info('Reading %s...' % preferencesFilename)
__builtin__.settings = Settings(preferencesFilename)
if 'fullscreen' not in settings:
    settings['fullscreen'] = False
if 'music' not in settings:
    settings['music'] = True
if 'sfx' not in settings:
    settings['sfx'] = True
if 'musicVol' not in settings:
    settings['musicVol'] = 1.0
if 'sfxVol' not in settings:
    settings['sfxVol'] = 1.0
if 'loadDisplay' not in settings:
    settings['loadDisplay'] = 'pandagl'
if 'toonChatSounds' not in settings:
    settings['toonChatSounds'] = True
if 'newGui' not in settings:
    settings['newGui'] = False
if 'show-disclaimer' not in settings:
    settings['show-disclaimer'] = True
if 'fieldofview' not in settings:
    settings['fieldofview'] = 52
if 'show-cog-levels' not in settings:
    settings['show-cog-levels'] = True
if 'health-meter-mode' not in settings:
    settings['health-meter-mode'] = 2
if 'experienceBarMode' not in settings:
    settings['experienceBarMode'] = True
settings['newGui'] = False # Force this to be false
loadPrcFileData('Settings: res', 'win-size %d %d' % tuple(settings.get('res', (1280, 720))))
loadPrcFileData('Settings: fullscreen', 'fullscreen %s' % settings['fullscreen'])
loadPrcFileData('Settings: music', 'audio-music-active %s' % settings['music'])
loadPrcFileData('Settings: sfx', 'audio-sfx-active %s' % settings['sfx'])
loadPrcFileData('Settings: musicVol', 'audio-master-music-volume %s' % settings['musicVol'])
loadPrcFileData('Settings: sfxVol', 'audio-master-sfx-volume %s' % settings['sfxVol'])
loadPrcFileData('Settings: loadDisplay', 'load-display %s' % settings['loadDisplay'])
loadPrcFileData('Settings: toonChatSounds', 'toon-chat-sounds %s' % settings['toonChatSounds'])

'''loadDisplay = settings.get('loadDisplay', 'pandagl')
loadPrcFileData('', 'load-display' % settings['loadDisplay'])'''

import os
import time
import sys
import random
import __builtin__

try:
    from toontown.launcher.TTALauncher import TTALauncher
    launcher = TTALauncher()
    __builtin__.launcher = launcher
except Exception as e:
    raise (e)

notify.info('Starting the game...')
if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http

from toontown.toonbase import ToontownGlobals
tempLoader = Loader()
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *

from toontown.pgui import DirectGuiGlobals as PGUIGlobals

notify.info('Setting the default font...')
DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
PGUIGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
from toontown.toonbase import ToonBase
ToonBase.ToonBase()
from pandac.PandaModules import *
if base.win is None:
    notify.error('Unable to open window; aborting.')
    
launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').hide()
logo = OnscreenImage(
    image='phase_3/maps/toontown-logo.png',
    scale=(1 / (4.0/3.0), 1, 1 / (4.0/3.0)),
    pos=backgroundNodePath.find('**/fg').getPos())
logo.setTransparency(TransparencyAttrib.MAlpha)
logo.setBin('fixed', 20)
logo.reparentTo(backgroundNodePath)
backgroundNodePath.find('**/bg').setBin('fixed', 10)
base.graphicsEngine.renderFrame()
DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
DirectGuiGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
PGUIGlobals.setDefaultRolloverSound(base.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
PGUIGlobals.setDefaultClickSound(base.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
PGUIGlobals.setDefaultDialogGeom(loader.loadModel('phase_3/models/gui/dialog_box_gui'))
from toontown.toonbase import TTLocalizer
from otp.otpbase import OTPGlobals
OTPGlobals.setDefaultProductPrefix(TTLocalizer.ProductPrefix)

#For Devs only. (The below)
'''from direct.stdpy import threading, thread
def __inject_wx(_):
    code = textbox.GetValue()
    exec (code, globals())

def openInjector_wx():
    import wx
    
    app = wx.App(redirect = False)
        
    frame = wx.Frame(None, title = "TTPA Dev Injector", size=(640, 400), style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.MINIMIZE_BOX)
    panel = wx.Panel(frame)
    button = wx.Button(parent = panel, id = -1, label = "Inject", size = (50, 20), pos = (295, 0))
    global textbox
    textbox = wx.TextCtrl(parent = panel, id = -1, pos = (20, 22), size = (600, 340), style = wx.TE_MULTILINE)
    frame.Bind(wx.EVT_BUTTON, __inject_wx, button)

    frame.Show()
    app.SetTopWindow(frame)
    
    textbox.AppendText(" ")
    
    threading.Thread(target = app.MainLoop).start()

openInjector_wx()'''

if base.musicManagerIsValid:
    music = base.loader.loadMusic('phase_3/audio/bgm/tt_theme.ogg')
    if music:
        music.setLoop(1)
        music.setVolume(0.9)
        music.play()
    notify.info('Loading the default GUI sounds...')
    DirectGuiGlobals.setDefaultRolloverSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_rollover.ogg'))
    DirectGuiGlobals.setDefaultClickSound(base.loader.loadSfx('phase_3/audio/sfx/GUI_create_toon_fwd.ogg'))
else:
    music = None
from toontown.toonbase import ToontownLoader
from direct.gui.DirectGui import *
serverVersion = base.config.GetString('server-version', 'no_version_set')

'''
Let's have these here so you can tell if dev or debug mode is enabled or not
easily.
'''
if __dev__:
    serverVersionText = serverVersion + "-dev"
elif __debug__:
    serverVersionText = serverVersion + "-debug"
else:
    serverVersionText = serverVersion
    
version = OnscreenText(serverVersionText, pos=(-1.3, -0.975), scale=0.06, fg=Vec4(0, 0, 0, 1), align=TextNode.ALeft)
version.setPos(0.03,0.03)
version.reparentTo(base.a2dBottomLeft)
from toontown.suit import Suit
Suit.loadModels()
loader.beginBulkLoad('init', TTLocalizer.LoaderLabel, 138, 0, TTLocalizer.TIP_NONE, 0)
from toontown.toonbase.ToonBaseGlobal import *
from direct.showbase.MessengerGlobal import *
from toontown.distributed import ToontownClientRepository
cr = ToontownClientRepository.ToontownClientRepository(serverVersion, launcher)
cr.music = music
del music
base.initNametagGlobals()
base.cr = cr
loader.endBulkLoad('init')
from otp.friends import FriendManager
from otp.distributed.OtpDoGlobals import *
cr.generateGlobalObject(OTP_DO_ID_FRIEND_MANAGER, 'FriendManager')
if not launcher.isDummy():
    base.startShow(cr, launcher.getGameServer())
else:
    base.startShow(cr)
backgroundNodePath.reparentTo(hidden)
backgroundNodePath.removeNode()
del backgroundNodePath
del backgroundNode
del tempLoader
version.cleanup()
del version
base.loader = base.loader
__builtin__.loader = base.loader
autoRun = ConfigVariableBool('toontown-auto-run', 1)
if autoRun:
    try:
        run()
    except SystemExit:
        raise
    except:
        from toontown.toonbase import ToonPythonUtil as PythonUtil
        print PythonUtil.describeException()
        raise