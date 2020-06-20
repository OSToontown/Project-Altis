from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from direct.distributed.MsgTypes import *
from otp.ai.MagicWordGlobal import *
from otp.otpbase import OTPGlobals
from datetime import datetime
from direct.distributed.PyDatagram import PyDatagram
import time
import uuid
import string
import random

class FriendManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("FriendManagerAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.air = air
        self.currentContext = 0
        self.requests = {}
        self.trueFriendFSMs = {}
        # We comment this function out due to it being hardcoded to Mongo.
        # TODO: Detect if user is using Mongo and enable TFs.
        # self.trueFriendDatabase() # store true friends stuf in a diff database
        
    def trueFriendDatabase(self):
        self.air.dbGlobalCursor.trueFriendCodes.ensure_index('date', expireAfterSeconds = OTPGlobals.TF_CODE_EXPIRE)
        
    def getRandomCharSequence(self, count):
        return ''.join(random.choice(string.ascii_lowercase + string.digits) for i in xrange(count))
    
    def getCode(self):        
        code = 'TTPA %s %s' % (self.getRandomCharSequence(3), self.getRandomCharSequence(3))
        
        if (hasattr(self, 'data') and code in self.data) or (self.air.dbConn and self.air.dbGlobalCursor.trueFriendCodes.find({'_id': code}).count() > 0):
            return self.getCode()
        
        return code
    
    def requestTrueFriendCode(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        
        if not av:
            return

        self.air.banManager.ban(avId, "An error occured while processing your request.")
        datagram = PyDatagram()
        datagram.addServerHeader(
            av.GetPuppetConnectionChannel(av.doId),
            self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(155)
        datagram.addString("An error occured while processing your request.")
        self.air.send(datagram)
        
    def useTrueFriendCode(self, code):
        avId = self.air.getAvatarIdFromSender()
        print("%s entered code %s" %(avId, code))
        if avId in self.trueFriendFSMs:
            self.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_CALM_DOWN_PLEASE, ''])
            return
        
        av = self.air.doId2do.get(avId)
        if not av:
            return
        if hasattr(self, 'data'):
            if code not in self.data:
                print("not in data")
                self.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_UNKNOWN_CODE, ''])
                return
            
            targetId = self.data[code]
        else:
            fields = self.air.dbGlobalCursor.trueFriendCodes.find_one({'_id': code})
            print(fields)
            if not fields:
                self.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_UNKNOWN_CODE, ''])
                print("code not in fields")
                return
            targetId = fields['avId']
        if avId == targetId:
            self.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_SELF_CODE, ''])
            return
        elif av.isTrueFriends(targetId):
            self.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_ALREADY_FRIENDS, ''])
            return
        elif targetId not in av.getFriendsList() and len(av.getFriendsList()) >= OTPGlobals.MaxFriends:
            self.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_FRIENDS_FULL_LOCAL, ''])
            return
        
        operationTrueFriendStorm = AddTrueFriend(self, av, targetId, code)
        operationTrueFriendStorm.start()
        self.trueFriendFSMs[avId] = operationTrueFriendStorm

    def friendQuery(self, requested):
        avId = self.air.getAvatarIdFromSender()
        if not requested in self.air.doId2do:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to friend a player that does not exist!')
            return
        context = self.currentContext
        self.requests[context] = [ [ avId, requested ], 'friendQuery']
        self.currentContext += 1
        self.sendUpdateToAvatarId(requested, 'inviteeFriendQuery', [avId, self.air.doId2do[avId].getName(), self.air.doId2do[avId].getDNAString(), context])

    def cancelFriendQuery(self, context):
        avId = self.air.getAvatarIdFromSender()
        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel a request that doesn\'t exist!')
            return
        if avId != self.requests[context][0][0]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel someone elses request!')
            return
        self.requests[context][1] = 'cancelled'
        self.sendUpdateToAvatarId(self.requests[context][0][1], 'inviteeCancelFriendQuery', [context])

    def inviteeFriendConsidering(self, yesNo, context):
        avId = self.air.getAvatarIdFromSender()
        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to consider a friend request that doesn\'t exist!')
            return
        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to consider for someone else!')
            return
        if self.requests[context][1] != 'friendQuery':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to reconsider friend request!')
            return
        if yesNo != 1:
            self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendConsidering', [yesNo, context])
            del self.requests[context]
            return
        self.requests[context][1] = 'friendConsidering'
        self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendConsidering', [yesNo, context])

    def inviteeFriendResponse(self, response, context):
        avId = self.air.getAvatarIdFromSender()
        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to a friend request that doesn\'t exist!')
            return
        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to someone else\'s request!')
            return
        if self.requests[context][1] == 'cancelled':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to respond to non-active friend request!')
            return
        self.sendUpdateToAvatarId(self.requests[context][0][0], 'friendResponse', [response, context])
        if response == 1:

            requested = self.requests[context][0][1]
            if requested in self.air.doId2do:
                requested = self.air.doId2do[requested]
            else:
                del self.requests[context]
                return

            requester = self.requests[context][0][0]
            if requester in self.air.doId2do:
                requester = self.air.doId2do[requester]
            else:
                del self.requests[context]
                return

            requested.extendFriendsList(requester.getDoId(), 0)
            requester.extendFriendsList(requested.getDoId(), 0)

            requested.d_setFriendsList(requested.getFriendsList())
            requester.d_setFriendsList(requester.getFriendsList())
        del self.requests[context]


    def inviteeAcknowledgeCancel(self, context):
        avId = self.air.getAvatarIdFromSender()
        if not context in self.requests:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to acknowledge the cancel of a friend request that doesn\'t exist!')
            return
        if avId != self.requests[context][0][1]:
            self.air.writeServerEvent('suspicious', avId, 'Player tried to acknowledge someone else\'s cancel!')
            return
        if self.requests[context][1] != 'cancelled':
            self.air.writeServerEvent('suspicious', avId, 'Player tried to cancel non-cancelled request!')
            return
        del self.requests[context]


    def friendConsidering(self, todo0, todo1):
        pass

    def friendResponse(self, todo0, todo1):
        pass

    def inviteeFriendQuery(self, todo0, todo1, todo2, todo3):
        pass

    def inviteeCancelFriendQuery(self, todo0):
        pass

    def requestSecret(self):
        pass

    def requestSecretResponse(self, todo0, todo1):
        pass

    def submitSecret(self, todo0):
        pass

    def submitSecretResponse(self, todo0, todo1):
        pass
    
class AddTrueFriend:

    def __init__(self, manager, av, targetId, code):
        self.air = manager.air
        self.manager = manager
        self.av = av
        self.targetId = targetId
        self.code = code

    def start(self):
        self.air.dbInterface.queryObject(self.air.dbId, self.targetId, self.__gotAvatar)
    
    def __gotAvatar(self, dclass, fields):
        if dclass != self.air.dclassesByName['DistributedToonAI']:
            return
        
        friendsList = fields['setFriendsList'][0]
        try:
            trueFriendsList = fields['setTrueFriends'][0]
        except:
            trueFriendsList = []
        name = fields['setName'][0]
        avId = self.av.doId
        
        if avId in trueFriendsList:
            self.manager.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_ALREADY_FRIENDS, name])
            print('%s is already tf with %s (%s)'%(avId, self.targetId, name))
            return
        elif avId not in friendsList:
            if len(friendsList) >= OTPGlobals.MaxFriends:
                self.manager.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_FRIENDS_FULL_TARGET, ''])
                return
            
            friendsList.append((avId, 0))
        
        if self.targetId not in self.av.getFriendsList():
            self.av.extendFriendsList(self.targetId, 0)
        
        if hasattr(self.manager, 'data'):
            del self.manager.data[self.code]
        else:
            self.air.dbGlobalCursor.trueFriendCodes.remove({'_id': self.code})

        self.av.addTrueFriend(self.targetId)
        trueFriendsList.append(avId)
        self.air.send(dclass.aiFormatUpdate('setFriendsList', self.targetId, self.targetId, self.air.ourChannel, [friendsList]))
        self.air.send(dclass.aiFormatUpdate('setTrueFriends', self.targetId, self.targetId, self.air.ourChannel, [trueFriendsList]))
        self.air.dbInterface.updateObject(self.air.dbId, self.targetId, self.air.dclassesByName['DistributedToonAI'], {'setFriendsList' : [friendsList], 'setTrueFriends' : [trueFriendsList]})
        self.manager.sendUpdateToAvatarId(avId, 'trueFriendResponse', [OTPGlobals.TF_SUCCESS, name])
        del self.manager.trueFriendFSMs[avId]
