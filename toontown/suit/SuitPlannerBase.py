from pandac.PandaModules import *
from direct.directnotify.DirectNotifyGlobal import *
from toontown.hood import ZoneUtil, HoodUtil
from toontown.toonbase import ToontownGlobals, ToontownBattleGlobals
from toontown.building import SuitBuildingGlobals
from toontown.dna.DNAParser import DNASuitPoint, DNAStorage, DNAInteractiveProp, loadDNAFileAI

class SuitPlannerBase:
    notify = directNotify.newCategory('SuitPlannerBase')

    SuitHoodInfo = [[ToontownGlobals.ToontownCentralOld, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (40, 40, 0, 0, 20), (5, 6, 7, 8), [], 5],
    [ToontownGlobals.SillyStreet, 8, 20, 0, 5, 20, 3, (1, 5, 10, 40, 60, 80), (20, 20, 20, 20, 20), (2, 3, 4), [], 10],
    [ToontownGlobals.LoopyLane, 8, 20, 0, 5, 15, 3, (1, 5, 10, 40, 60, 80), (30, 40, 5, 5, 20), (2, 3, 4), [], 5],
    [ToontownGlobals.PunchlinePlace, 8, 20, 0, 5, 15, 3, (1, 5, 10, 40, 60, 80), (5, 5, 40, 40, 10), (1, 2, 3), [], 5],
    [ToontownGlobals.WackyWay, 8, 20, 0, 5, 15, 3, (1, 5, 10, 40, 60, 80), (30, 20, 5, 5, 40), (1, 2, 3), [], 5],
    [ToontownGlobals.BarnacleBoulevard, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (80, 10, 0, 0, 10), (3, 4, 5),[], 7.5],
    [ToontownGlobals.SeaweedStreet, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 10, 60, 30, 0), (3, 4, 5, 6),[], 10],
    [ToontownGlobals.LighthouseLane, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (10, 40, 10, 10, 30), (4, 5, 6, 7),[], 15],
    [ToontownGlobals.AhoyAvenue, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (40, 0, 0, 50, 10), (4, 5, 6),[], 10],
    [ToontownGlobals.WalrusWay, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (75, 5, 0, 0, 20), (5, 6, 7), [], 20],
    [ToontownGlobals.SleetStreet, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 30, 60, 10), (5, 6, 7, 8), [], 20],
    [ToontownGlobals.PolarPlace, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (5, 80, 5, 5, 5), (7, 8, 9), [], 25],
    [ToontownGlobals.ArcticAvenue, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (10, 5, 5, 10, 70), (7, 8, 9), [], 25],
    [ToontownGlobals.AltoAvenue, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 25, 50, 25),(5, 6), [], 7.5],
    [ToontownGlobals.BaritoneBoulevard, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 40, 10, 50), (5, 6, 7), [], 10],
    [ToontownGlobals.TenorTerrace, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (40, 40, 0, 0, 20), (5, 6, 7, 8), [], 15],
    [ToontownGlobals.SopranoStreet, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (5, 5, 80, 5, 5), (6, 7, 8), [], 25],
    [ToontownGlobals.ElmStreet, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (5, 5, 40, 40, 10), (4, 5, 6), [], 7.5],
    [ToontownGlobals.MapleStreet, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (30, 60, 0, 0, 10), (4, 5, 6, 7), [], 10],
    [ToontownGlobals.OakStreet, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (5, 5, 5, 80, 5), (5, 6, 7), [], 15],
    [ToontownGlobals.RoseValley, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (40, 10, 30, 10, 10), (5, 6), [], 10],
    [ToontownGlobals.AcornAvenue, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (10, 10, 10, 20, 50), (4, 5, 6), [], 10],
    [ToontownGlobals.PeanutPlace, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 30, 30, 30, 10), (3, 4, 5, 6), [], 7.5],
    [ToontownGlobals.WalnutWay, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (80, 5, 5, 5, 5), (5, 6, 7, 8, 9), [], 20],
    [ToontownGlobals.LegumeLane, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (20, 40, 40, 0, 0), (2, 3, 4, 5), [], 7.5],
    [ToontownGlobals.LullabyLane, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (20, 20, 20, 20, 20), (6, 7, 8, 9, 10), [], 30],
    [ToontownGlobals.PajamaPlace, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (5, 5, 5, 5, 80), (6, 7, 8, 9, 10), [], 25],
    [ToontownGlobals.BossbotHQ, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (100, 0, 0, 0, 0), (8, 9, 10), [], 20],            
    [ToontownGlobals.SellbotHQ, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 0, 100, 0), (4, 5, 6, 7), [], 20],
    [ToontownGlobals.SellbotFactoryExt, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 0, 100, 0), (5, 6, 7), [], 20],
    [ToontownGlobals.CashbotHQ, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 0, 100, 0, 0), (6, 7, 8), [], 20],
    [ToontownGlobals.LawbotHQ, 8, 20, 0, 99, 100, 4, (1, 5, 10, 40, 60, 80), (0, 100, 0, 0, 0), (7, 8, 9), [], 20],
    [19000, 8, 20, 0, 0, 0, 4, (1,5, 10, 40, 60, 80), (0, 0, 0, 0, 100), (9, 10, 11), [], 20]]
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
    TOTAL_BWEIGHT_PER_TRACK = [0, 0, 0, 0, 0]
    TOTAL_BWEIGHT_PER_HEIGHT = [0, 0, 0, 0, 0, 0]
    for currHoodInfo in SuitHoodInfo:
        weight = currHoodInfo[SUIT_HOOD_INFO_BWEIGHT]
        tracks = currHoodInfo[SUIT_HOOD_INFO_TRACK]
        levels = currHoodInfo[SUIT_HOOD_INFO_LVL]
        heights = [0, 0, 0, 0, 0, 0]
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
        if zoneId == 20000:
            phase = 4
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
                
            if True:
                for i in range(vg.getNumChildren()):
                    childDnaGroup = vg.at(i)
                    if isinstance(childDnaGroup, DNAInteractiveProp):
                        self.notify.debug('got interactive prop %s' % childDnaGroup)
                        battleCellId = childDnaGroup.getCellId()
                        if battleCellId == -1:
                            self.notify.warning('interactive prop %s  at %s not associated with a a battle' % (childDnaGroup, zoneId))
                        elif battleCellId == 0:
                            if self.cellToGagBonusDict.has_key(zoneId):
                                self.notify.error('FIXME battle cell at zone %s has two props %s %s linked to it' % (zoneId, self.cellToGagBonusDict[zoneId], childDnaGroup))
                            else:
                                name = childDnaGroup.getName()
                                propType = HoodUtil.calcPropType(name)
                                if propType in ToontownBattleGlobals.PropTypeToTrackBonus:
                                    trackBonus = ToontownBattleGlobals.PropTypeToTrackBonus[propType]
                                    self.cellToGagBonusDict[zoneId] = trackBonus

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
