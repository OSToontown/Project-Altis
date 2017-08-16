from toontown.toonbase import ToontownGlobals
from toontown.suit import SuitDNA

CAT_FRIENDS = 0
CAT_CATALOG = 1
CAT_TROLLEY = 2
CAT_COGS = 3
CAT_GAGS = 4
CAT_FISHING = 5
CAT_VISIT = 6
CAT_SPECIAL = 7

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

    def __init__(self, times):
        self.neededTimes = times

    def hasComplete(self, av):
        times = av.getStat(ToontownGlobals.STATS_TROLLEY)
        if times >= self.neededTimes:
            return 1
        else:
            return 0

class LoopysBallsAchievement:

    def hasComplete(self, av):
        return 1
		
class SofieSquirtAchievement:

    def hasComplete(self, av):
        return 1
		
class ResistanceAchievement:

    def hasComplete(self, av):
        return 1
		
class DoodleAchievement:

    def hasComplete(self, av):
        return 1

class VPAchievement:

    def __init__(self, times, solo = 0):
        self.neededTimes = times
        self.isSolo = solo

    def hasComplete(self, av, solo = 0):
        times = av.getStat(ToontownGlobals.STATS_VP)
        if self.isSolo:
            if solo:
                return 1
            else:
                return 0
        if times >= self.neededTimes:
            return 1
        else:
            return 0

class CFOAchievement:

    def __init__(self, times, solo = 0):
        self.neededTimes = times
        self.isSolo = solo

    def hasComplete(self, av, solo = 0):
        times = av.getStat(ToontownGlobals.STATS_CFO)
        if self.isSolo:
            if solo:
                return 1
            else:
                return 0
        if times >= self.neededTimes:
            return 1
        else:
            return 0

class CJAchievement:

    def __init__(self, times, solo = 0):
        self.neededTimes = times
        self.isSolo = solo

    def hasComplete(self, av, solo = 0):
        times = av.getStat(ToontownGlobals.STATS_CJ)
        if self.isSolo:
            if solo:
                return 1
            else:
                return 0
        if times >= self.neededTimes:
            return 1
        else:
            return 0

class CEOAchievement:

    def __init__(self, times, solo = 0):
        self.neededTimes = times
        self.isSolo = solo

    def hasComplete(self, av, solo = 0):
        times = av.getStat(ToontownGlobals.STATS_CEO)
        if self.isSolo:
            if solo:
                return 1
            else:
                return 0
        if times >= self.neededTimes:
            return 1
        else:
            return 0
			
class CMAchievement:

    def __init__(self, times, solo = 0):
        self.neededTimes = times
        self.isSolo = solo

    def hasComplete(self, av, solo = 0):
        times = av.getStat(ToontownGlobals.STATS_CM)
        if self.isSolo:
            if solo:
                return 1
            else:
                return 0
        if times >= self.neededTimes:
            return 1
        else:
            return 0

class DisguiseAchievement:
    def __init__(self, dept):
        self.neededDept = dept

    def hasComplete(self, av, dept):
        if dept == self.neededDept:
            if av.cogLevels[SuitDNA.suitDepts.index(dept)] >= 49:
                return 1
            else:
                return 0
        else:
            return 0
		
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
			
class BuildingAchievement:

    def __init__(self, bldgs):
        self.neededBuildings = bldgs
		
    def hasComplete(self, av):
        bldgs = av.getStat(ToontownGlobals.STATS_BLDGS)
        if bldgs >= self.neededBuildings:
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
			
class FactoryAchievement:

    def __init__(self, facilities):
        self.neededFacilities = facilities
		
    def hasComplete(self, av):
        facilities = av.getStat(ToontownGlobals.STATS_FACTORIES)
        if facilities >= self.neededFacilities:
            return 1
        else:
            return 0
			
class MintAchievement:

    def __init__(self, facilities):
        self.neededFacilities = facilities
		
    def hasComplete(self, av):
        facilities = av.getStat(ToontownGlobals.STATS_MINTS)
        if facilities >= self.neededFacilities:
            return 1
        else:
            return 0

class StageAchievement:

    def __init__(self, facilities):
        self.neededFacilities = facilities
		
    def hasComplete(self, av):
        facilities = av.getStat(ToontownGlobals.STATS_STAGES)
        if facilities >= self.neededFacilities:
            return 1
        else:
            return 0

class ClubAchievement:

    def __init__(self, facilities):
        self.neededFacilities = facilities
		
    def hasComplete(self, av):
        facilities = av.getStat(ToontownGlobals.STATS_CLUBS)
        if facilities >= self.neededFacilities:
            return 1
        else:
            return 0

class BoardOfficeAchievement:

    def __init__(self, facilities):
        self.neededFacilities = facilities
		
    def hasComplete(self, av):
        facilities = av.getStat(ToontownGlobals.STATS_BOARD_OFFICES)
        if facilities >= self.neededFacilities:
            return 1
        else:
            return 0
			
# WORD OF CAUTION: After release DO NOT add in achievements into the middle of the dictionary, ONLY append

AchievementsDict = (FriendAchievement(neededFriends = 1),
                    FriendAchievement(neededFriends = 10),
                    FriendAchievement(neededFriends = 50),
                    CatalogAchievement(items = 1),
                    CatalogAchievement(items = 10),
                    CatalogAchievement(items = 50),
                    CatalogAchievement(items = 100),
                    TrolleyAchievement(times = 1),
                    LoopysBallsAchievement(),
                    VPAchievement(times = 1),
                    VPAchievement(times = 10),
                    CFOAchievement(times = 1),
                    CFOAchievement(times = 10),
                    CJAchievement(times = 1),
                    CJAchievement(times = 10),
                    CEOAchievement(times = 1),
                    CEOAchievement(times = 10),
                    CMAchievement(times = 1),
                    CMAchievement(times = 10),
                    DisguiseAchievement(dept = 's'),
                    DisguiseAchievement(dept = 'm'),
                    DisguiseAchievement(dept = 'l'),
                    DisguiseAchievement(dept = 'c'),
                    DisguiseAchievement(dept = 'g'),
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
                    MaxGagAchievement(track = 7),
                    SofieSquirtAchievement(),
                    DoodleAchievement(),
                    ResistanceAchievement(),
                    TrolleyAchievement(times=10),
                    TrolleyAchievement(times=50),
                    TrolleyAchievement(times=100),
                    VPAchievement(times=1, solo=1),
                    CFOAchievement(times=1, solo=1),
                    CJAchievement(times=1, solo=1),
                    CEOAchievement(times=1, solo=1),
                    CMAchievement(times=1, solo=1),
                    BuildingAchievement(bldgs = 1),
                    BuildingAchievement(bldgs = 10),
                    BuildingAchievement(bldgs = 50),
                    BuildingAchievement(bldgs = 100),
                    BuildingAchievement(bldgs = 250),
                    FactoryAchievement(facilities = 1),
                    FactoryAchievement(facilities = 10),
                    FactoryAchievement(facilities = 50),
                    MintAchievement(facilities = 1),
                    MintAchievement(facilities = 10),
                    MintAchievement(facilities = 50),
                    StageAchievement(facilities = 1),
                    StageAchievement(facilities = 10),
                    StageAchievement(facilities = 50),
                    ClubAchievement(facilities = 1),
                    ClubAchievement(facilities = 10),
                    ClubAchievement(facilities = 50),
                    BoardOfficeAchievement(facilities = 1),
                    BoardOfficeAchievement(facilities = 10),
                    BoardOfficeAchievement(facilities = 50))

type2AchievementIds = {FriendAchievement: [0, 1, 2],
                       CatalogAchievement: [3, 4, 5, 6],
                       TrolleyAchievement: [7, 65, 66, 67],
                       LoopysBallsAchievement: [8],
                       VPAchievement: [9, 10, 68],
                       CFOAchievement: [11, 12, 69],
                       CJAchievement: [13, 14, 70],
                       CEOAchievement: [15, 16, 71],
                       CMAchievement: [17, 18, 72],
                       DisguiseAchievement: [19, 20, 21, 22, 23],
                       GagTrackAchievement: [24, 25, 26, 27, 28, 29],
                       ZoneAchievement: [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41],
                       CogAchievement: [42, 43, 44, 45, 46, 47, 48],
                       FishAchievement: [49, 50, 51, 52, 53],
                       MaxGagAchievement: [54, 55, 56, 57, 58, 59, 60, 61],
                       SofieSquirtAchievement: [62],
                       DoodleAchievement: [63],
                       ResistanceAchievement: [64],
                       BuildingAchievement: [73, 74, 75, 76, 77],
                       FactoryAchievement: [78, 79, 80],
                       MintAchievement: [81, 82, 83],
                       StageAchievement: [84, 85, 86],
                       ClubAchievement: [87, 88, 89],
                       BoardOfficeAchievement: [90, 91, 92]}
					   
type2Category = {FriendAchievement: CAT_FRIENDS,
                 CatalogAchievement: CAT_CATALOG,
                 TrolleyAchievement: CAT_TROLLEY,
                 LoopysBallsAchievement: CAT_SPECIAL,
                 VPAchievement: CAT_COGS,
                 CFOAchievement: CAT_COGS,
                 CJAchievement: CAT_COGS,
                 CEOAchievement: CAT_COGS,
                 CMAchievement: CAT_COGS,
                 DisguiseAchievement: CAT_COGS,
                 GagTrackAchievement: CAT_GAGS,
                 ZoneAchievement: CAT_VISIT,
                 CogAchievement: CAT_COGS,
                 FishAchievement: CAT_FISHING,
                 MaxGagAchievement: CAT_GAGS,
                 SofieSquirtAchievement: CAT_SPECIAL,
                 DoodleAchievement: CAT_FRIENDS,
                 ResistanceAchievement: CAT_SPECIAL,
                 BuildingAchievement: CAT_COGS,
                 FactoryAchievement: CAT_COGS,
                 MintAchievement: CAT_COGS,
                 StageAchievement: CAT_COGS,
                 ClubAchievement: CAT_COGS,
                 BoardOfficeAchievement: CAT_COGS}

def getAchievementsOfType(type):
    return type2AchievementIds.get(type)
