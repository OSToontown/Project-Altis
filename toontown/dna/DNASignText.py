import DNANode

class DNASignText(DNANode.DNANode):
    __slots__ = (
        'name', 'children', 'parent', 'visGroup', 'pos', 'hpr', 'scale', 'letters')

    COMPONENT_CODE = 7

    def __init__(self):
        DNANode.DNANode.__init__(self, '')
        self.letters = ''