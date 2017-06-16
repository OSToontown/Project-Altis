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

    def __init__(self, track):
        self.neededTrack = track

    def hasComplete(self, av, track):
        if track == self.neededTrack:
            return 1
        else:
            return 0
		
class ZoneAchievement:

    def __init__(self, zone):
        self.neededZone = zone

    def hasComplete(self, av, zone):
        if zone == self.neededZone:
            return 1
        else:
            return 0

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
                    GagTrackAchievement(track = 7),
                    ZoneAchievement(zone = 1000),
                    ZoneAchievement(zone = 3000),
                    ZoneAchievement(zone = 4000),
                    ZoneAchievement(zone = 5000),
                    ZoneAchievement(zone = 6000),
                    ZoneAchievement(zone = 8000),
                    ZoneAchievement(zone = 9000),
                    ZoneAchievement(zone = 10000),
                    ZoneAchievement(zone = 11000),
                    ZoneAchievement(zone = 12000),
                    ZoneAchievement(zone = 13000),
                    ZoneAchievement(zone = 19000))

type2AchievementIds = {FriendAchievement: [0, 1, 2],
                       CatalogAchievement: [3, 4, 5, 6],
                       TrolleyAchievement: [7],
                       LoopysBallsAchievement: [8],
                       VPAchievement: [9, 10],
                       DisguiseAchievement: [11],
                       GagTrackAchievement: [12, 13, 14, 15, 16, 17],
                       ZoneAchievement: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]}

def getAchievementsOfType(type):
    return type2AchievementIds.get(type)
