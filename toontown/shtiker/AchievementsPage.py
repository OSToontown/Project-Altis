from toontown.shtiker import ShtikerPage
from direct.gui.DirectGui import *
from pandac.PandaModules import *
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
from toontown.achievements import AchievementsGlobals

POSITIONS = [(-.45, 0, .3), (-.15, 0, .3), (.15, 0, .3), (.45, 0, .3),
             (-.45, 0, .0), (-.15, 0, .0), (.15, 0, .0), (.45, 0, .0),
             (-.45, 0, -.3), (-.15, 0, -.3), (.15, 0, -.3), (.45, 0, -.3)]

class AchievementsPage(ShtikerPage.ShtikerPage):

    def __init__(self):
        ShtikerPage.ShtikerPage.__init__(self)
        self.avatar = None
        self.achievements = []

        self.gui = loader.loadModel('phase_3.5/models/gui/friendslist_gui')
        self.accept(localAvatar.uniqueName('achievementsChange'), self.updatePage)

    def load(self):
        ShtikerPage.ShtikerPage.load(self)
        self.avAchievements = localAvatar.achievements
        self.title = DirectLabel(parent=self, relief=None, text=TTLocalizer.AchievementsPageTitle, text_scale=0.12, textMayChange=1, pos=(0, 0, 0.62))

        cardModel = loader.loadModel('phase_3.5/models/gui/playingCard')

        incButton = (self.gui.find('**/FndsLst_ScrollUp'),
                     self.gui.find('**/FndsLst_ScrollDN'),
                     self.gui.find('**/FndsLst_ScrollUp_Rllvr'),
                     self.gui.find('**/FndsLst_ScrollUp'))

        self.updatePage()

    def setAvatar(self, av):
        self.avatar = av

    def updatePage(self):
        self.avAchievements = localAvatar.achievements

        for achievement in self.achievements:
            achievement.destroy()

        del self.achievements
        self.achievements = []

        start_pos = LVecBase3(.4, 1, -0.26)
        seperation = LVecBase3(0, 0, 0.7)

        for achievement in xrange(len(AchievementsGlobals.AchievementTitles)):
            achievementFrame = DirectFrame(parent=self, image=DGG.getDefaultDialogGeom(), scale=(0.25, 0, 0.25),
                                           relief=None, pos=(POSITIONS[achievement]),
                                           text=AchievementsGlobals.AchievementTitles[achievement], text_scale=(.08),
                                           text_font=ToontownGlobals.getMinnieFont(), text_pos=(0, 0, 0))

            self.achievements.append(achievementFrame)

            if achievement in  self.avAchievements:
                achievementFrame['text'] = AchievementsGlobals.AchievementTitles[achievement]
                achievementFrame['text_pos'] = (0, .4, 0)

                currentAchievement = AchievementsGlobals.AchievementImages[achievement]

                img = OnscreenImage(image=currentAchievement, parent=achievementFrame, scale = (.2, 1, .2))
                img.setTransparency(TransparencyAttrib.MAlpha)
                experience = OnscreenText(parent=achievementFrame, text=str(AchievementsGlobals.AchievementExperience[achievement]) + " experience", scale=(.08), font = ToontownGlobals.getMinnieFont(), fg = (.2, .8, .2, 1), pos = (0, -.4))
            else:
                achievementFrame['text'] = 'Achievement locked'