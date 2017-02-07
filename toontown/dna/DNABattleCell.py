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

    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
        
    def getPos(self):
        return self.pos