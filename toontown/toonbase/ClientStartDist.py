# This is a temp patch.
# It should really be done by the runtime (e.g. altis.exe):
import sys
sys.path = ['.']

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: tuple

#Disable both dev and debug before anything else.
#This is to make sure the distrubution client doesn'tell
#get any special perms or anything of the sort.
__dev__ = False
__debug__ = False

# TODO: append resources, and load config from stream string.

# Finally, start the game:
import toontown.toonbase.ClientStart