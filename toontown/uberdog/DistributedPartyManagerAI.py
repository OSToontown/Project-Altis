from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.task import Task
from toontown.catalog.CatalogBeanItem import CatalogBeanItem
from otp.distributed.OtpDoGlobals import *
from panda3d.core import *
from toontown.parties.DistributedPartyAI import DistributedPartyAI
from datetime import datetime
from toontown.parties.PartyGlobals import *
from otp.ai.MagicWordGlobal import *
from toontown.toonbase.TTLocalizer import EventsPageCancelPartyResultOk
from toontown.toonbase.ToontownGlobals import GIFT_partyrefund, MaxMailboxContents

import time

class DistributedPartyManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyManagerAI")

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self.partyId2Zone = {}
        self.partyId2PlanningZone = {}
        self.partyId2Host = {}
        self.host2PartyId = {}
        self.avId2PartyId = {}
        self.id2Party = {}
        self.pubPartyInfo = {}
        self.idPool = range(self.air.ourChannel, self.air.ourChannel + 100000)
        # get 100 ids at the start and top up
        #taskMgr.doMethodLater(0, self.__getIds, 'DistributedPartyManagerAI___getIds')

    def receiveId(self, ids):
        self.idPool += ids

#    def __getIds(self, task):
#        if len(self.idPool) < 50:
#            self.air.globalPartyMgr.allocIds(100 - len(self.idPool))
#        taskMgr.doMethodLater(180, self.__getIds, 'DistributedPartyManagerAI___getIds')

    def _makePartyDict(self, struct):
        PARTY_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
        party = {}
        party['partyId'] = struct[0]
        party['hostId'] = struct[1]
        start = '%s-%s-%s %s:%s:00' % (struct[2], struct[3], struct[4], struct[5], struct[6])
        party['start'] = datetime.strptime(start, PARTY_TIME_FORMAT)
        end = '%s-%s-%s %s:%s:00' % (struct[7], struct[8], struct[9], struct[10], struct[11])
        party['end'] = datetime.strptime(end, PARTY_TIME_FORMAT)
        party['isPrivate'] = struct[12]
        party['inviteTheme'] = struct[13]
        party['activities'] = struct[14]
        party['decorations'] = struct[15]
        # struct[16] = partystatus
        return party

    # Management stuff
    def partyManagerUdStartingUp(self):
        # This is sent in reply to the GPMAI's hello
        self.notify.info("uberdog has said hello")
        simbase.air.globalPartyMgr.startHeartbeat()

    def partyManagerUdLost(self):
        # well fuck. ud died.
        self.notify.warning("uberdog lost!")

    def canBuyParties(self):
        return True


    def addPartyRequest(self, hostId, startTime, endTime, isPrivate, inviteTheme, activities, decorations, inviteeIds):
        if hostId != simbase.air.getAvatarIdFromSender():
            self.air.writeServerEvent('suspicious',simbase.air.getAvatarIdFromSender(),'Toon tried to create a party as someone else!')
            return
        print 'party requested: host %s, start %s, end %s, private %s, invitetheme %s, activities omitted, decor omitted, invitees %s' % (hostId, startTime, endTime, isPrivate, inviteTheme, inviteeIds)
        simbase.air.globalPartyMgr.sendAddParty(hostId, self.host2PartyId[hostId], startTime, endTime, isPrivate, inviteTheme, activities, decorations, inviteeIds)

    def addPartyResponseUdToAi(self, partyId, errorCode, partyStruct):
        avId = partyStruct[1]
        print 'responding to client now that ud got back to us'
        self.sendUpdateToAvatarId(avId, 'addPartyResponse', [avId, errorCode])
        # We also need to remember to update the field on the DToon indicating parties he's hosting
        self.air.doId2do[avId].sendUpdate('setHostedParties', [[partyStruct]])
        pass

    def markInviteAsReadButNotReplied(self, avId, inviteKey):
        simbase.air.globalPartyMgr.sendInviteAsReadButNotReplied(avId, inviteKey)

    def respondToInvite(self, fromId, todo0, context, inviteKey, inviteStatus):
        simbase.air.globalPartyMgr.respondToInviteAiToUd(fromId, todo0, context, inviteKey, inviteStatus)

    def respondToInviteResponse(self, toId, context, inviteKey, retcode, inviteStatus):
        pass

    def changePrivateRequest(self, partyId, isPrivate):
        hostId = simbase.air.getAvatarIdFromSender()
        simbase.air.globalPartyMgr.changePrivateRequestAiToUd(hostId, partyId, isPrivate)

    def changePrivateResponseUdToAi(self, hostId, partyId, newPrivateStatus, errorCode):
        if hostId in self.air.doId2do:
            self.sendUpdateToAvatarId(hostId, 'changePrivateResponse', [partyId, newPrivateStatus, errorCode])

    def changePrivateResponse(self, partyId, newPrivateStatus, errorCode):
        pass

    def changePartyStatusRequest(self, partyId, newPartyStatus):
        hostId = simbase.air.getAvatarIdFromSender()
        simbase.air.globalPartyMgr.changePartyStatusRequestAiToUd(hostId, partyId, newPartyStatus)

    def changePartyStatusResponseUdToAi(self, hostId, partyId, newPartyStatus, errorCode, refund):
        self.sendUpdateToAvatarId(hostId, 'changePartyStatusResponse', [partyId, newPartyStatus, errorCode, refund])
        if refund:
            self.refundAvatar(hostId, refund)

    def refundAvatar(self, hostId, refund):
        refundItem = CatalogBeanItem(refund, GIFT_partyrefund)
        refundItem.deliveryDate = int(time.time() / 60) + 1
        av = self.air.doId2do.get(hostId)
        if not av:
            return
        av.d_setSystemMessage(0, EventsPageCancelPartyResultOk % refund)
        if len(av.mailboxContents) + len(av.onGiftOrder) >= MaxMailboxContents:
            # Mailbox is full, let's just give them the money directly.
            av.addMoney(refund)
            return
        av.onOrder.append(refundItem)
        av.b_setDeliverySchedule(av.onOrder)

    def changePartyStatusResponse(self, partyId, newPartyStatus, errorCode, beansRefunded):
        pass

    def partyInfoOfHostFailedResponseUdToAi(self, todo0):
        pass

    def givePartyRefundResponse(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def getPartyZone(self, hostId, zoneId, isAvAboutToPlanParty):
        self.notify.debug('getPartyZone(hostId = %s, zoneId = %s, isAboutToPlan = %s' % (hostId, zoneId, isAvAboutToPlanParty))
        avId = self.air.getAvatarIdFromSender()
        if isAvAboutToPlanParty:
            partyId = self.idPool.pop()
            print 'pid %s' % partyId
            self.partyId2Host[partyId] = hostId
            self.partyId2PlanningZone[partyId] = zoneId
            self.host2PartyId[hostId] = partyId
            print 'Responding to a get party zone when planning, av,party,zone: %s %s %s' % (avId, partyId, zoneId)
        else:
            if hostId not in self.host2PartyId:
                # Uhh, we don't know if the host even has a party. Better ask the ud
                self.air.globalPartyMgr.queryPartyForHost(hostId)
                print 'querying for details against hostId %s ' % hostId
                return
            partyId = self.host2PartyId[hostId]
            # Is the party already running?
            if partyId in self.partyId2Zone:
                # Yep!
                zoneId = self.partyId2Zone[partyId]
            else:
                self.notify.warning("getPartyZone did not match a case!")

        self.sendUpdateToAvatarId(avId, 'receivePartyZone', [hostId, partyId, zoneId])

    def partyInfoOfHostResponseUdToAi(self, partyStruct, inviteeIds):
        party = self._makePartyDict(partyStruct)
        av = self.air.doId2do.get(party['hostId'], None)
        if not av:
            return  # The host isn't on the district... wat do
        party['inviteeIds'] = inviteeIds
        partyId = party['partyId']
        # This is issued in response to a request for the party to start, essentially. So let's alloc a zone
        zoneId = self.air.allocateZone()
        self.partyId2Zone[partyId] = zoneId
        self.host2PartyId[party['hostId']] = partyId

        # We need to setup the party itself on our end, so make an ai party
        partyAI = DistributedPartyAI(self.air, party['hostId'], zoneId, party)
        partyAI.generateWithRequiredAndId(self.air.allocateChannel(), self.air.districtId, zoneId)
        self.id2Party[partyId] = partyAI

        # Alert the UD
        self.air.globalPartyMgr.d_partyStarted(partyId, self.air.ourChannel, zoneId, av.getName())

        # Don't forget this was initially started by a getPartyZone, so we better tell the host the partyzone
        self.sendUpdateToAvatarId(party['hostId'], 'receivePartyZone', [party['hostId'], partyId, zoneId])

        # And last, set up our cleanup stuff
        taskMgr.doMethodLater(PARTY_DURATION, self.closeParty, 'DistributedPartyManagerAI_cleanup%s' % partyId, [partyId])

    def closeParty(self, partyId):
        partyAI = self.id2Party[partyId]
        self.air.globalPartyMgr.d_partyDone(partyId)
        for av in partyAI.avIdsAtParty:
            self.sendUpdateToAvatarId(av, 'sendAvToPlayground', [av, 0])
        partyAI.b_setPartyState(PartyStatus.Finished)
        taskMgr.doMethodLater(10, self.__deleteParty, 'closeParty%d' % partyId, extraArgs=[partyId])

    def __deleteParty(self, partyId):
        partyAI = self.id2Party[partyId]
        for av in partyAI.avIdsAtParty:
            self.sendUpdateToAvatarId(av, 'sendAvToPlayground', [av, 1])
        partyAI.requestDelete()
        zoneId = self.partyId2Zone[partyId]
        del self.partyId2Zone[partyId]
        del self.id2Party[partyId]
        del self.pubPartyInfo[partyId]
        self.air.deallocateZone(zoneId)


    def freeZoneIdFromPlannedParty(self, hostId, zoneId):
        sender = self.air.getAvatarIdFromSender()
        # Only the host of a party can free its zone
        if sender != hostId:
            self.air.writeServerEvent('suspicious',sender,'Toon tried to free zone for someone else\'s party!')
            return
        partyId = self.host2PartyId[hostId]
        if partyId in self.partyId2PlanningZone:
            self.air.deallocateZone(self.partyId2PlanningZone[partyId])
            del self.partyId2PlanningZone[partyId]
            del self.host2PartyId[hostId]
            del self.partyId2Host[partyId]
        return

    def sendAvToPlayground(self, avId, retCode):
        pass

    def exitParty(self, partyZone):
        avId = simbase.air.getAvatarIdFromSender()
        for partyInfo in self.pubPartyInfo.values():
            if partyInfo['zoneId'] == partyZone:
                party = self.id2Party.get(partyInfo['partyId'])
                if party:
                    party.removeAvatar(avId)

    def removeGuest(self, ownerId, avId):
        pass

    def partyManagerAIStartingUp(self, todo0, todo1):
        pass

    def partyManagerAIGoingDown(self, todo0, todo1):
        pass

    def toonHasEnteredPartyAiToUd(self, todo0):
        pass

    def toonHasExitedPartyAiToUd(self, todo0):
        pass

    def partyHasFinishedUdToAllAi(self, partyId):
        del self.pubPartyInfo[partyId]

    def updateToPublicPartyInfoUdToAllAi(self, shardId, zoneId, partyId, hostId, numGuests, maxGuests, hostName, activities, minLeft):
        # The uberdog is informing us of a public party.
        # Note that we never update the publicPartyInfo of our own parties without going through the UD. It's just good practice :)
        started = None
        self.pubPartyInfo[partyId] = {
          'shardId': shardId,
          'zoneId': zoneId,
          'partyId': partyId,
          'hostId': hostId,
          'numGuests': numGuests,
          'maxGuests': maxGuests,
          'hostName': hostName,
          'minLeft': minLeft,
          'started': datetime.now(),
          'activities': activities}

    def updateToPublicPartyCountUdToAllAi(self, partyCount, partyId):
        # Update the number of guests at a party
        if partyId in self.pubPartyInfo.keys():
            self.pubPartyInfo[partyId]['numGuests'] = partyCount

    def getPublicParties(self):
        p = []
        for partyId in self.pubPartyInfo:
            party = self.pubPartyInfo[partyId]
            # calculate time left
            minLeft = party['minLeft'] - int((datetime.now() - party['started']).seconds / 60)
            #less band-aidy bandaid
            guests = party.get('numGuests', 0)
            if guests > 255:
                guests = 255
            elif guests < 0:
                guests = 0
            p.append([party['shardId'], party['zoneId'], guests, party.get('hostName', ''), party.get('activities', []), minLeft])
        return p

    def requestShardIdZoneIdForHostId(self, hostId):
        avId = self.air.getAvatarIdFromSender()

        if hostId not in self.host2PartyId:
            self.notify.warning('Avatar %s attempted to teleport to an invalid party!' % avId)
            return

        partyId = self.host2PartyId[hostId]
        if partyId in self.pubPartyInfo:
            party = self.pubPartyInfo[partyId]
            shardId = party['shardId']
            zoneId = party['zoneId']
            self.sendUpdateToAvatarId(avId, 'sendShardIdZoneIdToAvatar', [shardId, zoneId])
        else:
            self.notify.warning("Found partyId without a zone!")
            return

    def sendShardIdZoneIdToAvatar(self, todo0, todo1):
        pass

    def updateAllPartyInfoToUd(self, todo0, todo1, todo2, todo3, todo4, todo5, todo6, todo7, todo8):
        pass

    def forceCheckStart(self):
        pass

    def requestMw(self, todo0, todo1, todo2, todo3):
        pass

    def mwResponseUdToAllAi(self, todo0, todo1, todo2, todo3):
        pass
