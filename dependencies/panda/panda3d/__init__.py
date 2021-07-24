"Python bindings for the Panda3D libraries"

__version__ = '1.11.0'

if __debug__:
    import sys
    if sys.version_info < (3, 0):
        sys.stderr.write("WARNING: Python 2.7 has reached EOL as of January 1, 2020.\n")
        sys.stderr.write("To suppress this warning, upgrade to Python 3.\n")
        sys.stderr.flush()
    del sys

if '__file__' in locals():
    import os

    bindir = os.path.join(os.path.dirname(__file__), '..', 'bin')
    if os.path.isdir(bindir):
        if hasattr(os, 'add_dll_directory'):
            os.add_dll_directory(bindir)
        elif not os.environ.get('PATH'):
            os.environ['PATH'] = bindir
        else:
            os.environ['PATH'] = bindir + os.pathsep + os.environ['PATH']
    del os, bindir
