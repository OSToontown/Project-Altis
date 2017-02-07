from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyTeamActivityAI import DistributedPartyTeamActivityAI
from toontown.parties import PartyGlobals

scoreRef = {'cat': (PartyGlobals.TugOfWarTieReward, PartyGlobals.TugOfWarTieReward),
            0: (PartyGlobals.TugOfWarWinReward, PartyGlobals.TugOfWarLossReward),
            1: (PartyGlobals.TugOfWarLossReward, PartyGlobals.TugOfWarWinReward),
            2:(PartyGlobals.TugOfWarFallInWinReward, PartyGlobals.TugOfWarFallInLossReward),
            3: (PartyGlobals.TugOfWarFallInLossReward, PartyGlobals.TugOfWarFallInWinReward),
           }

class DistributedPartyTugOfWarActivityAI(DistributedPartyTeamActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyTugOfWarActivityAI")
    
    def __init__(self, air, parent, activityTuple):
        DistributedPartyTeamActivityAI.__init__(self, air, parent, activityTuple)
        self.forces = {}
        self.pos = 0
        self._hasFall = 0
    
    def getDuration(self):
        return PartyGlobals.TugOfWarDuration

    def reportKeyRateForce(self, todo0, todo1):
        pass

    def reportFallIn(self, todo0):
        pass

    def updateToonKeyRate(self, todo0, todo1):
        pass

    def d_updateToonPositions(self):
        pass

