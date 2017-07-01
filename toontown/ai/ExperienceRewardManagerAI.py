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
        if av.getToonLevel() in ToontownGlobals.ExperienceTrainingPointLevels:
            self.addTrainingPoint(av)
        if av.getToonLevel() in ToontownGlobals.ExperienceGagLevels:
            self.addGagCapacity(av)
        if av.getToonLevel() in ToontownGlobals.ExperienceMoneyLevels:
            self.addMaxMoney(av)
	
    def addMaxMoney(self, av):
        av.b_setMaxMoney(av.getMaxMoney() + ToontownGlobals.ExpMoneyCarryReward)
	
    def addGagCapacity(self, av):
        av.b_setMaxCarry(av.getMaxCarry() + ToontownGlobals.ExpGagCarryReward)
		
    def addTrainingPoint(self, av):
        av.b_setTrainingPoints(av.getTrainingPoints() + ToontownGlobals.ExpTrainingPointReward)
		
    def getMoneyMult(self, av):
        return 10 + int((av.getToonLevel()+1)/10)
        
        
