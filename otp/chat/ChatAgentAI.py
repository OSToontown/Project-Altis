from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal
from toontown.chat.ChatGlobals import *
from otp.distributed import OtpDoGlobals
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *

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

    def getToonAccess(self, avId):
        av = self.air.doId2do[avId]

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
            
        simbase.air.newsManager.sendSystemMessageToAvatar(av, message, 10)       
    
    def updateWarnings(self, avId, count, doBan):
        av = self.air.doId2do.get(avId, 0)
        if av == 0:
            self.notify.warning("Failed to update %d's warnings!" % (int(avId)))
            return
    
        av.b_setWarningCount(count, doBan)
        
    def kickForSpam(self, avatar):
        pass