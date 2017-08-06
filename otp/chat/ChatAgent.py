from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from panda3d.core import *
from panda3d.direct import *
from otp.otpbase import OTPGlobals
from otp.ai.MagicWordGlobal import *

class ChatAgent(DistributedObjectGlobal):

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.chatMode = 0

    def delete(self):
        self.ignoreAll()
        self.cr.chatManager = None
        DistributedObjectGlobal.delete(self)

    def adminChat(self, aboutId, message):
        self.notify.warning('Admin Chat(%s): %s' % (aboutId, message))
        messenger.send('adminChat', [aboutId, message])

    def sendChatMessage(self, message):
        self.sendUpdate('chatMessage', [message, self.chatMode])
        
    def kickForSpam(self, av):
        self.sendUpdate('kickForSpam', [av.doId])
