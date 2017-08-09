from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from toontown.pets.DistributedPublicPetAI import DistributedPublicPetAI
from toontown.toonbase import ToontownGlobals

class DistributedPublicPetMgrAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetMgrAI')
    wantPetMgr = False

    def requestAppearance(self):
        if DistributedPublicPetMgrAI.wantPetMgr == False:
            return

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

        def generateCallback(pet):
            self.notify.info("Doing callback")
            pet.generateWithRequired(av.zoneId)

        pet = DistributedPublicPetAI(self.air, av, generateCallback)
        pet.generateInit()





