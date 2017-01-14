# This is a temp patch.
# It should really be done by the runtime (e.g. altis.exe):
import sys
import __builtin__

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: list

# set the import path to current directory for Nuitka generated executable
#sys.path = ['.']

# Disable both dev before anything else.
# This is to make sure the distrubution client doesn't
# get any special perms or anything of the sort.
__builtin__.__dev__ = False

#def __runfunc(*args, **kw):
#    raise SystemExit

# replace these methods to prevent injection...
#__builtin__.exec = lambda *args, **kw: raise SystemExit
#__builtin__.eval = __runfunc
#__builtin__.compile = __runfunc
#__builtin__.execfile = __runfunc
#__builtin__.globals = __runfunc
#__builtin__.locals = __runfunc

# TODO: append resources

configStream = """# Window settings:
window-title Project Altis
win-origin -1 -1
icon-filename phase_3/etc/icon.ico
cursor-filename phase_3/etc/toonmono.cur
show-frame-rate-meter #t
default-directnotify-level info
notify-level-DistributedNPCScientistAI info

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
sync-video #t
texture-power-2 none
gl-check-errors #f
garbage-collect-states #t

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
#active-holidays 116, 63, 64, 65, 66, 128

# Temporary:
want-old-fireworks #t

# Live updates:
want-live-updates #t

# Art assets:
model-path ../resources

# Server:
server-version TTPA-Alpha-1.2.0
min-access-level 600
accountdb-type developer
shard-low-pop 50
shard-mid-pop 100

# RPC:
want-rpc-server #f
rpc-server-endpoint http://localhost:8080/

# DClass file:
dc-file astron/dclass/toon.dc

# Core features:
want-pets #t
want-parties #t
want-cogdominiums #t
want-achievements #f

# Chat:
want-whitelist #t

# Cashbot boss:
want-resistance-toonup #t
want-resistance-restock #t

# Developer options:
show-population #t
force-skip-tutorial #t
want-instant-parties #t"""

from panda3d.core import loadPrcFileData
import StringIO

io = StringIO.StringIO(configStream)

for line in io.readlines():
    # check if the current line is a comment...
    if line.startswith('#'):
        continue

    # load the prc file value
    loadPrcFileData('', '%s' % (line.split()))

# Finally, start the game:
import toontown.toonbase.ClientStart