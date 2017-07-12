import AchievementsGlobals
from direct.gui.DirectGui import DirectFrame, DirectLabel
from direct.interval.IntervalGlobal import *
from direct.interval.LerpInterval import *
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from direct.gui.DirectGui import *
from panda3d.core import *

class AchievementGui(DirectFrame):
    
    def __init__(self):
        DirectFrame.__init__(self, relief=None, sortOrder=50)
        self.initialiseoptions(AchievementGui)
        self.queue = []
        self.currentShowingAward = -1
    
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
            if self.currentShowingAward == -1:
                self.currentShowingAward = self.queue[0]
                self.displayAchievement()
                self.frameSequence()
    
    def displayAchievement(self):
        currentAchievement = AchievementsGlobals.AchievementImages[self.currentShowingAward]
        
        self.frame = DirectFrame(relief=None, geom='phase_3/models/gui/dialog_box_gui', geom_scale=(1.5, 0.5, 0.5), scale=(1, 1, 1), parent=self,
                                  pos=(0, 0, 0.7))
        
        self.image = DirectFrame(relief=None, image=currentAchievement, scale=0.2, parent=self.frame)
        self.image.setTransparency(TransparencyAttrib.MAlpha)

        self.title = DirectLabel(parent=self.frame, relief=None, pos=(0, 0, 0.2), text=TTLocalizer.EarnedAchievement, text_scale=0.08, text_font=ToontownGlobals.getInterfaceFont())
        
        self.achievementName = DirectLabel(parent=self.frame, relief=None, pos=(0, 0, 0.1), text=TTLocalizer.Achievements[self.currentShowingAward], text_scale=0.07, text_font=ToontownGlobals.getMinnieFont())
        
        self.details = DirectLabel(parent=self.frame, relief=None, pos=(0, 0, -0.2), text=TTLocalizer.AchievementsDesc[self.currentShowingAward], text_scale=0.05, text_font=ToontownGlobals.getInterfaceFont())
        
    def frameSequence(self):
        self.seq = Sequence()
        self.seq.append(LerpScaleInterval(self.frame, 0.25, (1, 1, 1), (0.01, 0.01, 0.01)))
        self.seq.append(Wait(3))
        self.seq.append(LerpScaleInterval(self.frame, 0.25, (0.01, 0.01, 0.01), (1, 1, 1)))
        self.seq.append(Func(self.cleanupCurrentFrame))
        self.seq.append(Wait(1))
        
        self.seq.start()
        
    def cleanupCurrentFrame(self):
        self.image.destroy()
        del self.image

        self.title.destroy()
        del self.title
		
        self.achievementName.destroy()
        del self.achievementName
		
        self.details.destroy()
        del self.details

        self.frame.destroy()
        del self.frame
        
        del self.queue[0]
        self.currentShowingAward = -1
        self.showAchievement()