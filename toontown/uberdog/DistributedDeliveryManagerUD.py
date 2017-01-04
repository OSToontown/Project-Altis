from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD

class DistributedDeliveryManagerUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDeliveryManagerUD")
    
    def announceGenerate(self):
        DistributedObjectUD.announceGenerate(self)
        self.toonDoId = 0
        self.toonName = ''

    def receiveRejectGetName(self, string):
        self.notify.warning(string)
        self.resetToonInfo()
        
    def resetToonInfo(self):
        self.toonDoId = 0
        self.toonName = ''

    def receiveAcceptGetName(self, todo0):
        pass

    def addName(self, avId, name):
        if not avId:
            self.sendUpdate('receiveRejectAddName', [0])
            return
        if not name:
            self.sendUpdate('receiveRejectAddName', [avId])
            return
        
        #There has to be a better way to do this.
        self.toonDoId = avId
        self.toonName = name

    def addGift(self, todo0, todo1, todo2, todo3, todo4):
        pass

    def receiveRejectAddGift(self, todo0):
        pass

    def receiveAcceptAddGift(self, todo0, todo1, todo2, todo3):
        pass

    def deliverGifts(self, todo0, todo1):
        pass

    def receiveAcceptDeliverGifts(self, todo0, todo1):
        pass

    def receiveRejectDeliverGifts(self, todo0, todo1):
        pass

    def receiveRequestPayForGift(self, todo0, todo1, todo2):
        pass

    def receiveRequestPurchaseGift(self, todo0, todo1, todo2, todo3):
        pass

    def receiveAcceptPurchaseGift(self, todo0, todo1, todo2):
        pass

    def receiveRejectPurchaseGift(self, todo0, todo1, todo2, todo3):
        pass

    def heartbeat(self):
        pass

    def giveBeanBonus(self, todo0, todo1):
        pass

    def givePartyRefund(self, todo0, todo1, todo2, todo3, todo4):
        pass

