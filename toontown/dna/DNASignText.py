from toontown.dna import DNANode

class DNASignText(DNANode.DNANode):
    __slots__ = (
    	'letters')
    
    COMPONENT_CODE = 7

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.letters = ''

    def __del__(self):
        DNANode.DNANode.__del__(self)
        del self.letters