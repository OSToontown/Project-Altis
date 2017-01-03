from panda3d.core import BamFile, NodePath, StringStream, decompressString
<<<<<<< HEAD
from toontown.dna import DNANode
=======
from DNAUtil import *
import DNANode
>>>>>>> origin/master

class DNASignBaseline(DNANode.DNANode):
    __slots__ = (
        'data', 'code', 'color', 'flags', 'indent', 'kern', 'wiggle', 
        'stumble', 'stomp', 'width', 'height')

    COMPONENT_CODE = 6

    def __init__(self):
        DNANode.DNANode.__init__(self, '')
        self.code = ''
        self.color = (1, 1, 1, 1)
        self.flags = ''
        self.indent = 0.0
        self.kern = 0.0
        self.wiggle = 0.0
        self.stumble = 0.0
        self.stomp = 0.0
        self.width = 0.0
        self.height = 0.0
        self.data = ''
        
    def setCode(self, code):
        self.code = code

    def setColor(self, color):
        self.color = color

    def setHeight(self, height):
        self.height = height

    def setIndent(self, indent):
        self.indent = indent

    def setKern(self, kern):
        self.kern = kern

    def setStomp(self, stomp):
        self.stomp = stomp

    def setStumble(self, stumble):
        self.stumble = stumble

    def setWiggle(self, wiggle):
        self.wiggle = wiggle

    def setWidth(self, width):
        self.width = width

    def setFlags(self, flags):
        self.flags = flags

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.data = dgi.getString()
        
        if len(self.data):
            self.data = decompressString(self.data)

    def traverse(self, nodePath, dnaStorage):
        node = nodePath.attachNewNode('baseline', 0)
        node.setPosHpr(self.pos, self.hpr)
        node.setPos(node, 0, -0.1, 0)
        if self.data:
            bf = BamFile()
            ss = StringStream()
            ss.setData(self.data)
            bf.openRead(ss)

            if not bf.getReader().getSource():
                # failed to load sign text.
                return
            
            signText = NodePath(bf.readNode())
            signText.reparentTo(node)
        
        node.flattenStrong()
        for child in self.children:
            child.traverse(nodePath, dnaStorage)
            
    def packerTraverse(self, recursive=True, verbose=False):
        packer = DNANode.DNANode.packerTraverse(self, recursive=False, verbose=verbose)
        packer.name = 'DNASignBaseline'  # Override the name for debugging.

        traversed_data = ''
        text = ''

        for child in self.children:
            if child.__class__.__name__ == 'DNASignText':
                text += child.letters
            else:
                if recursive:
                    traversed_data += child.packerTraverse(recursive=recursive, verbose=verbose)

        packer.pack('sign node text', text, STRING)
        packer.pack('sign node code', self.code, STRING)
        packer.packColor('sign node color', *self.color)
        packer.pack('sign node flags', self.flags, STRING)
        packer.pack('sign node indent', self.indent, FLOAT32)
        packer.pack('sign node kern', self.kern, FLOAT32)
        packer.pack('sign node wiggle', self.wiggle, FLOAT32)
        packer.pack('sign node stumble', self.stumble, FLOAT32)
        packer.pack('sign node stomp', self.stomp, FLOAT32)
        packer.pack('sign node width', self.width, FLOAT32)
        packer.pack('sign node height', self.height, FLOAT32)

        if recursive:
            packer += traversed_data + chr(255)

        return packer