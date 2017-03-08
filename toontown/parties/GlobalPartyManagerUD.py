from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import *
from direct.task import Task
from toontown.parties.PartyGlobals import *
from datetime import datetime, timedelta
from pandac.PandaModules import *
from toontown.toonbase.ToontownGlobals import P_InvalidIndex, P_ItemAvailable


PARTY_TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
LOAD_TIME_FORMAT = '%Y-%m-%dT%H:%M:%S'


class GlobalPartyManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('GlobalPartyManagerUD')

    # This uberdog MUST be up before the AIs, as AIs talk to this UD

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)
        self.notify.debug("GPMUD generated")
        self.senders2Mgrs = {}
        self.host2PartyId = {}
        self.id2Party = {}
        self.party2PubInfo = {}
        self.tempSlots = {}
        self.inviteKey2Invite = {}
        self.inviteKeyAllocator = UniqueIdAllocator(0, 1000000)
        self.partyId2InviteKeys = {}
        self.hostsToRefund = {}
        self.inviteeId2Invites = {}
        self.hostId2PartyReplies = {}

        self.load()

        # Preallocate any used invite keys.
        if self.inviteKey2Invite:
            for inviteKey in self.inviteKey2Invite.keys():
                self.inviteKeyAllocator.initialReserveId(inviteKey)

        self.wantInstantParties = simbase.config.GetBool('want-instant-parties', 0)

        # Setup tasks
        self.runAtNextInterval()

    def save(self, dictName=None):
        try:
            saveDict = lambda d: self.air.backups.save('parties', (d,), eval('self.' + d))
            if isinstance(dictName, (tuple, list, set)):
                for x in dictName:
                    saveDict(x)
                return
            elif dictName:
                saveDict(dictName)
                return

            self.air.backups.save('parties', ('hostsToRefund',), self.hostsToRefund)
            self.air.backups.save('parties', ('inviteeId2Invites',), self.inviteeId2Invites)
            self.air.backups.save('parties', ('hostId2PartyReplies',), self.hostId2PartyReplies)
            self.air.backups.save('parties', ('inviteKey2Invite',), self.inviteKey2Invite)
            self.air.backups.save('parties', ('partyId2InviteKeys',), self.partyId2InviteKeys)
            self.air.backups.save('parties', ('host2PartyId',), self.host2PartyId)
            self.air.backups.save('parties', ('id2Party',), self.id2Party)
        except Exception as e:
            self.notify.warning('Party dats saving failed!\n%s' % e.message)

    def load(self):
        try:
            convert = lambda d: dict((int(k), v) for k, v in d.iteritems())

            self.hostsToRefund = convert(self.air.backups.load('parties', ('hostsToRefund',), default=({})))

            self.inviteeId2Invites = convert(self.air.backups.load('parties', ('inviteeId2Invites',), default=({})))

            self.host2PartyId = convert(self.air.backups.load('parties', ('host2PartyId',), default=({})))

            self.partyId2InviteKeys = convert(self.air.backups.load('parties', ('partyId2InviteKeys'), default=({})))

            self.inviteKey2Invite = convert(self.air.backups.load('parties', ('inviteKey2Invite',), default=({})))

            self.hostId2PartyReplies = convert(self.air.backups.load('parties', ('hostId2PartyReplies',), default=({})))

            self.id2Party = convert(self.air.backups.load('parties', ('id2Party',), default=({})))

            if self.id2Party:
                for partyId in self.id2Party.keys():
                    self.id2Party[partyId]['start'] = datetime.strptime(
                        self.id2Party[partyId]['start'].split('-04:00')[0], LOAD_TIME_FORMAT)
                    self.id2Party[partyId]['end'] = datetime.strptime(
                        self.id2Party[partyId]['end'].split('-04:00')[0], LOAD_TIME_FORMAT)
                    self.checkForDeletion(partyId, refund=True)

        except Exception as e:
            self.notify.warning('Party backup loading failed!\n%s' % e.message)

    def checkForDeletion(self, partyId, refund=False):
        party = self.id2Party.get(int(partyId))
        if not party:
            return
        if datetime.now() > party['start'] or party['status'] == PartyStatus.Cancelled:
            hostId = party['hostId']
            if refund:
                self.hostsToRefund[hostId] = self.calculateRefund(party['activities'], party['decorations'])
            del self.hostId2PartyReplies[hostId]
            del self.host2PartyId[hostId]
            del self.id2Party[int(partyId)]

            inviteKeys = self.partyId2InviteKeys.get(int(partyId))
            if not inviteKeys:
                return

            for inviteKey in inviteKeys:
                del self.inviteKey2Invite[inviteKey]
            del self.partyId2InviteKeys[int(partyId)]

    # GPMUD -> PartyManagerAI messaging
    def _makeAIMsg(self, field, values, recipient):
        return self.air.dclassesByName['DistributedPartyManagerUD'].getFieldByName(field).aiFormatUpdate(recipient, recipient, simbase.air.ourChannel, values)

    def sendToAI(self, field, values, sender=None):
        if not sender:
            sender = self.air.getAvatarIdFromSender()
        dg = self._makeAIMsg(field, values, self.senders2Mgrs.get(sender, sender + 8))
        self.air.send(dg)

    # GPMUD -> toon messaging
    def _makeAvMsg(self, field, values, recipient):
        return self.air.dclassesByName['DistributedToonUD'].getFieldByName(field).aiFormatUpdate(recipient, recipient, simbase.air.ourChannel, values)

    def sendToAv(self, avId, field, values):
        dg = self._makeAvMsg(field, values, avId)
        self.air.send(dg)

    # Task stuff
    def runAtNextInterval(self):
        now = datetime.now()
        howLongUntilAFive = (60 - now.second) + 60 * (4 - (now.minute % 5))
        taskMgr.doMethodLater(howLongUntilAFive, self.__checkPartyStarts, 'GlobalPartyManager_checkStarts')

    def canPartyStart(self, party):
        now = datetime.now()
        if self.wantInstantParties:
            return True
        else:
            return party['start'] < now

    def isTooLate(self, party):
        now = datetime.now()
        delta = timedelta(minutes=15)
        endStartable = party['start'] + delta
        return endStartable < now

    def __checkPartyStarts(self, task):
        now = datetime.now()
        for partyId in self.id2Party.keys():
            party = self.id2Party[int(partyId)]
            hostId = party['hostId']
            if self.canPartyStart(party) and party['status'] == PartyStatus.Pending:
                # Time to start party
                party['status'] = PartyStatus.CanStart
                self.id2Party[partyId] = party
                self.sendToAv(hostId, 'setHostedParties', [[self._formatParty(party)]])
                self.sendToAv(hostId, 'setPartyCanStart', [int(partyId)])
            elif self.isTooLate(party) and not self.wantInstantParties:
                if party['status'] == PartyStatus.Finished:
                    self.checkForDeletion(int(partyId))
                    continue
                elif party['status'] == PartyStatus.NeverStarted:
                    self.checkForDeletion(int(partyId), refund=True)
                    continue
                party['status'] = PartyStatus.NeverStarted
                self.id2Party[int(partyId)] = party
                self.sendToAv(hostId, 'setHostedParties', [[self._formatParty(party)]])
                self.checkForDeletion(int(partyId), refund=True)
        self.save()
        self.runAtNextInterval()

    # Format a party dict into a party struct suitable for the wire
    def _formatParty(self, partyDict):
        start = partyDict['start']
        end = partyDict['end']
        return [partyDict['partyId'],
                partyDict['hostId'],
                start.year,
                start.month,
                start.day,
                start.hour,
                start.minute,
                end.year,
                end.month,
                end.day,
                end.hour,
                end.minute,
                partyDict['isPrivate'],
                partyDict['inviteTheme'],
                partyDict['activities'],
                partyDict['decorations'],
                partyDict.get('status', PartyStatus.Pending)]

    # Avatar joined the game, invoked by the CSMUD
    def avatarJoined(self, avId):
        # First check if the avatar has a party and start it if possible.
        partyId = self.host2PartyId.get(avId)
        if partyId:
            party = self.id2Party.get(partyId)
            if not party:
                del self.host2PartyId[avId]
                self.save(dictName='host2PartyId')
                return  # There's a partyId without an actual party?? What is this madness.
            self.sendToAv(avId, 'setHostedParties', [[self._formatParty(party)]])
            if partyId not in self.party2PubInfo and self.canPartyStart(party):
                # The party hasn't started and it can start
                self.sendToAv(avId, 'setPartyCanStart', [partyId])

            inviteReplies = self.hostId2PartyReplies.get(avId)
            if not inviteReplies:
                return
            self.sendToAv(avId, 'setPartyReplies', [[[partyId, self.hostId2PartyReplies[avId]]]])

        # Now lets check if they have been invited to any other parties.
        invites = self.inviteeId2Invites.get(avId)
        if invites:
            self.sendToAv(avId, 'setInvites', [invites])
            parties = [self._formatParty(self.id2Party[invite[1]]) for invite in invites if invite[1] in self.id2Party]
            if parties:
                self.sendToAv(avId, 'setPartiesInvitedTo',
                              [parties])

        # Check if we need to refund this avatar.
        if avId in self.hostsToRefund:
            self.sendToAv(avId, 'refundParty', [self.hostsToRefund[avId]])
            del self.hostsToRefund[avId]
            self.save(dictName='hostsToRefund')

    # uberdog coordination of public party info
    def __updatePartyInfo(self, partyId):
        # Update all the AIs about this public party
        if partyId not in self.party2PubInfo:
            return
            
        party = self.party2PubInfo[partyId]
        for sender in self.senders2Mgrs.keys():
            actIds = []
            for activity in self.id2Party[partyId]['activities']:
                actIds.append(activity[0])  # First part of activity tuple should be actId
            minLeft = int((PARTY_DURATION - (datetime.now() - party['started']).seconds) / 60)
            self.sendToAI('updateToPublicPartyInfoUdToAllAi',
                          [party['shardId'], party['zoneId'], partyId, self.id2Party[partyId]['hostId'],
                           party['numGuests'], party['maxGuests'], party['hostName'], actIds, minLeft], sender=sender)

    def __updatePartyCount(self, partyId):
        # Update the party guest count
        for sender in self.senders2Mgrs.keys():
            if partyId in self.party2PubInfo:
                self.sendToAI('updateToPublicPartyCountUdToAllAi', [self.party2PubInfo[partyId]['numGuests'], partyId], sender=sender)

    def partyHasStarted(self, partyId, shardId, zoneId, hostName):
        if not self.id2Party[partyId]['isPrivate']:
            self.party2PubInfo[partyId] =\
                {'partyId': partyId, 'shardId': shardId, 'zoneId': zoneId, 'hostName': hostName, 'numGuests': 0,
                 'maxGuests': MaxToonsAtAParty, 'started': datetime.now()}
        self.__updatePartyInfo(partyId)
        # update the host's book
        if partyId not in self.id2Party:
            self.notify.warning("didn't find details for starting party id %s hosted by %s" % (partyId, hostName))
            return
        self.id2Party[partyId]['status'] = PartyStatus.Started
        party = self.id2Party.get(partyId, None)
        self.sendToAv(party['hostId'], 'setHostedParties', [[self._formatParty(party)]])
        self.sendToAv(party['hostId'], 'announcePartyStarted', [partyId])

    def partyDone(self, partyId):
        del self.party2PubInfo[partyId]
        self.id2Party[partyId]['status'] = PartyStatus.Finished
        party = self.id2Party.get(partyId, None)
        hostId = party['hostId']
        self.sendToAv(hostId, 'setHostedParties', [[self._formatParty(party)]])
        del self.id2Party[partyId]
        del self.host2PartyId[hostId]
        for inviteKey in self.partyId2InviteKeys[partyId]:
            self.inviteKeyAllocator.free(inviteKey)
            del self.inviteKey2Invite[inviteKey]
        del self.partyId2InviteKeys[partyId]
        del self.hostId2PartyReplies[hostId]
        self.save()
        self.air.writeServerEvent('party-done', '%s')

    def toonJoinedParty(self, partyId, avId):
        if avId in self.tempSlots:
            del self.tempSlots[avId]
            return
        self.party2PubInfo.get(partyId, {'numGuests': 0})['numGuests'] += 1
        self.__updatePartyCount(partyId)

    def toonLeftParty(self, partyId, avId):
        if self.party2PubInfo.get(partyId, {'numGuests': 0}) != {'numGuests': 0}:
            self.party2PubInfo.get(partyId, {'numGuests': 0})['numGuests'] -= 1
        self.__updatePartyCount(partyId)

    def partyManagerAIHello(self, channel):
        # Upon AI boot, DistributedPartyManagerAIs are supposed to say hello. 
        # They send along the DPMAI's doId as well, so that I can talk to them later.
        print 'AI with base channel %s, will send replies to DPM %s' % (simbase.air.getAvatarIdFromSender(), channel)
        self.senders2Mgrs[simbase.air.getAvatarIdFromSender()] = channel
        self.sendToAI('partyManagerUdStartingUp', [])

        # In addition, set up a postRemove where we inform this AI that the UD has died
        self.air.addPostRemove(self._makeAIMsg('partyManagerUdLost', [], channel))

    def heartbeat(self, channel):
        if simbase.air.getAvatarIdFromSender() not in self.senders2Mgrs:
            self.senders2Mgrs[simbase.air.getAvatarIdFromSender()] = channel
        self.sendUpdateToChannel(simbase.air.getAvatarIdFromSender(), 'heartbeatResponse', [])

    def addParty(self, hostId, partyId, start, end, isPrivate, inviteTheme, activities, decorations, inviteeIds):
        startTime = datetime.strptime(start.split('-04:00')[0], PARTY_TIME_FORMAT)
        endTime = datetime.strptime(end.split('-04:00')[0], PARTY_TIME_FORMAT)
        _party = {'partyId': partyId, 'hostId': hostId, 'start': startTime, 'end': endTime,
                  'isPrivate': isPrivate, 'inviteTheme': inviteTheme, 'activities': activities,
                  'decorations': decorations, 'inviteeIds': inviteeIds, 'status': PartyStatus.Pending}

        if hostId in self.host2PartyId:
            # Sorry, one party at a time
            self.sendToAI('addPartyResponseUdToAi', [partyId, AddPartyErrorCode.TooManyHostedParties, self._formatParty(_party)])
            return

        self.id2Party[partyId] = _party

        self.host2PartyId[hostId] = partyId

        self.hostId2PartyReplies[hostId] = []

        self.partyId2InviteKeys[partyId] = []
        # Time to send out the invites.
        for avId in inviteeIds:
            inviteKey = self.inviteKeyAllocator.allocate()
            self.partyId2InviteKeys[partyId].append(inviteKey)
            invite = [inviteKey, partyId, InviteStatus.NotRead]
            self.inviteKey2Invite[inviteKey] = invite
            if avId not in self.inviteeId2Invites:
                self.inviteeId2Invites[avId] = []
            self.inviteeId2Invites[avId].append(invite)
            self.sendToAv(avId, 'setInvites', [self.inviteeId2Invites[avId]])

            partiesInvitedTo = []
            for invite in self.inviteeId2Invites[avId]:
                if invite[1] in self.id2Party:
                    partiesInvitedTo.append(self._formatParty(self.id2Party[invite[1]]))

            self.sendToAv(avId, 'setPartiesInvitedTo', [partiesInvitedTo])
            self.hostId2PartyReplies[hostId].append([avId, InviteStatus.NotRead])

        self.sendToAI('addPartyResponseUdToAi', [partyId, AddPartyErrorCode.AllOk, self._formatParty(self.id2Party[partyId])])
        self.sendToAv(hostId, 'setPartyReplies', [[[partyId, self.hostId2PartyReplies[hostId]]]])

        if self.wantInstantParties:
            taskMgr.remove('GlobalPartyManager_checkStarts')
            taskMgr.doMethodLater(15, self.__checkPartyStarts, 'GlobalPartyManager_checkStarts')

        self.save()
        return

    def queryParty(self, hostId):
        # An AI is wondering if the host has a party. We'll tell em!
        if hostId in self.host2PartyId:
            # Yep, he has a party.
            party = self.id2Party[self.host2PartyId[hostId]]
            self.sendToAI('partyInfoOfHostResponseUdToAi', [self._formatParty(party), party.get('inviteeIds', [])])
            return
        print 'query failed, av %s isnt hosting anything' % hostId

    def requestPartySlot(self, partyId, avId, gateId):
        if partyId not in self.party2PubInfo:
            recipient = self.GetPuppetConnectionChannel(avId)
            sender = simbase.air.getAvatarIdFromSender()
            dg = self.air.dclassesByName['DistributedPartyGateAI'].getFieldByName('partyRequestDenied').aiFormatUpdate(gateId, recipient, sender, [PartyGateDenialReasons.Unavailable])
            self.air.send(dg)
            return
        party = self.party2PubInfo[partyId]
        if party['numGuests'] >= party['maxGuests']:
            recipient = self.GetPuppetConnectionChannel(avId)
            sender = simbase.air.getAvatarIdFromSender()
            dg = self.air.dclassesByName['DistributedPartyGateAI'].getFieldByName('partyRequestDenied').aiFormatUpdate(gateId, recipient, sender, [PartyGateDenialReasons.Full])
            self.air.send(dg)
            return
        # get them a slot
        party['numGuests'] += 1
        self.__updatePartyCount(partyId)
        # note that they might not show up
        self.tempSlots[avId] = partyId

        # give the client a minute to connect before freeing their slot
        taskMgr.doMethodLater(60, self._removeTempSlot, 'partyManagerTempSlot%d' % avId, extraArgs=[avId])

        # now format the pubPartyInfo
        actIds = []
        try:
            for activity in self.id2Party[partyId]['activities']:
                actIds.append(activity[0])
        except:
            pass
        info = [party['shardId'], party['zoneId'], party['numGuests'], party['hostName'], actIds, 0]
        hostId = self.id2Party[int(party['partyId'])]['hostId']
        # send update to client's gate
        recipient = self.GetPuppetConnectionChannel(avId)
        sender = simbase.air.getAvatarIdFromSender() # try to pretend the AI sent it. ily2 cfsworks
        dg = self.air.dclassesByName['DistributedPartyGateAI'].getFieldByName('setParty').aiFormatUpdate(gateId, recipient, sender, [info, hostId])
        self.air.send(dg)

    def _removeTempSlot(self, avId):
        partyId = int(self.tempSlots.get(avId))
        if partyId:
            del self.tempSlots[avId]
            self.party2PubInfo.get(partyId, {'numGuests': 0})['numGuests'] -= 1
            self.__updatePartyCount(partyId)

    def changePrivateRequest(self, hostId, partyId, isPrivate):
        party = self.id2Party.get(partyId)
        if party is None:
            self.notify.warning('Avatar %s tried to update a invalid party %s!' % (hostId, partyId))
            self.sendToAI('changePrivateResponseUdToAi', [hostId, int(partyId), isPrivate, ChangePartyFieldErrorCode.ValidationError])
            return
        if party['hostId'] != hostId:
            self.air.writeServerEvent('suspicious', hostId, 'Avatar tried to update a party that is not thiers!')
            self.sendToAI('changePrivateResponseUdToAi', [hostId, int(partyId), isPrivate, ChangePartyFieldErrorCode.ValidationError])
            return
        if party['status'] not in (PartyStatus.CanStart, PartyStatus.Pending):
            self.sendToAI('changePrivateResponseUdToAi',
                          [hostId, int(partyId), isPrivate, ChangePartyFieldErrorCode.AlreadyStarted])
            return
        party['isPrivate'] = isPrivate
        self.sendToAv(hostId, 'setHostedParties', [[self._formatParty(party)]])
        self.sendToAI('changePrivateResponseUdToAi', [hostId, int(partyId), isPrivate, ChangePartyFieldErrorCode.AllOk])

    def changePartyStatusRequest(self, hostId, partyId, newPartyStatus):
        party = self.id2Party.get(int(partyId))
        refund = 0
        if party is None:
            self.notify.warning('Avatar %s tried to update a invalid party %s!' % (hostId, int(partyId)))
            self.sendToAI('changePartyStatusResponseUdToAi',
                          [hostId, int(partyId), newPartyStatus, ChangePartyFieldErrorCode.ValidationError, refund])
            return
        if party['hostId'] != hostId:
            self.air.writeServerEvent('suspicious', hostId, 'Avatar tried to update a party that is not thiers!')
            self.sendToAI('changePartyStatusResponseUdToAi',
                          [hostId, int(partyId), newPartyStatus, ChangePartyFieldErrorCode.ValidationError, refund])
            return
        if party['status'] not in (PartyStatus.CanStart, PartyStatus.Pending):
            self.sendToAI('changePartyStatusResponseUdToAi',
                          [hostId, int(partyId), newPartyStatus, ChangePartyFieldErrorCode.AlreadyStarted, refund])
            return
        party['status'] = newPartyStatus
        self.id2Party[int(partyId)] = party
        self.sendToAv(hostId, 'setHostedParties', [[self._formatParty(party)]])

        if newPartyStatus == PartyStatus.Cancelled:
            refund = self.calculateRefund(party['activities'], party['decorations'])

        self.sendToAI('changePartyStatusResponseUdToAi', [hostId, int(partyId), newPartyStatus, ChangePartyFieldErrorCode.AllOk, refund])
        self.save(dictName='id2Party')

    def respondToInvite(self, fromId, mailboxId, context, inviteKey, inviteStatus):
        invite = self.inviteKey2Invite.get(inviteKey)
        if not invite:
            return
        if invite[1] not in self.id2Party:
            if fromId in self.inviteeId2Invites.keys():
                if invite in self.inviteeId2Invites[fromId]:
                    self.inviteeId2Invites[fromId].remove(invite)

        hostId = self.id2Party[invite[1]]['hostId']
        partyReply = [fromId, inviteStatus]
        pastReplies = self.hostId2PartyReplies.get(hostId)

        if [fromId, InviteStatus.ReadButNotReplied] in pastReplies:
            self.sendToAv(hostId, 'updateReply', [invite[1]] + partyReply)
            self.hostId2PartyReplies[hostId].remove([fromId, InviteStatus.ReadButNotReplied])
        elif [fromId, InviteStatus.NotRead] in pastReplies:
            self.sendToAv(hostId, 'updateReply', [invite[1]] + partyReply)
            self.hostId2PartyReplies[hostId].remove([fromId, InviteStatus.NotRead])
        else:
            self.air.writeServerEvent('suspicious', fromId, 'Avatar tried to update a invalid invite!')
            return

        self.hostId2PartyReplies[hostId].append(partyReply)

        self.inviteKey2Invite[inviteKey][2] = inviteStatus
        if fromId in self.inviteeId2Invites:
            for x in self.inviteeId2Invites[fromId]:
                if x[1] == invite[1]:
                    self.inviteeId2Invites[fromId].remove(x)

        self.sendToAv(fromId, 'setInvites', [self.inviteeId2Invites[fromId]])

        self.save(dictName=('inviteKey2Invite', 'inviteeId2Invites', 'hostId2PartyReplies'))

    def markInviteAsReadButNotReplied(self, fromId, inviteKey):
        invite = self.inviteKey2Invite.get(inviteKey)
        if not invite:
            self.air.writeServerEvent('suspicious', fromId, 'Avatar tried to respond to a invalid invite!')
            return
        if invite[1] not in self.id2Party:
            self.air.writeServerEvent('suspicious', fromId, 'Avatar tried to respond to a invalid party!')
            if fromId in self.inviteeId2Invites.keys():
                if inviteKey in self.inviteeId2Invites[fromId]:
                    self.inviteeId2Invites[fromId].remove(inviteKey)
            return
        if fromId not in self.id2Party[invite[1]]['inviteeIds']:
            self.air.writeServerEvent('suspicious', fromId, 'Avatar tried to respond to a party they aren\'t invited to!')
            return

        hostId = self.id2Party[invite[1]]['hostId']
        pastReplies = self.hostId2PartyReplies.get(hostId)
        if not [fromId, InviteStatus.NotRead] in pastReplies:
            self.air.writeServerEvent('suspicious', fromId, 'Avatar tried to respond to a party they aren\'t invited to!')
            return

        for reply in pastReplies:
            if reply[0] == fromId and reply[1] != InviteStatus.NotRead:
                self.air.writeServerEvent('suspicious', fromId, 'Avatar tried to update a already responded invite!')
                return

        newReply = [fromId, InviteStatus.ReadButNotReplied]
        newInvite = [inviteKey, invite[1], InviteStatus.ReadButNotReplied]
        self.inviteeId2Invites[fromId].remove(invite)
        self.inviteeId2Invites[fromId].append(newInvite)
        self.inviteKey2Invite[inviteKey] = newInvite
        self.hostId2PartyReplies[hostId].remove([fromId, InviteStatus.NotRead])
        self.hostId2PartyReplies[hostId].append(newReply)
        self.sendToAv(hostId, 'updateReply', [invite[1]] + newReply)
        self.save(dictName=('inviteKey2Invite', 'inviteeId2Invites', 'hostId2PartyReplies'))

    def delete(self):
        self.save()
        DistributedObjectGlobalUD.delete(self)

    def calculateRefund(self, activites, decorations):
        cost = 0
        for activity in [activityInfo[0] for activityInfo in activites]:
            cost += ActivityInformationDict[activity]['cost']
        for decor in [decorInfo[0] for decorInfo in decorations]:
            cost += DecorationInformationDict[decor]['cost']
        return int(round(cost * PartyRefundPercentage))
