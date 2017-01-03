# This is a temp patch.
# It should really be done by the runtime (e.g. infinite.exe):
import sys
sys.path = ['.']

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: tuple

# TODO: append resources, and load config from stream string.

# Finally, start the game:
import toontown.toonbase.ClientStart