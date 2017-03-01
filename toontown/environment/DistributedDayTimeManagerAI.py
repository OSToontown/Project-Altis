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

class DistributedDayTimeManagerAI(DistributedWeatherMGRAI):
    notify = directNotify.newCategory('DistributedDayTimeManagerAI')

    def __init__(self, air):
        DistributedWeatherMGRAI.__init__(self, air)
        self.air = air
        self.interval = 150
        self.currentHour = air.startTime

    def announceGenerate(self):
        DistributedWeatherMGRAI.announceGenerate(self)

        # send update to start initial hour
        self.d_update(self.currentHour)

        # set AI's initial time, then allow update to change this...
        self.air.setHour(self.currentHour)

        # start the ticking process
        taskMgr.doMethodLater(self.interval, self.update, 'time-update-%s' % id(self))

    def d_requestUpdate(self):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'update', [
            self.currentHour])

    def update(self, task):
        if self.currentHour >= 23:
            # reset current time back to 0
            self.currentHour = 0

        # update the currentHour variable
        self.currentHour += 1

        # update the AI's current time.
        self.air.setHour(self.currentHour)

        # send time update to change sky state
        self.d_update(self.currentHour)

        # loop task preserving the timeout interval
        return task.again

    def d_update(self, currentHour):
        self.sendUpdate('update', [currentHour])

    def stop(self):
        # reset currentHour, and remove time update task
        self.currentHour = 0
        taskMgr.remove('time-update-%s' % id(self))
