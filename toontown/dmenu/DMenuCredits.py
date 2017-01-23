from panda3d.core import Vec4, TransparencyAttrib, Point3, VBase3, VBase4, TextNode
from direct.interval.IntervalGlobal import * 
from toontown.toon import Toon, ToonDNA
from direct.actor.Actor import Actor
from direct.gui.DirectGui import *
from toontown.toonbase import ToontownGlobals

class DMenuCredits:

    def __init__(self):
        '''
        Setup the screen
        '''
        self.creditsSequence = None
        self.text = None
        self.roleText = None
        cm = CardMaker('screen-cover')
        cm.setFrameFullscreenQuad()
        self.screenCover = aspect2d.attachNewNode(cm.generate())
        self.screenCover.show()
        self.screenCover.setScale(100)
        self.screenCover.setColor((0, 0, 0, 1))
        self.screenCover.setTransparency(1)
        
        self.extremelylargecredits = '''
\1orangeText\1Credits\2

\1orangeText\1Directors\2
Drew
Dubito

\1orangeText\1Assistant Director\2
Bethy / Limey Mouse

\1orangeText\1Investor\2
Judge

\1orangeText\1Content Director\2
LoopyGoopyG

\1orangeText\1Developers\2
SkippsDev | Lead Developer
Drew | Game Developer
Alice | Web Developer
Barks | Game Developer
Dan | Game Developer
Malverde | Game Developer
Sir Tubby Cheezyfish | Game Developer
Xanon | Web Developer

\1orangeText\1Artists\2
Bethy / Limey Mouse | Lead Artist
Old Geezer | Modeller | Composer
Maddie | Texture Artist
VoidPoro | Texture Artist

\1orangeText\1Community Managers\2
Smirky Bumberpop | External Community Manager
Remot | Noted | Internal Staff Manager

\1orangeText\1Contributors\2
Dank Mickey | Former Developer | Boardbot Development
Josh Zimmer | Former developer | One of the founders
Swag Foreman | Boardbot Models | Various parts of Cog Rooftops
Aura | Pick-A-Toon Concept / Inspiration

\1orangeText\1Special thanks to\2
Toontown Infinite | Various Resources
Chandler | DNA Parser | Safely disclosing security issues
Developers of Panda3D
Developers of Astron
Toontown Rewritten | Reviving the sprit of Toontown
'''
            
        self.text = OnscreenText(text = self.extremelylargecredits, style=3, fg=(1, 1, 1, 1), align = TextNode.ACenter, scale = 0.08, wordwrap = 30, parent=aspect2d)
        self.text.setPos(0, -1)
        self.text.setColorScale(1, 1, 1, 0)
        self.logo = OnscreenImage(image='phase_3/maps/toontown-logo.png',
                                  scale=(0.8 * (4.0/3.0), 0.8, 0.8 / (4.0/3.0)))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.logo.reparentTo(self.text)
        self.logo.setPos(0, 0, 0)
        self.logo.setColorScale(1, 1, 1, 1)
        self.startCredits()
        base.transitions.fadeScreen(0)
        base.accept('space', self.removeCredits)
        base.accept('escape', self.removeCredits)

    def startCredits(self):
        self.creditsSequence = Sequence(
        LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0)),
        LerpColorScaleInterval(self.text, 1, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0)),
        Wait(1),
        self.text.posInterval(25, Point3(0, 0, 6)),
        Wait(1),
        LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1)),
        Func(self.removeCredits)
        ).start()

    def removeCredits(self):
        base.ignore('space')
        base.ignore('escape')
        base.transitions.noFade()
        if self.creditsSequence:
            self.creditsSequence.finish()
            self.creditsSequence = None
        if self.text:
            self.text.destroy()
            self.text = None
        if self.screenCover:
            self.screenCover.removeNode()
            self.screenCover = None