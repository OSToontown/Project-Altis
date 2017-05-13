from panda3d.core import *
from toontown.dna import DNASuitEdge
from toontown.dna import DNASuitPath
from toontown.dna import DNASuitPoint
from toontown.dna import DNAError

class DNAStorage(object):
    __slots__ = ('visGroups', 'DNAGroups', 'textures', 'fonts', 'fontFilenames', 'catalogCodes', 'nodes', 'hoodNodes', 'placeNodes', 
        'blockDoors', 'blockZones', 'blockNumbers', 'blockTitles', 'blockArticles', 'blockBuildingTypes', 'suitEdges', 'suitPoints', 'suitBlocks', 'cogdoBlocks',)

    def __init__(self):
        self.visGroups = []
        self.DNAGroups = {}
        self.textures = {}
        self.fonts = {}
        self.fontFilenames = {}
        self.catalogCodes = {}
        self.nodes = {}
        self.hoodNodes = {}
        self.placeNodes = {}
        self.blockDoors = {}
        self.blockZones = {}
        self.blockNumbers = {}
        self.blockTitles = {}
        self.blockArticles = {}
        self.blockBuildingTypes = {}
        self.suitEdges = {}
        self.suitPoints = []
        self.suitBlocks = {}
        self.cogdoBlocks = {}
        
    def cleanup(self):
        self.resetBattleCells()
        self.resetBlockNumbers()
        self.resetDNAGroups()
        self.resetDNAVisGroups()
        self.resetDNAVisGroupsAI()
        self.resetFonts()
        self.resetHood()
        self.resetHoodNodes()
        self.resetNodes()
        self.resetPlaceNodes()
        self.resetSuitPoints()
        self.resetSuitEdges()
        self.resetTextures()
        self.resetCatalogCodes()
        self.resetSuitBlocks()
        self.resetCogdoBlocks()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        
    def resetBattleCells(self):
        pass

    def storeDNAVisGroup(self, group):
        self.visGroups.append(group)

    def getNumDNAVisGroups(self):
        return len(self.visGroups)

    def getNumDNAVisGroupsAI(self):
        return self.getNumDNAVisGroups()

    def getNumVisiblesInDNAVisGroup(self, index):
        return self.getDNAVisGroupAI(index).getNumVisibles()

    def getVisibleName(self, index, visibleIndex):
        return self.getDNAVisGroupAI(index).getVisible(visibleIndex)

    def getDNAVisGroupAI(self, index):
        return self.visGroups[index]

    def getDNAVisGroupName(self, index):
        return self.getDNAVisGroupAI(index).getName()

    def resetDNAVisGroups(self):
        for group in self.visGroups:
            del group

        self.visGroups = []

    def resetDNAVisGroupsAI(self):
        self.resetDNAVisGroups()

    def storeTexture(self, name, texture):
        self.textures[name] = texture

    def findTexture(self, name):
        if name in self.textures:
            return self.textures[name]

    def resetTextures(self):
        self.textures = {}

    def storeFont(self, code, font, filename = ''):
        self.fonts[code] = font
        self.fontFilenames[code] = filename

    def findFont(self, code):
        if code in self.fonts:
            return self.fonts[code]

    def resetFonts(self):
        self.fonts = {}
        self.fontFilenames = {}

    def storeCatalogCode(self, category, code):
        if not category in self.catalogCodes:
            self.catalogCodes[category] = []
        
        self.catalogCodes[category].append(code)

    def getNumCatalogCodes(self, category):
        if category not in self.catalogCodes:
            return 0
        
        return len(self.catalogCodes[category])

    def getCatalogCode(self, category, index):
        return self.catalogCodes[category][index]
        
    def resetCatalogCodes(self):
        self.catalogCodes = {}

    def findNode(self, code):
        if code in self.nodes:
            nodes = self.nodes
        elif code in self.hoodNodes:
            nodes = self.hoodNodes
        elif code in self.placeNodes:
            nodes = self.placeNodes
        else:
            return NodePath()
        
        filename = nodes[code][0]
        search = nodes[code][1]
        try:
           model = loader.pdnaModel(Filename(filename))
        except:
           print "DNAStorage: Failed to load %s!" % (filename)
           return
        
        if search:
            newModel = model.find("**/" + search).copyTo(NodePath())
            model.removeNode()
            model = newModel
        
        model.setTag("DNACode", code)
        return model

    def storeNode(self, filename, search, code):
        self.nodes[code] = [filename, search]

    def storeHoodNode(self, filename, search, code):
        self.hoodNodes[code] = [filename, search]

    def storePlaceNode(self, filename, search, code):
        self.placeNodes[code] = [filename, search]

    def resetNodes(self):
        self.nodes = {}

    def resetHoodNodes(self):
        self.hoodNodes = {}

    def resetPlaceNodes(self):
        self.placeNodes = {}

    def resetHood(self):
        self.resetBlockNumbers()

    def storeBlockDoor(self, blockNumber, door):
        self.blockDoors[str(blockNumber)] = door

    def storeBlockZone(self, blockNumber, zoneId):
        self.blockZones[blockNumber] = zoneId

    def storeBlockNumber(self, blockNumber):
        if not self.blockNumbers:
            self.blockNumbers = []
         
        self.blockNumbers.append(blockNumber)

    def storeBlockTitle(self, blockNumber, title):
        self.blockTitles[blockNumber] = title

    def storeBlockArticle(self, blockNumber, article):
        self.blockArticles[blockNumber] = article

    def storeBlockBuildingType(self, blockNumber, bldgType):
        self.blockBuildingTypes[blockNumber] = bldgType

    def storeBlock(self, blockNumber, title, article, bldgType, zoneId):
        self.storeBlockNumber(blockNumber)
        self.storeBlockTitle(blockNumber, title)
        self.storeBlockArticle(blockNumber, article)
        self.storeBlockBuildingType(blockNumber, bldgType)
        self.storeBlockZone(blockNumber, zoneId)

    def getNumBlockNumbers(self):
        return len(self.blockNumbers)

    def getBlock(self, name):
        block = name[name.find(':')-2:name.find(':')]
        if not block[0].isdigit():
            block = block[1:]
        
        return block

    def getBlockBuildingType(self, blockNumber):
        if blockNumber in self.blockBuildingTypes:
            return self.blockBuildingTypes[blockNumber]

    def getTitleFromBlockNumber(self, blockNumber):
        if blockNumber in self.blockTitles:
            return self.blockTitles[blockNumber]
        
        return ''
        
    def getDoorPosHprFromBlockNumber(self, blockNumber):
        key = str(blockNumber)
        if key in self.blockDoors:
            return self.blockDoors[key]

    def getDoorPosHprFromBlockHpr(self, blockNumber):
        if str(blockNumber) in self.blockDoors:
            return self.blockDoors[str(blockNumber)]

    def getBlockNumberAt(self, index):
        return self.blockNumbers[index]

    def getZoneFromBlockNumber(self, blockNumber):
        if blockNumber in self.blockZones:
            return self.blockZones[blockNumber]

    def resetBlockNumbers(self):
        self.blockNumbers = []
        self.blockZones = {}
        self.blockArticles = {}

        for door in self.blockDoors:
            del door

        self.blockDoors = {}

        for titles in self.blockTitles:
            del titles

        self.blockTitles = {}
        self.blockBuildingTypes = {}

    def resetBlockZones(self):
        self.blockZones = {}

    def allowSuitOrigin(self, np):
        # NOTICE: Game-specific hack
        if 'gag_shop' in np.getName():
            return False
        
        if 'pet_shop' in np.getName():
            return False
        
        return True

    def storeSuitBlock(self, blockNumber, dept):
        self.suitBlocks[blockNumber] = dept

    def resetSuitBlocks(self):
        self.suitBlocks.clear()

    def isSuitBlock(self, blockNumber):
        return blockNumber in self.suitBlocks

    def getSuitBlockTrack(self, blockNumber):
        return self.suitBlocks.get(blockNumber)
        
    def storeCogdoBlock(self, blockNumber, dept):
        self.cogdoBlocks[blockNumber] = dept

    def resetCogdoBlocks(self):
        self.cogdoBlocks.clear()

    def isCogdoBlock(self, blockNumber):
        return blockNumber in self.cogdoBlocks

    def getCogdoBlockTrack(self, blockNumber):
        return self.cogdoBlocks.get(blockNumber)
        
    def storeSuitEdge(self, startIndex, endIndex, zoneId):
        startPoint = self.getSuitPointWithIndex(startIndex)
        endPoint = self.getSuitPointWithIndex(endIndex)

        if not startPoint or not endPoint:
            print "DNAStorage: Attempted to add edge with unknown startPoint(%s) and/or endPoint(%s)" % (startIndex, endIndex)

        if not startIndex in self.suitEdges:
            self.suitEdges[startIndex] = []
        
        self.suitEdges[startIndex].append(DNASuitEdge.DNASuitEdge(startPoint, endPoint, zoneId))

    def getSuitEdge(self, startIndex, endIndex):
        edges = self.suitEdges[startIndex]
        for edge in edges:
            if edge.getEndPoint().getIndex() == endIndex:
                return edge

    def storeSuitPoint(self, suitPoint):
        self.suitPoints.append(suitPoint)

    def getSuitPointAtIndex(self, index):
        return self.suitPoints[index]

    def getSuitPointWithIndex(self, index):
        for point in self.suitPoints:
            if point.getIndex() == index:
                return point

    def getNumSuitPoints(self):
        return len(self.suitPoints)

    def resetSuitPoints(self):
        for suitPoint in self.suitPoints:
            del suitPoint

        self.suitPoints = []

    def resetSuitEdges(self):
        for suitEdge in self.suitEdges.items():
            del suitEdge

    def findDNAGroup(self, node):
        return self.DNAGroups[node]

    def removeDNAGroup(self, dnagroup):
        for node, group in self.DNAGroups.items():
            if group == dnagroup:
                del self.DNAGroups[node]

    def resetDNAGroups(self):
        for group in self.DNAGroups.items():
            del group

        self.DNAGroups = {}

    def getSuitPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        path = DNASuitPath.DNASuitPath()
        path.addPoint(startPoint)
        while path.getNumPoints() < maxPathLen:
            if startPoint == endPoint and path.getNumPoints() >= minPathLen:
                break

            adjacentPoints = self.getAdjacentPoints(startPoint)
            if adjacentPoints.getNumPoints() == 0:
                raise DNAError.DNAError("could not find DNASuitPath: point %s has no edges") %startPoint.getIndex()

            # First, let's see if our end point is an adjacent point
            # If it's not, or path is still too short, advance to first
            # non-door adjacent point
            nonDoorPoint = None
            for i in range(adjacentPoints.getNumPoints()):
                _startPoint = adjacentPoints.getPoint(i)
                if _startPoint == endPoint and path.getNumPoints() >= (minPathLen + 1):
                    del adjacentPoints
                    path.addPoint(_startPoint)
                    return path

                startPointType = _startPoint.getPointType()
                if (startPointType != DNASuitPoint.DNASuitPoint.FRONT_DOOR_POINT) and (startPointType != DNASuitPoint.DNASuitPoint.SIDE_DOOR_POINT) and (nonDoorPoint == None):
                    nonDoorPoint = _startPoint

            del adjacentPoints

            if nonDoorPoint == None:
                raise DNAError.DNAError("could not find DNASuitPath: point %s has no non-door point edge" %startPoint.getIndex())

            startPoint = nonDoorPoint
            path.addPoint(startPoint)

        return path

    def getSuitEdgeTravelTime(self, startIndex, endIndex, suitWalkSpeed):
        startPoint = self.getSuitPointWithIndex(startIndex)
        endPoint = self.getSuitPointWithIndex(endIndex)
        if not startPoint or not endPoint:
            return 0

        return (endPoint.getPos() - startPoint.getPos()).length() / suitWalkSpeed

    def getSuitEdgeZone(self, startIndex, endIndex):
        edge = self.getSuitEdge(startIndex, endIndex)
        assert edge != None
        return edge.getZoneId()

    def getAdjacentPoints(self, point):
        path = DNASuitPath.DNASuitPath()
        startIndex = point.getIndex()
        if not startIndex in self.suitEdges:
            return path

        for edge in self.suitEdges[startIndex]:
            path.addPoint(edge.getEndPoint())

        return path

    def discoverContinuity(self):
        return True
