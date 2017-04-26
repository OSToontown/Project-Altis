from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.showbase import Loader as nLoader
from toontown.toontowngui import ToontownLoadingScreen
from toontown.dna.DNAParser import *
import traceback

class ToontownLoader(nLoader.Loader):
    TickPeriod = 0.1

    def __init__(self, base):
        nLoader.Loader.__init__(self, base)
        self.inBulkBlock = None
        self.blockName = None
        self.loadingScreen = ToontownLoadingScreen.ToontownLoadingScreen()

    def destroy(self):
        self.loadingScreen.destroy()
        del self.loadingScreen
        nLoader.Loader.destroy(self)

    def loadDNAFile(self, dnastore, filename):
        return loadDNAFile(dnastore, filename)

    def beginBulkLoad(self, name, label, range, gui, tipCategory, zoneId):
        self._loadStartT = globalClock.getRealTime()
        nLoader.Loader.notify.info("starting bulk load of block '%s'" % name)
        if self.inBulkBlock:
            Loader.Loader.notify.warning("Tried to start a block ('%s'), but am already in a block ('%s')" % (name, self.blockName))
            return
        
        self.inBulkBlock = 1
        self._lastTickT = globalClock.getRealTime()
        self.blockName = name
        self.loadingScreen.begin(range, label, gui, tipCategory, zoneId)
         
    def endBulkLoad(self, name):
        if not self.inBulkBlock:
            nLoader.Loader.notify.warning("Tried to end a block ('%s'), but not in one" % name)
            return
        
        if name != self.blockName:
            nLoader.Loader.notify.warning("Tried to end a block ('%s'), other then the current one ('%s')" % (name, self.blockName))
            return
        
        self.inBulkBlock = None
        expectedCount, loadedCount = self.loadingScreen.end()
        now = globalClock.getRealTime()
        nLoader.Loader.notify.info("At end of block '%s', expected %s, loaded %s, duration=%s" % (self.blockName,
         expectedCount,
         loadedCount,
         now - self._loadStartT))

    def abortBulkLoad(self):
        if self.inBulkBlock:
            nLoader.Loader.notify.info("Aborting block ('%s')" % self.blockName)
            self.inBulkBlock = None
            self.loadingScreen.abort()

    def tick(self):
        if self.inBulkBlock:
            now = globalClock.getRealTime()
            if now - self._lastTickT > self.TickPeriod:
                self._lastTickT += self.TickPeriod
                self.loadingScreen.tick()
                if hasattr(base, 'cr'):
                    base.cr.considerHeartbeat()

    def loadModel(self, *args, **kw):
        ret = nLoader.Loader.loadModel(self, *args, **kw)
        if ret:
            gsg = base.win.getGsg()
            if gsg:
                ret.prepareScene(gsg)
        
        self.tick()
        return ret

    def loadFont(self, *args, **kw):
        ret = nLoader.Loader.loadFont(self, *args, **kw)
        self.tick()
        return ret

    def loadTexture(self, texturePath, alphaPath = None, okMissing = False):
        ret = nLoader.Loader.loadTexture(self, texturePath, alphaPath, okMissing=okMissing)
        self.tick()
        if alphaPath:
            self.tick()
        
        return ret

    def playSfx(self, *args, **kw):
        ret = base.playSfx(*args, **kw)
        self.tick()
        return ret

    def pdnaModel(self, *args, **kw):
        ret = nLoader.Loader.loadModel(self, *args, **kw)
        if ret:
            gsg = base.win.getGsg()
            if gsg:
                ret.prepareScene(gsg)
        self.tick()
        return ret

    def pdnaFont(self, *args, **kw):
        ret = nLoader.Loader.loadFont(self, *args, **kw)
        self.tick()
        return ret

    def pdnaTexture(self, texturePath, alphaPath = None, okMissing = False):
        ret = nLoader.Loader.loadTexture(self, texturePath, alphaPath, okMissing=okMissing)
        self.tick()
        return ret

    def loadSfx(self, soundPath):
        ret = nLoader.Loader.loadSfx(self, soundPath)
        self.tick()
        return ret

    def loadMusic(self, soundPath):
        ret = nLoader.Loader.loadMusic(self, soundPath)
        self.tick()
        return ret