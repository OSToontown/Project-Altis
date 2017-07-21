import json, httplib, threading
from panda3d.core import *
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.interval.IntervalGlobal import *
from direct.task import Task 
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from direct.gui.DirectGui import DirectLabel

class CharityScreenAI(DistributedObjectAI):
    notify = directNotify.newCategory('CharityScreenAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.count = 0
        
    def start(self):
        threading.Thread(target=taskMgr.add, args=(self.getJson, 'jsonTask')).start()
        
    def getJson(self, task):
        information = httplib.HTTPConnection('www.projectaltis.com')
        information.request('GET', '/api/getcogs')
        info = json.loads(information.getresponse().read())
        self.count = info['counter']
        self.b_setCount(self.count)
        taskMgr.doMethodLater(10, self.getJson, 'jsonTask')
        
    def setCount(self, count):
        self.count = count
        
    def b_setCount(self, count):
        self.d_setCount(count)
        self.setCount(count)
        
    def d_setCount(self, count):
        self.sendUpdate('setCount', [count])
        
    def unload(self):
        taskMgr.remove('jsonTask')