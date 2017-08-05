from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI

class DistributedPublicPetMgrAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetMgrAI')

    def requestAppearance(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        self.sendUpdateToAvatarId(avId, 'requestAppearanceResp', 1)
