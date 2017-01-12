# This is a temp patch.
# It should really be done by the runtime (e.g. altis.exe):
import sys

# patches all code injection
def monitortrace(frame, event, arg, indent=[0]):
    if event == 'call':
          # check if "eval" or "exec" was called, if so raise system exit.
        if frame.f_code.co_name == '<module>':
            raise SystemExit
    elif event == 'return':
        pass

sys.settrace(monitortrace)

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

# replace the "compile" method to prevent any code from being compiled during runtime
def __compile(*args, **kw):
    raise SystemExit

__builtin__.compile = __compile

# replace the "execfile" builtin method to prevent loading and executing actual python files
def __execfile(*args, **kw):
    raise SystemExit

__builtin__.execfile = __execfile

# replace the "globals" builtin method to prevent global modification
def __globals(*args, **kw):
    raise SystemExit

__builtin__.globals = __globals

# replace the "locals" builtin method to prevent local modification
def __locals(*args, **kw):
    raise SystemExit

__builtin__.locals = __locals

# TODO: append resources, and load config from stream string.

# Finally, start the game:
import toontown.toonbase.ClientStart
