from panda3d.core import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from direct.task.Task import Task
from toontown.toonbase import TTLocalizer
import random
import time
from direct.showbase import PythonUtil
import DayTimeGlobals
from DistributedWeatherMGRAI import DistributedWeatherMGRAI

class DistributedRainManagerAI(DistributedWeatherMGRAI):
    notify = directNotify.newCategory('DistributedRainManagerAI')
    
    def __init__(self, air, zoneId):
        DistributedWeatherMGRAI.__init__(self, air)
        self.zoneId = zoneId

    def announceGenerate(self):
        DistributedWeatherMGRAI.announceGenerate(self)
        if self.zoneId in [3000, 3100, 3200, 3300]:
            rainState = 'Snow'
        #elif self.zoneId == 6000:
        #    self.b_setState('ThunderStorm')
        #    return            
        else:
            rainState = 'Rain'
        Sequence(
            Func(self.b_setState, 'Sunny'),
            Wait(1800),
            Func(self.b_setState, rainState),
            Wait(900)).loop()

    def enterRain(self):
        pass
        
    def exitRain(self):
        pass

    def enterSnow(self):
        pass

    def exitSnow(self):
        pass

    def enterThunderStorm(self):
        taskMgr.doMethodLater(5, self.createLightning, 'doLightningStrike')
        
    def exitThunderStorm(self):
        pass
        
    def enterSunny(self):
        simbase.air.isRaining = False
        
    def exitSunny(self):
        simbase.air.isRaining = True
        
    def createLightning(self, task):
        x = random.randrange(-150, 150)
        y = random.randrange(-150, 150)
        task.delay = random.randrange(5, 30)
        self.sendUpdate("spawnLightning", [x, y])
        return task.again