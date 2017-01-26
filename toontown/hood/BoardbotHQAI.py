from toontown.building import DistributedVPElevatorAI
from toontown.building import FADoorCodes
from toontown.building.DistributedBoardingPartyAI import DistributedBoardingPartyAI
from toontown.coghq.DistributedFactoryElevatorExtAI import DistributedFactoryElevatorExtAI
from toontown.hood import CogHQAI
from toontown.suit import DistributedSellbotBossAI
from toontown.suit import DistributedSuitPlannerAI
from toontown.toonbase import ToontownGlobals

class BoardbotHQAI(CogHQAI.CogHQAI):
    
    def __init__(self, air):
        CogHQAI.CogHQAI.__init__(
            self, air, ToontownGlobals.BoardbotHQ, ToontownGlobals.BoardbotLobby,
            FADoorCodes.BD_DISGUISE_INCOMPLETE,
            DistributedVPElevatorAI.DistributedVPElevatorAI,
            DistributedSellbotBossAI.DistributedSellbotBossAI)

        self.factoryElevators = []
        self.factoryBoardingParty = None
        self.suitPlanners = []

        self.startup()

    def startup(self):
        CogHQAI.CogHQAI.startup(self)

        # Sellbot HQ has not just one, but four lobby doors:
        self.cogHQDoors = [self.extDoor]
        for i in xrange(3):  # CogHQAI already created one of the doors for us.
            extDoor = self.makeCogHQDoor(self.lobbyZoneId, 0, i + 1, self.lobbyFADoorCode)
            self.cogHQDoors.append(extDoor)
        self.createFactoryElevators()
        if simbase.config.GetBool('want-boarding-groups', True):
            self.createFactoryBoardingParty()
        if simbase.config.GetBool('want-suit-planners', True):
            self.createSuitPlanners()

        # Our suit planner needs the Cog HQ doors as well:
        for sp in self.suitPlanners:
            if sp.zoneId == self.zoneId:
                sp.cogHQDoors = self.cogHQDoors

    def createFactoryElevators(self):
        pass

    def createFactoryBoardingParty(self):
        pass

    def createSuitPlanners(self):
        suitPlanner = DistributedSuitPlannerAI.DistributedSuitPlannerAI(self.air, self.zoneId)
        suitPlanner.generateWithRequired(self.zoneId)
        suitPlanner.d_setZoneId(self.zoneId)
        suitPlanner.initTasks()
        self.suitPlanners.append(suitPlanner)
        self.air.suitPlanners[self.zoneId] = suitPlanner
