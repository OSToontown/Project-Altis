from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
# TODO: OTP should not depend on Toontown... Hrrm.
from toontown.chat.TTWhiteList import TTWhiteList

class ChatAgentUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("ChatAgentUD")

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

        self.whiteList = TTWhiteList()
        self.chatMode2prefix = {
            1: "[MOD] ",
            2: "[ADMIN] ",
            3: "[SYSADMIN] "
        }

    def chatMessage(self, message, chatMode):
        sender = self.air.getAvatarIdFromSender()
        if not sender:
            self.air.writeServerEvent('suspicious', self.air.getAccountIdFromSender(),
                                         'Account sent chat without an avatar', message)
            return

        cleanMessage, modifications = message, []
        modifications = []
        words = message.split('\x20')
        offset = 0
        WantWhitelist = config.GetBool('want-whitelist', 1)
        for word in words:
            if word and not self.whiteList.isWord(word) and WantWhitelist:
                modifications.append((offset, offset+len(word)-1))
            
            offset += len(word) + 1

        self.air.writeServerEvent('chat-said', avId=sender, chatMode=chatMode, msg=message, cleanMsg=cleanMessage)

        if chatMode != 0:
            if message.startswith('.'):

                cleanMessage = '.' + self.chatMode2prefix.get(chatMode, "") + message[1:]
            else:
                cleanMessage = self.chatMode2prefix.get(chatMode, "") + message
            
            modifications = []
        
        # send chat message update to ai
        self.sendUpdate('chatMessageResponse', [sender, cleanMessage, 
            modifications, chatMode])
