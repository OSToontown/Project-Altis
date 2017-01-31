from direct.distributed.DistributedObject import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.State import State
from direct.fsm.ClassicFSM import ClassicFSM
from toontown.weather import WeatherGlobals
from direct.interval.LerpInterval import LerpColorScaleInterval

class DistributedWeatherCycle(DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedWeatherCycle')

    def __init__(self, cr):
        DistributedObject.__init__(self, cr)

        self.fsm = ClassicFSM(self.__class__.__name__, [
            State('off', self.enterOff, self.exitOff, ['morning']),
            State('morning', self.enterMorning, self.exitMorning, ['afternoon']),
            State('afternoon', self.enterAfternoon, self.exitAfternoon, ['evening']),
            State('evening', self.enterEvening, self.exitEvening, ['midnight']),
            State('midnight', self.enterMidnight, self.exitMidnight, ['morning'])], 'off', 'off')

        self.fsm.enterInitialState()
        self.__interval = None

    def setState(self, state):
        self.fsm.request(state)

    def getState(self):
        return self.fsm.getCurrentState()._State__name

    def setDuration(self, duration):
        self.duration = duration

    def getDuration(self):
        return self.duration

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterMorning(self):
        self.__interval = LerpColorScaleInterval(render, self.getDuration(), WeatherGlobals.cycleColors[0],
            startColorScale=render.getColorScale())

        self.__interval.start()

    def exitMorning(self):
        if not self.__interval:
            return

        self.__interval.finish()
        self.__interval = None

    def enterAfternoon(self):
        self.__interval = LerpColorScaleInterval(render, self.getDuration(), WeatherGlobals.cycleColors[1],
            startColorScale=render.getColorScale())
        
        self.__interval.start()

    def exitAfternoon(self):
        if not self.__interval:
            return

        self.__interval.finish()
        self.__interval = None

    def enterEvening(self):
        self.__interval = LerpColorScaleInterval(render, self.getDuration(), WeatherGlobals.cycleColors[2],
            startColorScale=render.getColorScale())

        self.__interval.start()

    def exitEvening(self):
        if not self.__interval:
            return

        self.__interval.finish()
        self.__interval = None

    def enterMidnight(self):
        self.__interval = LerpColorScaleInterval(render, self.getDuration(), WeatherGlobals.cycleColors[3],
            startColorScale=render.getColorScale())

        self.__interval.start()

    def exitMidnight(self):
        if not self.__interval:
            return

        self.__interval.finish()
        self.__interval = None