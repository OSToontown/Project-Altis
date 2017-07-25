import time
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from toontown.toonbase import ToontownGlobals
from toontown.estate import HouseGlobals, GardenGlobals
from toontown.fishing.DistributedFishingPondAI import DistributedFishingPondAI
from toontown.fishing.DistributedFishingTargetAI import DistributedFishingTargetAI
from toontown.fishing.DistributedPondBingoManagerAI import DistributedPondBingoManagerAI
from toontown.fishing import FishingTargetGlobals
from toontown.safezone.DistributedFishingSpotAI import DistributedFishingSpotAI
from toontown.safezone.SZTreasurePlannerAI import SZTreasurePlannerAI
from toontown.safezone import TreasureGlobals
from toontown.pets.DistributedPetAI import DistributedPetAI
# garden stuff
from toontown.estate.DistributedGardenPlotAI import DistributedGardenPlotAI
from toontown.estate.DistributedGardenBoxAI import DistributedGardenBoxAI
from toontown.estate.DistributedFlowerAI import DistributedFlowerAI
from toontown.estate.DistributedGagTreeAI import DistributedGagTreeAI
from toontown.estate.DistributedStatuaryAI import DistributedStatuaryAI
from toontown.estate.DistributedToonStatuaryAI import DistributedToonStatuaryAI
from toontown.estate.DistributedChangingStatuaryAI import DistributedChangingStatuaryAI
from toontown.estate.DistributedAnimatedStatuaryAI import DistributedAnimatedStatuaryAI
from toontown.distributed import ToontownInternalRepository

from toontown.parties import DistributedPartyJukebox40ActivityAI, DistributedPartyTrampolineActivityAI
from toontown.safezone import DistributedTreasureAI

from DistributedCannonAI import *
from DistributedTargetAI import *
import CannonGlobals
import random

NULL_PLANT = [-1, -1, 0, 0, 0]
NULL_TREES = [NULL_PLANT] * 8
NULL_FLOWERS = [NULL_PLANT] * 10
NULL_STATUARY = 0

NULL_DATA = {'trees': NULL_TREES, 'statuary': NULL_STATUARY, 'flowers': NULL_FLOWERS}

from direct.distributed.PyDatagramIterator import *
from direct.distributed.PyDatagram import *

class Garden:
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedEstateAI')

    def __init__(self, air, avId):
        self.air = air
        self.avId = avId

        self.trees = set()
        self.flowers = set()
        self.objects = set()
        self.intrepo = ToontownInternalRepository
        d = self.air.dbGlobalCursor.gardens.find_one({'avId': avId})
        if d is None:
            self.data = NULL_DATA.copy()
            self.air.dbGlobalCursor.gardens.update({'avId': avId}, {'$set': NULL_DATA}, upsert=True)

        else:
            self.data = d

        self.data.pop('_id', None)

    def destroy(self):
        for tree in self.trees:
            tree.requestDelete()

        for flower in self.flowers:
            flower.requestDelete()

        for object in self.objects:
            object.requestDelete()

        self.air = None
        self.estateMgr = None

    def create(self, estateMgr):
        self.estateMgr = estateMgr

        if self.avId not in estateMgr.toons:
            estateMgr.notify.warning('Garden associated to unknown avatar %d, deleting...' % self.avId)
            return False

        houseIndex = estateMgr.toons.index(self.avId)

        boxIndex = 0
        boxes = []

        self._boxes = boxes

        plots = GardenGlobals.estatePlots[houseIndex]
        treeIndex = 0
        flowerIndex = 0
        for plot, (x, y, h, type) in enumerate(plots):
            if type == GardenGlobals.GAG_TREE_TYPE:
                data = self.data['trees'][treeIndex]

                planted, waterLevel, lastCheck, growthLevel, lastHarvested = data

                if planted != -1:
                    obj = self.plantTree(treeIndex, planted, waterLevel=waterLevel,
                                         lastCheck=lastCheck, growthLevel=growthLevel,
                                         lastHarvested=lastHarvested, generate=False)

                    self.trees.add(obj)

                else:
                    obj = self.placePlot(treeIndex)

                obj.setPos(x, y, 0)
                obj.setH(h)
                obj.setPlot(plot)
                obj.setOwnerIndex(houseIndex)
                obj.generateWithRequired(estateMgr.zoneId)
                treeIndex += 1

            elif type == GardenGlobals.FLOWER_TYPE:
                pass
                '''
                data = self.data['flowers'][flowerIndex]

                planted, waterLevel, lastCheck, growthLevel, variety = data

                if planted != -1:
                    obj = self.plantFlower(flowerIndex, planted, variety, waterLevel=waterLevel,
                                           lastCheck=lastCheck, growthLevel=growthLevel,
                                           generate=False)

                else:
                    obj = self.placePlot(flowerIndex)
                    obj.flowerIndex = flowerIndex

                obj.setPlot(plot)
                obj.setOwnerIndex(houseIndex)
                obj.generateWithRequired(estateMgr.zoneId)

                index = (0, 1, 2, 2, 2, 3, 3, 3, 4, 4)[flowerIndex]
                idx = (0, 0, 0, 1, 2, 0, 1, 2, 0, 1)[flowerIndex]
                obj.sendUpdate('setBoxDoId', [boxes[index].doId, idx])
                flowerIndex += 1
                '''

            elif type == GardenGlobals.STATUARY_TYPE:
                data = self.data['statuary']
                if data == 0:
                    obj = self.placePlot(-1)

                else:
                    obj = self.placeStatuary(data, generate=False)

                obj.setPos(x, y, 0)
                obj.setH(h)
                obj.setPlot(plot)
                obj.setOwnerIndex(houseIndex)
                obj.generateWithRequired(estateMgr.zoneId)

        for tree in self.trees:
            tree.calcDependencies()

        self.reconsiderAvatarOrganicBonus()

        return True

    def hasTree(self, track, index):
        x = track * 7 + index
        for tree in self.data['trees']:
            if tree[0] == x:
                return True

        return False

    def getTree(self, track, index):
        for tree in self.trees:
            if tree.typeIndex == track * 7 + index:
                return tree

    def plantTree(self, treeIndex, value, plot=None, waterLevel=-1,
                  lastCheck=0, growthLevel=0, lastHarvested=0,
                  ownerIndex=-1, plotId=-1, pos=None, generate=True):
        if not self.air:
            return

        if plot:
            if plot not in self.objects:
                return

            plot.requestDelete()
            self.objects.remove(plot)

        tree = DistributedGagTreeAI(self)

        tree.setTypeIndex(value)
        tree.setWaterLevel(waterLevel)
        tree.setGrowthLevel(growthLevel)
        if ownerIndex != -1:
            tree.setOwnerIndex(ownerIndex)

        if plotId != -1:
            tree.setPlot(plotId)

        if pos is not None:
            pos, h = pos
            tree.setPos(pos)
            tree.setH(h)

        tree.treeIndex = treeIndex
        tree.calculate(lastHarvested, lastCheck)
        self.trees.add(tree)

        if generate:
            tree.generateWithRequired(self.estateMgr.zoneId)

        return tree

    def placePlot(self, treeIndex):
        obj = DistributedGardenPlotAI(self)
        obj.treeIndex = treeIndex
        self.objects.add(obj)

        return obj

    def plantFlower(self, flowerIndex, species, variety, plot=None, waterLevel=-1,
                    lastCheck=0, growthLevel=0, ownerIndex=-1, plotId=-1, generate=True):
        if not self.air:
            return

        if plot:
            if plot not in self.objects:
                return

            plot.slete()
            self.objects.remove(plot)

        flower = DistributedFlowerAI(self)

        flower.setTypeIndex(species)
        flower.setVariety(variety)
        flower.setWaterLevel(waterLevel)
        flower.setGrowthLevel(growthLevel)
        if ownerIndex != -1:
            flower.setOwnerIndex(ownerIndex)

        if plotId != -1:
            flower.setPlot(plotId)

        flower.flowerIndex = flowerIndex
        flower.calculate(lastCheck)
        self.flowers.add(flower)

        if generate:
            flower.generateWithRequired(self.estateMgr.zoneId)

        return flower

    def placeStatuary(self, data, plot=None, plotId=-1, ownerIndex=-1,
                      pos=None, generate=True):
        if not self.air:
            return

        if plot:
            if plot not in self.objects:
                return

            plot.requestDelete()
            self.objects.remove(plot)

        data, lastCheck, index, growthLevel = self.S_unpack(data)

        dclass = DistributedStatuaryAI
        if index in GardenGlobals.ToonStatuaryTypeIndices:
            dclass = DistributedToonStatuaryAI

        elif index in GardenGlobals.ChangingStatuaryTypeIndices:
            dclass = DistributedChangingStatuaryAI

        elif index in GardenGlobals.AnimatedStatuaryTypeIndices:
            dclass = DistributedAnimatedStatuaryAI

        obj = dclass(self)
        obj.growthLevel = growthLevel
        obj.index = index
        obj.data = data

        if ownerIndex != -1:
            obj.setOwnerIndex(ownerIndex)

        if plotId != -1:
            obj.setPlot(plotId)

        if pos is not None:
            pos, h = pos
            obj.setPos(pos)
            obj.setH(h)

        obj.calculate(lastCheck)

        self.objects.add(obj)

        if generate:
            obj.announceGenerate()

        return obj

    @staticmethod
    def S_pack(data, lastCheck, index, growthLevel):
        vh = data << 32 | lastCheck
        vl = index << 8 | growthLevel

        return vh << 16 | vl

    @staticmethod
    def S_unpack(x):
        vh = x >> 16
        vl = x & 0xFFFF

        data = vh >> 32
        lastCheck = vh & 0xFFFFFFFF

        index = vl >> 8
        growthLevel = vl & 0xFF

        return data, lastCheck, index, growthLevel

    def getNullPlant(self):
        return NULL_PLANT

    def reconsiderAvatarOrganicBonus(self):
        av = self.air.doId2do.get(self.avId)
        if not av:
            return
        bonus = [-1, -1, -1, -1, -1, -1, -1, -1]
        spentPoints = av.getSpentTrainingPoints()
        for i in xrange(8):
            if spentPoints[i] >= 3:
                bonus[i] = 6
        av.b_setTrackBonusLevel(bonus)

    def update(self):
        if self.air.dbConn:
            self.air.dbGlobalCursor.gardens.update({'avId': self.avId}, {'$set': self.data}, upsert=True)

class GardenManager:
    def __init__(self, mgr):
        self.mgr = mgr
        self.gardens = {}

    def handleSingleGarden(self, avId):
        g = Garden(self.mgr.air, avId)
        g.gardenMgr = self
        res = g.create(self.mgr)
        if res:
            self.gardens[avId] = g

    def destroy(self):
        messenger.send('garden-%d-1-gardenDestroy')
        for garden in self.gardens.values():
            garden.destroy()

        del self.gardens

class DistributedEstateAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedEstateAI")

    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)
        self.toons = [0, 0, 0, 0, 0, 0]
        self.items = [[], [], [], [], [], []]
        self.decorData = []
        self.estateType = 0 # NOT SURE IF THIS HAS ANY USE BUT THANKS DISNEY
        self.cloudType = 0
        self.dawnTime = 0
        self.lastEpochTimestamp = 0
        self.rentalTimestamp = 0
        self.houses = [None] * 6
        self.gardenBoxes = [[]] * 6
        self.gardenPlots = [[]] * 6

        self.pond = None
        self.spots = []

        # Estate Update Stuff
        self.jukebox = None
        # self.trampolines = []

        self.targets = []
        self.cannons = []
        self.target = None
        self.treasures = []
        self.treasureIds = []
        
        self.pets = []
        self.owner = None
        self.gardenManager = GardenManager(self)
        self.pendingGardens = {}

        
    # if i dont do this the jukebox will have a fuckin mental breakdown
    @property
    def hostId(self):
        return 1000000001

    def generate(self):
        DistributedObjectAI.generate(self)

        self.pond = DistributedFishingPondAI(simbase.air)
        self.pond.setArea(ToontownGlobals.MyEstate)
        self.pond.generateWithRequired(self.zoneId)

        for i in xrange(FishingTargetGlobals.getNumTargets(ToontownGlobals.MyEstate)):
            target = DistributedFishingTargetAI(self.air)
            target.setPondDoId(self.pond.getDoId())
            target.generateWithRequired(self.zoneId)
            self.targets.append(target)

        spot = DistributedFishingSpotAI(self.air)
        spot.setPondDoId(self.pond.getDoId())
        spot.setPosHpr(49.1029, -124.805, 0.344704, 90, 0, 0)
        spot.generateWithRequired(self.zoneId)
        self.spots.append(spot)

        spot = DistributedFishingSpotAI(self.air)
        spot.setPondDoId(self.pond.getDoId())
        spot.setPosHpr(46.5222, -134.739, 0.390713, 75, 0, 0)
        spot.generateWithRequired(self.zoneId)
        self.spots.append(spot)

        spot = DistributedFishingSpotAI(self.air)
        spot.setPondDoId(self.pond.getDoId())
        spot.setPosHpr(41.31, -144.559, 0.375978, 45, 0, 0)
        spot.generateWithRequired(self.zoneId)
        self.spots.append(spot)

        spot = DistributedFishingSpotAI(self.air)
        spot.setPondDoId(self.pond.getDoId())
        spot.setPosHpr(46.8254, -113.682, 0.46015, 135, 0, 0)
        spot.generateWithRequired(self.zoneId)
        self.spots.append(spot)

        self.createTreasurePlanner()
        
        self.jukebox = DistributedPartyJukebox40ActivityAI.DistributedPartyJukebox40ActivityAI(self.air, self.doId, (0, 0, 0, 0))
        self.jukebox.generateWithRequired(self.zoneId)
        self.jukebox.sendUpdate('setX', [118])
        self.jukebox.sendUpdate('setY', [-18])
        self.jukebox.sendUpdate('setH', [-80])
        
        # trampoline = DistributedPartyTrampolineActivityAI.DistributedPartyTrampolineActivityAI(self.air, self.doId, (0, 0, 0, 0))
        # trampoline.generateWithRequired(self.zoneId)
        # trampoline.sendUpdate('setX', [-130])
        # trampoline.sendUpdate('setY', [27])
        # trampoline.sendUpdate('setH', [80])
        # self.trampolines.append(trampoline)
        
        # trampoline2 = DistributedPartyTrampolineActivityAI.DistributedPartyTrampolineActivityAI(self.air, self.doId, (0, 0, 0, 0))
        # trampoline2.generateWithRequired(self.zoneId)
        # trampoline2.sendUpdate('setX', [-104])
        # trampoline2.sendUpdate('setY', [-56])
        # trampoline2.sendUpdate('setH', [80])
        # self.trampolines.append(trampoline2)
        
        # self.target = DistributedTargetAI(self.air)
        # self.target.generateWithRequired(self.zoneId)
        # self.target.setPosition(0, 0, 40)
        # for drop in CannonGlobals.cannonDrops:
            # cannon = DistributedCannonAI(self.air)
            # cannon.setEstateId(self.doId)
            # cannon.setTargetId(self.target.doId)
            # cannon.setPosHpr(*drop)
            # cannon.generateWithRequired(self.zoneId)
            # self.cannons.append(cannon)
        # self.b_setClouds(True)
        doIds = []
        for i in range(40):
            x = random.randint(100, 300) - 200
            y = random.randint(100, 300) - 200
            treasure = DistributedTreasureAI.DistributedTreasureAI(self.air, self, 8, x, y, 35)
            treasure.generateWithRequired(self.zoneId)
            self.treasures.append(treasure)
            doIds.append(treasure.doId)
        self.setTreasureIds(doIds)
        
    def grabAttempt(self, avId, treasureId):
        av = self.air.doId2do.get(avId)
        if not av:
            return
            
        treasure = self.air.doId2do.get(treasureId)
        if av.getMaxHp() != av.getHp():
            av.toonUp(5)
            treasure.d_setGrab(avId)
            treasure.requestDelete()
            
        else:
            treasure.d_setReject()

    def announceGenerate(self):
        DistributedObjectAI.announceGenerate(self)
        self.sendUpdate('setIdList', [self.toons])

        for index, started in self.pendingGardens.items():
            if started:
                self.gardenManager.handleSingleGarden(self.toons[index])

        self.pendingGardens = {}

    def destroy(self):
        for house in self.houses:
            if house:
                house.requestDelete()
        self.houses = []
        if self.pond:
            self.pond.requestDelete()
            for spot in self.spots:
                spot.requestDelete()

            self.spots = []
            
        for treasure in self.treasures:
            if not treasure.isDeleted():
                treasure.requestDelete()
            
        # for target in self.targets:
            # target.requestDelete()
      
        for pet in self.pets:
            pet.requestDelete()
            
        # self.b_setClouds(False)
        # if self.target:
            # self.target.requestDelete()
            
        # for cannon in self.cannons:
            # cannon.requestDelete()
        if self.jukebox:
            self.jukebox.requestDelete()
            
        # for trampoline in self.trampolines:
            # trampoline.requestDelete()
            
        if self.treasurePlanner:
            self.treasurePlanner.stop()
            
        if self.gardenManager:
            self.gardenManager.destroy()

        self.requestDelete()

    def setEstateReady(self):
        pass

    def setClientReady(self):
        self.sendUpdate('setEstateReady', [])

    def setEstateType(self, type):
        self.estateType = type

    def d_setEstateType(self, type):
        self.sendUpdate('setEstateType', [type])

    def b_setEstateType(self, type):
        self.setEstateType(type)
        self.d_setEstateType(type)

    def getEstateType(self):
        return self.estateType

    def setClosestHouse(self, todo0):
        pass

    def setTreasureIds(self, doIds):
        self.treasureIds = doIds
        self.sendUpdate("setTreasureIds", [doIds])

    def createTreasurePlanner(self):
        treasureType, healAmount, spawnPoints, spawnRate, maxTreasures = TreasureGlobals.SafeZoneTreasureSpawns[ToontownGlobals.MyEstate]
        self.treasurePlanner = SZTreasurePlannerAI(self.zoneId, treasureType, healAmount, spawnPoints, spawnRate, maxTreasures)
        self.treasurePlanner.start()

    def initPets(self, owner):

        def _queryAccount(dclass, fields):
            avatarList = fields['ACCOUNT_AV_SET']

            def _queryToon(dclass, fields):
                petId, = fields['setPetId']

                if not petId:
                    return

                # activate the pet object on the dbss
                self.air.sendActivate(petId, self.air.districtId, self.zoneId, dclass=\
                    self.air.dclassesByName['DistributedPetAI'])

                # keep track of what pets are activated.
                self.pets.append(petId)

            for avId in avatarList:
                if not avId:
                    continue

                self.air.dbInterface.queryObject(self.air.dbId, avId,
                    callback=_queryToon)

        self.air.dbInterface.queryObject(self.air.dbId, owner.DISLid,
            callback=_queryAccount)

    def destroyPet(self, owner):
        for petId in self.pets:
            if owner != self.air.doId2do.get(petId):
                return

            # now check if the pet has actually been activated
            self.air.getActivated(petId, self.__handleGetPetActivated)

    def __handleGetPetActivated(self, doId, activated):
        # if the pet wasn't activated, dont destroy it.
        if not activated or doId not in self.air.doId2do.keys():
            return

        # alright, all's good destroy the pet instance
        self.air.doId2do[doId].requestDelete()

    def requestServerTime(self):
        self.sendUpdateToAvatarId(self.air.getAvatarIdFromSender(), 'setServerTime', [
            time.time() % HouseGlobals.DAY_NIGHT_PERIOD])

    def setServerTime(self, todo0):
        pass

    def setDawnTime(self, dawnTime):
        self.dawnTime = dawnTime

    def d_setDawnTime(self, dawnTime):
        self.sendUpdate('setDawnTime', [dawnTime])

    def b_setDawnTime(self, dawnTime):
        self.setDawnTime(dawnTime)
        self.d_setDawnTime(dawnTime)

    def getDawnTime(self):
        return self.dawnTime

    def placeOnGround(self, todo0):
        pass

    def setDecorData(self, decorData):
        self.decorData = decorData

    def d_setDecorData(self, decorData):
        self.sendUpdate('setDecorData', [decorData])

    def b_setDecorData(self, decorData):
        self.setDecorData(decorData)
        self.d_setDecorData(decorData)

    def getDecorData(self):
        return self.decorData

    def setLastEpochTimeStamp(self, last): #how do I do this
        self.lastEpochTimestamp = last

    def d_setLastEpochTimeStamp(self, last):
        self.sendUpdate('setLastEpochTimeStamp', [last])

    def b_setLastEpochTimeStamp(self, last):
        self.setLastEpochTimeStamp(last)
        self.d_setLastEpochTimeStamp(last)

    def getLastEpochTimeStamp(self):
        return self.lastEpochTimestamp

    def setRentalTimeStamp(self, rental):
        self.rentalTimestamp = rental

    def d_setRentalTimeStamp(self, rental):
        self.sendUpdate('setRentalTimeStamp', [rental])

    def b_setRentalTimeStamp(self, rental):
        self.setRentalTimeStamp(self, rental)
        self.b_setRentalTimeStamp(self, rental)

    def getRentalTimeStamp(self):
        return self.rentalTimestamp

    def setRentalType(self, todo0):
        pass

    def getRentalType(self):
        return 0

    def setSlot0ToonId(self, id):
        self.toons[0] = id

    def d_setSlot0ToonId(self, id):
        self.sendUpdate('setSlot0ToonId', [id])

    def b_setSlot0ToonId(self, id):
        self.setSlot0ToonId(id)
        self.d_setSlot0ToonId(id)

    def getSlot0ToonId(self):
        return self.toons[0]

    def setSlot0Items(self, items):
        self.items[0] = items

    def d_setSlot0Items(self, items):
        self.sendUpdate('setSlot5Items', [items])

    def b_setSlot0Items(self, items):
        self.setSlot0Items(items)
        self.d_setSlot0Items(items)

    def getSlot0Items(self):
        return self.items[0]

    def setSlot1ToonId(self, id):
        self.toons[1] = id

    def d_setSlot1ToonId(self, id):
        self.sendUpdate('setSlot1ToonId', [id])

    def b_setSlot1ToonId(self, id):
        self.setSlot1ToonId(id)
        self.d_setSlot1ToonId(id)

    def getSlot1ToonId(self):
        return self.toons[1]

    def setSlot1Items(self, items):
        self.items[1] = items

    def d_setSlot1Items(self, items):
        self.sendUpdate('setSlot2Items', [items])

    def b_setSlot1Items(self, items):
        self.setSlot2Items(items)
        self.d_setSlot2Items(items)

    def getSlot1Items(self):
        return self.items[1]

    def setSlot2ToonId(self, id):
        self.toons[2] = id

    def d_setSlot2ToonId(self, id):
        self.sendUpdate('setSlot2ToonId', [id])

    def b_setSlot2ToonId(self, id):
        self.setSlot2ToonId(id)
        self.d_setSlot2ToonId(id)

    def getSlot2ToonId(self):
        return self.toons[2]

    def setSlot2Items(self, items):
        self.items[2] = items

    def d_setSlot2Items(self, items):
        self.sendUpdate('setSlot2Items', [items])

    def b_setSlot2Items(self, items):
        self.setSlot2Items(items)
        self.d_setSlot2Items(items)

    def getSlot2Items(self):
        return self.items[2]

    def setSlot3ToonId(self, id):
        self.toons[3] = id

    def d_setSlot3ToonId(self, id):
        self.sendUpdate('setSlot3ToonId', [id])

    def b_setSlot3ToonId(self, id):
        self.setSlot3ToonId(id)
        self.d_setSlot3ToonId(id)

    def getSlot3ToonId(self):
        return self.toons[3]

    def setSlot3Items(self, items):
        self.items[3] = items

    def d_setSlot3Items(self, items):
        self.sendUpdate('setSlot3Items', [items])

    def b_setSlot3Items(self, items):
        self.setSlot3Items(items)
        self.d_setSlot3Items(items)

    def getSlot3Items(self):
        return self.items[3]

    def setSlot4ToonId(self, id):
        self.toons[4] = id

    def d_setSlot4ToonId(self, id):
        self.sendUpdate('setSlot4ToonId', [id])

    def b_setSlot5ToonId(self, id):
        self.setSlot4ToonId(id)
        self.d_setSlot4ToonId(id)

    def getSlot4ToonId(self):
        return self.toons[4]

    def setSlot4Items(self, items):
        self.items[4] = items

    def d_setSlot4Items(self, items):
        self.sendUpdate('setSlot4Items', [items])

    def b_setSlot4Items(self, items):
        self.setSlot4Items(items)
        self.d_setSlot4Items(items)

    def getSlot4Items(self):
        return self.items[4]

    def setSlot5ToonId(self, id):
        self.toons[5] = id

    def d_setSlot5ToonId(self, id):
        self.sendUpdate('setSlot5ToonId', [id])

    def b_setSlot5ToonId(self, id):
        self.setSlot5ToonId(id)
        self.d_setSlot5ToonId(id)

    def getSlot5ToonId(self):
        return self.toons[5]

    def setSlot5Items(self, items):
        self.items[5] = items

    def d_setSlot5Items(self, items):
        self.sendUpdate('setSlot5Items', [items])

    def b_setSlot5Items(self, items):
        self.setSlot5Items(items)
        self.d_setSlot5Items(items)

    def getSlot5Items(self):
        return self.items[5]

    def setIdList(self, idList):
        for i in xrange(len(idList)):
            if i >= 6:
                return
            self.toons[i] = idList[i]

    def d_setIdList(self, idList):
        self.sendUpdate('setIdList', [idList])

    def b_setIdList(self, idList):
        self.setIdList(idList)
        self.d_setIdLst(idList)

    def completeFlowerSale(self, flag):
        if not flag:
            return

        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do.get(avId)
        if not av:
            return

        collection = av.flowerCollection

        earning = 0
        newSpecies = 0
        for flower in av.flowerBasket.getFlower():
            if collection.collectFlower(flower) == GardenGlobals.COLLECT_NEW_ENTRY:
                newSpecies += 1

            earning += flower.getValue()

        av.b_setFlowerBasket([], [])
        av.d_setFlowerCollection(*av.flowerCollection.getNetLists())
        av.addMoney(earning)

        oldSpecies = len(collection) - newSpecies
        dt = abs(len(collection) // 10 - oldSpecies // 10)
        if dt:
            maxHp = av.getMaxHp()
            maxHp = min(ToontownGlobals.MaxHpLimit, maxHp + dt)
            av.b_setMaxHp(maxHp)
            av.toonUp(maxHp)

            self.sendUpdate('awardedTrophy', [avId])

        av.b_setGardenTrophies(range(len(collection) // 10))

    def awardedTrophy(self, todo0):
        pass

    def setClouds(self, clouds):
        self.cloudType = clouds

    def d_setClouds(self, clouds):
        self.sendUpdate('setClouds', [clouds])

    def b_setClouds(self, clouds):
        self.setClouds(clouds)
        self.d_setClouds(clouds)

    def getClouds(self):
        return self.cloudType

    def cannonsOver(self):
        pass

    def gameTableOver(self):
        pass

    def addDistObj(self, distObj):
        self.doId2do[distObj.doId] = distObj

    def updateToons(self):
        self.d_setSlot0ToonId(self.toons[0])
        self.d_setSlot1ToonId(self.toons[1])
        self.d_setSlot2ToonId(self.toons[2])
        self.d_setSlot3ToonId(self.toons[3])
        self.d_setSlot4ToonId(self.toons[4])
        self.d_setSlot5ToonId(self.toons[5])
        self.sendUpdate('setIdList', [self.toons])

    def updateItems(self):
        self.d_setSlot0Items(self.items[0])
        self.d_setSlot1Items(self.items[1])
        self.d_setSlot2Items(self.items[2])
        self.d_setSlot3Items(self.items[3])
        self.d_setSlot4Items(self.items[4])
        self.d_setSlot5Items(self.items[5])

    # Garden stuff
    def getToonSlot(self, avId):
        if avId not in self.toons:
            return

        return self.toons.index(avId)

    def setSlot0Garden(self, flag):
        self.pendingGardens[0] = flag

    def setSlot1Garden(self, flag):
        self.pendingGardens[1] = flag

    def setSlot2Garden(self, flag):
        self.pendingGardens[2] = flag

    def setSlot3Garden(self, flag):
        self.pendingGardens[3] = flag

    def setSlot4Garden(self, flag):
        self.pendingGardens[4] = flag

    def setSlot5Garden(self, flag):
        self.pendingGardens[5] = flag

    def placeStarterGarden(self, avId, record=1):
        av = self.air.doId2do.get(avId)
        if not av:
            return

        slot = self.getToonSlot(avId)
        if slot is None:
            return

        if record:
            av.b_setGardenStarted(1)
            self.sendUpdate('setSlot%dGarden' % slot, ['started'])

        self.notify.info('placeStarterGarden %d %d' % (avId, slot))
        self.gardenManager.handleSingleGarden(avId)
