from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.FSM import FSM
import anydbm

class DistributedToonClubManagerAI(DistributedObjectGlobalAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubManagerAI')
    
    def __init__(self, cr):
        DistributedObjectGlobalAI.__init__(self, cr)
        FSM.__init__(self, 'DistributedToonClubManagerAI')

    def generate(self):
        DistributedObjectGlobalAI.generate(self)

        filename = simbase.config.GetString('toon-club-bridge-filename',
            'toon-clubs')
        
        self.dbm = anydbm.open(filename, 'c')

    def requestStatus(self):
        avId = self.air.getAvatarIdFromSender()
        av = self.air.doId2do[avId]

        if not av:
            return

        clubId = av.getClubId()

        if not clubId or clubId not in self.dbm:
            self.d_requestStatusResponse(avId, False, 0)
            return

        # query the club database file for all details
        self.request('QuertClub', clubId)

    def enterQuertyClub(self, clubId):
        pass

    def exitQueryClub(self):
        pass

    def d_requestStatusResponse(self, avId, clubFound, clubDoId):
        self.sendUpdateToAvatarId(avId, 'requestStatusResponse', [clubFound, clubDoId])