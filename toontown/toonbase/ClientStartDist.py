# This is a temp patch.
# It should really be done by the runtime (e.g. altis.exe):
import sys
import __builtin__

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: list

# Disable both dev,debug before anything else.
# This is to make sure the distrubution client doesn't
# get any special perms or anything of the sort.
__builtin__.__dev__ = False

#def __runfunc(*args, **kw):
#    raise SystemExit

# replace these methods to prevent injection...
#__builtin__.exec = __runfunc
#__builtin__.eval = __runfunc
#__builtin__.compile = __runfunc
#__builtin__.execfile = __runfunc
#__builtin__.globals = __runfunc
#__builtin__.locals = __runfunc

# TODO: append resources
import aes
import niraidata

iv = '\0' * 16
key = 'g89a1hU0acBrlcru'

#config = niraidata.CONFIG
#config = aes.decrypt(config, key, iv)

config = """# Window settings:
window-title Project Altis [ALPHA 1.2.4]
win-origin -2 -2
icon-filename phase_3/etc/icon.ico
cursor-filename phase_3/etc/toonmono.cur
show-frame-rate-meter #f

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
smooth-max-future 0.4
smooth-min-suggest-resync 15

average-frame-rate-interval 60.0
clock-frame-rate 60.0

# Textures:
texture-anisotropic-degree 16

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
server-version TTPA-Alpha-1.2.4
shard-low-pop 50
shard-mid-pop 150

# DC File
dc-file config/toon.dc

#Resources
model-path /

# Core features:
want-pets #t
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

del iv
del key

from panda3d.core import *
import StringIO

io = StringIO.StringIO(config)

vfs = VirtualFileSystem.getGlobalPtr()
import glob
print("No Content Packs Detected!")
print("Loading Default Pack...")
for file in glob.glob('resources/default/*.mf'):
    mf = Multifile()
    mf.openReadWrite(Filename(file))
    names = mf.getSubfileNames()
    vfs.mount(mf, Filename('/'), 0)
    print('Successfully Mounted:' + file[13:])
print("Default Pack Loaded!")

for line in io.readlines():
    # check if the current line is a comment...
    if line.startswith('#'):
        continue

    #print line
    # load the prc file value
    loadPrcFileData('', line)

del config

# Finally, start the game:
import toontown.toonbase.ClientStart
