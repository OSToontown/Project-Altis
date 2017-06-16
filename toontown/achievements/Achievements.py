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

    def hasComplete(self, av, items):
        items = av.getStat(ToontownGlobals.STATS_CATALOG)
        if items >= self.neededItems:
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
			
class MaxGagAchievement:

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
			
class CogAchievement:

    def __init__(self, cogs):
        self.neededCogs = cogs
		
    def hasComplete(self, av):
        cogs = av.getStat(ToontownGlobals.STATS_COGS)
        if cogs >= self.neededCogs:
            return 1
        else:
            return 0
			
class FishAchievement:

    def __init__(self, fish):
        self.neededFish = fish
		
    def hasComplete(self, av):
        fish = av.getStat(ToontownGlobals.STATS_FISH)
        if fish >= self.neededFish:
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
                    ZoneAchievement(zone = 19000),
                    CogAchievement(cogs = 1),
                    CogAchievement(cogs = 10),
                    CogAchievement(cogs = 100),
                    CogAchievement(cogs = 1000),
                    CogAchievement(cogs = 10000),
                    CogAchievement(cogs = 100000),
                    CogAchievement(cogs = 1000000),
                    FishAchievement(fish = 1),
                    FishAchievement(fish = 10),
                    FishAchievement(fish = 100),
                    FishAchievement(fish = 1000),
                    FishAchievement(fish = 10000),
                    MaxGagAchievement(track = 0),
                    MaxGagAchievement(track = 1),
                    MaxGagAchievement(track = 2),
                    MaxGagAchievement(track = 3),
                    MaxGagAchievement(track = 4),
                    MaxGagAchievement(track = 5),
                    MaxGagAchievement(track = 6),
                    MaxGagAchievement(track = 7))

type2AchievementIds = {FriendAchievement: [0, 1, 2],
                       CatalogAchievement: [3, 4, 5, 6],
                       TrolleyAchievement: [7],
                       LoopysBallsAchievement: [8],
                       VPAchievement: [9, 10],
                       DisguiseAchievement: [11],
                       GagTrackAchievement: [12, 13, 14, 15, 16, 17],
                       ZoneAchievement: [18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
                       CogAchievement: [30, 31, 32, 33, 34, 35, 36],
                       FishAchievement: [37, 38, 39, 40, 41],
                       MaxGagAchievement: [42, 43, 44, 45, 46, 47, 48, 49]}

def getAchievementsOfType(type):
    return type2AchievementIds.get(type)
