import time, math
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase import ToontownGlobals

class DistributedDeliveryManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedDeliveryManagerAI")
    
    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)

    def hello(self, message):
        #I dont know what determined a successfull message...
        #Or even it's purpose....
        self.sendUpdate('helloResponse', [message])

    def getName(self, avId):
        av = self.air.doId2do.get(avId, None)
        if not av:
           errorMsg = 'Avatar ID %d not found in AI doId2do!' % avId
           self.sendUpdate('receiveRejectGetName', [errorMsg])
           self.notify.warning("Avatar was not found in doId2do when trying to get avatar name for UD!")
           del errorMsg
           return
        
        self.sendUpdate('addName', [avId, str(av.name)])

    def receiveRejectAddName(self, avId):
        if avId == 0:
            self.notify.warning('Add Name Request was rejected because of an invalid avId!')
        else:
            self.notify.warning('Add Name Request for %d was rejected!' % avId)
       
    def receiveAcceptAddName(self, todo0):
        pass

    def addGift(self, avId, item, context, optional = -1, senderId = None):
        av = self.air.doId2do.get(avId)
        sender = self.air.doId2do.get(senderId)
        
        if not sender and senderId:
            self.notify.warning("Gift Sender %d is not online or doesn't exist!" % senderId)
            return
        
        if not av:
            self.notify.warning("Toon %d is not online or doesn't exist!" % avId)
            return
    
        item.deliveryDate = int(time.time()/60) + item.getDeliveryTime()
        av.onOrder.append(item)
        av.b_setDeliverySchedule(av.onOrder)
        self.air.popularItemManager.avBoughtItem(item)

    def receiveRejectAddGift(self, todo0):
        pass

    def receiveAcceptAddGift(self, todo0, todo1, todo2, todo3):
        pass

    def deliverGifts(self, avId, now):
        av = self.air.doId2do.get(avId, None)
        if av == None:
            self.notify.warning("Failed to deliver gifts for Toon %d!" % avId)
            return
        
        delivered, remaining = av.onGiftOrder.extractDeliveryItems(now)
        self.notify.info('Gift Delivery for %s: %s.' % (av.doId, delivered))
        av.b_setMailboxContents(av.mailboxContents + delivered)
        self.sendDeliverGifts(av.doId, now)
        av.b_setCatalogNotify(av.catalogNotify, ToontownGlobals.NewItems)
        
    def sendDeliverGifts(self, avId, now):
        av = self.air.doId2do.get(avId, None)
        if av == None:
            return
            
        deliveredGifts, remainingGifts = av.onGiftOrder.extractDeliveryItems(now)
        av.b_setBothSchedules(remaining, remainingGifts)

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
        Return the ack for Deliveries. Why this was needed is 
        unknown to this day.
        '''
        self.sendUpdate('returnAck', [])

    def givePartyRefund(self, todo0, todo1, todo2, todo3, todo4):
        pass

