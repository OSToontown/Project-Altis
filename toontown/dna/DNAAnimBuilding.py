from toontown.dna import DNALandmarkBuilding
from toontown.dna import DNAError
from toontown.dna import DNAUtil

class DNAAnimBuilding(DNALandmarkBuilding.DNALandmarkBuilding):
    __slots__ = (
        'animName')
    
    COMPONENT_CODE = 16
    
    def __init__(self, name):
        DNALandmarkBuilding.DNALandmarkBuilding.__init__(self, name)
        self.animName = ''

    def __del__(self):
        DNALandmarkBuilding.DNALandmarkBuilding.__del__(self)
        del self.animName
        
    def setAnimName(self, name):
        self.animName = str(name)
        
    def getAnimName(self):
        return self.animName
        
    def makeFromDGI(self, dgi, store):
        DNALandmarkBuilding.DNALandmarkBuilding.makeFromDGI(self, dgi, store)
        self.animName = dgi.getString()
        
    def traverse(self, np, store):
        result = store.findNode(self.code)
        if result.isEmpty():
            raise DNAError.DNAError('DNAAnimBuilding code ' + self.code + ' not found in dnastore')
        
        _np = result.copyTo(np)
        _np.setName(self.name)
        _np.setPosHprScale(self.pos, self.hpr, self.scale)
        _np.setTag("DNAAnim", self.animName)
        self.setupSuitBuildingOrigin(np, _np)
        self.traverseChildren(np, store)
        _np.flattenStrong()