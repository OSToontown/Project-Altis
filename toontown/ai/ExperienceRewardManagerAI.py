from otp.ai.AIBaseGlobal import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
import random

class ExperienceRewardManagerAI:
    notify = DirectNotifyGlobal.directNotify.newCategory('ExperienceRewardManagerAI')

    def __init__(self, air):
        self.air = air
			
    def checkForLevelUpReward(self, av):
        av.addMoney(av.getToonLevel() * self.getMoneyMult(av))
        if av.getToonLevel() in ToontownGlobals.ExperienceHPLevels:
            self.addLaff(av)
        #if av.getToonLevel() in ToontownGlobals.ExperienceGagLevels:
            #self.addGagCapacity(av)
        #if av.getToonLevel() in ToontownGlobals.ExperienceMoneyLevels:
            #self.addMaxMoney(av)
		
    def addLaff(self, av):
        av.b_setMaxHp(av.getMaxHp() + ToontownGlobals.ExpLaffBoost)
        av.toonUp(av.getMaxHp() - av.hp)
	
    def addMaxMoney(self, av):
        av.b_setMaxMoney(av.getMaxMoney() + ToontownGlobals.ExpMoneyCarryReward)
	
    def addGagCapacity(self, av):
        av.b_setMaxCarry(av.getMaxCarry() + ToontownGlobals.ExpGagCarryReward)
		
    def getMoneyMult(self, av):
        return 10 + int((av.getToonLevel()+1)/10)
        
        
