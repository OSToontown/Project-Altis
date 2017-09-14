from toontown.building.ElevatorConstants import *
from toontown.toonbase import ToontownGlobals

try:
    config = base.config
except:
    config = simbase.config
	
SUIT_BLDG_INFO_FLOORS = 0
SUIT_BLDG_INFO_SUIT_LVLS = 1
SUIT_BLDG_INFO_BOSS_LVLS = 2
SUIT_BLDG_INFO_LVL_POOL = 3
SUIT_BLDG_INFO_LVL_POOL_MULTS = 4
SUIT_BLDG_INFO_REVIVES = 5
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8

SUIT_PLANNER_VP = 10
SUIT_PLANNER_VP_SKELECOGS = 11
SUIT_PLANNER_NERFED_VP = 16
SUIT_PLANNER_NERFED_VP_SKELECOGS = 17
SUIT_PLANNER_CFO = 12
SUIT_PLANNER_CFO_SKELECOGS = 13
SUIT_PLANNER_CJ = 14
SUIT_PLANNER_CEO = 15
SUIT_PLANNER_CEO_DINERS = 18
SUIT_PLANNER_CM = 19
SUIT_PLANNER_CM_SKELECOGS = 20
SUIT_PLANNER_VP_EASY = 21
SUIT_PLANNER_VP_SKELECOGS_EASY = 22
SUIT_PLANNER_VP_HARD = 23
SUIT_PLANNER_VP_SKELECOGS_HARD = 24

SuitBuildingInfo = (((1, 1), (1, 3), (4, 4), (8, 10), (1,)), # Buildings
 ((1, 2), (2, 4), (5, 5), (10, 11), (1, 1.2)), # Buildings
 ((1, 3), (3, 5), (6, 6), (12, 13), (1, 1.3, 1.6)), # Buildings
 ((2, 3), (4, 6), (7, 7), (14, 15), (1, 1.4, 1.8)), # Buildings
 ((2, 4), (5, 7), (8, 8), (16, 17), (1, 1.6, 1.8, 2)), # Buildings
 ((3, 4), (6, 8), (9, 9), (17, 18), (1, 1.6, 2, 2.4)), # Buildings
 ((3, 5), (7, 9),(10, 10), (18, 19), (1, 1.6, 1.8, 2.2, 2.4)), # Buildings
 ((4, 5), (8, 10), (11, 11), (18, 19), (1, 1.8, 2.4, 3, 3.2)), # Buildings
 ((5, 6), (9, 11), (12, 12), (20, 22), (1.4, 1.8, 2.6, 3.4, 4, 4.8)), # Buildings
 ((6, 6), (8, 13), (14, 14), (22, 26), (1.8, 2.6, 3.4, 4, 4.8, 5.6)), # Buildings
 ((1, 1), (5, 13), (13, 13), (100, 100), (1, 1, 1, 1, 1)), # VP Round 1
 ((1, 1), (8, 13), (13, 13), (150, 150), (1, 1, 1, 1, 1)), # VP Round 2
 ((1, 1), (5, 14), (14, 14), (150, 150), (1, 1, 1, 1, 1)), # CFO Round 1 Cogs
 ((1, 1), (8, 14), (14, 14), (200, 200), (1, 1, 1, 1, 1)), # CFO Round 1 Skelecogs
 ((1, 1), (5, 16), (16, 16), (300, 300), (1, 1, 1, 1, 1)), # CJ Round 1 Cogs
 ((1, 1), (5, 18), (18, 18), (290, 290), (1, 1, 1, 1, 1)), # CEO Round 1 Cogs
 ((1, 1), (1, 5), (5, 5), (33, 33), (1, 1, 1, 1, 1)), # Storm Sellbot VP Round 1
 ((1, 1), (4, 7), (5, 5), (50, 50), (1, 1, 1, 1, 1)), # Storm Sellbot VP Round 2
 ((1, 1), (10, 12), (12, 12), (206, 206), (1, 1, 1, 1, 1), (1,)), # CEO Diner Cogs (Only uses level range and revives flag, cogs are decided based on tables served)
 ((1, 1), (5, 20), (20, 20), (206, 206), (1, 1, 1, 1, 1), (1,)), # Chairman Cogs
 ((1, 1), (10, 20), (20, 20), (206, 206), (1, 1, 1, 1, 1)), # Chairman Skelecogs
 ((1, 1), (5, 12), (12, 12), (100, 100), (1, 1, 1, 1, 1)), # VP Round 1 Easy
 ((1, 1), (8, 12), (12, 12), (150, 150), (1, 1, 1, 1, 1)), # VP Round 2 Easy
 ((1, 1), (5, 14), (14, 14), (100, 100), (1, 1, 1, 1, 1)), # VP Round 1 Hard
 ((1, 1), (8, 14), (14, 14), (150, 150), (1, 1, 1, 1, 1))) # VP Round 2 Hard

buildingMinMax = {
    ToontownGlobals.ToontownCentralOld: (0, 0),
    ToontownGlobals.SillyStreet: (config.GetInt('silly-street-building-min', 0),
                                  config.GetInt('silly-street-building-max', 3)),
    ToontownGlobals.LoopyLane: (config.GetInt('loopy-lane-building-min', 0),
                                config.GetInt('loopy-lane-building-max', 3)),
    ToontownGlobals.PunchlinePlace: (config.GetInt('punchline-place-building-min', 0),
                                     config.GetInt('punchline-place-building-max', 3)),
    ToontownGlobals.WackyWay: (config.GetInt('wacky-way-building-min', 0),
                                     config.GetInt('wacky-way-building-max', 3)),
    ToontownGlobals.BarnacleBoulevard: (config.GetInt('barnacle-boulevard-building-min', 1),
                                        config.GetInt('barnacle-boulevard-building-max', 5)),
    ToontownGlobals.SeaweedStreet: (config.GetInt('seaweed-street-building-min', 1),
                                    config.GetInt('seaweed-street-building-max', 5)),
    ToontownGlobals.LighthouseLane: (config.GetInt('lighthouse-lane-building-min', 1),
                                     config.GetInt('lighthouse-lane-building-max', 5)),
    ToontownGlobals.AhoyAvenue: (config.GetInt('ahoy-avenue-building-min', 1),
                                   config.GetInt('ahoy-avenue-building-max', 5)),
    ToontownGlobals.ElmStreet: (config.GetInt('elm-street-building-min', 2),
                                config.GetInt('elm-street-building-max', 6)),
    ToontownGlobals.MapleStreet: (config.GetInt('maple-street-building-min', 2),
                                  config.GetInt('maple-street-building-max', 6)),
    ToontownGlobals.RoseValley: (config.GetInt('rose-valley-building-min', 0),
                                  config.GetInt('rose-valley-building-max', 0)),
    ToontownGlobals.OakStreet: (config.GetInt('oak-street-building-min', 2),
                                config.GetInt('oak-street-building-max', 6)),
    ToontownGlobals.RoseValley: (config.GetInt('rose-valley-building-min', 2),
                                config.GetInt('rose-valley-building-max', 6)),
    ToontownGlobals.AcornAvenue: (config.GetInt('acorn-avenue-building-min', 3),
                                  config.GetInt('acorn-avenue-building-max', 7)),
    ToontownGlobals.PeanutPlace: (config.GetInt('peanut-place-building-min', 3),
                                  config.GetInt('peanut-place-building-max', 7)),
    ToontownGlobals.WalnutWay: (config.GetInt('walnut-way-building-min', 6),
                                  config.GetInt('walnut-way-building-max', 12)),
    ToontownGlobals.LegumeLane: (config.GetInt('legume-lane-building-min', 3),
                                  config.GetInt('legume-lane-building-max', 6)),
    ToontownGlobals.AltoAvenue: (config.GetInt('alto-avenue-building-min', 3),
                                 config.GetInt('alto-avenue-building-max', 7)),
    ToontownGlobals.BaritoneBoulevard: (config.GetInt('baritone-boulevard-building-min', 3),
                                        config.GetInt('baritone-boulevard-building-max', 7)),
    ToontownGlobals.TenorTerrace: (config.GetInt('tenor-terrace-building-min', 3),
                                   config.GetInt('tenor-terrace-building-max', 7)),
    ToontownGlobals.SopranoStreet: (config.GetInt('soprano-street-building-min', 6),
                                   config.GetInt('soprano-street-building-max', 12)),
    ToontownGlobals.WalrusWay: (config.GetInt('walrus-way-building-min', 5),
                                config.GetInt('walrus-way-building-max', 10)),
    ToontownGlobals.SleetStreet: (config.GetInt('sleet-street-building-min', 5),
                                  config.GetInt('sleet-street-building-max', 10)),
    ToontownGlobals.PolarPlace: (config.GetInt('polar-place-building-min', 5),
                                 config.GetInt('polar-place-building-max', 10)),
    ToontownGlobals.ArcticAvenue: (config.GetInt('arctic-avenue-building-min', 5),
                                 config.GetInt('arctic-avenue-building-max', 10)),
    ToontownGlobals.LullabyLane: (config.GetInt('lullaby-lane-building-min', 6),
                                  config.GetInt('lullaby-lane-building-max', 12)),
    ToontownGlobals.PajamaPlace: (config.GetInt('pajama-place-building-min', 6),
                                  config.GetInt('pajama-place-building-max', 12)),
    ToontownGlobals.TwilightTerrace: (config.GetInt('twilight-terrace-building-min', 6),
                                  config.GetInt('twilight-terrace-building-max', 12)),
    ToontownGlobals.SellbotHQ: (0, 0),
    ToontownGlobals.SellbotFactoryExt: (0, 0),
    ToontownGlobals.CashbotHQ: (0, 0),
    ToontownGlobals.LawbotHQ: (0, 0),
    ToontownGlobals.BossbotHQ: (0, 0),
    ToontownGlobals.BoardbotHQ : (0, 0)
}

buildingChance = {
    ToontownGlobals.ToontownCentralOld: 0.0,
    ToontownGlobals.SillyStreet: config.GetFloat('silly-street-building-chance', 2.0),
    ToontownGlobals.LoopyLane: config.GetFloat('loopy-lane-building-chance', 2.0),
    ToontownGlobals.PunchlinePlace: config.GetFloat('punchline-place-building-chance', 2.0),
    ToontownGlobals.WackyWay: config.GetFloat('wacky-way-building-chance', 10.0),
    ToontownGlobals.BarnacleBoulevard: config.GetFloat('barnacle-boulevard-building-chance', 75.0),
    ToontownGlobals.SeaweedStreet: config.GetFloat('seaweed-street-building-chance', 75.0),
    ToontownGlobals.LighthouseLane: config.GetFloat('lighthouse-lane-building-chance', 75.0),
    ToontownGlobals.AhoyAvenue: config.GetFloat('ahoy-avenue-building-chance', 50.0),
    ToontownGlobals.ElmStreet: config.GetFloat('elm-street-building-chance', 90.0),
    ToontownGlobals.MapleStreet: config.GetFloat('maple-street-building-chance', 90.0),
    ToontownGlobals.MapleStreet: config.GetFloat('rose-valley-building-chance', 0.0),
    ToontownGlobals.OakStreet: config.GetFloat('oak-street-building-chance', 90.0),
    ToontownGlobals.RoseValley: config.GetFloat('rose-valley-building-chance', 90.0),
    ToontownGlobals.AcornAvenue: config.GetFloat('acorn-avenue-building-chance', 75.0),
    ToontownGlobals.PeanutPlace: config.GetFloat('peanut-place-building-chance', 75.0),
    ToontownGlobals.WalnutWay: config.GetFloat('walnut-way-building-chance', 95.0),
    ToontownGlobals.LegumeLane: config.GetFloat('legume-lane-building-chance', 50.0),
    ToontownGlobals.AltoAvenue: config.GetFloat('alto-avenue-building-chance', 95.0),
    ToontownGlobals.BaritoneBoulevard: config.GetFloat('baritone-boulevard-building-chance', 95.0),
    ToontownGlobals.TenorTerrace: config.GetFloat('tenor-terrace-building-chance', 95.0),
    ToontownGlobals.SopranoStreet: config.GetFloat('soprano-street-building-chance', 95.0),
    ToontownGlobals.WalrusWay: config.GetFloat('walrus-way-building-chance', 100.0),
    ToontownGlobals.SleetStreet: config.GetFloat('sleet-street-building-chance', 100.0),
    ToontownGlobals.PolarPlace: config.GetFloat('polar-place-building-chance', 100.0),
    ToontownGlobals.ArcticAvenue: config.GetFloat('arctic-avenue-building-chance', 100.0),
    ToontownGlobals.LullabyLane: config.GetFloat('lullaby-lane-building-chance', 100.0),
    ToontownGlobals.PajamaPlace: config.GetFloat('pajama-place-building-chance', 100.0),
    ToontownGlobals.TwilightTerrace: config.GetFloat('twilight-terrace-building-chance', 100.0),
    ToontownGlobals.SellbotHQ: 0.0,
    ToontownGlobals.SellbotFactoryExt: 0.0,
    ToontownGlobals.CashbotHQ: 0.0,
    ToontownGlobals.LawbotHQ: 0.0,
    ToontownGlobals.BossbotHQ: 0.0,
    ToontownGlobals.BoardbotHQ: 0.0
}
