from panda3d.core import LVector3f, PandaNode
from toontown.dna import DNAGroup

class DNANode(DNAGroup.DNAGroup):
    __slots__ = (
        'pos', 'hpr', 'scale')
    
    COMPONENT_CODE = 3

    def __init__(self, name):
        DNAGroup.DNAGroup.__init__(self, name)
        self.pos = LVector3f()
        self.hpr = LVector3f()
        self.scale = LVector3f(1, 1, 1)

    def __del__(self):
        DNAGroup.DNAGroup.__del__(self)
        del self.pos
        del self.hpr
        del self.scale
        
    def setPos(self, pos):
        self.pos = LVector3f(int(pos))

    def getPos(self):
        return self.pos
        
    def setHpr(self, hpr):
        self.hpr = LVector3f(int(hpr))
        
    def getHpr(self):
        return self.hpr
        
    def setScale(self, scale):
        self.scale = LVector3f(int(scale))
        
    def getScale(self):
        return self.scale

    def makeFromDGI(self, dgi, store):
        DNAGroup.DNAGroup.makeFromDGI(self, dgi, store)

        x = dgi.getInt32() / 100.0
        y = dgi.getInt32() / 100.0
        z = dgi.getInt32() / 100.0
        self.pos = LVector3f(x, y, z)

        h = dgi.getInt32() / 100.0
        p = dgi.getInt32() / 100.0
        r = dgi.getInt32() / 100.0
        self.hpr = LVector3f(h, p, r)

        sx = dgi.getInt16() / 100.0
        sy = dgi.getInt16() / 100.0
        sz = dgi.getInt16() / 100.0
        self.scale = LVector3f(sx, sy, sz)

    def traverse(self, np, store):
        _np = np.attachNewNode(self.name)
        _np.setPosHprScale(self.pos, self.hpr, self.scale)
        self.traverseChildren(_np, store)