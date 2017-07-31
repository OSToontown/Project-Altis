#!/usr/bin/env python2
import __builtin__

__builtin__.process = 'client'

# Temporary hack patch:
__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist = ['*']).__dict__)
from direct.extensions_native import HTTPChannel_extensions
from direct.extensions_native import Mat3_extensions
from direct.extensions_native import VBase3_extensions
from direct.extensions_native import VBase4_extensions
from direct.extensions_native import NodePath_extensions
from panda3d.core import loadPrcFile

# if __debug__:
#     loadPrcFile('config/general.prc')
#     loadPrcFile('config/release/dev.prc')
# else:
# config = niraidata.CONFIG
# config = aes.decrypt(config, key, iv)

config = """# Window settings:
window-title Project Altis [BETA 1.0.4]
win-origin -2 -2
icon-filename phase_3/etc/icon.ico
cursor-filename phase_3/etc/toonmono.cur
show-frame-rate-meter #f

# Altis Engine 3.0
want-vive #f
want-android #f
want-headless #f
want-live-updates #f
want-cuda #t
loader-num-threads 25

# Debug
default-directnotify-level info
notify-level-DistributedNPCScientistAI info
want-pstats #f

# Audio:
audio-library-name p3fmod_audio

# Graphics:
aux-display pandagl
aux-display pandadx9
aux-display p3tinydisplay

# Models:
model-cache-models #f
model-cache-textures #f
default-model-extension .bam

# Performance
smooth-enable-prediction 1
smooth-enable-smoothing 1
smooth-lag 0.4
smooth-max-future 1.0
smooth-min-suggest-resync 0

average-frame-rate-interval 60.0
clock-frame-rate 60.0

# Preferences:
preferences-filename preferences.json

# Backups:
backups-filepath backups/
backups-extension .json

# Server:
server-timezone EST/EDT/-5
server-port 7198
account-bridge-filename astron/databases/account-bridge.db

# Performance:
sync-video #f
texture-power-2 none
gl-check-errors #f
garbage-collect-states #f

# Egg object types:
egg-object-type-barrier <Scalar> collide-mask { 0x01 } <Collide> { Polyset descend }
egg-object-type-trigger <Scalar> collide-mask { 0x01 } <Collide> { Polyset descend intangible }
egg-object-type-sphere <Scalar> collide-mask { 0x01 } <Collide> { Sphere descend }
egg-object-type-trigger-sphere <Scalar> collide-mask { 0x01 } <Collide> { Sphere descend intangible }
egg-object-type-floor <Scalar> collide-mask { 0x02 } <Collide> { Polyset descend }
egg-object-type-dupefloor <Scalar> collide-mask { 0x02 } <Collide> { Polyset keep descend }
egg-object-type-camera-collide <Scalar> collide-mask { 0x04 } <Collide> { Polyset descend }
egg-object-type-camera-collide-sphere <Scalar> collide-mask { 0x04 } <Collide> { Sphere descend }
egg-object-type-camera-barrier <Scalar> collide-mask { 0x05 } <Collide> { Polyset descend }
egg-object-type-camera-barrier-sphere <Scalar> collide-mask { 0x05 } <Collide> { Sphere descend }
egg-object-type-model <Model> { 1 }
egg-object-type-dcs <DCS> { 1 }

# Safe zones:
want-safe-zones #t
want-toontown-central #t
want-donalds-dock #t
want-daisys-garden #t
want-minnies-melodyland #t
want-the-burrrgh #t
want-donalds-dreamland #t
want-goofy-speedway #t
want-outdoor-zone #t
want-golf-zone #t

# Weather system
want-weather #f

# Options Page
change-display-settings #t
change-display-api #t

# Safe zone settings:
want-treasure-planners #t
want-suit-planners #t
want-butterflies #f

# Classic characters:
want-classic-chars #f
want-mickey #f
want-donald-dock #f
want-daisy #f
want-minnie #f
want-pluto #f
want-donald-dreamland #f
want-chip-and-dale #f
want-goofy #f

# Trolley minigames:
want-minigames #t
want-photo-game #f
want-travel-game #f

# Picnic table board games:
want-game-tables #f

# Cog Battles
base-xp-multiplier 5.0

# Cog headquarters:
want-cog-headquarters #t
want-sellbot-headquarters #t
want-cashbot-headquarters #t
want-lawbot-headquarters #t
want-bossbot-headquarters #t

# Cashbot boss:
want-resistance-toonup #f
want-resistance-restock #f

# Cog buildings:
want-cogbuildings #t

# Optional:
show-total-population #f
want-mat-all-tailors #t
want-long-pattern-game #f
show-population #t
show-total-population #t

# Animated Props
zero-pause-mult 1.0

# Interactive Props
randomize-interactive-idles #t
interactive-prop-random-idles #t
interactive-prop-info #f
props-buff-battles #t
prop-idle-pause-time 0.0

# Events
want-charity-screen #t

# Developer options:
want-dev #f
want-pstats #f
want-directtools #f
want-tk #f

# Holidays
active-holidays 64, 65, 66 #128, 116, 63

# Temporary:
want-old-fireworks #t


# Live updates:
want-live-updates #t

# Server:
server-version TTPA-Beta-1.0.4
shard-low-pop 50
shard-mid-pop 80

#Resources
model-path /

# Core features:
want-pets #t
want-parties #f
want-cogdominiums #t
want-achievements #f

# Chat:
want-whitelist #t

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t

# Developer options:
want-dev #f"""

import sys
from panda3d.core import *
import StringIO
io = StringIO.StringIO(config)
vfs = VirtualFileSystem.getGlobalPtr()
import glob

for line in io.readlines():
    # check if the current line is a comment...
    if line.startswith('#'):
        continue

    # print line
    # load the prc file value
    loadPrcFileData('', line)
del config

from direct.directnotify.DirectNotifyGlobal import directNotify
from otp.settings.Settings import Settings

notify = directNotify.newCategory('AltisClient')
notify.setInfo(True)

preferencesFilename = ConfigVariableString(
    'preferences-filename', 'preferences.json').getValue()
notify.info('Reading %s...' % preferencesFilename)
__builtin__.settings = Settings(preferencesFilename)
from toontown.settings import ToontownSettings
__builtin__.ttsettings = ToontownSettings

for setting in ttsettings.DefaultSettings:
    if setting not in settings:
        settings[setting] = ttsettings.DefaultSettings[setting]

loadPrcFileData('Settings: res', 'win-size %d %d' % tuple(settings.get('res', (1280, 720))))
loadPrcFileData('Settings: fullscreen', 'fullscreen %s' % settings['fullscreen'])
loadPrcFileData('Settings: music', 'audio-music-active %s' % settings['music'])
loadPrcFileData('Settings: sfx', 'audio-sfx-active %s' % settings['sfx'])
loadPrcFileData('Settings: musicVol', 'audio-master-music-volume %s' % settings['musicVol'])
loadPrcFileData('Settings: sfxVol', 'audio-master-sfx-volume %s' % settings['sfxVol'])
loadPrcFileData('Settings: loadDisplay', 'load-display %s' % settings['loadDisplay'])
loadPrcFileData('Settings: toonChatSounds', 'toon-chat-sounds %s' % settings['toonChatSounds'])
loadPrcFileData('', 'texture-anisotropic-degree %d' % settings['anisotropic-filtering'])
loadPrcFileData('', 'framebuffer-multisample %s' % settings['anti-aliasing'])
loadPrcFileData('', 'sync-video %s' % settings['vertical-sync'])

vfs = VirtualFileSystem.getGlobalPtr()
DefaultPhases = (3, 3.5, 4, 5, 5.5, 6, 7, 8, 9, 10, 11, 12, 13)
import glob
notify.info("Loading Default Pack...")
for file in glob.glob('resources/default/*.mf'):
    if float(file.replace('.mf', '').replace('resources/default\phase_', '')) in DefaultPhases:
        mf = Multifile()
        mf.openReadWrite(Filename(file))
        names = mf.getSubfileNames()
        vfs.mount(mf, Filename('/'), 0)
        notify.info('Successfully Mounted:' + file)
notify.info("Default Pack Loaded!")
from toontown.toonbase.ContentPackManager import ContentPackManager
__builtin__.ContentPackMgr = ContentPackManager()
ContentPackMgr.loadAll()

loadDisplay = settings.get('loadDisplay', 'pandagl')
loadPrcFileData('', 'load-display %s' % settings['loadDisplay'])

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

if launcher.isDummy():
    http = HTTPClient()
else:
    http = launcher.http

from toontown.toonbase import ToontownGlobals
tempLoader = Loader()

from direct.gui import DirectGuiGlobals
from direct.gui.DirectGui import *

from toontown.pgui import DirectGuiGlobals as PGUIGlobals

DirectGuiGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
PGUIGlobals.setDefaultFontFunc(ToontownGlobals.getInterfaceFont)
launcher.setPandaErrorCode(7)
notify.info('Loading AltisBase...')
from toontown.toonbase import ToonBase
ToonBase.ToonBase()
from panda3d.core import *
if base.win is None:
    notify.error('Unable to open window; aborting.')

launcher.setPandaErrorCode(0)
launcher.setPandaWindowOpen()
ConfigVariableDouble('decompressor-step-time').setValue(0.01)
ConfigVariableDouble('extractor-step-time').setValue(0.01)
backgroundNode = tempLoader.loadSync(Filename('phase_3/models/gui/loading-background'))
backgroundNodePath = aspect2d.attachNewNode(backgroundNode, 0)
backgroundNodePath.setPos(0.0, 0.0, 0.0)
backgroundNodePath.setScale(render2d, VBase3(1))
backgroundNodePath.find('**/fg').hide()
logo = OnscreenImage(
    image = 'phase_3/maps/toontown-logo.png',
    scale = (1 / (4.0 / 3.0), 1, 1 / (4.0 / 3.0)),
    pos = backgroundNodePath.find('**/fg').getPos())
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

# For Devs only. (The below)
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

version = OnscreenText(serverVersionText, pos = (-1.3, -0.975), scale = 0.06, fg = Vec4(0, 0, 0, 1), align = TextNode.ALeft)
version.setPos(0.03, 0.03)
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
        base.run()
    except SystemExit:
        raise
    except:
        from toontown.toonbase import ToonPythonUtil as PythonUtil
        print PythonUtil.describeException()
        from raven import Client
        Client('https://9f93fee0d57347bdae79c1190261c775:a0259c6732514a7a8a7f13446af83a3e@sentry.io/185896').captureMessage(message=PythonUtil.describeException())
        raise
