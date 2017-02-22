from direct.directnotify import DirectNotifyGlobal

from DistributedLawnDecorAI import DistributedLawnDecorAI
from otp.ai.MagicWordGlobal import *
import GardenGlobals


class DistributedGardenPlotAI(DistributedLawnDecorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedGardenPlotAI')

    def announceGenerate(self):
        DistributedLawnDecorAI.announceGenerate(self)
        self.plotType = GardenGlobals.whatCanBePlanted(self.ownerIndex, self.plot)
        self.__plantingAvId = 0

    def plantFlower(self, species, variety, usingGardenFlowerAll = 0):
        wantedType = GardenGlobals.FLOWER_TYPE if not usingGardenFlowerAll else None
        if self.__plantingAvId:
            return

        avId = self.air.getAvatarIdFromSender()

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if wantedType is not None and self.plotType != wantedType:
            return self.d_interactionDenied()


        if avId != self.ownerDoId:
            return self.d_interactionDenied()
        if not av:
            return

        def invalid(problem):
            msg = 'tried to plant flower but something went wrong: %s' % problem
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            if not usingGardenFlowerAll:
                return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        attr = GardenGlobals.PlantAttributes.get(species, {})
        if attr.get('plantType') != GardenGlobals.FLOWER_TYPE:
            return invalid('invalid species: %d' % species)

        if variety >= len(attr['varieties']):
            return invalid('invalid variety: %d' % variety)

        if not usingGardenFlowerAll:
            cost = len(GardenGlobals.Recipes[attr['varieties'][variety][0]]['beans'])
            av.takeMoney(cost)

            self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def _plant(task):
            flower = self.mgr.plantFlower(self.flowerIndex, species, variety, plot = self, ownerIndex = self.ownerIndex, plotId = self.plot, waterLevel = 0)
            index = (0, 1, 2, 2, 2, 3, 3, 3, 4, 4)[self.flowerIndex]
            idx = (0, 0, 0, 1, 2, 0, 1, 2, 0, 1)[self.flowerIndex]
            flower.sendUpdate('setBoxDoId', [self.mgr._boxes[index].doId, idx])

            if not usingGardenFlowerAll:
                flower.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
                flower.d_setMovie(GardenGlobals.MOVIE_CLEAR, self.__plantingAvId)

            self.air.writeServerEvent('plant-flower', self.__plantingAvId, species = species, variety = variety, plot = self.plot, name = attr.get('name', 'unknown garden flower'))
            if task:
                return task.done

        if usingGardenFlowerAll:
            _plant(None)

        else:
            taskMgr.doMethodLater(7, _plant, self.uniqueName('do-plant'))

        self.__plantingAvId = av.doId
        return 1

    def plantGagTree(self, track, index):
        if self.__plantingAvId:
            return

        avId = self.air.getAvatarIdFromSender()

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if self.plotType != GardenGlobals.GAG_TREE_TYPE:
            return self.d_interactionDenied()


        if avId != self.ownerDoId:
            return self.d_interactionDenied()
        if not av:
            return

        for i in xrange(index):
            if not self.mgr.hasTree(track, i):
                self.notify.warning('%d %s' % (av.doId, 'tried to plant tree but an index is missing: %d' % index))
                return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        if self.mgr.hasTree(track, index):
            self.notify.warning('%d %s' % (av.doId, 'tried to plant tree but gag already planted'))
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        if av.inventory.useItem(track, index) == -1:
            self.notify.warning('%d %s' % (av.doId, 'tried to plant tree but not carrying selected gag'))
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        av.d_setInventory(av.getInventory())
        self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def _plant(task):
            if not self.air:
                return

            tree = self.mgr.plantTree(self.treeIndex, track * 7 + index, plot = self, ownerIndex = self.ownerIndex, plotId = self.plot, pos = (self.getPos(), self.getH()))
            tree.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
            tree.d_setMovie(GardenGlobals.MOVIE_CLEAR, self.__plantingAvId)
            self.air.writeServerEvent('plant-tree', self.__plantingAvId, track = track, index = index, plot = self.plot)
            return task.done

        taskMgr.doMethodLater(7, _plant, self.uniqueName('do-plant'))
        self.__plantingAvId = av.doId

    def plantStatuary(self, species):
        if self.__plantingAvId:
            return

        avId = self.air.getAvatarIdFromSender()

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if self.plotType != GardenGlobals.STATUARY_TYPE:
            return self.d_interactionDenied()


        if avId != self.ownerDoId:
            return self.d_interactionDenied()
        if not av:
            return

        def invalid(problem):
            msg = 'Error when planting statuary! %s' % problem
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        attr = GardenGlobals.PlantAttributes.get(species, {})
        if attr.get('plantType') != GardenGlobals.STATUARY_TYPE:
            return invalid('invalid species: %d' % species)

        it = species - 100
        if it == 134:
            it = 135

        if not av.removeGardenItem(it, 1):
            return invalid("Avatar doesn't own %d" % species)

        self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def _plant(task):
            if not self.air:
                return

            statuary = self.mgr.placeStatuary(self.mgr.S_pack(0, 0, species, 0), plot = self,
                                              ownerIndex = self.ownerIndex, plotId = self.plot,
                                              pos = (self.getPos(), self.getH()), generate = False)
            statuary.generateWithRequired(self.zoneId)
            statuary.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
            statuary.d_setMovie(GardenGlobals.MOVIE_CLEAR, self.__plantingAvId)
            self.air.writeServerEvent('plant-statuary', self.__plantingAvId, species = species, plot = self.plot)
            return task.done

        taskMgr.doMethodLater(7, _plant, self.uniqueName('do-plant'))
        self.__plantingAvId = av.doId

    def plantToonStatuary(self, species, dnaCode):
        if self.__plantingAvId:
            return

        avId = self.air.getAvatarIdFromSender()

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if self.plotType != GardenGlobals.STATUARY_TYPE:
            return self.d_interactionDenied()


        if avId != self.ownerDoId:
            return self.d_interactionDenied()
        if not av:
            return

        def invalid(problem):
            msg = 'Error when planting statuary! %s' % problem
            self.notify.warning('%d %s' % (av.doId, msg))
            self.air.writeServerEvent('suspicious', av.doId, msg)
            return self.d_setMovie(GardenGlobals.MOVIE_PLANT_REJECTED)

        attr = GardenGlobals.PlantAttributes.get(species, {})
        if attr.get('plantType') != GardenGlobals.STATUARY_TYPE:
            return invalid('invalid species: %d' % species)

        if not av.removeGardenItem(species - 100, 1):
            return invalid("Avatar doesn't own %d" % species)

        self.d_setMovie(GardenGlobals.MOVIE_PLANT)

        def _plant(task):
            if not self.air:
                return

            statuary = self.mgr.placeStatuary(self.mgr.S_pack(dnaCode, 0, species, 0), plot = self, ownerIndex = self.ownerIndex, plotId = self.plot, pos = (self.getPos(), self.getH()), generate = False)
            statuary.generateWithRequired(self.zoneId)
            statuary.d_setMovie(GardenGlobals.MOVIE_FINISHPLANTING, self.__plantingAvId)
            self.air.writeServerEvent('plant-statuary', self.__plantingAvId, species = species, plot = self.plot)
            return task.done

        taskMgr.doMethodLater(7, _plant, self.uniqueName('do-plant'))
        self.__plantingAvId = av.doId

    def plantNothing(self, burntBeans):
        if self.__plantingAvId:
            return

        avId = self.air.getAvatarIdFromSender()

        av = self.air.doId2do.get(avId)
        if not av:
            return

        if self.plotType != None:
            return self.d_interactionDenied()


        if avId != self.ownerDoId:
            return self.d_interactionDenied()
        if av:
            av.takeMoney(burntBeans)

@magicWord(category = CATEGORY_PROGRAMMER, types = [int, int])
def gardenFlowerAll(species = 49, variety = 0):
    invoker = spellbook.getInvoker()
    av = spellbook.getTarget()
    estate = av.air.estateManager._lookupEstate(av)

    if not estate:
        return 'Estate not found!'

    garden = estate.gardenManager.gardens.get(av.doId)
    if not garden:
        return 'Garden not found!'

    i = 0
    for obj in garden.objects.copy():
        if isinstance(obj, DistributedGardenPlotAI):
            if obj.plotType != GardenGlobals.FLOWER_TYPE:
                continue

            if not obj.plantFlower(species, variety, 1):
                return 'Error on plot %d' % i

            i += 1

    return 'Planted %d flowers!' % i

@magicWord(category = CATEGORY_PROGRAMMER)
def allGardenSpecials():
    av = spellbook.getTarget()
    av.gardenSpecials = []
    for x in (100, 101, 103, 105, 106, 107, 108, 109, 130, 131, 135):
        av.addGardenItem(x, 99)
    return "Gave all gardenSpecials"