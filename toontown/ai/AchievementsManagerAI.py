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
					
    def gagTrack(self, av, track):
        av = self.air.doId2do.get(av)
        possibleAchievements = Achievements.getAchievementsOfType(Achievements.GagTrackAchievement)
		
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
