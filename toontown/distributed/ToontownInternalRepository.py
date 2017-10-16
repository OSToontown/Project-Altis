from direct.distributed.AstronInternalRepository import AstronInternalRepository
from otp.distributed.OtpDoGlobals import *
from toontown.distributed.ToontownNetMessengerAI import ToontownNetMessengerAI
from direct.distributed.PyDatagram import PyDatagram
import direct.distributed.MsgTypes
import traceback
import sys


class ToontownInternalRepository(AstronInternalRepository):
    GameGlobalsId = OTP_DO_ID_TOONTOWN
    dbId = 4003

    def __init__(self, baseChannel, serverId=None, dcFileNames=None,
                 dcSuffix='AI', connectMethod=None, threadedNet=None):
        AstronInternalRepository.__init__(
            self, baseChannel, serverId=serverId, dcFileNames=dcFileNames,
            dcSuffix=dcSuffix, connectMethod=connectMethod, threadedNet=threadedNet)

        self.netMessenger.register(0, 'shardStatus')
        self.netMessenger.register(1, 'queryShardStatus')
        self.netMessenger.register(2, 'startInvasion')
        self.netMessenger.register(3, 'stopInvasion')
        
        self.__messenger = ToontownNetMessengerAI(self)

    def getAvatarIdFromSender(self):
        return self.getMsgSender() & 0xFFFFFFFF

    def getAccountIdFromSender(self):
        return (self.getMsgSender()>>32) & 0xFFFFFFFF

    def _isValidPlayerLocation(self, parentId, zoneId):
        return False if zoneId < 1000 and zoneId != 1 else True
        
    def sendNetEvent(self, message, sentArgs=[], channels=None):
        self.__messenger.send(message, sentArgs, channels)

    def handleDatagram(self, di):
        msgType = self.getMsgType()

        if msgType == self.__messenger.msgType:
            self.__messenger.handle(msgType, di)
            return

        if msgType == CLIENTAGENT_GET_NETWORK_ADDRESS_RESP:
            context = di.getUint32()
            remoteIp = di.getString()
            port = di.getUint16()
            localIp = di.getString()
            localPort = di.getUint16()
            if self.csm:
                self.csm.completeLogin(context, remoteIp)

            return

        AstronInternalRepository.handleDatagram(self, di)

    def readerPollOnce(self):
        try:
            return AstronInternalRepository.readerPollOnce(self)
        except (SystemExit, KeyboardInterrupt):
            raise
        except Exception as e:
            if self.getAvatarIdFromSender() > 100000000: # If an avatar is sending, boot them
                dg = PyDatagram()
                dg.addServerHeader(self.getMsgSender(), self.ourChannel, CLIENTAGENT_EJECT)
                dg.addUint16(420)
                dg.addString('You were disconnected to prevent a district reset.')
                self.send(dg)
            self.writeServerEvent('EXCEPTION-POTENTIAL-CRASH', self.getAvatarIdFromSender(), self.getAccountIdFromSender(), repr(e), traceback.format_exc())
            self.notify.warning('EXCEPTION-POTENTIAL-CRASH: %s (%s)' % (repr(e), self.getAvatarIdFromSender()))
            print traceback.format_exc()
            sys.exc_clear()
            import os
            if os.getenv('DISTRICT_NAME', 'Test Canvas') == "Test Canvas":
                return 1
            from raven import Client
            from os.path import expanduser
            errorReporter = Client(
                'https://bd12b482b0d04047b97a99be5d8a59f8:cadf8d958a194867b89fd77b61fdad45@sentry.io/189240')
            errorReporter.tags_context({
                'district_name': os.getenv('DISTRICT_NAME', 'UNDEFINED'),
                'AVID_SENDER': self.getAvatarIdFromSender(),
                'ACID_SENDER': self.getAccountIdFromSender(),
                'homedir': expanduser('~'),
                'CRITICAL': 'False'
            })
            errorReporter.captureException()
            
        return 1
