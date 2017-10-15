from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal
from toontown.chat.ChatGlobals import *
from otp.distributed import OtpDoGlobals
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from time import gmtime, strftime
import json
import httplib
import six

def to_bool(boolorstr):
    if isinstance(boolorstr, six.string_types):
        return boolorstr.lower() == 'true'
    if isinstance(boolorstr, bool):
        return boolorstr
    else:
        return False

class ChatAgentAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("ChatAgentAI")

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)
        self.chatMode2channel = {
            1: OtpDoGlobals.OTP_MOD_CHANNEL,
            2: OtpDoGlobals.OTP_ADMIN_CHANNEL,
            3: OtpDoGlobals.OTP_SYSADMIN_CHANNEL,
        }
        self.air = air
        self.accept('requestToonAccess', self.getToonAccess)
        self.accept('warningUpdate', self.updateWarnings)
        self.accept('requestOffenses', self.sendAvatarOffenses)
        self.accept('sendSystemMessage', self.sendSystemMessage)
        self.accept('chatBan', self.banAvatar)
        self.accountId = 0
        self.domain = str(ConfigVariableString('ws-domain', 'localhost'))
        self.key = str(ConfigVariableString('ws-key', 'secretkey'))

    def chatMessage(self, message, fakeChatMode):
        sender = self.air.getAvatarIdFromSender()
        if not sender:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(),
                                      'Account sent chat without an avatar', message)
            return

        if fakeChatMode != 0:
            # We've caught a skid!
            self.notify.warning('Fake chat mode was not zero for avatar %s' % sender)
            return

        av = self.air.doId2do.get(sender)
        if not av:
            return

        chatMode = av.getChatMode()

        self.sendUpdate('chatMessageAiToUd', [sender, message, chatMode])

    def chatMessageResponse(self, sender, message, modifications, chatMode):
        if sender not in self.air.doId2do.keys():
            # found an invalid sender!
            return

        av = self.air.doId2do[sender]

        if not av:
            # got a invalid avatar object!
            return

        # broadcast chat message update
        av.b_setTalk(sender, self.chatMode2channel.get(chatMode, sender), av.getName(), message, modifications, 
            CFSpeech | CFQuicktalker | CFTimeout)
        self.air.dbInterface.queryObject(self.air.dbId, av.DISLid, self.dbCallback)
        getRealUsername = httplib.HTTPSConnection(self.domain)
        getRealUsername.request('GET', '/api/tokentousername/%s/%s' % (self.key, self.accountId))
        try:
            f = getRealUsername.getresponse().read()
            getRealUsernameResp = json.loads(f)
            if to_bool(getRealUsernameResp["error"]):
                username = "ERROR " + getRealUsernameResp["message"]
            else:
                username = getRealUsernameResp['username']
        except:
            self.notify.debug("Fatal Error During Logging!")
            username = 'ERRORED'
        filename = 'data/%s_chatlog.txt' % str(self.air.districtId)
        file = open(filename, 'a')
        file.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()) + ': ' + str(sender) + '(%s)' % username  + ': ' + message + "\n")
        file.close()

    def dbCallback(self, dclass, fields):
        if dclass != self.air.dclassesByName['AccountAI']:
            return

        self.accountId = fields.get('ACCOUNT_ID')

        if not self.accountId:
            return

    def getToonAccess(self, avId):
        av = self.air.doId2do.get(avId)

        if not av:
            return
            
        access = av.getAccessLevel()
        self.air.sendNetEvent('requestToonAccessResponse', [access])
        
    def sendAvatarOffenses(self, avId, sender):
        av = self.air.doId2do.get(avId, 0)
        if av == 0:
            self.notify.warning("Failed to update %d's chat offenses!" % (int(avId)))
            return
        
        self.air.sendNetEvent('setAvatarOffenses', [sender, int(av.getWarningCount())])
        
    def banAvatar(self, avId, msg, time):
        self.notify.debug("Got ban request from Uberdog!")
        av = self.air.doId2do.get(avId, 0)
        if av == 0:
            self.notify.warning("Failed to ban %d for chat abuse!" % (int(avId)))
            return
         
        if av.getAdminAccess() < MINIMUM_MAGICWORD_ACCESS:
            av.doWarningBan('Chat Abuse', 24)
               
    def sendSystemMessage(self, message, avId):
        av = self.air.doId2do.get(avId, 0)
        if av == 0:
            self.notify.warning("Failed to send system message for %d" % (int(avId)))
            return
            
        self.air.newsManager.sendSystemMessageToAvatar(av, message, 10)
    
    def updateWarnings(self, avId, count, doBan):
        av = self.air.doId2do.get(avId, 0)
        if av == 0:
            self.notify.warning("Failed to update %d's warnings!" % (int(avId)))
            return
    
        av.b_setWarningCount(count, doBan)
        
    def kickForSpam(self, avatar):
        pass
