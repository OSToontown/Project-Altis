from direct.directnotify import DirectNotifyGlobal
from toontown.ai.DistributedPhaseEventMgrAI import DistributedPhaseEventMgrAI
from otp.ai.MagicWordGlobal import *

class DistributedMailboxZeroMgrAI(DistributedPhaseEventMgrAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMailboxZeroMgrAI")
    
    def __init__(self, air):
        DistributedPhaseEventMgrAI.__init__(self, air)

@magicWord(category=CATEGORY_PROGRAMMER)
def setMailboxMgrOnline():
    simbase.air.mailboxZeroMgr.b_setIsRunning(True)
    return "Mailbox Mgr is now running!"