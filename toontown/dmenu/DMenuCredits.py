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
        self.screenCover.setColor((0, 0, 0, 0.8))
        self.screenCover.setTransparency(1)

        self.extremelylargecredits = '''
\1orangeText\1Credits\2

\1orangeText\1Open Source Toontown Servers\2
Cranky Supertoon | Director
ComradeNapCal | Notorious Leaker
Rocket | Hackerman
Leo | Major Oofenton
ToonJoey | Resident Dinosaur Planet Guy

\1orangeText\1Management Team\2
Dubito | Director
Bethy / Limey Mouse | Director
Owen | Content Director | Community Manager
Royko | External Community Manager
Loopy Goopy Googlenerd | Content Director
 
\1orangeText\1Technical Team\2
Sir Tubby Cheezyfish | Lead Game Developer | Father Of Zap Gags
Barks | Game Developer
Tessler | Game Developer
Atomizer | Game Developer
Nosyliam | Game Developer
Ben | Launcher Developer
Judge2020 | Launcher Developer
Xanon | Web Developer
 
\1orangeText\1Creative Team\2
Bethy / Limey Mouse | Lead Artist
Old Geezer | Modeller | Composer
Polygon | Modeller
Maddie | Texture Artist
VoidPoro | Texture Artist
Pascal | Modeller | Head of Moderation
SpookiRandi | Graphical Artist
 
\1orangeText\1Moderation Team\2
Dr. Sovietoon
TheTabKey
Kryptic Kaleidoscope
The Professional
SpookiRandi
 
\1orangeText\1Contributors\2
Dank Mickey | Former Developer | Boardbot Development
KHDecoder | Boardbot Development
Josh Zimmer | Former Developer
SkippsDev | Former Developer
Swag Foreman | Boardbot Models | Various parts of Cog Rooftops
Aura | Pick-A-Toon Concept / Inspiration
John Linderman | Deer Models
Smirky Bumberpop | Former External Community Manager
Malverde | Former Developer | Various playground redesigns
Alice | Web Developer
WhoeverTheFuckMadeOurLogo | Creator of the Project Altis Logo
John Linderman | Deer Models
 
\1orangeText\1Special thanks to\2
The Corporate Clash Crew | Revieving Project Altis Offically
Toontown Infinite | Various Resources
Piplup | New battle GUI concept
Chandler | DNA Parser | Safely disclosing security issues
Developers of Panda3D
Developers of Astron
Toontown Rewritten | Reviving the spirit of Toontown
Project Altis Team | Original Developers | None of this would be possible without you guys!
Toontown Onlines Developers | Creating a game with care that lasted for years to come | Thanks for everything!
You | Playing the game and supporting it (even if you didn't like it)
'''

        self.text = OnscreenText(text = self.extremelylargecredits, style = 3, fg = (1, 1, 1, 1), align = TextNode.ACenter, scale = 0.08, wordwrap = 30, parent = aspect2d)
        self.text.setPos(0, -1)
        self.text.setColorScale(1, 1, 1, 0)
        self.logo = OnscreenImage(image = 'phase_3/maps/toontown-logo.png',
                                  scale = (0.8 * (4.0 / 3.0), 0.8, 0.8 / (4.0 / 3.0)))
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
        LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 1), startColorScale = Vec4(1, 1, 1, 0)),
        LerpColorScaleInterval(self.text, 1, Vec4(1, 1, 1, 1), startColorScale = Vec4(1, 1, 1, 0)),
        Wait(1),
        self.text.posInterval(35, Point3(0, 0, 6)),
        Wait(1),
        LerpColorScaleInterval(self.screenCover, 1, Vec4(1, 1, 1, 0), startColorScale = Vec4(1, 1, 1, 1)),
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