from toontown.achievements import Achievements

class AchievementsManagerAI():
    def __init__(self, air):
        self.air = air

    def friends(self, avId):
        av = self.air.doId2do.get(avId)
        if not av:
            return

        possibleAchievements = Achievements.getAchievementsOfType(Achievements.FriendAchievement)
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)

    def catalog(self, av, items):
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.CatalogAchievement)

        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, items):
                    av.addAchievement(achievementId)

    def rideTrolley(self, av):
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.TrolleyAchievement)

        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)

    def loopysBalls(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.LoopysBallsAchievement)

        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def sofie(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.SofieSquirtAchievement)

        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def resistance(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.ResistanceAchievement)

        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def doodle(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.DoodleAchievement)

        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def gagTrack(self, av, track):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.GagTrackAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, track):
                    av.addAchievement(achievementId)
					
    def maxGag(self, av, track):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.MaxGagAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, track):
                    av.addAchievement(achievementId)
					
    def zone(self, av, zone):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.ZoneAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, zone):
                    av.addAchievement(achievementId)
					
    def cogs(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.CogAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def fish(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.FishAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def vp(self, av, solo = 0):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.VPAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, solo):
                    av.addAchievement(achievementId)
					
    def cfo(self, av, solo = 0):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.CFOAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, solo):
                    av.addAchievement(achievementId)
					
    def cj(self, av, solo = 0):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.CJAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, solo):
                    av.addAchievement(achievementId)
					
    def ceo(self, av, solo = 0):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.CEOAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, solo):
                    av.addAchievement(achievementId)
					
    def disguise(self, av, dept):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.DisguiseAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av, dept):
                    av.addAchievement(achievementId)

    def bldg(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.BuildingAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def factory(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.FactoryAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def mint(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.MintAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def stage(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.StageAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def club(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.ClubAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
					
    def bdo(self, av):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.BoardOfficeAchievement)
		
        for achievementId in possibleAchievements:
            if not achievementId in av.getAchievements():
                if Achievements.AchievementsDict[achievementId].hasComplete(av):
                    av.addAchievement(achievementId)
