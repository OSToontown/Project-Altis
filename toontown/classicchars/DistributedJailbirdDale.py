from direct.showbase.ShowBaseGlobal import *
from toontown.classicchars import DistributedCCharBase
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.classicchars import CharStateDatas
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.classicchars import DistributedDale

class DistributedJailbirdDale(DistributedDale.DistributedDale):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedJailbirdDale')

    def __init__(self, cr):
        try:
            self.DistributedDale_initialized
            return
        except:
            self.DistributedDale_initialized = 1
        
        DistributedCCharBase.DistributedCCharBase.__init__(self, cr, TTLocalizer.JailbirdDale, 'jda')
        self.fsm = ClassicFSM.ClassicFSM(self.getName(), [State.State('Off', self.enterOff, self.exitOff, ['Neutral']), State.State('Neutral', self.enterNeutral, self.exitNeutral, ['Walk']), State.State('Walk', self.enterWalk, self.exitWalk, ['Neutral'])], 'Off', 'Off')
        self.fsm.enterInitialState()
        self.handleHolidays()
        self.nametag.setText(TTLocalizer.Dale)