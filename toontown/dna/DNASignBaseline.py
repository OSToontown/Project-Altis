import math
from panda3d.core import BamFile, NodePath, TextNode, DecalEffect
from toontown.dna import DNANode, DNAUtil, DNAError

class DNASignBaseline(DNANode.DNANode):
    COMPONENT_CODE = 6

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)

    def __del__(self):
        DNANode.DNANode.__del__(self)

        if not hasattr(self, 'text'):
            return

        del self.text
        del self.code
        del self.color
        del self.flags
        del self.indent
        del self.kern
        del self.wiggle
        del self.stumble
        del self.stomp
        del self.width
        del self.height

    def makeFromDGI(self, dgi, store):
        DNANode.DNANode.makeFromDGI(self, dgi, store)
        self.text = dgi.getString()
        self.code = dgi.getString()
        self.color = DNAUtil.dgiExtractColor(dgi)
        self.flags = dgi.getString()
        self.indent = dgi.getFloat32()
        self.kern = dgi.getFloat32()
        self.wiggle = dgi.getFloat32()
        self.stumble = dgi.getFloat32()
        self.stomp = dgi.getFloat32()
        self.width = dgi.getFloat32()
        self.height = dgi.getFloat32()

    def traverse(self, nodePath, dnaStorage):
        root = NodePath('signroot')
        head_root = NodePath('root')
        wantDecalTest = base.config.GetBool('want-sign-decal-test', False)
        x = 0
        for i in range(len(self.text)):
            tn = TextNode("text")
            tn.setText(self.text[i])
            tn.setTextColor(self.color)
            font = dnaStorage.findFont(self.code)

            if font == None:
                raise DNAError.DNAError('Font code %s not found.' %self.code)

            tn.setFont(font)

            if i == 0 and 'b' in self.flags:
                tn.setTextScale(1.5)
            np = root.attachNewNode(tn)
            np.setScale(self.scale)
            np.setDepthWrite(0)

            if i % 2:
                np.setPos(x + self.stumble, 0, self.stomp)
                np.setR(-self.wiggle)
            else:
                np.setPos(x - self.stumble, 0, self.stomp)
                np.setR(self.wiggle)

            x += tn.getWidth() * np.getSx() + self.kern

        for i in range(root.getNumChildren()):
            c = root.getChild(i)
            c.setX(c.getX() - x / 2.)

        if self.width and self.height:
            for i in range(root.getNumChildren()):
                node = root.getChild(i)

                A = (node.getX() / (self.height / 2.))
                B = (self.indent * math.pi / 180.)

                theta = A + B
                d = node.getY()
                x = math.sin(theta) * (self.height / 2.)
                y = (math.cos(theta) - 1) * (self.height / 2.)
                radius = math.hypot(x, y)

                if radius != 0:
                    j = (radius + d) / radius
                    x *= j
                    y *= j
                node.setPos(x, 0, y)
                node.setR(node, (theta * 180.) / math.pi)

        collection = root.findAllMatches("**/+TextNode")
        for i in range(collection.getNumPaths()):
            xnp = collection.getPath(i)
            np2 = xnp.getParent().attachNewNode(xnp.node().generate())
            np2.setTransform(xnp.getTransform())
            xnp.removeNode()
        
        _np = nodePath.attachNewNode(root.node())
        _np.setPosHpr(self.pos, self.hpr)
        
        if wantDecalTest:
            root.setEffect(DecalEffect.make())
        else:
            _np.setDepthOffset(50)

        self.traverseChildren(_np, dnaStorage)

        _np.flattenStrong()
