from panda3d.core import LVector4f
from toontown.dna import DNANode
from toontown.dna import DNAError
from toontown.dna import DNAUtil

class DNAStreet(DNANode.DNANode):
    __slots__ = ('code', 'streetTexture', 'sideWalkTexture', 'curbTexture', 'streetColor', 
        'sideWalkColor', 'curbColor')
    
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

    def __del__(self):
        DNANode.DNANode.__del__(self)
        del self.code
        del self.streetTexture
        del self.sideWalkTexture
        del self.curbTexture
        del self.streetColor
        del self.sideWalkColor
        del self.curbColor
        
    def getCode(self):
        return self.code
        
    def setCode(self, code):
        self.code = str(code)
        
    def getStreetTexture(self):
        return self.streetTexture
        
    def setStreetTexture(self, texture):
        self.streetTexture = str(texture)
        
    def getSidewalkTexture(self):
        return self.sideWalkTexture
        
    def setSidewalkTexture(self, texture):
        self.sideWalkTexture = str(texture)
        
    def getCurbTexture(self):
        return self.curbTexture
        
    def setCurbTexture(self, texture):
        self.curbTexture = str(texture)
        
    def getStreetColor(self):
        return self.streetColor
        
    def setStreetColor(self, color):
        self.streetColor = LVector4f(int(color))
        
    def getSidewalkColor(self):
        return self.sidewalkColor
        
    def setSidewalkColor(self, color):
        self.sidewalkColor = LVector4f(int(color))
        
    def getCurbColor(self):
        return self.curbColor
        
    def setCurbColor(self, color):
        self.curbColor = LVector4f(int(color))

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.streetTexture = DNAUtil.dgiExtractString8(dgi)
        self.sideWalkTexture = DNAUtil.dgiExtractString8(dgi)
        self.curbTexture = DNAUtil.dgiExtractString8(dgi)
        self.streetColor = DNAUtil.dgiExtractColor(dgi)
        self.sideWalkColor = DNAUtil.dgiExtractColor(dgi)
        self.curbColor = DNAUtil.dgiExtractColor(dgi)

    def traverse(self, np, store):
        result = store.findNode(self.code)
        if result.isEmpty():
            raise DNAError.DNAError('DNAStreet code ' + self.code + ' not found in DNAStorage')
        
        _np = result.copyTo(np)
        _np.setName(self.name)
        
        streetTexture = self.getTexture(self.streetTexture, store)
        sidewalkTexture = self.getTexture(self.sideWalkTexture, store)
        curbTexture = self.getTexture(self.curbTexture, store)
        
        streetNode = _np.find("**/*_street")
        sidewalkNode = _np.find("**/*_sidewalk")
        curbNode = _np.find("**/*_curb")
        
        if not streetNode.isEmpty() and streetTexture:
            streetNode.setTexture(streetTexture, 1)
            streetNode.setColorScale(self.streetColor)
            
        if not sidewalkNode.isEmpty() and sidewalkTexture:
            sidewalkNode.setTexture(sidewalkTexture, 1)
            sidewalkNode.setColorScale(self.sideWalkColor)
            
        if not curbNode.isEmpty() and curbNode:
            curbNode.setTexture(curbTexture, 1)
            curbNode.setColorScale(self.curbColor)
            
        _np.setPosHprScale(self.pos, self.hpr, self.scale)
        
    def getTexture(self, texture, store):
        if not texture:
            return
        
        tex = store.findTexture(texture)
        if not tex:
            raise DNAError.DNAError("DNAStreet texture not found %s" % (texture))
        
        return tex