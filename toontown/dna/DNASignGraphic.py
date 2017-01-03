from panda3d.core import LVector4f, DecalEffect
<<<<<<< HEAD
from toontown.dna import DNANode
from toontown.dna import DNAError
from toontown.dna import DNAUtil
=======
from DNAUtil import *
import DNANode
import DNAError
import DNAUtil
>>>>>>> origin/master

class DNASignGraphic(DNANode.DNANode):
    __slots__ = (
        'code', 'color', 'width', 'height', 'bDefaultColor')

    COMPONENT_CODE = 8

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1, 1, 1, 1)
        self.width = 0
        self.height = 0
        self.bDefaultColor = True

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setColor(self, color):
        self.color = color
        self.bDefaultColor = False

    def getColor(self):
        return self.Color

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)
        self.width = dgi.getInt16() / 100.0
        self.height = dgi.getInt16() / 100.0
        self.bDefaultColor = dgi.getBool()

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNASignGraphic code ' + self.code + ' not found in storage')
        
        node = node.copyTo(nodePath, 0)
        node.setScale(self.scale)
        node.setScale(node, self.getParent().scale)
        node.setPosHpr(self.getParent().pos, self.getParent().hpr)
        node.setPos(node, 0, -0.1, 0)
        node.setColor(self.color)
        node.flattenStrong()
        for child in self.children:
            child.traverse(node, dnaStorage)
            
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNASignGraphic'  # Override the name for debugging.
        packer.pack('code', self.code, STRING)
        packer.packColor('color', *self.color)
        packer.pack('width', int(self.width * 100), INT16)
        packer.pack('height', int(self.height * 100), INT16)
        packer.pack('bDefaultColor', self.bDefaultColor, BOOLEAN)
        if recursive:
            packer += self.packerTraverseChildren(verbose=verbose)
        return packer
