from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import Loader as nLoader
from toontown.dna.DNAParser import *
from direct.stdpy.file import open
from direct.stdpy import threading

class ToontownAsyncLoader(nLoader.Loader):

    def __init__(self, base):
        nLoader.Loader.__init__(self, base)
        
    def loadModel(self, *args, **kw):
        ret = nLoader.Loader.loadModel(self, *args, **kw)
        return ret
        
    def destroy(self):
        nLoader.Loader.destroy(self)
