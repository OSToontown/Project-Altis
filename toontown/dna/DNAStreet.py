from panda3d.core import LVector4f
import DNANode
import DNAError
from DNAUtil import *

class DNAStreet(DNANode.DNANode):
    __slots__ = (
        'code', 'streetTexture', 'sideWalkTexture', 'curbTexture', 'streetColor', 'sideWalkColor', 'curbColor',
        'setTexCnt', 'setColCnt', 'sidewalkTexture')

    COMPONENT_CODE = 19

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.streetTexture = ''
        self.sideWalkTexture = ''
        self.curbTexture = ''
        self.streetColor = LVector4f(1, 1, 1, 1)
        self.sideWalkColor = LVector4f(1, 1, 1, 1)
        self.curbColor = LVector4f(1, 1, 1, 1)
        self.setTexCnt = 0
        self.setColCnt = 0

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setStreetTexture(self, texture):
        self.streetTexture = texture

    def getStreetTexture(self):
        return self.streetTexture

    def setSideWalkTexture(self, texture):
        self.sideWalkTexture = texture

    def getSideWalkTexture(self):
        return self.sideWalkTexture

    def setCurbTexture(self, texture):
        self.curbTexture = texture

    def getCurbTexture(self):
        return self.curbTexture

    def setStreetColor(self, color):
        self.streetColor = color

    def getStreetColor(self):
        return self.streetColor

    def setSideWalkColor(self, color):
        self.sideWalkColor = color

    def getSideWalkColor(self):
        return self.sideWalkColor

    def getCurbColor(self):
        return self.curbColor

    def setTextureColor(self, color):
        self.Color = color

    def setTexture(self, texture):
        if self.setTexCnt == 0:
            self.streetTexture = texture
        
        if self.setTexCnt == 1:
            self.sidewalkTexture = texture
        
        if self.setTexCnt == 2:
            self.curbTexture = texture
        
        self.setTexCnt += 1

    def setColor(self, color):
        if self.setColCnt == 0:
            self.streetColor = color
        
        if self.setColCnt == 1:
            self.sideWalkColor = color
        
        if self.setColCnt == 2:
            self.curbColor = color
        
        self.setColCnt += 1

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.code = dgiExtractString8(dgi)
        self.streetTexture = dgiExtractString8(dgi)
        self.sideWalkTexture = dgiExtractString8(dgi)
        self.curbTexture = dgiExtractString8(dgi)
        self.streetColor = dgiExtractColor(dgi)
        self.sideWalkColor = dgiExtractColor(dgi)
        self.curbColor = dgiExtractColor(dgi)

    def traverse(self, nodePath, dnaStorage):
        node = dnaStorage.findNode(self.code)
        if node is None:
            raise DNAError.DNAError('DNAStreet code %s' % self.code + ' not found in DNAStorage')
        
        nodePath = node.copyTo(nodePath, 0)
        node.setName(self.getName())
        streetTexture = dnaStorage.findTexture(self.streetTexture)
        sidewalkTexture = dnaStorage.findTexture(self.sideWalkTexture)
        curbTexture = dnaStorage.findTexture(self.curbTexture)
        
        if streetTexture is None:
            raise DNAError.DNAError('street texture not found in DNAStorage : ' + self.streetTexture)
        
        if sidewalkTexture is None:
            raise DNAError.DNAError('sidewalk texture not found in DNAStorage : ' + self.sideWalkTexture)
        
        if curbTexture is None:
            raise DNAError.DNAError('curb texture not found in DNAStorage : ' + self.curbTexture)
        
        streetNode = nodePath.find('**/*_street')
        sidewalkNode = nodePath.find('**/*_sidewalk')
        curbNode = nodePath.find('**/*_curb')

        if not streetNode.isEmpty():
            streetNode.setTexture(streetTexture, 1)
            streetNode.setColorScale(self.streetColor, 0)
        
        if not sidewalkNode.isEmpty():
            sidewalkNode.setTexture(sidewalkTexture, 1)
            sidewalkNode.setColorScale(self.sideWalkColor, 0)
        
        if not curbNode.isEmpty():
            curbNode.setTexture(curbTexture, 1)
            curbNode.setColorScale(self.curbColor, 0)

        nodePath.setPosHprScale(self.getPos(), self.getHpr(), self.getScale())
        nodePath.flattenStrong()
        
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNAStreet'  # Override the name for debugging.
        packer.pack('code', self.code, STRING)
        packer.pack('street texture', self.streetTexture, STRING)
        packer.pack('side walk texture', self.sideWalkTexture, STRING)
        packer.pack('curb texture', self.curbTexture, STRING)
        packer.packColor('street color', *self.streetColor)
        packer.packColor('side walk color', *self.sideWalkColor)
        packer.packColor('curb color', *self.curbColor)
        return packer