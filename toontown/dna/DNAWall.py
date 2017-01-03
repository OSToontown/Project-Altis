from panda3d.core import LVector4f
import DNANode
import DNAFlatBuilding
import DNAError
from DNAUtil import *

class DNAWall(DNANode.DNANode):
    __slots__ = (
        'code', 'height', 'color')

    COMPONENT_CODE = 10

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.height = 10
        self.color = LVector4f(1, 1, 1, 1)

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.code = dgiExtractString8(dgi)
        self.height = dgi.getInt16() / 100.0
        self.color = dgiExtractColor(dgi)

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNAWall code %s' % self.code + ' not found in DNAStorage')
        
        node = node.copyTo(nodePath, 0)
        self.pos.setZ(DNAFlatBuilding.DNAFlatBuilding.currentWallHeight)
        self.scale.setZ(self.height)
        node.setPosHprScale(self.pos, self.hpr, self.scale)
        node.setColor(self.color)
        for child in self.children:
            child.traverse(node, dnaStorage)
        
        node.flattenStrong()
        DNAFlatBuilding.DNAFlatBuilding.currentWallHeight += self.height
        
        
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNAWall'  # Override the name for debugging.
        packer.pack('code', self.code, STRING)
        packer.pack('height', int(self.height * 100), INT16)
        packer.packColor('color', *self.color)
        if recursive:
            packer += self.packerTraverseChildren(verbose=verbose)
        return packer