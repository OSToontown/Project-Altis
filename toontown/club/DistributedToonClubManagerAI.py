from direct.distributed.DistributedObjectGlobalAI import DistributedObjectGlobalAI
from direct.directnotify import DirectNotifyGlobal
from direct.fsm.FSM import FSM
import anydbm

class ClubQueryFSM(FSM):

    def __init__(self, clubManager):
        self.clubManager = clubManager

    def enterQuertyClub(self, clubId):
        self.air.dbInterface.queryObject(self.air.dbId, clubId, callback=self.__queryClubCallback)

    def exitQueryClub(self):
        pass

    def __queryClubCallback(dclass, fields):
        pass

class DistributedToonClubManagerAI(DistributedObjectGlobalAI, FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedToonClubManagerAI')
    
    def __init__(self, cr):
        DistributedObjectGlobalAI.__init__(self, cr)
        FSM.__init__(self, 'DistributedToonClubManagerAI')

        self.avatar2fsm = {}

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

        self.avatar2fsm[avId] = ClubQueryFSM(self)
        self.avatar2fsm[avId].request('QueryClub', clubId)

    def d_requestStatusResponse(self, avId, clubFound, clubDoId):
        self.sendUpdateToAvatarId(avId, 'requestStatusResponse', [clubFound, clubDoId])