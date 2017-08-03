from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from toontown.pets import DistributedPetProxyAI
from direct.task import Task


class DistributedPublicPetAI(DistributedObjectAI.DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetAI')

    def __init__(self, air, owner):
        DistributedObjectAI.DistributedObjectAI.__init__(self, air)
        self.owner = owner
        self.proxy = None

    def acquireProxyFields(self):
        if self.proxy == None:
            notify.warning("No pet proxy is present in public pet %d" % self.doId)
            return

        if self.owner.getPetId() == 0:
            notify.warning("Toon %d doesn't have a pet" % owner.doId)

        self.petId = self.owner.getPetId()
        def handleGenerate(pet):
            self.proxy.setOwnerId(pet.getOwnerId())
            self.proxy.setPetName(pet.getPetName())
            self.proxy.setTraitSeed(pet.getTraitSeed())
            self.proxy.setSafeZone(pet.getSafeZone())
            self.proxy.setForgetfulness(pet.getForgetfulness())
            self.proxy.setBoredomThreshold(pet.getBoredomThreshold())
            self.proxy.setRestlessnessThreshold(pet.getRestlessnessThreshold())
            self.proxy.setPlayfulnessThreshold(pet.getPlayfulnessThreshold())
            self.proxy.setLonelinessThreshold(pet.getLonelinessThreshold())
            self.proxy.setSadnessThreshold(pet.getSadnessThreshold())
            self.proxy.setFatigueThreshold(pet.getFatigueThreshold())
            self.proxy.setHungerThreshold(pet.getHungerThreshold())
            self.proxy.setConfusionThreshold(pet.getConfusionThreshold())
            self.proxy.setExcitementThreshold(pet.getExcitementThreshold())
            self.proxy.setAngerThreshold(pet.getAngerThreshold())
            self.proxy.setSurpriseThreshold(pet.getSurpriseThreshold())
            self.proxy.setAffectionThreshold(pet.getAffectionThreshold())
            self.proxy.setHead(pet.getHead())
            self.proxy.setEars(pet.getEars())
            self.proxy.setNose(pet.getNose())
            self.proxy.setTail(pet.getTail())
            self.proxy.setBodyTexture(pet.getBodyTexture())
            self.proxy.setColor(pet.getColor())
            self.proxy.setColorScale(pet.getColorScale())
            self.proxy.setEyeColor(pet.getEyeColor())
            self.proxy.setGender(pet.getGender())
            self.proxy.setLastSeenTimestamp(pet.getLastSeenTimestamp())
            self.proxy.setBoredom(pet.getBoredom())
            self.proxy.setRestlessness(pet.getRestlessness())
            self.proxy.setPlayfulness(pet.getPlayfulness())
            self.proxy.setLoneliness(pet.getLoneliness())
            self.proxy.setSadness(pet.getSadness())
            self.proxy.setAffection(pet.getAffection())
            self.proxy.setHunger(pet.getHunger())
            self.proxy.setConfusion(pet.getConfusion())
            self.proxy.setExcitement(pet.getExcitement())
            self.proxy.setFatigue(pet.getFatigue())
            self.proxy.setAnger(pet.getAnger())
            self.proxy.setSurprise(pet.getSurprise())
            self.proxy.setTrickAptitudes(pet.getTrickAptitudes())
            pet.requestDelete()

            def activatePet(self):
                self.proxy.doNotDeallocateChannel = True
                self.proxy.generateWithRequiredAndId(self.petId, self.owner.air.districtId, self.owner.zoneId)
                self.proxy.broadcastDominantMood()
                self.b_setProxyDo(self.proxy.doId)
                return Task.done

            self.acceptOnce(self.air.getAvatarExitEvent(self.petId),
                            lambda: taskMgr.doMethodLater(0,
                            activatePet, self.uniqueName('petdel-%d' % self.petId)))

        self.air.sendActivate(self.petId, self.owner.air.districtId, 0)
        self.acceptOnce('generate-%d' % self.petId, handleGenerate)

    def generate(self):
        self.proxy = DistributedPetProxyAI.DistributedPetProxyAI(self.air)
        self.acquireProxyFields()
        DistributedObjectAI.DistributedObjectAI.generate(self)

    def announceGenerate(self):
        self.setLocation(self.owner.air.districtId, self.owner.zoneId)
        # self.sendUpdate("beginPublicDisplay", [])
        DistributedObjectAI.DistributedObjectAI.announceGenerate(self)

    def setProxyDo(self, do):
        self.proxyDo = do

    def b_setProxyDo(self, do):
        self.d_setProxyDo(do)
        self.setProxyDo(do)

    def d_setProxyDo(self, do):
        self.sendUpdate('setProxyDo', [do])
