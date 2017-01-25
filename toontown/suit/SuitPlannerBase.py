from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.building import SuitBuildingGlobals
from toontown.dna.DNAParser import DNASuitPoint, DNAStorage, loadDNAFileAI

class SuitPlannerBase:
    notify = directNotify.newCategory('SuitPlannerBase')
    SuitHoodInfo = [[ToontownGlobals.SillyStreet,
      15,
      30,
      0,
      5,
      20,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (20,
       20,
       20,
       20,
       20),
      (2, 3, 4),
      []],
     [ToontownGlobals.LoopyLane,
      15,
      30,
      0,
      5,
      15,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (30,
       40,
       5,
       5,
       20),
      (1, 2, 3),
      []],
     [ToontownGlobals.PunchlinePlace,
      15,
      30,
      0,
      5,
      15,
      3,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       40,
       40,
       10),
      (1, 2, 3),
      []],
     [ToontownGlobals.BarnacleBoulevard,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (80,
       10,
       0,
       0,
       10),
      (2, 3, 4, 5),
      []],
     [ToontownGlobals.SeaweedStreet,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       10,
       60,
       30,
       0),
      (3, 4, 5),
      []],
     [ToontownGlobals.LighthouseLane,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (10,
       40,
       10,
       10,
       30),
      (3,
       4,
       5,
       6),
      []],
     [ToontownGlobals.WalrusWay,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (75,
       5,
       0,
       0,
       20),
      (5, 6, 7, 8),
      []],
     [ToontownGlobals.SleetStreet,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       30,
       60,
       10),
      (5, 6, 7, 8),
      []],
     [ToontownGlobals.PolarPlace,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       80,
       5,
       5,
       5),
      (7, 8, 9),
      []],
     [ToontownGlobals.AltoAvenue,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       50,
       50,
       0),
      (3, 4, 5),
      []],
     [ToontownGlobals.BaritoneBoulevard,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       90,
       10,
       0),
      (4,
       5,
       6,
       7),
      []],
     [ToontownGlobals.TenorTerrace,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (15,
       10,
       0,
       0,
       75),
      (5,
       6,
       7,
       8),
      []],
     [ToontownGlobals.ElmStreet,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       40,
       40,
       10),
      (2,
	   3,
	   4,
	   5,
	   6),
      []],
     [ToontownGlobals.MapleStreet,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (30,
       60,
       0,
       0,
       10),
      (4, 5, 6),
      []],
     [ToontownGlobals.OakStreet,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80,
       0),
      (5,
       5,
       5,
       80,
       5),
      (4,
       5,
       6,
	   7),
      []],
     [ToontownGlobals.LullabyLane,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (20,
       20,
       20,
       20,
       20),
      (7,
       8,
       9,
       10),
      []],
     [ToontownGlobals.PajamaPlace,
      15,
      30,
      0,
      99,
      100,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (5,
       5,
       80,
       5,
       5),
      (6,
       7,
       8,
       9),
      []],
     [ToontownGlobals.BossbotHQ,
      15,
      30,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (100,
       0,
       0,
       0,
       0),
      (8, 9, 10),
      []],  
     [ToontownGlobals.SellbotHQ,
      15,
      30,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100,
       0),
      (3, 4, 5, 6),
      []],
     [ToontownGlobals.SellbotFactoryExt,
      15,
      30,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       0,
       100,
       0),
      (4, 5, 6),
      []],
     [ToontownGlobals.CashbotHQ,
      15,
      30,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       0,
       100,
       0,
       0),
      (6, 7, 8, 9),
      []],
     [ToontownGlobals.LawbotHQ,
      15,
      30,
      0,
      0,
      0,
      4,
      (1,
       5,
       10,
       40,
       60,
       80),
      (0,
       100,
       0,
       0,
       0),
      (7, 8, 9, 10),
      []]]
    SUIT_HOOD_INFO_ZONE = 0
    SUIT_HOOD_INFO_MIN = 1
    SUIT_HOOD_INFO_MAX = 2
    SUIT_HOOD_INFO_BMIN = 3
    SUIT_HOOD_INFO_BMAX = 4
    SUIT_HOOD_INFO_BWEIGHT = 5
    SUIT_HOOD_INFO_SMAX = 6
    SUIT_HOOD_INFO_JCHANCE = 7
    SUIT_HOOD_INFO_TRACK = 8
    SUIT_HOOD_INFO_LVL = 9
    SUIT_HOOD_INFO_HEIGHTS = 10
    TOTAL_BWEIGHT = 0
    TOTAL_BWEIGHT_PER_TRACK = [0,
     0,
     0,
     0,
     0]
    TOTAL_BWEIGHT_PER_HEIGHT = [0,
     0,
     0,
     0,
     0,
     0]
    for currHoodInfo in SuitHoodInfo:
        weight = currHoodInfo[SUIT_HOOD_INFO_BWEIGHT]
        tracks = currHoodInfo[SUIT_HOOD_INFO_TRACK]
        levels = currHoodInfo[SUIT_HOOD_INFO_LVL]
        heights = [0,
         0,
         0,
         0,
         0,
         0]
        for level in levels:
            minFloors, maxFloors = SuitBuildingGlobals.SuitBuildingInfo[level - 1][0]
            for i in xrange(minFloors - 1, maxFloors):
                heights[i] += 1

        currHoodInfo[SUIT_HOOD_INFO_HEIGHTS] = heights
        TOTAL_BWEIGHT += weight
        TOTAL_BWEIGHT_PER_TRACK[0] += weight * tracks[0]
        TOTAL_BWEIGHT_PER_TRACK[1] += weight * tracks[1]
        TOTAL_BWEIGHT_PER_TRACK[2] += weight * tracks[2]
        TOTAL_BWEIGHT_PER_TRACK[3] += weight * tracks[3]
        TOTAL_BWEIGHT_PER_TRACK[4] += weight * tracks[4]
        TOTAL_BWEIGHT_PER_HEIGHT[0] += weight * heights[0]
        TOTAL_BWEIGHT_PER_HEIGHT[1] += weight * heights[1]
        TOTAL_BWEIGHT_PER_HEIGHT[2] += weight * heights[2]
        TOTAL_BWEIGHT_PER_HEIGHT[3] += weight * heights[3]
        TOTAL_BWEIGHT_PER_HEIGHT[4] += weight * heights[4]
        TOTAL_BWEIGHT_PER_HEIGHT[5] += weight * heights[5]

    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.SuitWalkSpeed
        self.dnaStore = None
        self.pointIndexes = {}

    def delete(self):
        del self.dnaStore

    def setupDNA(self):
        if self.dnaStore:
            return

        self.dnaStore = DNAStorage()
        loadDNAFileAI(self.dnaStore, self.genDNAFileName())
        self.initDNAInfo()

    def genDNAFileName(self):
        zoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        phase = ToontownGlobals.streetPhaseMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
        return 'phase_%s/dna/%s_%s.pdna' % (phase, hood, zoneId)

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    def extractGroupName(self, groupFullName):
        return groupFullName.split(':', 1)[0]

    def initDNAInfo(self):
        numGraphs = self.dnaStore.discoverContinuity()
        if numGraphs != 1:
            self.notify.info('zone %s has %s disconnected suit paths.' % (self.zoneId, numGraphs))
        self.battlePosDict = {}
        self.cellToGagBonusDict = {}
        for i in xrange(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))
            if vg.getNumBattleCells() == 1:
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        self.cogHQDoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in xrange(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.FRONT_DOOR_POINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDE_DOOR_POINT:
                self.sidedoorPointList.append(point)
            elif (point.getPointType() == DNASuitPoint.COGHQ_IN_POINT) or (point.getPointType() == DNASuitPoint.COGHQ_OUT_POINT):
                self.cogHQDoorPointList.append(point)
            else:
                self.streetPointList.append(point)
            self.pointIndexes[point.getIndex()] = point

    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in xrange(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `(i + 1)` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')

    def genPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        return self.dnaStore.getSuitPath(startPoint, endPoint, minPathLen, maxPathLen)

    def getDnaStore(self):
        return self.dnaStore
