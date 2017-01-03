import math
from pandac.PandaModules import *
from toontown.dna.DNAError import DNAError
from toontown.dna.DNAPacker import DNAPacker
from toontown.dna.DNASuitPoint import DNASuitPoint
from toontown.dna.DNASuitPath import DNASuitPath
from toontown.dna.DNASuitEdge import DNASuitEdge

class DNAStorage:
    __slots__ = (
        'suitPoints', 'suitPointMap', 'DNAGroups', 'DNAVisGroups', 'suitEdges', 'battleCells', 'nodes', 'hoodNodes',
        'placeNodes', 'fonts', 'blockTitles', 'blockArticles', 'blockBuildingTypes', 'blockDoors', 'blockNumbers',
        'blockZones', 'textures', 'catalogCodes', 'packerNodes', 'packerHoodNodes', 'packerPlaceNodes', 
        'packerCatalogCodes', 'packerBlockNumbers')

    def __init__(self):
        self.suitPoints = []
        self.suitPointMap = {}
        self.DNAGroups = {}
        self.DNAVisGroups = []
        self.suitEdges = {}
        self.battleCells = []
        self.nodes = {}
        self.hoodNodes = {}
        self.placeNodes = {}
        self.packerNodes = {}
        self.packerHoodNodes = {}
        self.packerPlaceNodes = {}
        self.fonts = {}
        self.blockTitles = {}
        self.blockArticles = {}
        self.blockBuildingTypes = {}
        self.blockDoors = {}
        self.blockNumbers = []
        self.packerBlockNumbers = []
        self.blockZones = {}
        self.textures = {}
        self.catalogCodes = {}
        self.packerCatalogCodes = {}

    def getSuitPath(self, startPoint, endPoint, minPathLen=40, maxPathLen=300):
        path = DNASuitPath()
        path.addPoint(startPoint)
        while path.getNumPoints() < maxPathLen:
            startPointIndex = startPoint.getIndex()
            if startPointIndex == endPoint.getIndex():
                if path.getNumPoints() >= minPathLen:
                    break
            if startPointIndex not in self.suitEdges:
                raise DNAError('Could not find DNASuitPath.')
            edges = self.suitEdges[startPointIndex]
            for edge in edges:
                startPoint = edge.getEndPoint()
                startPointType = startPoint.getPointType()
                if startPointType != DNASuitPoint.FRONT_DOOR_POINT:
                    if startPointType != DNASuitPoint.SIDE_DOOR_POINT:
                        break
            else:
                raise DNAError('Could not find DNASuitPath.')
            path.addPoint(startPoint)
        return path

    def getSuitEdgeTravelTime(self, startIndex, endIndex, suitWalkSpeed):
        startPoint = self.suitPointMap.get(startIndex)
        endPoint = self.suitPointMap.get(endIndex)
        if (not startPoint) or (not endPoint):
            return 0.0
        
        distance = (endPoint.getPos()-startPoint.getPos()).length()
        return distance / suitWalkSpeed

    def getSuitEdgeZone(self, startIndex, endIndex):
        return self.getSuitEdge(startIndex, endIndex).getZoneId()

    def getAdjacentPoints(self, point):
        path = DNASuitPath()
        startIndex = point.getIndex()
        if startIndex not in self.suitEdges:
            return path
        for edge in self.suitEdges[startIndex]:
            path.addPoint(edge.getEndPoint())
        return path

    def storeSuitPoint(self, suitPoint):
        if not isinstance(suitPoint, DNASuitPoint):
            raise TypeError('suitPoint must be an instance of DNASuitPoint')
        self.suitPoints.append(suitPoint)
        self.suitPointMap[suitPoint.getIndex()] = suitPoint

    def getSuitPointAtIndex(self, index):
        return self.suitPoints[index]

    def getSuitPointWithIndex(self, index):
        return self.suitPointMap.get(index)

    def resetSuitPoints(self):
        self.suitPoints = []
        self.suitPointMap = {}
        self.suitEdges = {}

    def resetTextures(self):
        self.textures = {}

    def resetHood(self):
        self.resetBlockNumbers()

    def findDNAGroup(self, node):
        return self.DNAGroups[node]

    def removeDNAGroup(self, dnagroup):
        for node, group in self.DNAGroups.items():
            if group == dnagroup:
                del self.DNAGroups[node]

    def resetDNAGroups(self):
        self.DNAGroups = {}

    def getNumDNAVisGroups(self):
        return len(self.DNAVisGroups)

    def getDNAVisGroupName(self, i):
        return self.DNAVisGroups[i].getName()

    def storeDNAVisGroup(self, group):
        self.DNAVisGroups.append(group)

    def storeSuitEdge(self, startIndex, endIndex, zoneId):
        startPoint = self.getSuitPointWithIndex(startIndex)
        endPoint = self.getSuitPointWithIndex(endIndex)
        edge = DNASuitEdge(startPoint, endPoint, zoneId)
        self.suitEdges.setdefault(startIndex, []).append(edge)
        return edge

    def getSuitEdge(self, startIndex, endIndex):
        edges = self.suitEdges[startIndex]
        for edge in edges:
            if edge.getEndPoint().getIndex() == endIndex:
                return edge

    def removeBattleCell(self, cell):
        self.battleCells.remove(cell)

    def storeBattleCell(self, cell):
        self.battleCells.append(cell)

    def resetBattleCells(self):
        self.battleCells = []

    def findNode(self, code):
        if code in self.nodes:
            return self.nodes[code]
        if code in self.hoodNodes:
            return self.hoodNodes[code]
        if code in self.placeNodes:
            return self.placeNodes[code]

    def resetNodes(self):
        for node in self.nodes:
            self.nodes[node].removeNode()
        self.nodes = {}

    def resetHoodNodes(self):
        for node in self.hoodNodes:
            self.hoodNodes[node].removeNode()
        self.hoodNodes = {}

    def resetPlaceNodes(self):
        for node in self.placeNodes:
            self.placeNodes[node].removeNode()
        self.placeNodes = {}

    def storeNode(self, node, code):
        self.nodes[code] = node
        
    def storePackerNode(self, code, filename, search):
        self.packerNodes[code] = (filename, search)

    def storeHoodNode(self, node, code):
        self.hoodNodes[code] = node

    def storePackerHoodNode(self, code, filename, search):
        self.packerHoodNodes[code] = (filename, search)
        
    def storePlaceNode(self, node, code):
        self.placeNodes[code] = node
        
    def storePackerPlaceNode(self, code, filename, search):
        self.packerPlaceNodes[code] = (filename, search)

    def findFont(self, code):
        if code in self.fonts:
            return self.fonts[code]

    def resetFonts(self):
        self.fonts = {}

    def storeFont(self, font, code):
        self.fonts[code] = font

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

    def storeBlockDoor(self, blockNumber, door):
        self.blockDoors[str(blockNumber)] = door

    def storeBlockTitle(self, blockNumber, title):
        self.blockTitles[blockNumber] = title

    def storeBlockArticle(self, blockNumber, article):
        self.blockArticles[blockNumber] = article

    def storeBlockBuildingType(self, blockNumber, buildingType):
        self.blockBuildingTypes[blockNumber] = buildingType

    def storeBlock(self, blockNumber, title, article, bldgType, zoneId):
        self.storeBlockNumber(blockNumber)
        self.storeBlockTitle(blockNumber, title)
        self.storeBlockArticle(blockNumber, article)
        self.storeBlockBuildingType(blockNumber, bldgType)
        self.storeBlockZone(blockNumber, zoneId)

    def storeTexture(self, name, texture):
        self.textures[name] = texture

    def resetDNAVisGroups(self):
        self.DNAVisGroups = []

    def resetDNAVisGroupsAI(self):
        self.resetDNAVisGroups()

    def getNumDNAVisGroupsAI(self):
        return self.getNumDNAVisGroups()

    def getNumSuitPoints(self):
        return len(self.suitPoints)

    def getNumVisiblesInDNAVisGroup(self, i):
        return self.DNAVisGroups[i].getNumVisibles()

    def getVisibleName(self, i, j):
        return self.DNAVisGroups[i].getVisibleName(j)

    def getDNAVisGroupAI(self, i):
        return self.DNAVisGroups[i]

    def storeCatalogCode(self, category, code):
        if not category in self.catalogCodes:
            self.catalogCodes[category] = []
        self.catalogCodes[category].append(code)
        
    def storePackerCatalogCode(self, root, code):
        self.packerCatalogCodes.setdefault(root, []).append(code)

    def getNumCatalogCodes(self, category):
        if category not in self.catalogCodes:
            return -1
        
        return len(self.catalogCodes[category])

    def resetCatalogCodes(self):
        self.catalogCodes = {}

    def getCatalogCode(self, category, index):
        return self.catalogCodes[category][index]

    def findTexture(self, name):
        if name in self.textures:
            return self.textures[name]

    def discoverContinuity(self):
        return 1  # TODO

    def resetBlockNumbers(self):
        self.blockNumbers = []
        self.blockZones = {}
        self.blockArticles = {}
        self.resetBlockDoors()
        self.blockTitles = {}
        self.blockBuildingTypes = {}

    def getNumBlockNumbers(self):
        return len(self.blockNumbers)

    def storeBlockNumber(self, blockNumber):
        self.blockNumbers.append(blockNumber)
        
    def storePackerBlockNumber(self, blockNumber):
        self.packerBlockNumbers.append(blockNumber)

    def getBlockNumberAt(self, index):
        return self.blockNumbers[index]

    def getZoneFromBlockNumber(self, blockNumber):
        if blockNumber in self.blockZones:
            return self.blockZones[blockNumber]

    def storeBlockZone(self, blockNumber, zoneId):
        self.blockZones[blockNumber] = zoneId

    def resetBlockZones(self):
        self.blockZones = {}

    def resetBlockDoors(self):
        self.blockDoors = {}

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
        self.resetTextures()
        self.resetCatalogCodes()
        ModelPool.garbageCollect()
        TexturePool.garbageCollect()
        
    def PACK_NODES(self, dgi, nodes):
        '''
        C++ Version Below
        
        #define PACK_NODES(X) dg.add_uint16(X.size()); for (nodes_t::iterator it = X.begin(); it != X.end(); ++it) {dg.add_string(it->first);\
                                    dg.add_string((it->second)[0]); dg.add_string((it->second)[1]);}
        '''
        
        X = nodes
        dgi.addUint16(X.size())
        it = X.begin()
        while it != X.end():
            it += 1
            dgi.addString(it[0])
            dgi.addString(it[1][0])
            dgi.addString(it[1][1])
        
    def writePDNA(self, dgi):
        '''Write a .PDNA file from the current loaded scene'''
    
        # Catalog Codes #
        dgi.addUint16(self.catalogCodes.size())
        it = self.catalogCodes.begin()
        while it != self.catalogCodes.end():
            it += 1
            dgi.addString(it[0])
            codes = it[1]
            dg.addUint8(codes.size())
            code = codes.begin()
            while code != codes.end():
                code += 1
                dg.addString(str(code))
                
        # Textures # 
        dgi.addUint16(self.textures.size())
        it = self.textures.begin()
        while it != self.textures.end():
            it += 1
            dgi.addString(it[0])
            dgi.addString(it[1].getFilename())
            
        # Nodes #
        PACK_NODES(dgi, self.nodes)
        PACK_NODES(dgi, self.hoodNodes)
        PACK_NODES(dgi, self.placeNodes)
        
        # Blocks #
        dgi.addUint16(self.blockNumbers.size())
        it = self.blockNumbers.begin()
        while it != self.blockNumbers.end():
            it += 1
            blockNumber = it
            dgi.addUint8(blockNumber)
            dgi.addUint16(self.blockZones[blockNumber])
            dgi.addString(self.blockTitles[blockNumber])
            dgi.addString(self.blockArticles[blockNumber])
            dgi.addString(self.blockBuildingTypes[blockNumber])
            
        # Suit Points #
        dgi.addUint16(self.suitPoints.size())
        it = self.suitPoints.begin()
        while it != self.suitPoints.end():
            it += 1
            dgi.addUint16(it.getIndex())
            dgi.addUint8(it.getPointType())
            dgi.addInt32(math.floor(it.getX() * 100))
            dgi.addInt32(math.floor(it.getY() * 100))
            dgi.addInt32(math.floor(it.getZ() * 100))
            dgi.addInt16(it.getLandmarkBuildingIndex())
        
        # Suit Edges #
        dgi.addUnit16(self.suitEdges.size())
        it = self.suitEdges.begin()
        while it != self.suitEdges.end():
            it += 1
            startPointIndex = it[0]
            edges = it[1]
            
            dgi.addUint16(startPointIndex)
            dgi.addUint16(edges.size())
            
            eit = edges.begin()
            while eit != edges.end():
                edge = eit
                dgi.addUnit16(edge.getEndPoint().getIndex())
                dgi.addUint16(edge.getZoneId())
                
    def dump(self, verbose=False):
        packer = DNAPacker(name='DNAStorage', verbose=verbose)

        # Catalog codes...
        packer.pack('catalog code root count', len(self.packerCatalogCodes), UINT16)
        for root, codes in self.packerCatalogCodes.items():
            packer.pack('root', root, STRING)
            packer.pack('root code count', len(codes), UINT8)
            for code in codes:
                packer.pack('code', code, STRING)

        # Textures...
        packer.pack('texture count', len(self.textures), UINT16)
        for code, filename in self.textures.items():
            packer.pack('code', code, STRING)
            packer.pack('filename', filename, STRING)

        # Fonts are packed again now we have C++ signs
        packer.pack('font count', len(self.fonts), UINT16)
        for code, filename in self.fonts.items():
            packer.pack('code', code, STRING)
            packer.pack('filename', filename, STRING)

        # Nodes...
        packer.pack('node count', len(self.nodes), UINT16)
        for code, (filename, search) in self.packerNodes.items():
            packer.pack('code', code, STRING)
            packer.pack('filename', filename, STRING)
            packer.pack('search', search, STRING)

        # Hood nodes...
        packer.pack('hood node count', len(self.hoodNodes), UINT16)
        for code, (filename, search) in self.packerHoodNodes.items():
            packer.pack('code', code, STRING)
            packer.pack('filename', filename, STRING)
            packer.pack('search', search, STRING)

        # Place nodes...
        packer.pack('place node count', len(self.placeNodes), UINT16)
        for code, (filename, search) in self.packerPlaceNodes.items():
            packer.pack('code', code, STRING)
            packer.pack('filename', filename, STRING)
            packer.pack('search', search, STRING)

        # Blocks...
        packer.pack('block number count', len(self.packerBlockNumbers), UINT16)
        for blockNumber in self.packerBlockNumbers:
            packer.pack('number', blockNumber, UINT8)
            packer.pack('zone ID', self.blockZones[blockNumber], UINT16)
            title = self.blockTitles.get(blockNumber, '')
            packer.pack('title', title, STRING)
            article = self.blockArticles.get(blockNumber, '')
            packer.pack('article', article, STRING)
            buildingType = self.blockBuildingTypes.get(blockNumber, '')
            packer.pack('building type', buildingType, STRING)

        # Suit points...
        packer.pack('suit point count', len(self.suitPoints), UINT16)
        for point in self.suitPoints:
            packer.pack('index', point.index, UINT16)
            packer.pack('type', point.pointType, UINT8)
            for component in point.pos:
                packer.pack('position', int(component * 100), INT32)
            packer.pack('landmark building index',
                        point.landmarkBuildingIndex, INT16)

        # Suit edges...
        packer.pack('suit edge count', len(self.suitEdges), UINT16)
        for startPointIndex, edges in self.suitEdges.items():
            packer.pack('start point index', startPointIndex, UINT16)
            packer.pack('edge count', len(edges), UINT16)
            for edge in edges:
                packer.pack('end point', edge.endPoint.index, UINT16)
                packer.pack('zone ID', edge.zoneId, UINT16)

        return packer