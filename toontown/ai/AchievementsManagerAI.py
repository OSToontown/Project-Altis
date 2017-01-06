from toontown.achievements import Achievements

class AchievementsManagerAI():
    def __init__(self, air):
        self.air = air

    def friends(self, avId):
        av = self.air.doId2do.get(avId)
        if not av:
            return

        pass
    
    def rideTrolley(self, av):
        pass