from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.State import State
from direct.fsm.ClassicFSM import ClassicFSM

class DistributedWeatherCycleAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedWeatherCycleAI')

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

        self.fsm = ClassicFSM(self.__class__.__name__, [
            State('off', self.enterOff, self.exitOff, ['morning']),
            State('morning', self.enterMorning, self.exitMorning, ['afternoon']),
            State('afternoon', self.enterAfternoon, self.exitAfternoon, ['evening']),
            State('evening', self.enterEvening, self.exitEvening, ['midnight']),
            State('midnight', self.enterMidnight, self.exitMidnight, ['morning'])], 'off', 'off')

        self.fsm.enterInitialState()
        self.duration = 0

    def generate(self):
        DistributedObjectAI.generate(self)

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

        taskMgr.doMethodLater(self.getDuration(), self.update, 'update-time')

    def delete(self):
        DistributedObjectAI.delete(self)

        taskMgr.remove('update-time')

    def update(self, task):
        self.b_setState(self.fsm.getCurrentState()._State__transitions[0])
        return task.again

    def setState(self, state):
        self.fsm.request(state)

    def d_setState(self, state):
        self.sendUpdate('setState', [state])

    def b_setState(self, state):
        self.setState(state)
        self.d_setState(state)

    def getState(self):
        return self.fsm.getCurrentState()._State__name

    def setDuration(self, duration):
        self.duration = duration

    def d_setDuration(self, duration):
        self.sendUpdate('setDuration', [duration])

    def b_setDuration(self, duration):
        self.setDuration(duration)
        self.d_setDuration(duration)

    def getDuration(self):
        return self.duration

    def enterOff(self):
        pass

    def exitOff(self):
        pass

    def enterMorning(self):
        pass

    def exitMorning(self):
        pass

    def enterAfternoon(self):
        pass

    def exitAfternoon(self):
        pass

    def enterEvening(self):
        pass

    def exitEvening(self):
        pass

    def enterMidnight(self):
        pass

    def exitMidnight(self):
        pass