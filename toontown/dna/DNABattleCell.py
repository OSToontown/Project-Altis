from panda3d.core import LVector3f
from toontown.dna.DNAUtil import *

class DNABattleCell(object):
    __slots__ = (
        'width', 'height', 'pos')
    
    COMPONENT_CODE = 21

    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.pos = pos

    def __del__(self):
        del self.width
        del self.height
        del self.pos
        
    def setWidth(self, width):
        self.width = int(width)

    def getWidth(self):
        return self.width
        
    def setHeight(self, height):
        self.height = int(height)
        
    def getHeight(self):
        return self.height
        
    def setPos(self, pos):
        self.pos = LVector3f(int(pos))
        
    def getPos(self):
        return self.pos