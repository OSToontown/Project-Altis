from toontown.achievements import AchievementsGlobals
from direct.interval.IntervalGlobal import *
from direct.interval.LerpInterval import *
from toontown.toonbase import ToontownGlobals
from direct.gui.DirectGui import *
from pandac.PandaModules import *

class AchievementGui:
    
    def __init__(self):
        self.queue = []
        self.currentShowingAward = 0
    
    def earnAchievement(self, achievementId):
        if self.queue == []:
            sound = loader.loadSfx('phase_3.5/audio/sfx/AV_levelup.ogg')
            sound.play()
            
            self.queue.append(achievementId)
            self.showAchievement()
        else:
            self.queue.append(achievementId)

    def showAchievement(self):
        if self.queue != []:
            if self.currentShowingAward == 0:
                self.currentShowingAward = self.queue[0]
                self.displayAchievement()
                self.frameSequence()
    
    def displayAchievement(self):
        try:
            currentAchievement = AchievementsGlobals.AchievementImages[self.currentShowingAward]
        except:
            currentAchievement = 'phase_3/maps/achievements/ttpa_achievement_unknown.png'
        experience = AchievementsGlobals.AchievementExperience[self.currentShowingAward]
        
        self.frame = OnscreenImage(image='phase_3/maps/achievements/ttpa_achievement_background.png', scale=(0.5, 1, 0.5), parent=base.a2dBottomCenter,
                                  pos=(0, 0, -.45))
        self.frame.setTransparency(TransparencyAttrib.MAlpha)
        self.frame.wrtReparentTo(base.a2dBottomCenter, 4000)
        
        self.image = OnscreenImage(image=currentAchievement, parent=self.frame, scale = .3, pos = (.6, 0, 0))
        self.image.setTransparency(TransparencyAttrib.MAlpha)

        self.title = OnscreenText(text='Achievement Unlocked', scale=(0.1), font=ToontownGlobals.getMinnieFont(),
                                  parent=self.frame, pos=(0, 0.33), style = 3, align=TextNode.ACenter)
        
        self.achievementName = OnscreenText(text=AchievementsGlobals.AchievementTitles[self.currentShowingAward], wordwrap = 12, scale=(0.1),
                                            font=ToontownGlobals.getMinnieFont(), parent=self.frame, style = 3, align=TextNode.ACenter, pos=(0, 0.2))
        self.experience = OnscreenText(parent=self.frame, text=str(experience) + " experience earned!", scale=(0.09), style = 3, font = ToontownGlobals.getMinnieFont(), fg = (0, .8, 0, 1), pos = (0, -.4))
        
    def frameSequence(self):
        self.seq = Sequence()
        self.seq.append(self.frame.posInterval(.5, (0, 0, .45), blendType = 'easeInOut'))
        self.seq.append(Wait(2))
        self.seq.append(self.frame.posInterval(.5, (0, 0, -.45), blendType = 'easeInOut'))
        self.seq.append(Func(self.cleanupCurrentFrame))
        
        self.seq.start()
        
    def cleanupCurrentFrame(self):
        self.frame.destroy()
        del self.frame
        
        self.title.destroy()
        del self.title
        
        self.achievementName.destroy()
        del self.achievementName
        
        self.experience.destroy()
        del self.experience
        
        del self.queue[0]
        self.currentShowingAward = 0
        self.showAchievement()