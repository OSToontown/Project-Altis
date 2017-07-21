import json, httplib, threading
from panda3d.core import *
from direct.distributed.DistributedObject import DistributedObject
from direct.interval.IntervalGlobal import *
from direct.task import Task 
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from direct.gui.DirectGui import DirectLabel

class CharityScreen(DistributedObject):
    notify = directNotify.newCategory('CharityScreen')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)
        self.zone2pos = {
            ToontownGlobals.ToontownCentral : (40, 0, 25),
            ToontownGlobals.DonaldsDock : (-25, 17, 25),
            ToontownGlobals.DaisyGardens : (5, 137, 25),
            ToontownGlobals.MinniesMelodyland : (0, 0, 8),
            ToontownGlobals.TheBrrrgh : (-111, -44, 25),
            ToontownGlobals.DonaldsDreamland : (0, 0, 6)}
        self.bob = None
        self.screenObject = None
        self.counter = None

    def announceGenerate(self):
        self.cr.chairityEvent = self

    def start(self, zoneId):
        threading.Thread(target=taskMgr.add, args=(self.setCount, 'countTask')).start()
        def startScreen(*args):
            self.screenObject = args[0]
            if not self.screenObject:
                return
            self.screenObject.reparentTo(render)
            text = '' # "Welcome to PRE-BETA!\nPlease note that there are bugs.\nReport them to the devs!"
            if ZoneUtil.getHoodId(zoneId) == ToontownGlobals.MinniesMelodyland:
                self.screenObject.reparentTo(self.cr.playGame.getPlace().loader.geom.find('**/center_icon'))
            self.screenObject.setPos(self.zone2pos.get(ZoneUtil.getHoodId(zoneId), (0, 0, 6)))
            self.screenObject.setHpr(-90, 0, 0)
            self.counter = DirectLabel(parent = render, pos = (0, 0, 0), relief = None, text = text, text_scale = 1, text_fg = (1, 1, 1, 1) , text_align = TextNode.ACenter, text_font = ToontownGlobals.getMinnieFont())
            self.counter.reparentTo(self.screenObject)
            self.counter.setPos(self.screenObject.find("**/front_screen").getPos() + Point3(0.0, -1.5, 0.3)) 
            
            self.counterback = DirectLabel(parent = render, pos = (0, 0, 0), relief = None, text = text, text_scale = 1, text_fg = (1, 1, 1, 1) , text_align = TextNode.ACenter, text_font = ToontownGlobals.getMinnieFont())
            self.counterback.reparentTo(self.screenObject)
            self.counterback.setPos(self.screenObject.find("**/back_screen").getPos() + Point3(0.0, 1.5, 0.3))
            self.counterback.setHpr(180, 0, 0)
            
            self.bob = Sequence(LerpPosInterval(nodePath=self.screenObject, duration=3.2, pos=(self.screenObject.getX(), self.screenObject.getY(), self.screenObject.getZ() + 1.65), blendType='easeInOut'), Sequence(Wait(0.050), LerpPosInterval(nodePath=self.screenObject, duration=3.0, pos=(self.screenObject.getX(), self.screenObject.getY(), self.screenObject.getZ()), blendType='easeInOut'), Sequence(Wait(0.050))))
            self.bob.loop()
            
        asyncloader.loadModel("phase_3.5/models/events/charity/flying_screen.bam", callback = startScreen)
        
    def setCount(self, task):
        self.count = base.localAvatar.getStat(ToontownGlobals.STATS_COGS)
        cash = self.count / 1000.0
        cash = '{:,.2f}'.format(cash)
        if self.counter and self.counterback:
            self.counter['text'] = (str(self.count) + "\nCogs Destroyed\nYou've earned %s USD\nfor the Extra Life Charity!") % cash
            self.counterback['text'] = (str(self.count) + "\nCogs Destroyed\nYou've earned %s USD\nfor the Extra Life Charity!") % cash
        taskMgr.doMethodLater(10, self.setCount, 'countTask')
            
    def unload(self):
        self.notify.debug("Unloading Charity Screen!")
        self.ignoreAll()
        if self.bob:
            self.bob.finish()
            self.bob = None
        if self.screenObject:
            self.screenObject.removeNode()
            self.screenObject = None       
    def delete(self):
        self.cr.chairityEvent = None
        self.notify.debug("Deleting Charity Screen!")
        taskMgr.remove('countTask')
        if self.bob:
            self.bob.finish()
            self.bob = None
        if self.screenObject:
            self.screenObject.removeNode()
            self.screenObject = None