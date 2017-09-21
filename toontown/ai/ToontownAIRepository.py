import httplib, json
from direct.distributed.PyDatagram import *
from panda3d.core import *
from otp.ai.AIZoneData import AIZoneDataStore
from otp.ai.MagicWordManagerAI import MagicWordManagerAI
from otp.ai.TimeManagerAI import TimeManagerAI
from otp.ai import BanManagerAI
from otp.distributed.OtpDoGlobals import *
from otp.friends.FriendManagerAI import FriendManagerAI
from toontown.ai import CogPageManagerAI
from toontown.ai import CogSuitManagerAI
from toontown.ai import PromotionManagerAI
from toontown.ai import ExperienceRewardManagerAI
from toontown.ai.AchievementsManagerAI import AchievementsManagerAI
from toontown.ai.CertificateManagerAI import CertificateManagerAI
from toontown.ai.FishManagerAI import  FishManagerAI
from toontown.ai.HolidayManagerAI import HolidayManagerAI
from toontown.ai.DialogueManagerAI import DialogueManagerAI
from toontown.ai.NewsManagerAI import NewsManagerAI
from toontown.ai.QuestManagerAI import QuestManagerAI
from toontown.coderedemption.TTCodeRedemptionMgrAI import TTCodeRedemptionMgrAI
from toontown.ai import DistributedSillyMeterMgrAI, DistributedHydrantZeroMgrAI, DistributedMailboxZeroMgrAI, DistributedTrashcanZeroMgrAI
from toontown.building.DistributedTrophyMgrAI import DistributedTrophyMgrAI
from toontown.catalog.CatalogManagerAI import CatalogManagerAI
from toontown.coghq import CountryClubManagerAI
from toontown.coghq import FactoryManagerAI
from toontown.coghq import LawOfficeManagerAI
from toontown.coghq import MintManagerAI
from toontown.coghq.boardbothq import BoardOfficeManagerAI
from toontown.distributed.ToontownDistrictAI import ToontownDistrictAI
from toontown.distributed.ToontownDistrictStatsAI import ToontownDistrictStatsAI
from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository
from toontown.dna.DNAParser import loadDNAFileAI
from toontown.estate.EstateManagerAI import EstateManagerAI
from toontown.fishing.BingoHolidayMgrAI import BingoHolidayMgrAI
from toontown.fishing.BingoWeekendMgrAI import BingoWeekendMgrAI
from toontown.hood import BRHoodAI
from toontown.hood import BossbotHQAI
from toontown.hood import CashbotHQAI
from toontown.hood import DDHoodAI
from toontown.hood import DGHoodAI
from toontown.hood import DLHoodAI
from toontown.hood import GSHoodAI
from toontown.hood import GZHoodAI
from toontown.hood import LawbotHQAI
from toontown.hood import MMHoodAI
from toontown.hood import OZHoodAI
from toontown.hood import SellbotHQAI
from toontown.hood import TTHoodAI
from toontown.hood import TTOHoodAI
from toontown.hood import ZoneUtil
from toontown.hood import BoardbotHQAI
from toontown.minigame.TrolleyHolidayMgrAI import TrolleyHolidayMgrAI
from toontown.minigame.TrolleyWeekendMgrAI import TrolleyWeekendMgrAI
from toontown.pets.PetManagerAI import PetManagerAI
from toontown.safezone.SafeZoneManagerAI import SafeZoneManagerAI
from toontown.suit import SuitInvasionGlobals
from toontown.suit.SuitInvasionManagerAI import SuitInvasionManagerAI
from toontown.toon import NPCToons
from toontown.toonbase import ToontownGlobals
from toontown.tutorial.TutorialManagerAI import TutorialManagerAI
from toontown.pets import DistributedPublicPetMgrAI
from toontown.events.CharityScreenAI import CharityScreenAI

import atexit


class ToontownAIRepository(ToontownInternalRepository):

    def __init__(self, baseChannel, stateServerChannel, districtName, startTime=6):
        ToontownInternalRepository.__init__(self, baseChannel, stateServerChannel, dcSuffix='AI')
        self.districtName = districtName
        self.notify.setInfo(True)
        self.hoods = []
        self.hoodId2Hood = {}
        self.cogHeadquarters = []
        self.dnaStoreMap = {}
        self.dnaDataMap = {}
        self.suitPlanners = {}
        self.buildingManagers = {}
        self.sillyMeterMgr = None
        self.factoryMgr = None
        self.mintMgr = None
        self.lawOfficeMgr = None
        self.countryClubMgr = None
        self.boardofficeMgr = None
        self.startTime = startTime
        import pymongo
        self.isRaining = False
        self.betaEventTTC = None
        self.betaEventBDHQ = None
        self.invLastPop = None
        self.invLastStatus = None

        import pymongo

        # Mongo stuff to store seperate database things
        self.dbConn = pymongo.MongoClient(config.GetString('mongodb-url', 'localhost'))
        self.dbGlobalCursor = self.dbConn.altis
        self.dbCursor = self.dbGlobalCursor['air-%d' % self.ourChannel]
        self.zoneAllocator = UniqueIdAllocator(ToontownGlobals.DynamicZonesBegin,
                                               ToontownGlobals.DynamicZonesEnd)
        self.zoneDataStore = AIZoneDataStore()

        self.wantFishing = self.config.GetBool('want-fishing', True)
        self.wantHousing = self.config.GetBool('want-housing', True)
        self.wantPets = self.config.GetBool('want-pets', True)
        self.wantParties = self.config.GetBool('want-parties', True)
        self.wantCogbuildings = self.config.GetBool('want-cogbuildings', True)
        self.wantCogdominiums = self.config.GetBool('want-cogdominiums', True)
        self.doLiveUpdates = self.config.GetBool('want-live-updates', False)
        self.wantTrackClsends = self.config.GetBool('want-track-clsends', False)
        self.wantAchievements = self.config.GetBool('want-achievements', True)
        self.wantCharityScreen = self.config.GetBool('want-charity-screen', False)
        self.baseXpMultiplier = self.config.GetFloat('base-xp-multiplier', 1.0)
        self.wantHalloween = self.config.GetBool('want-halloween', False)
        self.wantChristmas = self.config.GetBool('want-christmas', False)
        self.wantGardening = self.config.GetBool('want-gardening', False)
        self.cogSuitMessageSent = False
        self.weatherCycleDuration = self.config.GetInt('weather-cycle-duration', 100)

    def createManagers(self):
        self.timeManager = TimeManagerAI(self)
        self.timeManager.generateWithRequired(2)
        self.magicWordManager = MagicWordManagerAI(self)
        self.magicWordManager.generateWithRequired(2)
        self.newsManager = NewsManagerAI(self)
        self.newsManager.generateWithRequired(2)
        self.safeZoneManager = SafeZoneManagerAI(self)
        self.safeZoneManager.generateWithRequired(2)
        self.tutorialManager = TutorialManagerAI(self)
        self.tutorialManager.generateWithRequired(2)
        self.friendManager = FriendManagerAI(self)
        self.friendManager.generateWithRequired(2)
        self.questManager = QuestManagerAI(self)
        self.banManager = BanManagerAI.BanManagerAI(self)
        self.achievementsManager = AchievementsManagerAI(self)
        self.certManager = CertificateManagerAI(self)
        self.suitInvasionManager = SuitInvasionManagerAI(self)
        self.trophyMgr = DistributedTrophyMgrAI(self)
        self.trophyMgr.generateWithRequired(2)
        self.cogSuitMgr = CogSuitManagerAI.CogSuitManagerAI(self)
        self.promotionMgr = PromotionManagerAI.PromotionManagerAI(self)
        self.experienceMgr = ExperienceRewardManagerAI.ExperienceRewardManagerAI(self)
        self.cogPageManager = CogPageManagerAI.CogPageManagerAI()
        self.sillyMeterMgr = DistributedSillyMeterMgrAI.DistributedSillyMeterMgrAI(self)
        self.sillyMeterMgr.generateWithRequired(2)
        self.hydrantZeroMgr = DistributedHydrantZeroMgrAI.DistributedHydrantZeroMgrAI(self)
        self.hydrantZeroMgr.generateWithRequired(2)
        self.mailboxZeroMgr = DistributedMailboxZeroMgrAI.DistributedMailboxZeroMgrAI(self)
        self.mailboxZeroMgr.generateWithRequired(2)
        self.trashcanZeroMgr = DistributedTrashcanZeroMgrAI.DistributedTrashcanZeroMgrAI(self)
        self.trashcanZeroMgr.generateWithRequired(2)
        self.dialogueManager = DialogueManagerAI(self)
        self.bingoHolidayMgr = BingoHolidayMgrAI(self, ToontownGlobals.FISH_BINGO_NIGHT)
        self.bingoWeekendMgr = BingoWeekendMgrAI(self, ToontownGlobals.SILLY_SATURDAY_BINGO)
        self.trolleyHolidayMgr = TrolleyHolidayMgrAI(self, ToontownGlobals.TROLLEY_HOLIDAY)
        self.trolleyWeekendMgr = TrolleyWeekendMgrAI(self, ToontownGlobals.TROLLEY_WEEKEND)
        self.holidayManager = HolidayManagerAI(self)


        if self.wantFishing:
            self.fishManager = FishManagerAI(self)

        if self.wantHousing:
            self.estateManager = EstateManagerAI(self)
            self.estateManager.generateWithRequired(2)
            self.catalogManager = CatalogManagerAI(self)
            self.catalogManager.generateWithRequired(2)
            self.deliveryManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_DELIVERY_MANAGER, 'DistributedDeliveryManager')
            self.mailManager = self.generateGlobalObject(OTP_DO_ID_TOONTOWN_MAIL_MANAGER, 'DistributedMailManager')

        if self.wantPets:
            self.petMgr = PetManagerAI(self)

        self.publicPetMgr = DistributedPublicPetMgrAI.DistributedPublicPetMgrAI(self)
        self.publicPetMgr.generateWithRequired(2)

        if self.wantParties:
            self.partyManager = DistributedPartyManagerAI(self)
            self.partyManager.generateWithRequired(2)
            self.globalPartyMgr = self.generateGlobalObject(OTP_DO_ID_GLOBAL_PARTY_MANAGER, 'GlobalPartyManager')

        self.codeRedemptionMgr = TTCodeRedemptionMgrAI(self)
        self.codeRedemptionMgr.generateWithRequired(2)
        self.chatAgent = simbase.air.generateGlobalObject(OTP_DO_ID_CHAT_MANAGER, 'ChatAgent')

    def createSafeZones(self):
        NPCToons.generateZone2NpcDict()
        if self.config.GetBool('want-toontown-central', True):
            hood = TTHoodAI.TTHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-donalds-dock', True):
            hood = DDHoodAI.DDHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-daisys-garden', True):
            hood = DGHoodAI.DGHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-minnies-melodyland', True):
            hood = MMHoodAI.MMHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-the-burrrgh', True):
            hood = BRHoodAI.BRHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-donalds-dreamland', True):
            hood = DLHoodAI.DLHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-goofy-speedway', True):
            hood = GSHoodAI.GSHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-outdoor-zone', True):
            hood = OZHoodAI.OZHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        if self.config.GetBool('want-golf-zone', True):
            hood = GZHoodAI.GZHoodAI(self)
            self.hoods.append(hood)
            self.hoodId2Hood[hood.zoneId] = hood
        hood = TTOHoodAI.TTOHoodAI(self)
        self.hoods.append(hood)
        self.hoodId2Hood[hood.zoneId] = hood

    def createCogHeadquarters(self):
        NPCToons.generateZone2NpcDict()
        if self.config.GetBool('want-sellbot-headquarters', True):
            self.factoryMgr = FactoryManagerAI.FactoryManagerAI(self)
            self.cogHeadquarters.append(SellbotHQAI.SellbotHQAI(self))
        if self.config.GetBool('want-cashbot-headquarters', True):
            self.mintMgr = MintManagerAI.MintManagerAI(self)
            self.cogHeadquarters.append(CashbotHQAI.CashbotHQAI(self))
        if self.config.GetBool('want-lawbot-headquarters', True):
            self.lawOfficeMgr = LawOfficeManagerAI.LawOfficeManagerAI(self)
            self.cogHeadquarters.append(LawbotHQAI.LawbotHQAI(self))
        if self.config.GetBool('want-bossbot-headquarters', True):
            self.countryClubMgr = CountryClubManagerAI.CountryClubManagerAI(self)
            self.cogHeadquarters.append(BossbotHQAI.BossbotHQAI(self))
        #if self.config.GetBool('want-bdhq', True):
        #    self.boardofficeMgr = BoardOfficeManagerAI.BoardOfficeManagerAI(self)
        #    self.cogHeadquarters.append(BoardbotHQAI.BoardbotHQAI(self))

    def handleConnected(self):
        self.registerForChannel(MESSENGER_CHANNEL_AI)

        self.districtId = self.allocateChannel()
        self.notify.info('Creating ToontownDistrictAI(%d)...' % self.districtId)
        self.distributedDistrict = ToontownDistrictAI(self)
        self.distributedDistrict.setName(self.districtName)
        self.distributedDistrict.generateWithRequiredAndId(
            self.districtId, self.getGameDoId(), 2)

        self.notify.info('Claiming ownership of channel ID: %d...' % self.districtId)
        self.setAI(self.districtId, self.ourChannel)

        self.districtStats = ToontownDistrictStatsAI(self)
        self.districtStats.settoontownDistrictId(self.districtId)
        self.districtStats.generateWithRequiredAndId(self.allocateChannel(),
            self.getGameDoId(), 3)

        self.notify.info('Created ToontownDistrictStats(%d)' % self.districtStats.doId)

        self.notify.info('Creating managers...')
        self.createManagers()
        if self.config.GetBool('want-safe-zones', True):
            self.notify.info('Creating safe zones...')
            self.createSafeZones()

        if self.config.GetBool('want-cog-headquarters', True):
            self.notify.info('Creating Cog headquarters...')
            self.createCogHeadquarters()

        self.notify.info('Making district available...')
        self.distributedDistrict.b_setAvailable(1)
        self.notify.info('Done.')

        self.notify.info("Starting Invasion Tracker...")
        taskMgr.doMethodLater(2, self.updateInvasionTrackerTask, 'updateInvasionTracker-%d' % self.ourChannel)
        self.notify.info("Invasion Tracker Started!")
        self.sendNetEvent('registerShard', [self.districtId, True], channels=[MESSENGER_CHANNEL_UD])

        atexit.register(self.shardDeath)

    def shardDeath(self):
        self.sendNetEvent('registerShard', [self.districtId, False], channels=[MESSENGER_CHANNEL_UD])

    def lookupDNAFileName(self, zoneId):
        zoneId = ZoneUtil.getCanonicalZoneId(zoneId)
        hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
        hood = ToontownGlobals.dnaMap[hoodId]
        if hoodId == zoneId:
            zoneId = 'sz'
            phaseNum = ToontownGlobals.phaseMap[hoodId]
        else:
            phaseNum = ToontownGlobals.streetPhaseMap[hoodId]

        return 'phase_%s/dna/%s_%s.pdna' % (phaseNum, hood, zoneId)

    def loadDNAFileAI(self, dnastore, filename):
        return loadDNAFileAI(dnastore, filename)

    def incrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() + 1)

    def decrementPopulation(self):
        self.districtStats.b_setAvatarCount(self.districtStats.getAvatarCount() - 1)

    def setHour(self, hour):
        pass # Todo: Hour on district page

    def allocateZone(self):
        return self.zoneAllocator.allocate()

    def deallocateZone(self, zone):
        self.zoneAllocator.free(zone)

    def getZoneDataStore(self):
        return self.zoneDataStore

    def getTrackClsends(self):
        return self.wantTrackClsends

    def getAvatarExitEvent(self, avId):
        return 'distObjDelete-%d' % (avId)

    def trueUniqueName(self, name):
        return self.uniqueName(name)

    def updateInvasionTrackerTask(self, task):
        task.delayTime = 10 # Set it to 10 after doing it the first time
        statusToType = {
        0: 'None',
        1: 'Bossbot',
        2: 'Lawbot',
        3: 'Cashbot',
        4: 'Sellbot',
        5: 'Boardbot'}
        pop = self.districtStats.getAvatarCount()
        invstatus = statusToType.get(self.districtStats.getInvasionStatus(), 'None')
        total = self.districtStats.getInvasionTotal()
        defeated = total - self.districtStats.getInvasionRemaining()
        tupleStatus = (self.districtStats.getInvasionStatus(), self.districtStats.getInvasionType())
        invstatus = self.statusToType(tupleStatus)
        timeleft = self.districtStats.getInvasionTimeRemaining()

        self.invLastPop = pop
        self.invLastStatus = invstatus

        if self.districtName == "Test Canvas":
            return
        print invstatus
        domain = str(ConfigVariableString('ws-domain', 'localhost'))
        key = str(ConfigVariableString('ws-key', 'secretkey'))
        if invstatus == 'None':
            httpReqkill = httplib.HTTPSConnection(domain)
            httpReqkill.request('GET', '/api/addinvasion/%s/%s/%s/0/%s/0/0' % (key, self.districtName,
                                                                               pop, invstatus))
            resp = httpReqkill.getresponse()
            if resp.status != 200:
                print 'Invaison api returned response ' + str(resp.status)
        else:
            httpReq = httplib.HTTPSConnection(domain)
            httpReq.request('GET', '/api/addinvasion/%s/%s/%s/1/%s/%s/%s/%s' % (key, self.districtName,
                                                                           pop, invstatus, total, defeated, timeleft))
            resp = httpReq.getresponse()
            if resp.status != 200:
                print 'Invasion api returned response ' + str(resp.status)
        return task.again

    def statusToType(self, tupleInvasionStatus):
        try:
            statusToSuit = {
                0: 'None',
                1: 'Bossbot',
                2: 'Lawbot',
                3: 'Cashbot',
                4: 'Sellbot',
                5: 'Boardbot'
            }
            suit = statusToSuit.get(tupleInvasionStatus[0], 'None')
            if suit == 'None':
                return suit

            Type = SuitInvasionGlobals.comboToType.get(str(tupleInvasionStatus[0]) + str(tupleInvasionStatus[1]), 'None')
            Type = Type.replace(' ', '%20')
            if Type == 'None':
                return Type
            return Type + '|' + suit
        except:
            return 'None'
