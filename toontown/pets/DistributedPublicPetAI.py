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
        if self.owner.getPetId() == 0:
            DistributedPublicPetAI.notify.warning("Toon %d doesn't have a pet" % self.owner.doId)

        self.petId = self.owner.getPetId()
        def handleGenerate(pet):
            self.b_setOwnerId(pet.getOwnerId())
            self.b_setPetName(pet.getPetName())
            self.b_setTraitSeed(pet.getTraitSeed())
            self.b_setSafeZone(pet.getSafeZone())
            self.b_setForgetfulness(pet.getForgetfulness())
            self.b_setBoredomThreshold(pet.getBoredomThreshold())
            self.b_setRestlessnessThreshold(pet.getRestlessnessThreshold())
            self.b_setPlayfulnessThreshold(pet.getPlayfulnessThreshold())
            self.b_setLonelinessThreshold(pet.getLonelinessThreshold())
            self.b_setSadnessThreshold(pet.getSadnessThreshold())
            self.b_setFatigueThreshold(pet.getFatigueThreshold())
            self.b_setHungerThreshold(pet.getHungerThreshold())
            self.b_setConfusionThreshold(pet.getConfusionThreshold())
            self.b_setExcitementThreshold(pet.getExcitementThreshold())
            self.b_setAngerThreshold(pet.getAngerThreshold())
            self.b_setSurpriseThreshold(pet.getSurpriseThreshold())
            self.b_setAffectionThreshold(pet.getAffectionThreshold())
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
            self.b_setBoredom(pet.getBoredom())
            self.b_setRestlessness(pet.getRestlessness())
            self.b_setPlayfulness(pet.getPlayfulness())
            self.b_setLoneliness(pet.getLoneliness())
            self.b_setSadness(pet.getSadness())
            self.b_setAffection(pet.getAffection())
            self.b_setHunger(pet.getHunger())
            self.b_setConfusion(pet.getConfusion())
            self.b_setExcitement(pet.getExcitement())
            self.b_setFatigue(pet.getFatigue())
            self.b_setAnger(pet.getAnger())
            self.b_setSurprise(pet.getSurprise())
            self.b_setTrickAptitudes(pet.getTrickAptitudes())
            pet.requestDelete()

            def activatePet(task):
                return Task.done

            self.acceptOnce(self.air.getAvatarExitEvent(self.petId),
                            lambda: taskMgr.doMethodLater(0,
                            activatePet, self.uniqueName('petdel-%d' % self.petId)))

        self.air.sendActivate(self.petId, self.owner.air.districtId, 0)
        self.acceptOnce('generate-%d' % self.petId, handleGenerate)

    def generate(self):
        DistributedPetAI.DistributedPetAI.generate(self)

    def getFollowTaskName(self):
        return self.uniqueName('petfollow-%d' % self.petId)

    def followTask(self, task):
        print(self.actionFSM.state)
        if self.brain and self.shouldMove == True:
            self.mover.walkToAvatar(self.owner)

        taskMgr.doMethodLater(random.uniform(0.2, 0.7), self.followTask, self.getFollowTaskName())

    def announceGenerate(self):
        self.acquireProxyFields()
        self.setLocation(self.owner.air.districtId, self.owner.zoneId)

        def finishGenerate(task):
            self.sendUpdate('beginPublicDisplay', [])
            DistributedPetAI.DistributedPetAI.announceGenerate(self, public = True)

            position = self.owner.getPos() - Point3(-1, -1, 0)
            self.d_setPos(position.getX(), position.getY(), position.getZ())

            # Start following the toon
            taskMgr.doMethodLater(3.5, self.followTask, self.uniqueName('followStart'))

        # Leave a second so that doodle data can be fetched
        taskMgr.doMethodLater(2, finishGenerate, self.uniqueName('petactivate-%d') % self.petId)

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

    def disable(self):
        self.ignoreAll()
        taskMgr.remove(self.getFollowTaskName())
        DistributedObject.DistributedObject.disable(self)


