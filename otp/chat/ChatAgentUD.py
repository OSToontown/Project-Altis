from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
# TODO: OTP should not depend on Toontown... Hrrm.
from toontown.chat.TTWhiteList import TTWhiteList
from toontown.chat.BlackListData import BLACKLIST

OFFENSE_MSGS = ('-- DEV CHAT -- blocked blacklisted word!', 'Watch your language! This is your first offense.',
                'Watch your language! This is your second offense. Next offense you\'ll get banned for 24 hours.')

class ChatAgentUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("ChatAgentUD")

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

        self.whiteList = TTWhiteList()
        self.toonAccess = 100
        self.offenses = {}
        self.chatMode2prefix = {
            1: "[MOD] ",
            2: "[ADMIN] ",
            3: "[SYSADMIN] "
        }
        self.accept('setAvatarOffenses', self.updateAvatarOffenses)
        self.accept('requestToonAccessResponse', self.requestToonAccessResponse)

    def chatMessageAiToUd(self, sender, message, chatMode):
        if self.detectBadWords(sender, message):
            self.notify.info("Detected Bad Word or Blacklisted Pharse from %d" % (sender))
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
            
    def requestToonAccessResponse(self, access):
        self.toonAccess = access
        
    def updateAvatarOffenses(self, sender, count):
        avId = sender & 0xFFFFFFFF
        if not sender in self.offenses:
             self.offenses[sender] = 0
             
        self.offenses[sender] = count
        
        if self.offenses[sender] >= 3:
            # Ban the offender
            self.air.sendNetEvent('warningUpdate', [avId, 0, True])
            msg = 'banned'
            self.air.sendNetEvent('banAvatar', [avId, 'Chat Abuse', 24])
            
    def detectBadWords(self, sender, message):
        if message.lower() in BLACKLIST:
            avId = sender

            if not sender in self.offenses:
                self.offenses[sender] = 0
                
            self.air.sendNetEvent('requestToonAccess', [avId])
                
            if self.toonAccess < 300:                     
                self.offenses[sender] += 1
                self.air.sendNetEvent('warningUpdate', [avId, int(self.offenses[sender]), True])
           
            if self.offenses[sender] >= 3:
                # Ban the offender
                msg = 'banned'
                self.air.sendNetEvent('chatBan', [avId, 'Chat Abuse', 24])
            else:
                msg = OFFENSE_MSGS[self.offenses[sender]]
                self.air.sendNetEvent('sendSystemMessage', [msg, sender])
                
            if self.offenses[sender] >= 3:
                del self.offenses[sender]
                
            return 1
        words = message.split('\x20')
        for word in words:
            if word.lower() in BLACKLIST:
                avId = sender

                if not sender in self.offenses:
                    self.offenses[sender] = 0
                    
                self.air.sendNetEvent('requestToonAccess', [avId])
                    
                if self.toonAccess < 300:                     
                    self.offenses[sender] += 1
                    self.air.sendNetEvent('warningUpdate', [avId, int(self.offenses[sender]), True])
               
                if self.offenses[sender] >= 3:
                    # Ban the offender
                    msg = 'banned'
                    self.air.sendNetEvent('chatBan', [avId, 'Chat Abuse', 24])
                else:
                    msg = OFFENSE_MSGS[self.offenses[sender]]
                    self.air.sendNetEvent('sendSystemMessage', [msg, sender])
                    
                if self.offenses[sender] >= 3:
                    del self.offenses[sender]
                    
                return 1
                
        return 0
        
