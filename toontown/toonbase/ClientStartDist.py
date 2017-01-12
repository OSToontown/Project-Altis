# This is a temp patch.
# It should really be done by the runtime (e.g. altis.exe):
import sys
import __builtin__

sys.path = ['.']

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: tuple

#Disable both dev before anything else.
#This is to make sure the distrubution client doesn't
#get any special perms or anything of the sort.
__builtin__.__dev__ = False

# replace the "eval" method to prevent any injection, still need to find a way to replace
# the "exec" statement.
def __eval(*args, **kw):
    raise SystemExit

__builtin__.eval = __eval

# TODO: append resources, and load config from stream string.

# Finally, start the game:
import toontown.toonbase.ClientStart
