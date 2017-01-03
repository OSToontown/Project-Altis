from direct.directnotify import DirectNotifyGlobal
from direct.task import Task
from toontown.coghq import DistributedSwitchBase
from toontown.coghq import DistributedSwitchAI

class DistributedButtonAI(DistributedSwitchAI.DistributedSwitchAI):
    setColor = DistributedSwitchBase.stubFunction
    setModel = DistributedSwitchBase.stubFunction