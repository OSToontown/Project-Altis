from DNAUtil import *

class DNABattleCell:
    COMPONENT_CODE = 21

    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.pos = pos

    def getWidth(self):
        return self.width
        
    def getHeight(self):
        return self.height
        
    def getPos(self):
        return self.pos