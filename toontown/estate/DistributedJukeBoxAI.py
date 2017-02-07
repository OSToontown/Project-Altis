from toontown.estate import EstateGlobals
from toontown.parties.DistributedPartyJukeboxActivityAI import DistributedPartyJukeboxActivityAI

class DistributedJukeBoxAI(DistributedPartyJukeboxActivityAI):

    def __init__(self, air, estateDoId):
        DistributedPartyJukeboxActivityAI.__init__(self, air, parent=estateDoId, activityTuple=(0, *EstateGlobals.JUKE_BOX_POSITION))