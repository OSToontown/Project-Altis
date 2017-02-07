import time
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from toontown.catalog import CatalogItem
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem
from toontown.coderedemption import TTCodeRedemptionConsts
from toontown.toonbase import ToontownGlobals

class TTCodeRedemptionMgrAI(DistributedObjectGlobalAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("TTCodeRedemptionMgrAI")

    def __init__(self, air):
        DistributedObjectGlobalAI.__init__(self, air)

    def __getSender(self):
        avId = self.air.getAvatarIdFromSender()

        if avId not in self.air.doId2do.keys():
            return None

        return avId

    def giveAwardToToonResult(self, todo0, todo1):
        pass
        
    def deliverItem(self, avId, context, item):
        item = CatalogItem.getItem(item)
        if avId not in self.air.doId2do.keys():
            return 

        av = self.air.doId2do[avId]
        
        if isinstance(item, CatalogInvalidItem):
            self.notify.warning("A invalid item was going to be delivered for redeeming a code! The delivery has been cancelled!")
            self.d_redeemCodeResult(avId, context, TTCodeRedemptionConsts.RedeemErrors.AwardCouldntBeGiven, 0)
            return
            
        if len(av.mailboxContents) + len(av.onGiftOrder) >= ToontownGlobals.MaxMailboxContents:
            self.notify.debug("Avatar %d's mailbox is full! Not delivering item!" % (avId))
            self.d_redeemCodeResult(avId, context, TTCodeRedemptionConsts.RedeemErrors.AwardCouldntBeGiven, 0)
            return
            
        if av.isClosetFull():
            self.notify.debug("Avatar %d's closet is full! Not delivering item!" % (avId))
            self.d_redeemCodeResult(avId, context, TTCodeRedemptionConsts.RedeemErrors.AwardCouldntBeGiven, 0)
            return
            
        if item.reachedPurchaseLimit(av):
            self.notify.debug("Avatar %d already has reward! Not delivering item!" % (avId))
            self.d_redeemCodeResult(avId, context, TTCodeRedemptionConsts.RedeemErrors.CodeAlreadyRedeemed, 0)
            return
    
        item.deliveryDate = int(time.time() / 60) + 1 
        av.onOrder.append(item)
        av.b_setDeliverySchedule(av.onOrder)

        self.d_redeemCodeResult(avId, context, TTCodeRedemptionConsts.RedeemErrors.Success, 0)
        
    def redeemCode(self, context, code):
        avId = self.__getSender()

        if not avId:
            # got an invalid avatar id!
            return

        if len(code) > TTCodeRedemptionConsts.MaxCustomCodeLen:
            # got a code that exceeds the max code len.
            self.d_redeemCodeResult(avId, context, TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist,
                0)

            return

        self.redeemCodeAiToUd(avId, context, code)

    def redeemCodeAiToUd(self, avId, context, code):
        self.sendUpdate('redeemCodeAiToUd', [avId, context, code])

    def redeemCodeResultUdToAi(self, avId, context, result, awardMgrResult):
        self.d_redeemCodeResult(avId, context, result, awardMgrResult)

    def d_redeemCodeResult(self, avId, context, result, awardMgrResult):
        self.sendUpdateToAvatarId(avId, 'redeemCodeResult', [context, 
            result, awardMgrResult])