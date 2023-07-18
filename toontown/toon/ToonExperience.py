from panda3d.core import *
from toontown.toonbase.ToontownBattleGlobals import *
from direct.directnotify import DirectNotifyGlobal
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.PyDatagramIterator import PyDatagramIterator
from otp.otpbase import OTPGlobals
levels = [0]
for level in range(1,100):
    level += 1
    exp = int(15 * level * (level+5))
    levels.append(exp)

class ToonExperience:
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonExperience')
    ExpPerLevel = levels

    def __init__(self, experience = None, owner = None):
        self.owner = owner
        self.experience = experience

    def addExp(self, amount = 1):
        self.notify.debug('adding %d exp to toon %d' % (amount, owner))
        return (experience + amount)

    def zeroOutExp(self):
        self.experience = 0

    def getExp(self):
        return self.experience

    def setExp(self, exp):
        self.experience = exp

    def getExpLevel(self, experience):
        exp = self.ExpPerLevel
        for i in range(len(self.ExpPerLevel)):
            if experience < exp[i] and experience >= exp[i-1]:
               return i

            continue

    def getLevelMaxExp(self, level):
        exp = self.ExpPerLevel
        if int(level + 1) in exp:
            return exp[level+1]
        level += 1
        return int(15 * level * (level+5))
