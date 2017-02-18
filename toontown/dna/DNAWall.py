from panda3d.core import LVector4f, LPoint3f
from toontown.dna import DNANode

# For the oddest reason the toontown.dna breaks the import? Wth
import DNAFlatBuilding

from toontown.dna import DNAError
from toontown.dna import DNAUtil

class DNAWall(DNANode.DNANode):
    __slots__ = (
        'code', 'height', 'color')

    COMPONENT_CODE = 10

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.height = 0
        self.color = LVector4f(1, 1, 1, 1)

    def __del__(self):
        DNANode.DNANode.__del__(self)
        del self.code
        del self.height
        del self.color
        
    def getCode(self):
        return self.code
        
    def setCode(self, code):
        self.code = str(code)
        
    def getHeight(self):
        return self.height
        
    def setHeight(self, height):
        self.height = int(height)
        
    def getColor(self):
        return self.color
        
    def setColor(self, color):
        self.color = LVector4f(int(color))

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.height = dgi.getInt16() / 100.0
        self.color = DNAUtil.dgiExtractColor(dgi)

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNAWall code ' + self.code + ' not found in DNAStorage')
        
        node = node.copyTo(nodePath)
        pos = LPoint3f(self.pos)
        pos.setZ(DNAFlatBuilding.DNAFlatBuilding.currentWallHeight)
        scale = LPoint3f(self.scale)
        scale.setZ(self.height)
        node.setPosHprScale(pos, self.hpr, scale)
        node.setColor(self.color)
        self.traverseChildren(node, dnaStorage)
        DNAFlatBuilding.DNAFlatBuilding.currentWallHeight += self.height