from toontown.building import DistributedCFOElevatorAI
from toontown.building import FADoorCodes
from toontown.building.DistributedBoardingPartyAI import DistributedBoardingPartyAI
from toontown.coghq.boardbothq.DistributedBoardOfficeElevatorExtAI import DistributedBoardOfficeElevatorExtAI
from toontown.hood import CogHQAI
from toontown.suit import DistributedCashbotBossAI
from toontown.suit import DistributedSuitPlannerAI
from toontown.toonbase import ToontownGlobals

class BoardbotHQAI(CogHQAI.CogHQAI):
    
    def __init__(self, air):
        CogHQAI.CogHQAI.__init__(
            self, air, ToontownGlobals.BoardbotHQ, ToontownGlobals.BoardbotLobby,
            FADoorCodes.CB_DISGUISE_INCOMPLETE,
            DistributedCFOElevatorAI.DistributedCFOElevatorAI,
            DistributedCashbotBossAI.DistributedCashbotBossAI)

        self.boardofficeElevators = []
        self.boardofficeBoardingParty = None
        self.suitPlanners = []

        self.startup()

    def startup(self):
        CogHQAI.CogHQAI.startup(self)

        self.createBoardOfficeElevators()
        if simbase.config.GetBool('want-boarding-groups', True):
            self.createBoardOfficeBoardingParty()
        if simbase.config.GetBool('want-suit-planners', True):
            self.createSuitPlanners()

    def createBoardOfficeElevators(self):
        destZones = (
            ToontownGlobals.BoardOfficeIntA,
            ToontownGlobals.BoardOfficeIntB,
            ToontownGlobals.BoardOfficeIntC
        )
        mins = ToontownGlobals.FactoryLaffMinimums[1]
        for i in xrange(len(destZones)):
            boardofficeElevator = DistributedBoardOfficeElevatorExtAI(
                self.air, self.air.boardofficeMgr, destZones[i],
                antiShuffle=0, minLaff=mins[i])
            boardofficeElevator.generateWithRequired(self.zoneId)
            self.boardofficeElevators.append(boardofficeElevator)

    def createBoardOfficeBoardingParty(self):
        boardofficeIdList = []
        for boardofficeElevator in self.boardofficeElevators:
            boardofficeIdList.append(boardofficeElevator.doId)
        self.boardofficeBoardingParty = DistributedBoardingPartyAI(self.air, boardofficeIdList, 4)
        self.boardofficeBoardingParty.generateWithRequired(self.zoneId)

    def createSuitPlanners(self):
        suitPlanner = DistributedSuitPlannerAI.DistributedSuitPlannerAI(self.air, self.zoneId)
        suitPlanner.generateWithRequired(self.zoneId)
        suitPlanner.d_setZoneId(self.zoneId)
        suitPlanner.initTasks()
        self.suitPlanners.append(suitPlanner)
        self.air.suitPlanners[self.zoneId] = suitPlanner
