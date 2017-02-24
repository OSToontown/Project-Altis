from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyTeamActivityAI import DistributedPartyTeamActivityAI
from toontown.parties import PartyGlobals

scoreRef = {'cat': (PartyGlobals.TugOfWarTieReward, PartyGlobals.TugOfWarTieReward),
            0: (PartyGlobals.TugOfWarWinReward, PartyGlobals.TugOfWarLossReward),
            1: (PartyGlobals.TugOfWarLossReward, PartyGlobals.TugOfWarWinReward),
            2: (PartyGlobals.TugOfWarFallInWinReward, PartyGlobals.TugOfWarFallInLossReward),
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

    def reportKeyRateForce(self, rate, force):
        av = self._getCaller()
        if not av:
            self.notify.warning("Caller for report key rate doesnt exist!")
            return
        avId = av.doId
        if not (avId in self.toonIds[0] and avId not in self.toonIds[1]):
            self.notify.warning("%d called for report key force, but is not playing!")
            return
        self.forces[avId] = force
        self.updateToonKeyRate(avId, keyRate)

    def reportFallIn(self, team):
        pass

    def updateToonKeyRate(self, avId, keyRate):
        self.sendUpdate('updateToonKeyRate', [avId, keyRate])
        self.d_updateToonPositions()

    def d_updateToonPositions(self):
        pass

