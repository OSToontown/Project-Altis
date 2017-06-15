from toontown.toonbase import ToontownGlobals


class FriendAchievement:

    def __init__(self, neededFriends = 1):
        self.neededFriends = neededFriends

    def hasComplete(self, av):
        avatarsFriends = av.getFriendsList()

        if len(avatarsFriends) >= self.neededFriends:
            return 1

        return 0

class CatalogAchievement:
    def __init__(self, items):
        self.neededItems = items

    def hasComplete(self, av, times):
        items = av.getStat(ToontownGlobals.STATS_CATALOG)
        if items == self.neededItems:
            return 1
        return 0

class TrolleyAchievement:

    def hasComplete(self, av):
        return 1

class LoopysBallsAchievement:

    def hasComplete(self, av):
        return 1

class VPAchievement:

    def __init__(self, times):
        pass

    def hasComplete(self, times):
        return 1

class CFOAchievement:

    def __init__(self, times):
        pass

    def hasComplete(self, times):
        return 1

class CJAchievement:

    def __init__(self, times):
        pass

    def hasComplete(self, times):
        return 1

class CEOAchievement:

    def __init__(self, times):
        pass

    def hasComplete(self, times):
        return 1

class DisguiseAchievement:
    def __init__(self, dept):
        pass

    def hasComplete(self, dept):
        return 1
		
class GagTrackAchievement:

    def hasComplete(self, track):
        return 1

AchievementsDict = (FriendAchievement(neededFriends = 1),
                    FriendAchievement(neededFriends = 10),
                    FriendAchievement(neededFriends = 50),
                    CatalogAchievement(items = 1),
                    CatalogAchievement(items = 10),
                    CatalogAchievement(items = 50),
                    CatalogAchievement(items = 100),
                    TrolleyAchievement(),
                    LoopysBallsAchievement(),
                    VPAchievement(times = 1),
                    VPAchievement(times = 10),
                    DisguiseAchievement(dept = 's'),
                    GagTrackAchievement(track = 0),
                    GagTrackAchievement(track = 1),
                    GagTrackAchievement(track = 2),
                    GagTrackAchievement(track = 3),
                    GagTrackAchievement(track = 6),
                    GagTrackAchievement(track = 7))

type2AchievementIds = {FriendAchievement: [0, 1, 2],
                       CatalogAchievement: [3, 4, 5, 6],
                       TrolleyAchievement: [7],
                       LoopysBallsAchievement: [8],
                       VPAchievement: [9, 10],
                       DisguiseAchievement: [11],
                       GagTrackAchievement: [12, 13, 14, 15, 16, 17]}

def getAchievementsOfType(type):
    return type2AchievementIds.get(type)
