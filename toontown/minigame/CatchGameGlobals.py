EndlessGame = config.GetBool('endless-catch-game', 0)
GameDuration = 55.0

class DropObject:

    def __init__(self, name, good, onscreenDurMult, modelPath):
        self.name = name
        self.good = good
        self.onscreenDurMult = onscreenDurMult
        self.modelPath = modelPath

    def isBaseline(self):
        return self.onscreenDurMult == 1.0


DropObjectTypes = [DropObject('apple', 1, 1.0, 'phase_4/models/minigames/apple'),
 DropObject('orange', 1, 1.0, 'phase_4/models/minigames/orange'),
 DropObject('pear', 1, 1.0, 'phase_4/models/minigames/pear'),
 DropObject('coconut', 1, 1.0, 'phase_4/models/minigames/coconut'),
 DropObject('watermelon', 1, 1.0, 'phase_4/models/minigames/watermelon'),
 DropObject('pineapple', 1, 1.0, 'phase_4/models/minigames/pineapple'),
 DropObject('acorn', 1, 1.0, 'phase_4/models/minigames/acorn'),
 DropObject('anvil', 0, 0.4, 'phase_4/models/props/anvil-mod')]
Name2DropObjectType = {}
for type in DropObjectTypes:
    Name2DropObjectType[type.name] = type

Name2DOTypeId = {}
names = Name2DropObjectType.keys()
names.sort()
for i in xrange(len(names)):
    Name2DOTypeId[names[i]] = i

DOTypeId2Name = names
NumFruits = [{2000: 18,
  6000: 19,
  1000: 22,
  5000: 24,
  4000: 27,
  3000: 28,
  9000: 30},
 {2000: 30,
  6000: 33,
  1000: 38,
  5000: 42,
  4000: 46,
  3000: 50,
  9000: 55},
 {2000: 42,
  6000: 48,
  1000: 54,
  5000: 60,
  4000: 66,
  3000: 71,
  9000: 78},
 {2000: 56,
  6000: 63,
  1000: 70,
  5000: 78,
  4000: 85,
  3000: 92,
  9000: 100}]
