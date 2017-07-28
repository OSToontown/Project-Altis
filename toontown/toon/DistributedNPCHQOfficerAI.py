from otp.ai.AIBaseGlobal import *
from direct.task.Task import Task
from pandac.PandaModules import *
from toontown.toon import DistributedNPCToonAI
from toontown.quest import Quests

class DistributedNPCHQOfficerAI(DistributedNPCToonAI.DistributedNPCToonAI):
    FourthGagVelvetRopeBan = config.GetBool('want-ban-fourth-gag-velvet-rope', 0)

    def __init__(self, air, npcId, questCallback = None, hq = 1):
        DistributedNPCToonAI.DistributedNPCToonAI.__init__(self, air, npcId, questCallback)
        self.hq = hq