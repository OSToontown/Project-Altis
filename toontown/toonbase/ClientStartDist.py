# This is a temp patch.
# It should really be done by the runtime (e.g. Project Altis.exe):
import sys
import __builtin__

# Replace some modules that do exec:
import collections
collections.namedtuple = lambda *x: list

# Disable both dev,debug before anything else.
# This is to make sure the distrubution client doesn't
# get any special perms or anything of the sort.
__builtin__.__dev__ = False

def __runfunc(*args, **kw):
   print("Something Spoopys Happened!")

__builtin__.__dict__.update(__import__('pandac.PandaModules', fromlist = ['*']).__dict__)
# __builtin__.eval = __runfunc
# __builtin__.compile = __runfunc
# __builtin__.execfile = __runfunc
# __builtin__.globals = __runfunc
# __builtin__.locals = __runfunc

# TODO: append resources
import toontown.toonbase.DCImporter
