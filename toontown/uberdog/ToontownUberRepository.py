import urlparse
from direct.distributed.PyDatagram import *
from otp.distributed.DistributedDirectoryAI import DistributedDirectoryAI
from otp.distributed.OtpDoGlobals import *
from otp.otpbase import BackupManager
from toontown.distributed.ToontownInternalRepository import ToontownInternalRepository
from toontown.suit.SuitInvasionManagerUD import SuitInvasionManagerUD


from toontown.rpc.ToontownRPCServer import ToontownRPCServer
from toontown.rpc.ToontownRPCHandler import ToontownRPCHandler

if config.GetBool('want-mongo-client', False):
    import pymongo

class ToontownUberRepository(ToontownInternalRepository):

    def __init__(self, baseChannel, serverId):
        ToontownInternalRepository.__init__(self, baseChannel, serverId, dcSuffix='UD')
        self.rpcServer = None
        self.rpcClient = None
        if config.GetBool('want-mongo-client', False):
            url = config.GetString('mongodb-url', 'mongodb://localhost')
            replicaset = config.GetString('mongodb-replicaset', '')
            if replicaset:
                self.mongo = pymongo.MongoClient(url, replicaset=replicaset)
            else:
                self.mongo = pymongo.MongoClient(url)
            db = (urlparse.urlparse(url).path or '/test')[1:]
            self.mongodb = self.mongo[db]

        self.notify.setInfo(True)

    def handleConnected(self):
        self.registerForChannel(MESSENGER_CHANNEL_UD)

        rootObj = DistributedDirectoryAI(self)
        rootObj.generateWithRequiredAndId(self.getGameDoId(), 0, 0)

        endpoint = config.GetString('rpc-server-endpoint', 'http://localhost:8080/')

        self.rpcServer = ToontownRPCServer(endpoint, ToontownRPCHandler(self))
        self.rpcServer.start(useTaskChain=True)
        self.backups = BackupManager.BackupManager(
            filepath = 'backups/',
            extension = '.json')
        self.createGlobals()
        self.notify.info('Done.')

    def createGlobals(self):
        """
        Create "global" objects.
        """

        self.csm = simbase.air.generateGlobalObject(OTP_DO_ID_CLIENT_SERVICES_MANAGER, 'ClientServicesManager')
        self.chatAgent = simbase.air.generateGlobalObject(OTP_DO_ID_CHAT_MANAGER, 'ChatAgent')
        self.friendsManager = simbase.air.generateGlobalObject(OTP_DO_ID_TTA_FRIENDS_MANAGER, 'TTAFriendsManager')
        self.deliveryManager = simbase.air.generateGlobalObject(OTP_DO_ID_TOONTOWN_DELIVERY_MANAGER, 'DistributedDeliveryManager')
        self.codeRedemptionMgr = simbase.air.generateGlobalObject(OTP_DO_ID_TOONTOWN_CODE_REDEMPTION_MANAGER, 'TTCodeRedemptionMgr')
        self.invasionMgr = SuitInvasionManagerUD(self)
        self.invasionMgr.startInitialInvasion()
