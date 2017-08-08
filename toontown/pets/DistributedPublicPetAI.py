from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.task import Task
from toontown.pets import DistributedPetAI
import random

class DistributedPublicPetAI(DistributedPetAI.DistributedPetAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetAI')

    def __init__(self, air, owner, callback):
        from toontown.pets import DistributedPetAI
        DistributedPetAI.DistributedPetAI.__init__(self, air)
        self.owner = owner
        self.petId = 0
        self.shouldMove = True
        self.callback = callback

    def acquireProxyFields(self):
        self.notify.info("Beginning generate of pet")
        if self.owner.getPetId() == 0:
            DistributedPublicPetAI.notify.warning("Toon %d doesn't have a pet" % self.owner.doId)

        self.petId = self.owner.getPetId()
        def handleGenerate(pet):
            self.setOwnerId(pet.getOwnerId())
            self.setPetName(pet.getPetName())
            self.setTraitSeed(pet.getTraitSeed())
            self.setSafeZone(pet.getSafeZone())
            self.setForgetfulness(pet.getForgetfulness())
            self.setBoredomThreshold(pet.getBoredomThreshold())
            self.setRestlessnessThreshold(pet.getRestlessnessThreshold())
            self.setPlayfulnessThreshold(pet.getPlayfulnessThreshold())
            self.setLonelinessThreshold(pet.getLonelinessThreshold())
            self.setSadnessThreshold(pet.getSadnessThreshold())
            self.setFatigueThreshold(pet.getFatigueThreshold())
            self.setHungerThreshold(pet.getHungerThreshold())
            self.setConfusionThreshold(pet.getConfusionThreshold())
            self.setExcitementThreshold(pet.getExcitementThreshold())
            self.setAngerThreshold(pet.getAngerThreshold())
            self.setSurpriseThreshold(pet.getSurpriseThreshold())
            self.setAffectionThreshold(pet.getAffectionThreshold())
            self.setHead(pet.getHead())
            self.setEars(pet.getEars())
            self.setNose(pet.getNose())
            self.setTail(pet.getTail())
            self.setBodyTexture(pet.getBodyTexture())
            self.setColor(pet.getColor())
            self.setColorScale(pet.getColorScale())
            self.setEyeColor(pet.getEyeColor())
            self.setGender(pet.getGender())
            self.setLastSeenTimestamp(pet.getLastSeenTimestamp())
            self.setBoredom(pet.getBoredom())
            self.setRestlessness(pet.getRestlessness())
            self.setPlayfulness(pet.getPlayfulness())
            self.setLoneliness(pet.getLoneliness())
            self.setSadness(pet.getSadness())
            self.setAffection(pet.getAffection())
            self.setHunger(pet.getHunger())
            self.setConfusion(pet.getConfusion())
            self.setExcitement(pet.getExcitement())
            self.setFatigue(pet.getFatigue())
            self.setAnger(pet.getAnger())
            self.setSurprise(pet.getSurprise())
            self.setTrickAptitudes(pet.getTrickAptitudes())
            pet.requestDelete()
            self.callback(self)

        self.air.sendActivate(self.petId, self.air.districtId, 0)
        self.acceptOnce('generate-%d' % self.petId, handleGenerate)


    def generateInit(self):
        self.acquireProxyFields()

    def generate(self):
        self.owner.petPresent = True
        DistributedPetAI.DistributedPetAI.generate(self)

    def announceGenerate(self):
        self.finishGenerate()

    def getFollowTaskName(self):
        return self.uniqueName('petfollow-%d' % self.petId)

    def followTask(self, task):
        if self.brain and self.shouldMove == True:
            self.mover.walkToAvatar(self.owner)

        taskMgr.doMethodLater(random.uniform(1, 1.5), self.followTask, self.getFollowTaskName())

    def finishGenerate(self):
        self.setLocation(self.owner.air.districtId, self.owner.zoneId)
        if self.getPetName() == 'unnamed':
            self.disable()
            return

        DistributedPetAI.DistributedPetAI.announceGenerate(self, public=True)
        self.sendUpdate('beginPublicDisplay', [])

        position = self.owner.getPos() - Point3(-1, -1, 0)
        self.d_setPos(position.getX(), position.getY(), position.getZ())

        # Start following the toon
        taskMgr.doMethodLater(3.5, self.followTask, self.uniqueName('followStart'))
        self.acceptOnce(self.air.getAvatarExitEvent(self.owner.doId), self.__handleUnexpectedExit)

        # Listen for zone changes. Note that this is logical because we don't want to go to the quiet zone
        self.accept(self.owner.getZoneChangeEvent(), self.__handleOwnerZoneChange)

    def sphereEntered(self):
        try:
            if self.air.getAvatarIdFromSender() != self.owner.doId:
                self.notify.info("Invalid sphere update sent to pet %d" % self.petId)
                return

            self.shouldMove = False
        except:
            self.notify.info("Sphere update with exception sent to pet %d" % self.petId)
            return

    def sphereLeft(self):
        try:
            if self.air.getAvatarIdFromSender() != self.owner.doId:
                self.notify.info("Invalid sphere update sent to pet %d" % self.petId)
                return

            self.shouldMove = True
        except:
            self.notify.info("Sphere update with exception sent to pet %d" % self.petId)
            return

    def __handleOwnerZoneChange(self, newZoneId, oldZoneId):
        self.disable()

    def __handleUnexpectedExit(self):
        self.notify.info("Our owner %d is gone, disabling public pet!" % self.owner.doId)
        self.sendUpdate('finishPublicDisplay', [])
        taskMgr.doMethodLater(3, self.disable, self.uniqueName('cleanup-%d' % self.petId))

    def disable(self, task = None):
        self.ignoreAll()
        taskMgr.remove(self.getFollowTaskName())
        if self.owner:
            self.owner.petPresent = False

        DistributedPetAI.DistributedPetAI.delete(self)

