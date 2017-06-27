from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from direct.interval.IntervalGlobal import *
from otp.speedchat import SpeedChatGlobals

class DistributedSofieListenerMgr(DistributedObject.DistributedObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedSofieListenerMgr')

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)
        DistributedSofieListenerMgr.notify.debug('announceGenerate')
        self.accept(SpeedChatGlobals.SCStaticTextMsgEvent, self.phraseSaid)
        
    def phraseSaid(self, phraseId):
        helpPhrase = 1505
        if phraseId == helpPhrase:
            self.addAchievement()

    def delete(self):
        self.ignore(SpeedChatGlobals.SCStaticTextMsgEvent)
        DistributedObject.DistributedObject.delete(self)

    def addAchievement(self):
        DistributedSofieListenerMgr.notify.debug('addResitanceEffect')
        self.sendUpdate('addAchievement', [])