# This is a temp patch.
# It should really be done by the runtime (e.g. altis.exe):
import sys
import __builtin__

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: tuple

# set the import path to current directory for Nuitka generated executable
sys.path = ['.']

#Disable both dev before anything else.
#This is to make sure the distrubution client doesn't
#get any special perms or anything of the sort.
__builtin__.__dev__ = False

# replace these methods to prevent injection...
__builtin__.exec = lambda *args, **kw: raise SystemExit
__builtin__.eval = lambda *args, **kw: raise SystemExit
__builtin__.compile = lambda *args, **kw: raise SystemExit
__builtin__.execfile = lambda *args, **kw: raise SystemExit
__builtin__.globals = lambda *args, **kw: raise SystemExit
__builtin__.locals = lambda *args, **kw: raise SystemExit

# TODO: append resources, and load config from stream string.

# Finally, start the game:
import toontown.toonbase.ClientStart
