from toontown.suit import DistributedFactorySuit
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedBoardOfficeSuit(DistributedFactorySuit.DistributedFactorySuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedBoardOfficeSuit')
	
    def renameBoss(self):
        if self.getSkeleRevives() > 0:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.BoardExecutive,
             'dept': self.getStyleDept(),
             'level': '%s%s' % (self.getActualLevel(), TTLocalizer.SkeleRevivePostFix)}
            self.setName(TTLocalizer.BoardExecutive)
            self.setDisplayName(nameInfo)
        else:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': TTLocalizer.BoardExecutive,
             'dept': self.getStyleDept(),
             'level': self.getActualLevel()}
            self.setName(TTLocalizer.BoardExecutive)
            self.setDisplayName(nameInfo)
