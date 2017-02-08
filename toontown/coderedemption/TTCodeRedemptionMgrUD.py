from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal
from toontown.catalog import CatalogItem
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem
from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.catalog.CatalogClothingItem import CatalogClothingItem, getAllClothes
from toontown.catalog.CatalogBeanItem import CatalogBeanItem
from toontown.catalog.CatalogGardenStarterItem import CatalogGardenStarterItem
from toontown.coderedemption import TTCodeRedemptionConsts

class TTCodeRedemptionMgrUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("TTCodeRedemptionMgrUD")

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

        # Store codes to result
        self.__codes = {'sillymeter': CatalogClothingItem(1753, 0), 'sweet': CatalogBeanItem(12000), 'greengift': CatalogGardenStarterItem()}
        self.__altnames = {'silly meter': 'sillymeter', 'green gift': 'greengift'}
        
    def giveAwardToToon(self, avId, code, context):
        item = CatalogInvalidItem()
         
        if code in self.__codes:
            item = self.__codes[code]
           
        if isinstance(item, CatalogInvalidItem):
            self.notify.warning("A invalid item was going to be delivered for redeeming a code! The delivery has been cancelled!")
            self.d_redeemCodeResultUdToAi(avId, context, TTCodeRedemptionConsts.RedeemErrors.AwardCouldntBeGiven, 1)
            return
            
        item = item.getBlob(store=CatalogItem.Customization)
           
        self.sendUpdate('deliverItem', [avId, context, item])


    def redeemCodeAiToUd(self, avId, context, code):
        if code in self.__altnames:
            if str(self.__altnames[code]) in self.__codes:
                self.notify.info(code)
                code = str(self.__altnames[code])
            
        if code not in self.__codes.keys():
            # Recieved an invalid code from AI, Deny redeem request.
            self.d_redeemCodeResultUdToAi(avId, context, TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist, 0)
            return
        
        self.giveAwardToToon(avId, code, context)

    def d_redeemCodeResultUdToAi(self, avId, context, result, awardMgrResult):
        self.sendUpdate('redeemCodeResultUdToAi', [avId, context, result, awardMgrResult])