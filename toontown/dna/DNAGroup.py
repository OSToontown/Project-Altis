from panda3d.core import PandaNode
from toontown.dna import DNAUtil

class DNAGroup(object):
    __slots__ = (
        'name', 'children', 'parent', 'visGroup')
    
    COMPONENT_CODE = 1

    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
        self.visGroup = None

    def __del__(self):
        del self.name

        for child in self.children:
            del child

        del self.children
        del self.parent
        del self.visGroup

    def getName(self):
        return self.name
        
    def setName(self, name):
        self.name = str(name)

    def add(self, child):
        self.children += [child]

    def remove(self, child):
        self.children.remove(child)

    def at(self, index):
        return self.children[index]

    def setParent(self, parent):
        self.parent = parent
        self.visGroup = parent.visGroup

    def getParent(self):
        return self.parent

    def clearParent(self):
        self.parent = None
        self.visGroup = None

    def getNumChildren(self):
        return len(self.children)

    def makeFromDGI(self, dgi, store):
        self.name = DNAUtil.dgiExtractString8(dgi)

    def traverse(self, nodePath, dnaStorage):
        np = nodePath.attachNewNode(self.name)
        self.traverseChildren(np, dnaStorage)
        
    def traverseChildren(self, np, store):
        for child in self.children:
            child.traverse(np, store)