from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from toontown.pets.DistributedPublicPetAI import DistributedPublicPetAI
from toontown.toonbase import ToontownGlobals

class DistributedPublicPetMgrAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetMgrAI')

    def requestAppearance(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        if av.petPresent == True:
            self.sendUpdateToAvatarId(avId, 'requestAppearanceResp', [2])
            return

        if not (av.zoneId in ToontownGlobals.safeZones):
            self.sendUpdateToAvatarId(avId, 'requestAppearanceResp', [1])
            return

        pet = DistributedPublicPetAI(self.air, av)
        pet.generateWithRequired(av.zoneId)




