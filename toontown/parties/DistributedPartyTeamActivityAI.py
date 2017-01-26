from direct.directnotify import DirectNotifyGlobal
from toontown.parties.DistributedPartyActivityAI import DistributedPartyActivityAI

class DistributedPartyTeamActivityAI(DistributedPartyActivityAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyTeamActivityAI")
    
    def __init__(self, air, parent, activityTuple):
        DistributedPartyActivityAI.__init__(self, air, parent, activityTuple)
        self.toonIds = ([], [])
        self.responses = set()

    def toonJoinRequest(self, todo0):
        pass

    def toonExitRequest(self, todo0):
        pass

    def toonSwitchTeamRequest(self):
        pass

    def setPlayersPerTeam(self, todo0, todo1):
        pass
        
    def getPlayersPerTeam(self):
        pass

    def setDuration(self, todo0):
        pass
        
    def getDuration(self):
        pass

    def setCanSwitchTeams(self, todo0):
        pass
        
    def getCanSwitchTeams(self):
        pass

    def setState(self, todo0, todo1, todo2):
        pass
        
    def getState(self):
        pass

    def setToonsPlaying(self, todo0, todo1):
        pass
        
    def getToonsPlaying(self):
        pass

    def setAdvantage(self, todo0):
        pass
        
    def getAdvantage(self):
        pass

    def switchTeamRequestDenied(self, todo0):
        pass

