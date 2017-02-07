from toontown.suit import DistributedFactorySuit
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedMintSuit(DistributedFactorySuit.DistributedFactorySuit):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedMintSuit')
	
    def renameBoss(self):
        if self.getStyleDept() == TTLocalizer.Cashbot:
           name = TTLocalizer.Supervisor
        else:
           name = TTLocalizer.President
        if self.getSkeleRevives() > 0:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': name,
             'dept': self.getStyleDept(),
             'level': '%s%s' % (self.getActualLevel(), TTLocalizer.SkeleRevivePostFix)}
            self.setName(name)
            self.setDisplayName(nameInfo)
        else:
            nameInfo = TTLocalizer.SuitBaseNameWithLevel % {'name': name,
             'dept': self.getStyleDept(),
             'level': self.getActualLevel()}
            self.setName(name)
            self.setDisplayName(nameInfo)
