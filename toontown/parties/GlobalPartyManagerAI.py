from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.distributed.PyDatagram import *
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.task import Task
from PartyGlobals import AddPartyErrorCode

class GlobalPartyManagerAI(DistributedObjectGlobalAI):
    notify = directNotify.newCategory('GlobalPartyManagerAI')
    
    def announceGenerate(self):
        DistributedObjectGlobalAI.announceGenerate(self)
        # Inform the UD that we as an AI have started up
        self.uberdogUp = False
        self.sendUpdate('partyManagerAIHello', [simbase.air.partyManager.doId])
        #taskMgr.doMethodLater(30, self.reportUdLost, 'noResponseTask')

    def startHeartbeat(self):
        taskMgr.remove('noResponseTask')
        self.uberdogUp = True
        #taskMgr.doMethodLater(15, self.heartbeat, 'heartbeatTask')

    def heartbeat(self, task):
        self.sendUpdate('heartbeat', [simbase.air.partyManager.doId])
        #taskMgr.doMethodLater(15, self.reportUdLost, 'heartbeatLostTask')
        return Task.again

    def heartbeatResponse(self):
        self.uberdogUp = True
        self.notify.debug('Heartbeat responded!')
        taskMgr.remove('heartbeatLostTask')

    def reportUdLost(self, task):
        self.notify.warning('heck!!! party connection to uberdog was lost!')
        self.uberdogUp = False
        if task.name == 'noResponseTask':
            self.startHeartbeat()
            return Task.done

    def sendAddParty(self, avId, partyId, start, end, isPrivate, inviteTheme, activities, decorations, inviteeIds):
        if not self.uberdogUp:
            self.sendUpdateToAvatarId(avId, 'addPartyResponse', [avId, AddPartyErrorCode.DatabaseError])
            return
        self.sendUpdate('addParty', [avId, partyId, start, end, isPrivate, inviteTheme, activities, decorations, inviteeIds])
        
    def queryPartyForHost(self, hostId):
        self.sendUpdate('queryParty', [hostId])

    def d_partyStarted(self, partyId, shardId, zoneId, hostName):
        self.sendUpdate('partyHasStarted', [partyId, shardId, zoneId, hostName])
        
    def partyStarted(self, partyId, shardId, zoneId, hostName):
        pass

    def d_partyDone(self, partyId):
        self.sendUpdate('partyDone', [partyId])
        
    def partyDone(self, partyId):
        pass

    def d_toonJoinedParty(self, partyId, avId):
        self.sendUpdate('toonJoinedParty', [partyId, avId])
        
    def toonJoinedParty(self, partyId, avId):
        pass

    def d_toonLeftParty(self, partyId, avId):
        self.sendUpdate('toonLeftParty', [partyId, avId])
        
    def toonLeftParty(self, partyId, avId):
        pass
        
    def d_requestPartySlot(self, partyId, avId, gateId):
        self.sendUpdate('requestPartySlot', [partyId, avId, gateId])
        
    def requestPartySlot(self, partyId, avId, gateId):
        pass

    def changePrivateRequestAiToUd(self, hostId, partyId, isPrivate):
        self.sendUpdate('changePrivateRequest', [hostId, partyId, isPrivate])

    def changePartyStatusRequestAiToUd(self, hostId, partyId, newPartyStatus):
        self.sendUpdate('changePartyStatusRequest', [hostId, partyId, newPartyStatus])

    def respondToInviteAiToUd(self, fromId, todo0, context, inviteKey, inviteStatus):
        self.sendUpdate('respondToInvite', [fromId, todo0, context, inviteKey, inviteStatus])

    def sendInviteAsReadButNotReplied(self, avId, inviteKey):
        self.sendUpdate('markInviteAsReadButNotReplied', [avId, inviteKey])
