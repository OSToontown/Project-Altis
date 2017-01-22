from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal
from toontown.chat.ChatGlobals import *
from otp.distributed import OtpDoGlobals

class ChatAgentAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("ChatAgentAI")

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)
        self.chatMode2channel = {
            1: OtpDoGlobals.OTP_MOD_CHANNEL,
            2: OtpDoGlobals.OTP_ADMIN_CHANNEL,
            3: OtpDoGlobals.OTP_SYSADMIN_CHANNEL,
        }

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
