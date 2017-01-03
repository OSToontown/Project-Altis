from toontown.dna.DNAUtil import *

class DNABattleCell(object):
    __slots__ = (
        'width', 'height', 'pos')

    COMPONENT_CODE = 21

    def __init__(self, width, height, pos):
        self.width = width
        self.height = height
        self.pos = pos

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setPos(self, pos):
        self.pos = pos

    def getPos(self):
        return self.pos

    def setWidthHeight(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'DNABattleCell width: %s' % str(self.width) + ' height: %s' % str(self.height) + ' pos: %s' % str(self.pos)