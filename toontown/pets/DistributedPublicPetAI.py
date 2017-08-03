from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from toontown.pets import DistributedPetProxyAI, DistributedPetAI
from direct.task import Task


class DistributedPublicPetAI(DistributedPetAI.DistributedPetAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetAI')

    def __init__(self, air, owner):
        DistributedPetAI.DistributedPetAI.__init__(self, air)
        self.owner = owner
        self.proxy = None
        self.proxyDo = 0
        self.petId = 0

    def acquireProxyFields(self):
        if self.proxy == None:
            DistributedPublicPetAI.notify.warning("No pet proxy is present in public pet %d" % self.doId)
            return

        if self.owner.getPetId() == 0:
            DistributedPublicPetAI.notify.warning("Toon %d doesn't have a pet" % self.owner.doId)

        self.petId = self.owner.getPetId()
        def handleGenerate(pet):
            self.setOwnerId_b(pet.getOwnerId())
            self.setPetName_b(pet.getPetName())
            self.setTraitSeed_b(pet.getTraitSeed())
            self.setSafeZone_b(pet.getSafeZone())
            self.setForgetfulness_b(pet.getForgetfulness())
            self.setBoredomThreshold_b(pet.getBoredomThreshold())
            self.setRestlessnessThreshold_b(pet.getRestlessnessThreshold())
            self.setPlayfulnessThreshold_b(pet.getPlayfulnessThreshold())
            self.setLonelinessThreshold_b(pet.getLonelinessThreshold())
            self.setSadnessThreshold_b(pet.getSadnessThreshold())
            self.setFatigueThreshold_b(pet.getFatigueThreshold())
            self.setHungerThreshold_b(pet.getHungerThreshold())
            self.setConfusionThreshold_b(pet.getConfusionThreshold())
            self.setExcitementThreshold_b(pet.getExcitementThreshold())
            self.setAngerThreshold_b(pet.getAngerThreshold())
            self.setSurpriseThreshold_b(pet.getSurpriseThreshold())
            self.setAffectionThreshold_b(pet.getAffectionThreshold())
            self.setHead_b(pet.getHead())
            self.setEars_b(pet.getEars())
            self.setNose_b(pet.getNose())
            self.setTail_b(pet.getTail())
            self.setBodyTexture_b(pet.getBodyTexture())
            self.setColor_b(pet.getColor())
            self.setColorScale_b(pet.getColorScale())
            self.setEyeColor_b(pet.getEyeColor())
            self.setGender_b(pet.getGender())
            self.setLastSeenTimestamp_b(pet.getLastSeenTimestamp())
            self.setBoredom_b(pet.getBoredom())
            self.setRestlessness_b(pet.getRestlessness())
            self.setPlayfulness_b(pet.getPlayfulness())
            self.setLoneliness_b(pet.getLoneliness())
            self.setSadness_b(pet.getSadness())
            self.setAffection_b(pet.getAffection())
            self.setHunger_b(pet.getHunger())
            self.setConfusion_b(pet.getConfusion())
            self.setExcitement_b(pet.getExcitement())
            self.setFatigue_b(pet.getFatigue())
            self.setAnger_b(pet.getAnger())
            self.setSurprise_b(pet.getSurprise())
            self.setTrickAptitudes_b(pet.getTrickAptitudes())
            pet.requestDelete()

            def activatePet(task):
                return Task.done

            self.acceptOnce(self.air.getAvatarExitEvent(self.petId),
                            lambda: taskMgr.doMethodLater(0,
                            activatePet, self.uniqueName('petdel-%d' % self.petId)))

        self.air.sendActivate(self.petId, self.owner.air.districtId, 0)
        self.acceptOnce('generate-%d' % self.petId, handleGenerate)

    def generate(self):
        self.proxy = DistributedPetProxyAI.DistributedPetProxyAI(self.air)
        self.acquireProxyFields()
        DistributedPetAI.DistributedPetAI.generate(self)

    def announceGenerate(self):
        self.setLocation(self.owner.air.districtId, self.owner.zoneId)
        DistributedPetAI.DistributedPetAI.announceGenerate(self)


