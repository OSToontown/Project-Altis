import DNANode

class DNASignText(DNANode.DNANode):
    COMPONENT_CODE = 7
    __slots__ = ('letters')

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.letters = ''