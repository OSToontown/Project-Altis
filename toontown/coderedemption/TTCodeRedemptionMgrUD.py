from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.directnotify import DirectNotifyGlobal
from toontown.coderedemption import TTCodeRedemptionConsts

class TTCodeRedemptionMgrUD(DistributedObjectGlobalUD):
    notify = DirectNotifyGlobal.directNotify.newCategory("TTCodeRedemptionMgrUD")

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

        # store codes to result
        self.__codes = {}

    def giveAwardToToonResult(self, todo0, todo1):
        pass

    def redeemCodeAiToUd(self, avId, context, code):
        if code not in self.__codes.keys():
            # recieved an invalid code from ai, deny redeem request.
            self.d_redeemCodeResultUdToAi(avId, context, TTCodeRedemptionConsts.RedeemErrors.CodeDoesntExist,
                0)

            return

    def d_redeemCodeResultUdToAi(self, avId, context, result, awardMgrResult):
        self.sendUpdate('redeemCodeResultUdToAi', [avId, context, result, awardMgrResult])