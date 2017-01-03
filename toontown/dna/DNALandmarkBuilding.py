from panda3d.core import LVector4f
<<<<<<< HEAD
from toontown.dna import DNANode
from toontown.dna import DNAUtil
from toontown.dna import DNAError
=======
from DNAUtil import *
import DNANode
import DNAUtil
import DNAError
>>>>>>> origin/master

class DNALandmarkBuilding(DNANode.DNANode):
    __slots__ = (
        'code', 'wallColor', 'title', 'article', 'buildingType', 'door')
   
    COMPONENT_CODE = 13

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.wallColor = LVector4f(1, 1, 1, 1)
        self.title = ''
        self.article = ''
        self.buildingType = ''
        self.door = None

    def setArticle(self, article):
        self.article = article

    def getArticle(self):
        return self.article

    def setBuildingType(self, buildingType):
        self.buildingType = buildingType

    def getBuildingType(self):
        return self.buildingType

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def getCode(self):
        return self.code

    def setCode(self, code):
        self.code = code

    def setWallColor(self, color):
        self.wallColor = color

    def getWallColor(self):
        return self.wallColor

    def setupSuitBuildingOrigin(self, nodePathA, nodePathB):
        if (self.getName()[:2] == 'tb') and (self.getName()[3].isdigit()) and (self.getName().find(':') != -1):
            name = self.getName()
            name = 's' + name[1:]
            node = nodePathB.find('**/*suit_building_origin')
            
            if node.isEmpty():
                node = nodePathA.attachNewNode(name)
                node.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
            else:
                node.wrtReparentTo(nodePathA, 0)
                node.setName(name)

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.wallColor = DNAUtil.dgiExtractColor(dgi)
        self.title = DNAUtil.dgiExtractString8(dgi)
        self.article = DNAUtil.dgiExtractString8(dgi)
        self.buildingType = DNAUtil.dgiExtractString8(dgi)

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNALandmarkBuilding code %s' % str(self.code) + ' not found in DNAStorage')
        
        npA = nodePath
        nodePath = node.copyTo(nodePath, 0)
        nodePath.setName(self.getName())
        nodePath.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
        self.setupSuitBuildingOrigin(npA, nodePath)
        for child in self.children:
            child.traverse(nodePath, dnaStorage)
        
        nodePath.flattenStrong()
        
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNALandmarkBuilding'  # Override the name for debugging.
        packer.pack('code', self.code, STRING)
        packer.packColor('wall color', *self.wallColor)

        if recursive:
            packer += self.packerTraverseChildren(verbose=verbose)
        return packer
