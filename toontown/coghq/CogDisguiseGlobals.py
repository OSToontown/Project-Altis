from toontown.suit import SuitDNA
import types
from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToonPythonUtil as PythonUtil
from otp.otpbase import OTPGlobals
PartsPerSuit = (10,
 10,
 10,
 10,
 10)
PartsPerSuitBitmasks = (56411,
 56411,
 56411,
 56411,
 56411)
AllBits = 56411
MinPartLoss = 1
MaxPartLoss = 2
leftLegUpper = 1
leftLegLower = 2
leftLegFoot = 4
rightLegUpper = 8
rightLegLower = 16
rightLegFoot = 32
torsoLeftShoulder = 64
torsoRightShoulder = 128
torsoChest = 256
torsoHealthMeter = 512
torsoPelvis = 1024
leftArmUpper = 2048
leftArmLower = 4096
leftArmHand = 8192
rightArmUpper = 16384
rightArmLower = 32768
rightArmHand = 65536
upperTorso = torsoLeftShoulder
leftLegIndex = 0
rightLegIndex = 1
torsoIndex = 2
leftArmIndex = 3
rightArmIndex = 4
PartsQueryShifts = (leftLegUpper,
 rightLegUpper,
 torsoLeftShoulder,
 leftArmUpper,
 rightArmUpper)
PartsQueryMasks = (leftLegFoot + leftLegLower + leftLegUpper,
 rightLegFoot + rightLegLower + rightLegUpper,
 torsoPelvis + torsoHealthMeter + torsoChest + torsoRightShoulder + torsoLeftShoulder,
 leftArmHand + leftArmLower + leftArmUpper,
 rightArmHand + rightArmLower + rightArmUpper)
PartNameStrings = TTLocalizer.CogPartNames
SimplePartNameStrings = TTLocalizer.CogPartNamesSimple
PartsQueryNames = ({1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]},
 {1: PartNameStrings[0],
  2: PartNameStrings[1],
  4: PartNameStrings[1],
  8: PartNameStrings[3],
  16: PartNameStrings[4],
  32: PartNameStrings[4],
  64: SimplePartNameStrings[0],
  128: SimplePartNameStrings[0],
  256: SimplePartNameStrings[0],
  512: SimplePartNameStrings[0],
  1024: PartNameStrings[10],
  2048: PartNameStrings[11],
  4096: PartNameStrings[12],
  8192: PartNameStrings[12],
  16384: PartNameStrings[14],
  32768: PartNameStrings[15],
  65536: PartNameStrings[15]})
MeritsPerLevel = ((100, 130, 160, 190, 800), # Flunky
 (160, 210, 260, 310, 1300), # Pencil Pusher
 (260, 340, 420, 500, 2100), # Yesman
 (420, 550, 680, 810, 3400), # Micromanager
 (680, 890, 1100, 1310, 5500), # Downsizer
 (1100, 1440, 1780, 2120, 8900), # Head Hunter
 (1780, 2330, 2880, 3430, 14400), # Corporate Raider
 (2880, 3770, 4660, 5500, 23300, # The Big Cheese 8-12
  2880, 23300, # 13-14
  2880, 3770, 4660, 5500, 23300, # 15-19
  2880, 3770, 4660, 5500, 6440, 7330, 8220, 9110, 10000, 23300, # 20-29
  2880, 3770, 4660, 5500, 6440, 7330, 8220, 9110, 10000, 23300, # 30-39
  2880, 3770, 4660, 5500, 6440, 7330, 8220, 9110, 10000, 23300, 0), # 40-50
 (60, 80, 100, 120, 500), # Bottom Feeder
 (100, 130, 160, 190, 800), # Bloodsucker
 (160, 210, 260, 310, 1300), # Double Talker
 (260, 340, 420, 500, 2100), # Ambulance Chaser
 (420, 550, 680, 810, 3400), # Backstabber
 (680, 890, 1100, 1310, 5500), # Spin Doctor
 (1100, 1440, 1780, 2120, 8900), # Legal Eagle
 (1780, 2330, 2880, 3430, 14400, # Big Wig 8-12
  1780, 14400, # 13-14
  1780, 2330, 2880, 3430, 14400, # 15-19
  1780, 2330, 2880, 3430, 3980, 4530, 5080, 5630, 6180, 14400, # 20-29
  1780, 2330, 2880, 3430, 3980, 4530, 5080, 5630, 6180, 14400, # 30-39
  1780, 2330, 2880, 3430, 3980, 4530, 5080, 5630, 6180, 14400, 0), # 40-50
 (40, 50, 60, 70, 300), # Short Change
 (60, 80, 100, 120, 500), # Penny Pincher
 (100, 130, 160, 190, 800), # Tightwad
 (160, 210, 260, 310, 1300), # Bean Counter
 (260, 340, 420, 500, 2100), # Number Cruncher
 (420, 550, 680, 810, 3400), # Money Bags
 (680, 890, 1100, 1310, 5500), # Loan Shark
 (1100, 1440, 1780, 2120, 8900, # Robber Baron 8-12
  1100, 8900, # 13-14
  1100, 1440, 1780, 2120, 8900, # 15-19
  1100, 1440, 1780, 2120, 2460, 2800, 3140, 3480, 3820, 8900, # 20-29
  1100, 1440, 1780, 2120, 2460, 2800, 3140, 3480, 3820, 8900, # 30-39
  1100, 1440, 1780, 2120, 2460, 2800, 3140, 3480, 3820, 8900, 0), # 40-50
 (20, 30, 40, 50, 200), # Cold Caller
 (40, 50, 60, 70, 300), # Telemarketer
 (60, 80, 100, 120, 500), # Name Dropper
 (100, 130, 160, 190, 800), # Glad Hander
 (160, 210, 260, 310, 1300), # Mover and Shaker
 (260, 340, 420, 500, 2100), # Two-face
 (420, 550, 680, 810, 3400), # The Mingler
 (680, 890, 1100, 1310, 5500, # Mr. Hollywood 8-12
  680, 5500, # 13-14
  680, 890, 1100, 1310, 5500, # 15-19 
  680, 890, 1100, 1310, 1520, 1730, 1940, 2150, 2360, 5500, # 20-29
  680, 890, 1100, 1310, 1520, 1730, 1940, 2150, 2360, 5500, # 30-39
  680, 890, 1100, 1310, 1520, 1730, 1940, 2150, 2360, 5500, 0), # 40-50
 (160, 210, 260, 310, 1300), # Con Artist
 (260, 340, 420, 500, 2100), # Connoisseur
 (420, 550, 680, 810, 3400), # The Swindler
 (680, 890, 1100, 1310, 5500), # Middleman
 (1100, 1440, 1780, 2120, 8900), # Toxic Manager
 (1780, 2330, 2880, 34300, 14400), # Magnate
 (2880, 3770, 4660, 5500, 23300), # Big Fish
 (4660, 6100, 7540, 8930, 37700, # Head Honcho 8-12
  4660, 37700, # 13-14
  4660, 6100, 7540, 8930, 37700, # 15-19
  4660, 6100, 7540, 8930, 10420, 11860, 13300, 14740, 16180, 37700, # 20-29
  4660, 6100, 7540, 8930, 10420, 11860, 13300, 14740, 16180, 37700, # 30-39
  4660, 6100, 7540, 8930, 10420, 11860, 13300, 14740, 16180, 37700, 0)) # 40-50
suitTypes = PythonUtil.Enum(('NoSuit', 'NoMerits', 'FullSuit'))

def getNextPart(parts, partIndex, dept):
    dept = dept2deptIndex(dept)
    suitBitMask = PartsPerSuitBitmasks[dept] 
    queryMask = PartsQueryMasks[partIndex]
    needMask = queryMask & suitBitMask
    parts = parts[dept]
    haveMask = parts & queryMask
    nextPart = ~needMask | haveMask
    nextPart = nextPart ^ nextPart + 1
    nextPart = nextPart + 1 >> 1
    return nextPart


def getPartName(partArray):
    index = 0
    for part in partArray:
        if part:
            return PartsQueryNames[index][part]
        index += 1


def isSuitComplete(parts, dept):
    dept = dept2deptIndex(dept)
    for p in range(len(PartsQueryMasks)):
        if getNextPart(parts, p, dept):
            return 0

    return 1
    
def isPaidSuitComplete(av, parts, dept):
    isPaid = 0
    base = getBase()
    if av and av.getGameAccess() == OTPGlobals.AccessFull:
        isPaid = 1
    if isPaid:
        if isSuitComplete(parts, dept):
            return 1
    return 0


def getTotalMerits(toon, index):
    from toontown.battle import SuitBattleGlobals
    cogIndex = toon.cogTypes[index] + SuitDNA.suitsPerDept * index
    cogTypeStr = SuitDNA.suitHeadTypes[cogIndex]
    cogBaseLevel = SuitBattleGlobals.SuitAttributes[cogTypeStr]['level']
    cogLevel = toon.cogLevels[index] - cogBaseLevel
    cogLevel = max(min(cogLevel, len(MeritsPerLevel[cogIndex]) - 1), 0)
    return MeritsPerLevel[cogIndex][cogLevel]


def getTotalParts(bitString, shiftWidth = 40):
    sum = 0
    for shift in xrange(0, shiftWidth):
        sum = sum + (bitString >> shift & 1)

    return sum


def asBitstring(number):
    array = []
    shift = 0
    if number == 0:
        array.insert(0, '0')
    while pow(2, shift) <= number:
        if number >> shift & 1:
            array.insert(0, '1')
        else:
            array.insert(0, '0')
        shift += 1

    str = ''
    for i in xrange(0, len(array)):
        str = str + array[i]

    return str


def asNumber(bitstring):
    num = 0
    for i in xrange(0, len(bitstring)):
        if bitstring[i] == '1':
            num += pow(2, len(bitstring) - 1 - i)

    return num


def dept2deptIndex(dept):
    if type(dept) == types.StringType:
        dept = SuitDNA.suitDepts.index(dept)
    return dept