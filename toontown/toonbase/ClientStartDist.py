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

config = niraidata.CONFIG
config = aes.decrypt(config, key, iv)

del iv
del key

from panda3d.core import loadPrcFileData
import StringIO

io = StringIO.StringIO(config)

for line in io.readlines():
    # check if the current line is a comment...
    if line.startswith('#'):
        continue

    print line
    # load the prc file value
    loadPrcFileData('', line)

del config

# Finally, start the game:
import toontown.toonbase.ClientStart
