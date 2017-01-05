import DNALandmarkBuilding
import DNAError
import DNAUtil

class DNAAnimBuilding(DNALandmarkBuilding.DNALandmarkBuilding):
    COMPONENT_CODE = 16
    
    def __init__(self, name):
        DNALandmarkBuilding.DNALandmarkBuilding.__init__(self, name)
        self.animName = ""
        
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