from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI

class DistributedDeliveryManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDeliveryManagerAI")

    def hello(self, message):
        #I dont know what determined a successfull message...
        #Or even it's purpose....
        self.sendUpdate('helloResponse', [message])

    def getName(self, avId):
        av = self.air.doId2do.get(avId, None)
        if not av:
           self.notify.warning("Avatar was not found in doId2do when trying to get avatar name!")
           return
        
        self.sendUpdate('addName', [avId, str(av.name)])

    def receiveRejectGetName(self, todo0):
        pass

    def receiveAcceptGetName(self, todo0):
        pass

    def receiveRejectAddName(self, todo0):
        pass

    def receiveAcceptAddName(self, todo0):
        pass

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

    def requestAck(self):
        '''
        Return the ack for Gifts in the Catalog. Why this was needed is 
        unknown to this day.
        '''
        self.sendUpdate('returnAck', [])

    def givePartyRefund(self, todo0, todo1, todo2, todo3, todo4):
        pass

