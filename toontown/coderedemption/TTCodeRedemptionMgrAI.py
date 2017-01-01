from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from toontown.coderedemption import TTCodeRedemptionConsts

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