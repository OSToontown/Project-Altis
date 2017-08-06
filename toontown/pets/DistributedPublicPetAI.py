from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObjectAI
from direct.task import Task
from toontown.pets import DistributedPetAI
import random

class DistributedPublicPetAI(DistributedPetAI.DistributedPetAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedPublicPetAI')

    def __init__(self, air, owner):
        from toontown.pets import DistributedPetAI
        DistributedPetAI.DistributedPetAI.__init__(self, air)
        self.owner = owner
        self.petId = 0
        self.shouldMove = True

    def acquireProxyFields(self):
        self.notify.info("Beginning generate of pet")
        if self.owner.getPetId() == 0:
            DistributedPublicPetAI.notify.warning("Toon %d doesn't have a pet" % self.owner.doId)

        self.petId = self.owner.getPetId()
        def handleGenerate(pet):
            self.notify.info("Reading pet!")
            self.b_setOwnerId(pet.getOwnerId())
            self.b_setPetName(pet.getPetName())
            self.b_setTraitSeed(pet.getTraitSeed())
            self.b_setSafeZone(pet.getSafeZone())
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
            self.notify.info(pet.getTail())
            self.b_setHead(pet.getHead())
            self.b_setEars(pet.getEars())
            self.b_setNose(pet.getNose())
            self.b_setTail(pet.getTail())
            self.b_setBodyTexture(pet.getBodyTexture())
            self.b_setColor(pet.getColor())
            self.b_setColorScale(pet.getColorScale())
            self.b_setEyeColor(pet.getEyeColor())
            self.b_setGender(pet.getGender())
            self.b_setLastSeenTimestamp(pet.getLastSeenTimestamp())
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
            self.b_setTrickAptitudes(pet.getTrickAptitudes())
            pet.requestDelete()

            self.acceptOnce(self.air.getAvatarExitEvent(self.petId),
                            lambda: taskMgr.doMethodLater(0,
                                                          self.finishGenerate,
                                                          self.uniqueName('petdel-%d' % self.petId)))

        self.air.sendActivate(self.petId, self.air.districtId, 0)
        self.acceptOnce('generate-%d' % self.petId, handleGenerate)

    def generate(self):
        self.owner.petPresent = True
        self.acquireProxyFields()
        DistributedPetAI.DistributedPetAI.generate(self)

    def announceGenerate(self):
        self.notify.info("Announcing generate")

    def getFollowTaskName(self):
        return self.uniqueName('petfollow-%d' % self.petId)

    def followTask(self, task):
        if self.brain and self.shouldMove == True:
            self.mover.walkToAvatar(self.owner)

        taskMgr.doMethodLater(random.uniform(1, 1.5), self.followTask, self.getFollowTaskName())

    def finishGenerate(self, task):
        self.notify.info("Finishing generate!")
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
        self.accept(self.owner.getLogicalZoneChangeEvent(), self.__handleOwnerZoneChange)
        return task.done

    def sphereEntered(self):
        if self.air.getAvatarIdFromSender() != self.owner.doId:
            self.notify.info("Invalid sphere update sent to pet %d" % self.petId)
            return

        self.shouldMove = False

    def sphereLeft(self):
        if self.air.getAvatarIdFromSender() != self.owner.doId:
            self.notify.info("Invalid sphere update sent to pet %d" % self.petId)
            return

        self.shouldMove = True

    def __handleOwnerZoneChange(self, newZoneId, oldZoneId):
        self.disable()

    def __handleUnexpectedExit(self):
        self.notify.info("Our owner %d is gone, disabling public pet!" % avId)
        self.sendUpdate('finishPublicDisplay', [])
        taskMgr.doMethodLater(3, self.disable, self.uniqueName('cleanup-%d' % self.petId))

    def disable(self, task = None):
        self.ignoreAll()
        taskMgr.remove(self.getFollowTaskName())
        if self.owner:
            self.owner.petPresent = False

        DistributedPetAI.DistributedPetAI.delete(self)

