from pandac.PandaModules import *
from direct.gui.DirectGui import *
from direct.gui.DirectGuiGlobals import NO_FADE_SORT_INDEX
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.hood import ZoneUtil
from direct.interval.IntervalGlobal import Sequence, Wait
import random

class ToontownLoadingScreen:

    def __init__(self):
        self.__expectedCount = 0
        self.__count = 0
        self.gui = loader.loadModel('phase_3/models/gui/progress-background.bam')
        self.title = DirectLabel(guiId = 'ToontownLoadingScreenTitle', parent = self.gui, relief = None, pos = (0, 0, 0.23), text = '', textMayChange = 1, text_scale = 0.08, text_fg = (0.03, 0.83, 0, 1), text_align = TextNode.ACenter, text_font = ToontownGlobals.getSignFont())
        self.tip = DirectLabel(guiId = 'ToontownLoadingScreenTip', parent = self.gui, relief = None, pos = (0, 0, .5), text = '', textMayChange = 1, text_scale = 0.05, text_fg = (1, 1, 1, 1), text_shadow = (0, 0, 0, 1), text_wordwrap = 40, text_align = TextNode.ACenter, text_font = ToontownGlobals.getMinnieFont())
        self.waitBar = DirectWaitBar(guiId = 'ToontownLoadingScreenWaitBar', parent = self.gui, frameSize = (base.a2dLeft + (base.a2dRight / 4.95), base.a2dRight - (base.a2dRight / 4.95), -0.04, 0.04), pos = (0, 0, 0.15), text = '')
        logoScale = 0.3625 # Scale for our locked aspect ratio (2:1).
        self.logo = OnscreenImage(image = 'phase_3/maps/toontown-logo.png',
            scale = (logoScale * 2.0, 1, logoScale))

        self.logo.reparentTo(hidden)
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        scale = self.logo.getScale()
        # self.logo.setPos(scale[0], 0, -scale[2])
        self.logo.setPos(0, 0, -scale[2] * 2)

    def destroy(self):
        self.tip.destroy()
        self.title.destroy()
        self.gui.removeNode()
        self.logo.removeNode()

    def getTip(self, tipCategory):
        return TTLocalizer.TipTitle + '\n' + random.choice(TTLocalizer.TipDict.get(tipCategory))

    def begin(self, range, label, gui, tipCategory, zoneId):
        self.zone2background = {
            ToontownGlobals.ToontownCentral: 'ttc.jpg',
            ToontownGlobals.DonaldsDock: 'dd.jpg',
            ToontownGlobals.DaisyGardens: 'dg.jpg',
            ToontownGlobals.MinniesMelodyland: 'mml.jpg',
            ToontownGlobals.TheBrrrgh: 'tb.jpg',
            ToontownGlobals.DonaldsDreamland: 'ddl.jpg',
            ToontownGlobals.OutdoorZone: 'aa.jpg',
            ToontownGlobals.GoofySpeedway: 'gs.jpg',
            ToontownGlobals.SellbotHQ: 'sbhq.jpg',
            ToontownGlobals.SellbotFactoryExt: 'sbhqext.jpg',
            ToontownGlobals.LawbotHQ: 'lbhq.jpg',
            ToontownGlobals.CashbotHQ: 'cbhq.jpg',
            ToontownGlobals.BossbotHQ: 'bbhq.jpg'
            }
        self.zone2fontcolor = {
            ToontownGlobals.GoofySpeedway : VBase4(ToontownGlobals.GSCOLOR),
            ToontownGlobals.ToontownCentral : VBase4(ToontownGlobals.TTCOLOR),
            ToontownGlobals.SillyStreet : VBase4(ToontownGlobals.TTCOLOR),
            ToontownGlobals.LoopyLane : VBase4(ToontownGlobals.TTCOLOR),
            ToontownGlobals.PunchlinePlace : VBase4(ToontownGlobals.TTCOLOR),
            ToontownGlobals.DonaldsDock : VBase4(ToontownGlobals.DDCOLOR),
            ToontownGlobals.BarnacleBoulevard : VBase4(ToontownGlobals.DDCOLOR),
            ToontownGlobals.SeaweedStreet : VBase4(ToontownGlobals.DDCOLOR),
            ToontownGlobals.LighthouseLane : VBase4(ToontownGlobals.DDCOLOR),
            ToontownGlobals.AhoyAvenue : VBase4(ToontownGlobals.DDCOLOR),
            ToontownGlobals.DaisyGardens : VBase4(ToontownGlobals.DGCOLOR),
            ToontownGlobals.ElmStreet : VBase4(ToontownGlobals.DGCOLOR),
            ToontownGlobals.MapleStreet : VBase4(ToontownGlobals.DGCOLOR),
            ToontownGlobals.OakStreet : VBase4(ToontownGlobals.DGCOLOR),
            ToontownGlobals.RoseValley : VBase4(ToontownGlobals.DGCOLOR),
            ToontownGlobals.MinniesMelodyland : VBase4(ToontownGlobals.MMCOLOR),
            ToontownGlobals.AltoAvenue : VBase4(ToontownGlobals.MMCOLOR),
            ToontownGlobals.BaritoneBoulevard : VBase4(ToontownGlobals.MMCOLOR),
            ToontownGlobals.TenorTerrace : VBase4(ToontownGlobals.MMCOLOR),
            ToontownGlobals.SopranoStreet : VBase4(ToontownGlobals.MMCOLOR),
            ToontownGlobals.TheBrrrgh : VBase4(ToontownGlobals.BRCOLOR),
            ToontownGlobals.WalrusWay : VBase4(ToontownGlobals.BRCOLOR),
            ToontownGlobals.SleetStreet : VBase4(ToontownGlobals.BRCOLOR),
            ToontownGlobals.PolarPlace : VBase4(ToontownGlobals.BRCOLOR),
            ToontownGlobals.DonaldsDreamland : VBase4(ToontownGlobals.DLCOLOR),
            ToontownGlobals.LullabyLane : VBase4(ToontownGlobals.DLCOLOR),
            ToontownGlobals.PajamaPlace : VBase4(ToontownGlobals.DLCOLOR),
            ToontownGlobals.OutdoorZone : VBase4(ToontownGlobals.OZCOLOR),
            ToontownGlobals.GolfZone : VBase4(ToontownGlobals.OZCOLOR),
            ToontownGlobals.SellbotHQ : (0.2, 0.2, 0.2, 1.0),
            ToontownGlobals.SellbotFactoryExt : (0.2, 0.2, 0.2, 1.0),
            ToontownGlobals.SellbotFactoryInt : (0.2, 0.2, 0.2, 1.0),
            ToontownGlobals.CashbotHQ : (0.2, 0.2, 0.2, 1.0),
            ToontownGlobals.LawbotHQ : (0.2, 0.2, 0.2, 1.0),
            ToontownGlobals.BossbotHQ : (0.2, 0.2, 0.2, 1.0)
        }

        self.waitBar['barColor'] = self.zone2fontcolor.get(ZoneUtil.getBranchZone(zoneId), ToontownGlobals.DEFAULTCOLOR)
        self.waitBar['range'] = range*2
        self.title['text'] = label
        self.__count = 0
        self.__expectedCount = range*2
        if gui:
            self.title.reparentTo(base.a2dpBottomCenter, NO_FADE_SORT_INDEX)
            self.title.setPos(0, 0, 0.23)
            self.gui.setPos(0, -0.1, 0)
            self.gui.reparentTo(aspect2d, NO_FADE_SORT_INDEX)
            self.tip['text'] = self.getTip(tipCategory)
            bg = 'phase_3.5/maps/loading/' + self.zone2background.get(ZoneUtil.getBranchZone(zoneId), 'toon.jpg')
            self.gui.setTexture(loader.loadTexture(bg), 1)
            self.logo.reparentTo(base.a2dpTopCenter, NO_FADE_SORT_INDEX)
        else:
            self.title.reparentTo(base.a2dpTopCenter, NO_FADE_SORT_INDEX)
            self.gui.reparentTo(hidden)
            self.logo.reparentTo(hidden)
        self.title['text_fg'] = self.zone2fontcolor.get(ZoneUtil.getBranchZone(zoneId), ToontownGlobals.DEFAULTCOLOR)
        self.tip.reparentTo(base.a2dpBottomCenter, NO_FADE_SORT_INDEX)
        self.waitBar.reparentTo(base.a2dpBottomCenter, NO_FADE_SORT_INDEX)
        self.waitBar.update(self.__count)

    def end(self):
        self.waitBar.finish()
        self.waitBar.reparentTo(self.gui)
        self.title.reparentTo(self.gui)
        self.tip.reparentTo(self.gui)
        self.gui.reparentTo(hidden)
        self.logo.reparentTo(hidden)
        return (self.__expectedCount, self.__count)

    def abort(self):
        self.gui.reparentTo(hidden)

    def tick(self):
        self.__count = self.__count + 1
        base.graphicsEngine.renderFrame()
        self.waitBar.update(self.__count)
