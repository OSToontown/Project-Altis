from toontown.shtiker import ShtikerPage
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.achievements import AchievementsGlobals

POSITIONS = [(-.45, 0, .45), (-.15, 0, .45), (.15, 0, .45), (.45, 0, .45),
             (-.45, 0, .15), (-.15, 0, .15), (.15, 0, .15), (.45, 0, .15),
             (-.45, 0, -.15), (-.15, 0, -.15), (.15, 0, -.15), (.45, 0, -.15),
             (-.45, 0, -.45), (-.15, 0, -.45), (.15, 0, -.45), (.45, 0, -.45)]

class AchievementsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.avatar = None
        self.achievements = []
        self.statRows = []

        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.accept(localAvatar.uniqueName('achievementsChange'), self.updatePage)

        gui = loader.loadModel('phase_3.5/models/gui/fishingBook.bam')
        normalColor = (1, 1, 1, 1)
        clickColor = (0.8, 0.8, 0, 1)
        rolloverColor = (0.15, 0.82, 1.0, 1)
        diabledColor = (1.0, 0.98, 0.15, 1)
        self.achievementsBtn = DirectButton(
            parent = self, relief = None, text = "Achievements",
            text_scale = 0.05, text_align = TextNode.ACenter,
            image = gui.find('**/tabs/polySurface2'), image_pos = (0, 1, -0.91),
            image_hpr = (0, 0, -90), image_scale = (0.033, 0.033, 0.035),
            image_color = normalColor, image1_color = clickColor,
            image2_color = rolloverColor, image3_color = diabledColor,
            text_fg = Vec4(0.2, 0.1, 0, 1),
            command = self.showAchievements,
            pos = (-0.64, 0, 0.77))
        self.statsBtn = DirectButton(
            parent = self, relief = None, text = "Statistics",
            text_scale = 0.05, text_align = TextNode.ACenter,
            image = gui.find('**/tabs/polySurface2'), image_pos = (0, 1, -0.91),
            image_hpr = (0, 0, -90), image_scale = (0.033, 0.033, 0.035),
            image_color = normalColor, image1_color = clickColor,
            image2_color = rolloverColor, image3_color = diabledColor,
            text_fg = Vec4(0.2, 0.1, 0, 1),
            command = self.showStatsPage,
            pos = (0.64, 0, 0.77))

        self.achievementsPageNode = self.attachNewNode("achievements")
        self.statsPageNode = self.attachNewNode("stats")


    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.avAchievements = localAvatar.achievements
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.AchievementsPageTitle, text_scale = 0.12, textMayChange = 1, pos = (0, 0, 0.62))

        cardModel = loader.loadModel('phase_3.5/models/gui/playingCard')

        incButton = (self.gui.find('**/FndsLst_ScrollUp'),
                     self.gui.find('**/FndsLst_ScrollDN'),
                     self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
                     self.gui.find('**/FndsLst_ScrollUp'))

        self.updatePage()
        self.updateStats()
        self.showAchievements()

    def enter(self):
        self.updatePage()
        self.updateStats()
        ShtikerPage.ShtikerPage.enter(self)

    def unload(self):
        self.title.destroy()

        for achievement in self.achievements:
            achievement.destroy()
        self.achievements = []

        for row in self.statRows:
            row.destroy()
        self.statRows = []

        self.achievementsPageNode.removeNode()
        self.statsPageNode.removeNode()

    def setAvatar(self, av):
        self.avatar = av

    def showAchievements(self):
        self.title['text'] = TTLocalizer.AchievementsPageTitle
        self.achievementsPageNode.show()
        self.statsPageNode.hide()
        self.achievementsBtn['state'] = DGG.DISABLED
        self.statsBtn['state'] = DGG.NORMAL

    def showStatsPage(self):
        self.title['text'] = TTLocalizer.StatsPageTitle
        self.achievementsPageNode.hide()
        self.statsPageNode.show()
        self.achievementsBtn['state'] = DGG.NORMAL
        self.statsBtn['state'] = DGG.DISABLED

    def updatePage(self):
        self.avAchievements = localAvatar.achievements

        for achievement in self.achievements:
            achievement.destroy()

        self.achievements = []

        start_pos = LVecBase3(.4, 1, -0.26)
        seperation = LVecBase3(0, 0, 0.7)

        for achievement in xrange(len(AchievementsGlobals.AchievementTitles)):
            achievementFrame = DirectFrame(parent = self.achievementsPageNode, image = DGG.getDefaultDialogGeom(), scale = (0.25, 0, 0.25),
                                           relief = None, pos = (POSITIONS[achievement]),
                                           text = AchievementsGlobals.AchievementTitles[achievement], text_scale = (.08),
                                           text_font = ToontownGlobals.getMinnieFont(), text_wordwrap = 10, text_pos = (0, 0, 0))

            self.achievements.append(achievementFrame)

            if achievement in  self.avAchievements:
                achievementFrame['text'] = AchievementsGlobals.AchievementTitles[achievement]
                achievementFrame['text_pos'] = (0, .4, 0)

                currentAchievement = AchievementsGlobals.AchievementImages[achievement]

                img = OnscreenImage(image = currentAchievement, parent = achievementFrame, scale = (.2, 1, .2))
                img.setTransparency(TransparencyAttrib.MAlpha)
                experience = OnscreenText(parent = achievementFrame, text = str(AchievementsGlobals.AchievementExperience[achievement]) + " experience", scale = (.08), font = ToontownGlobals.getMinnieFont(), fg = (.2, .8, .2, 1), pos = (0, -.4))
            else:
                achievementFrame['text'] = 'Achievement locked'

    def updateStats(self):
        rowYs = (.5, .4, .3, .2, .1, 0, -.1, -.2, -.3, -.4, -.5)
        for statRows in self.statRows:
            statRows.destroy()
        self.statRows = [self.createStat(y) for y in (rowYs)]
        self.stats = base.localAvatar.getStats()
        for stat in range(len(self.stats)):
            statText = TTLocalizer.StatsList[stat] % self.stats[stat]
            self.statRows[stat]['text'] = statText

    def createStat(self, y):
        row = DirectLabel(parent = self.statsPageNode, relief = None, text_align = TextNode.ALeft, text = '', text_scale = 0.045, text_wordwrap = 16, text_style = 3)
        row.setPos(-0.8, 0, y)
        return row
