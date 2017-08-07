from toontown.shtiker import ShtikerPage
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.achievements import AchievementsGlobals
from toontown.achievements import Achievements
from toontown.makeatoon.MakeAToonGlobals import *
import math

POSITIONS = [(-.45, 0, .2), (.45, 0, .2),
             (-.45, 0, -.4), (.45, 0, -.4)]

class AchievementsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.avatar = None
        self.achievements = []
        self.categories = [[], [], [], [], [], [], [], []]
        self.statRows = []
        self.index = 0
        self.offset = 0
        self.statOffset = 0

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
		
        gui = loader.loadModel('phase_3/models/gui/tt_m_gui_mat_mainGui')
        shuffleFrame = gui.find('**/tt_t_gui_mat_shuffleFrame')
        shuffleUp = gui.find('**/tt_t_gui_mat_shuffleUp')
        shuffleDown = gui.find('**/tt_t_gui_mat_shuffleDown')
        shuffleImage = (gui.find('**/tt_t_gui_mat_shuffleArrowUp'), gui.find('**/tt_t_gui_mat_shuffleArrowDown'), gui.find('**/tt_t_gui_mat_shuffleArrowUp'), gui.find('**/tt_t_gui_mat_shuffleArrowDisabled'))
        gui.removeNode()
		
        self.nameFrame = DirectFrame(parent=self.achievementsPageNode, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, 0.6), hpr=(0, 0, 3), scale=(1.2), frameColor=(1, 1, 1, 1), text=TTLocalizer.AchievementCategories[self.index], text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.achievementLButton = DirectButton(parent=self.nameFrame, relief=None, image=shuffleImage, image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.doAchievementPageChange, extraArgs = [-1])
        self.achievementLButton['state'] = DGG.DISABLED
        self.achievementRButton = DirectButton(parent=self.nameFrame, relief=None, image=shuffleImage, image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.doAchievementPageChange, extraArgs = [1])
        self.setFrame = DirectFrame(parent=self.achievementsPageNode, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0.5, 0, 0.6), hpr=(0, 0, 3), scale=(0.8), frameColor=(1, 1, 1, 1), text='', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.setLButton = DirectButton(parent=self.setFrame, relief=None, image=shuffleImage, image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.doSetPageChange, extraArgs = [-1])
        self.setRButton = DirectButton(parent=self.setFrame, relief=None, image=shuffleImage, image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.doSetPageChange, extraArgs = [1])
        self.setFrame.hide()
        self.statFrame = DirectFrame(parent=self.statsPageNode, image=shuffleFrame, image_scale=halfButtonInvertScale, relief=None, pos=(0, 0, 0.4), hpr=(0, 0, 3), scale=(0.8), frameColor=(1, 1, 1, 1), text='', text_scale=0.0625, text_pos=(-0.001, -0.015), text_fg=(1, 1, 1, 1))
        self.statLButton = DirectButton(parent=self.statFrame, relief=None, image=shuffleImage, image_scale=halfButtonScale, image1_scale=halfButtonHoverScale, image2_scale=halfButtonHoverScale, pos=(-0.2, 0, 0), command=self.doStatPageChange, extraArgs = [-1])
        self.statRButton = DirectButton(parent=self.statFrame, relief=None, image=shuffleImage, image_scale=halfButtonInvertScale, image1_scale=halfButtonInvertHoverScale, image2_scale=halfButtonInvertHoverScale, pos=(0.2, 0, 0), command=self.doStatPageChange, extraArgs = [1])
        self.statFrame.hide()
        self.doAchievementPageChange(0)
        self.doStatPageChange(0)


    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.avAchievements = localAvatar.achievements
        self.title = DirectLabel(parent = self, relief = None, text = TTLocalizer.AchievementsPageTitle, text_scale = 0.1, textMayChange = 1, pos = (0, 0, 0.665))

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
		
        del self.categories

        self.achievementsPageNode.removeNode()
        self.statsPageNode.removeNode()

    def setAvatar(self, av):
        self.avatar = av

    def showAchievements(self):
        self.title['text'] = ''
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
        self.categories = [[], [], [], [], [], [], [], []]
        engageModulusMode = False
        setNum = 0

        start_pos = LVecBase3(.4, 1, -0.26)
        seperation = LVecBase3(0, 0, 0.7)
		
        possibleAchievementTypes = Achievements.type2AchievementIds.keys()
		
        for type in xrange(len(possibleAchievementTypes)):
            for achievement in Achievements.AchievementsDict:
                if isinstance(achievement, possibleAchievementTypes[type]):
                    cat = Achievements.type2Category.get(achievement.__class__)
                    self.categories[cat].append(Achievements.AchievementsDict.index(achievement))
		
        if len(self.categories[self.index]) > 4:
            self.setFrame.show()
        else:
            self.setFrame.hide()

        for achievement in xrange(self.offset, self.offset + 4):
            try:
                achievementFrame = DirectFrame(parent = self.achievementsPageNode, image = DGG.getDefaultDialogGeom(), scale = (0.55, 0, 0.55),
                                               relief = None, pos = (POSITIONS[achievement % 4]),
                                               text = TTLocalizer.Achievements[self.categories[self.index][achievement]], text_scale = (.08),
                                               text_font = ToontownGlobals.getMinnieFont(), text_wordwrap = 10, text_pos = (0, 0, 0))
            except:
                return

            self.achievements.append(achievementFrame)

            if self.categories[self.index][achievement] in self.avAchievements:
                achievementFrame['text'] = TTLocalizer.Achievements[self.categories[self.index][achievement]]
                achievementFrame['text_pos'] = (0, .4, 0)

                currentAchievement = AchievementsGlobals.AchievementImages[self.categories[self.index][achievement]]

                img = OnscreenImage(image = currentAchievement, parent = achievementFrame, scale = (.2, 1, .2))
                img.setTransparency(TransparencyAttrib.MAlpha)
                experience = OnscreenText(parent = achievementFrame, text = TTLocalizer.AchievementsDesc[self.categories[self.index][achievement]], scale = (.06), wordwrap = 10, font = ToontownGlobals.getMinnieFont(), pos = (0, -.3))
            else:
                achievementFrame['text'] = TTLocalizer.LockedAchievement
				
    def doAchievementPageChange(self, direction):
        self.index += direction
        self.nameFrame['text'] = TTLocalizer.AchievementCategories[self.index]
        if self.index <= 0:
            self.achievementLButton['state'] = DGG.DISABLED
            self.achievementRButton['state'] = DGG.NORMAL
        elif self.index >= (len(TTLocalizer.AchievementCategories) - 1):
            self.achievementLButton['state'] = DGG.NORMAL
            self.achievementRButton['state'] = DGG.DISABLED
        else:
            self.achievementLButton['state'] = DGG.NORMAL
            self.achievementRButton['state'] = DGG.NORMAL
        self.offset = 0
        self.setFrame['text'] = 'Page ' + str((self.offset/4) + 1)
        self.setLButton['state'] = DGG.DISABLED
        self.setRButton['state'] = DGG.NORMAL		
        self.updatePage()
		
    def doSetPageChange(self, direction):
        self.offset += (direction * 4)
        if self.offset <= 0:
            self.setLButton['state'] = DGG.DISABLED
            self.setRButton['state'] = DGG.NORMAL
        elif self.offset >= len(self.categories[self.index]) - 4:
            self.setLButton['state'] = DGG.NORMAL
            self.setRButton['state'] = DGG.DISABLED
        else:
            self.setLButton['state'] = DGG.NORMAL
            self.setRButton['state'] = DGG.NORMAL
        self.setFrame['text'] = 'Page ' + str((self.offset/4) + 1)
        self.updatePage()
		
    def doStatPageChange(self, direction):
        self.statOffset += (direction * 26)
        if self.statOffset <= 0:
            self.statLButton['state'] = DGG.DISABLED
            self.statRButton['state'] = DGG.NORMAL
        elif self.statOffset >= len(base.localAvatar.getStats()) - 26:
            self.statLButton['state'] = DGG.NORMAL
            self.statRButton['state'] = DGG.DISABLED
        else:
            self.statLButton['state'] = DGG.NORMAL
            self.statRButton['state'] = DGG.NORMAL
        self.statFrame['text'] = 'Page ' + str((self.statOffset/26) + 1)
        self.updateStats()

    def updateStats(self):
        rowYs = (.6, .5, .4, .3, .2, .1, 0, -.1, -.2, -.3, -.4, -.5, -.6)
        for statRows in self.statRows:
            statRows.destroy()
        self.statRows = [self.createStat(y) for y in (rowYs)]
        statRows2 = [self.createStat(y, 0.8) for y in (rowYs)]
        self.statRows += statRows2
        self.stats = base.localAvatar.getStats()
        for stat in xrange(self.statOffset, self.statOffset + 26):
            try:
                statText = TTLocalizer.StatsList[stat] % self.stats[stat]
                self.statRows[stat - 26]['text'] = statText
            except:
                pass
        if len(self.stats) > 26:
            self.statFrame.show()
        else:
            self.statFrame.hide()

    def createStat(self, y, x = -0.8):
        if x < 0:
            align = TextNode.ALeft
        else:
            align = TextNode.ARight
        row = DirectLabel(parent = self.statsPageNode, relief = None, text_align = align, text = '', text_scale = 0.045, text_font = ToontownGlobals.getBuildingNametagFont(), text_wordwrap = 16, text_style = 3)
        row.setPos(x, 0, y)
        return row
