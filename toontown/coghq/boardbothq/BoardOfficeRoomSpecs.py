from toontown.toonbase.ToonPythonUtil import invertDict
from toontown.toonbase import ToontownGlobals
from toontown.coghq import NullCogs
from toontown.coghq.boardbothq import BoardOfficeBoilerRoom_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeBoilerRoom_Battle01_Cogs
from toontown.coghq.boardbothq import BoardOfficeControlRoom_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeDuctRoom_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeDuctRoom_Battle01_Cogs
from toontown.coghq.boardbothq import BoardOfficeGearRoom_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeGearRoom_Battle01_Cogs
from toontown.coghq.boardbothq import BoardOfficeLavaRoomFoyer_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeLavaRoomFoyer_Battle01_Cogs
from toontown.coghq.boardbothq import BoardOfficeLobby_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeLobby_Battle01_Cogs
from toontown.coghq.boardbothq import BoardOfficeOilRoom_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficePaintMixerReward_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficePipeRoom_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficePipeRoom_Battle01_Cogs
from toontown.coghq.boardbothq import BoardOfficePaintMixer_Battle00
from toontown.coghq.boardbothq import BoardOfficePaintMixer_Battle00_Cogs
from toontown.coghq.boardbothq import BoardOfficeStomperAlley_Action01

# Explicit imports for the below room modules:
from toontown.coghq.boardbothq import BoardOfficeEntrance_Action00
from toontown.coghq.boardbothq import BoardOfficeBoilerRoom_Action00
from toontown.coghq.boardbothq import BoardOfficeBoilerRoom_Battle00
from toontown.coghq.boardbothq import BoardOfficeDuctRoom_Action00
from toontown.coghq.boardbothq import BoardOfficeDuctRoom_Battle00
from toontown.coghq.boardbothq import BoardOfficeGearRoom_Action00
from toontown.coghq.boardbothq import BoardOfficeGearRoom_Battle00
from toontown.coghq.boardbothq import BoardOfficeLavaRoomFoyer_Action00
from toontown.coghq.boardbothq import BoardOfficeLavaRoomFoyer_Action01
from toontown.coghq.boardbothq import BoardOfficeLavaRoomFoyer_Battle00
from toontown.coghq.boardbothq import BoardOfficeLavaRoom_Action00
from toontown.coghq.boardbothq import BoardOfficeLobby_Action00
from toontown.coghq.boardbothq import BoardOfficeLobby_Battle00
from toontown.coghq.boardbothq import BoardOfficePaintMixer_Action00
from toontown.coghq.boardbothq import BoardOfficePipeRoom_Action00
from toontown.coghq.boardbothq import BoardOfficePipeRoom_Battle00
from toontown.coghq.boardbothq import BoardOfficeStomperAlley_Action00
from toontown.coghq.boardbothq import BoardOfficeBoilerRoom_Battle01
from toontown.coghq.boardbothq import BoardOfficeControlRoom_Battle00
from toontown.coghq.boardbothq import BoardOfficeDuctRoom_Battle01
from toontown.coghq.boardbothq import BoardOfficeGearRoom_Battle01
from toontown.coghq.boardbothq import BoardOfficeLavaRoomFoyer_Battle01
from toontown.coghq.boardbothq import BoardOfficeOilRoom_Battle00
from toontown.coghq.boardbothq import BoardOfficeLobby_Battle01
from toontown.coghq.boardbothq import BoardOfficePaintMixerReward_Battle00
from toontown.coghq.boardbothq import BoardOfficePipeRoom_Battle01

def getBoardOfficeRoomSpecModule(roomId):
    return BoardOfficeSpecModules[roomId]


def getCogSpecModule(roomId):
    roomName = BoardOfficeRoomId2RoomName[roomId]
    return CogSpecModules.get(roomName, NullCogs)


def getNumBattles(roomId):
    return roomId2numBattles[roomId]


BoardOfficeRoomId2RoomName = {0: 'BoardOfficeEntrance_Action00',
 1: 'BoardOfficeBoilerRoom_Action00',
 2: 'BoardOfficeBoilerRoom_Battle00',
 3: 'BoardOfficeDuctRoom_Action00',
 4: 'BoardOfficeDuctRoom_Battle00',
 5: 'BoardOfficeGearRoom_Action00',
 6: 'BoardOfficeGearRoom_Battle00',
 7: 'BoardOfficeLavaRoomFoyer_Action00',
 8: 'BoardOfficeLavaRoomFoyer_Action01',
 9: 'BoardOfficeLavaRoomFoyer_Battle00',
 10: 'BoardOfficeLavaRoom_Action00',
 11: 'BoardOfficeLobby_Action00',
 12: 'BoardOfficeLobby_Battle00',
 13: 'BoardOfficePaintMixer_Action00',
 14: 'BoardOfficePaintMixer_Battle00',
 15: 'BoardOfficePipeRoom_Action00',
 16: 'BoardOfficePipeRoom_Battle00',
 17: 'BoardOfficeStomperAlley_Action00',
 18: 'BoardOfficeStomperAlley_Action01',
 19: 'BoardOfficeBoilerRoom_Battle01',
 20: 'BoardOfficeControlRoom_Battle00',
 21: 'BoardOfficeDuctRoom_Battle01',
 22: 'BoardOfficeGearRoom_Battle01',
 23: 'BoardOfficeLavaRoomFoyer_Battle01',
 24: 'BoardOfficeOilRoom_Battle00',
 25: 'BoardOfficeLobby_Battle01',
 26: 'BoardOfficePaintMixerReward_Battle00',
 27: 'BoardOfficePipeRoom_Battle01'}
BoardOfficeRoomName2RoomId = invertDict(BoardOfficeRoomId2RoomName)
BoardOfficeEntranceIDs = (0,)
BoardOfficeMiddleRoomIDs = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18)
BoardOfficeFinalRoomIDs = (19, 20, 21, 22, 23, 24, 25, 26, 27)
BoardOfficeConnectorRooms = ('phase_14/models/boardbotHQ/BD_connector_7cubeL2', 'phase_14/models/boardbotHQ/BD_connector_7cubeLR')
BoardOfficeSpecModules = {}
for roomName, roomId in BoardOfficeRoomName2RoomId.items():
    BoardOfficeSpecModules[roomId] = locals()[roomName]

CogSpecModules = {'BoardOfficeBoilerRoom_Battle00': BoardOfficeBoilerRoom_Battle00_Cogs,
 'BoardOfficeBoilerRoom_Battle01': BoardOfficeBoilerRoom_Battle01_Cogs,
 'BoardOfficeControlRoom_Battle00': BoardOfficeControlRoom_Battle00_Cogs,
 'BoardOfficeDuctRoom_Battle00': BoardOfficeDuctRoom_Battle00_Cogs,
 'BoardOfficeDuctRoom_Battle01': BoardOfficeDuctRoom_Battle01_Cogs,
 'BoardOfficeGearRoom_Battle00': BoardOfficeGearRoom_Battle00_Cogs,
 'BoardOfficeGearRoom_Battle01': BoardOfficeGearRoom_Battle01_Cogs,
 'BoardOfficeLavaRoomFoyer_Battle00': BoardOfficeLavaRoomFoyer_Battle00_Cogs,
 'BoardOfficeLavaRoomFoyer_Battle01': BoardOfficeLavaRoomFoyer_Battle01_Cogs,
 'BoardOfficeLobby_Battle00': BoardOfficeLobby_Battle00_Cogs,
 'BoardOfficeLobby_Battle01': BoardOfficeLobby_Battle01_Cogs,
 'BoardOfficeOilRoom_Battle00': BoardOfficeOilRoom_Battle00_Cogs,
 'BoardOfficePaintMixer_Battle00': BoardOfficePaintMixer_Battle00_Cogs,
 'BoardOfficePaintMixerReward_Battle00': BoardOfficePaintMixerReward_Battle00_Cogs,
 'BoardOfficePipeRoom_Battle00': BoardOfficePipeRoom_Battle00_Cogs,
 'BoardOfficePipeRoom_Battle01': BoardOfficePipeRoom_Battle01_Cogs}
roomId2numBattles = {}
for roomName, roomId in BoardOfficeRoomName2RoomId.items():
    if roomName not in CogSpecModules:
        roomId2numBattles[roomId] = 0
    else:
        cogSpecModule = CogSpecModules[roomName]
        roomId2numBattles[roomId] = len(cogSpecModule.BattleCells)

name2id = BoardOfficeRoomName2RoomId
roomId2numBattles[name2id['BoardOfficeBoilerRoom_Battle00']] = 3
roomId2numBattles[name2id['BoardOfficePipeRoom_Battle00']] = 2
del name2id
middleRoomId2numBattles = {}
for roomId in BoardOfficeMiddleRoomIDs:
    middleRoomId2numBattles[roomId] = roomId2numBattles[roomId]
