from toontown.building.ElevatorConstants import *
from toontown.building import DistributedBossElevatorAI

class DistributedCFOElevatorAI(DistributedBossElevatorAI.DistributedBossElevatorAI):

    def __init__(self, air, bldg, zone, antiShuffle = 0, minLaff = 0):
        DistributedBossElevatorAI.DistributedBossElevatorAI.__init__(self, air, bldg, zone, antiShuffle=antiShuffle, minLaff=minLaff)
        self.type = ELEVATOR_CFO
        self.countdownTime = ElevatorData[self.type]['countdown']
