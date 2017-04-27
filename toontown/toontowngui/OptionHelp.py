from panda3d.core import CardMaker, NodePath, TransparencyAttrib, TextureStage, TextNode
from direct.gui.DirectGui import *
from toontown.toontowngui.TTGui import btnDn, btnRlvr, btnUp
from toontown.toonbase import ToontownGlobals, TTLocalizer

class OptionHelp(DirectFrame):
    notify = directNotify.newCategory('OptionHelp')

    def __init__(self, parent = aspect2d, moviePath = None, helpText = None, **kw):
        optiondefs = (
        )
        self.defineoptions(kw, optiondefs)
        DirectFrame.__init__(self, parent)
        self.initialiseoptions(OptionHelp)

        self.helpText = DirectLabel(parent = self, relief = None, text = helpText, pos = (0, 0, -.1), text_align = TextNode.ALeft, text_wordwrap = 16, text_scale = (0.05))

        tex = loader.loadTexture(moviePath)
        tex.play()
        cm = CardMaker(moviePath + ' card')
        self.movieCard = NodePath(cm.generate())
        self.movieCard.set_texture(tex)
        self.movieCard.setTexScale(TextureStage.getDefault(), tex.getTexScale())
        self.movieCard.reparent_to(self)
        self.movieCard.set_scale(.6)

    def destroy(self):
        DirectFrame.destroy(self)
