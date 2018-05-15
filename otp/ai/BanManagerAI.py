import datetime
from direct.directnotify import DirectNotifyGlobal
from toontown.uberdog.ClientServicesManagerUD import executeHttpRequest
from direct.fsm.FSM import FSM
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from otp.ai.MagicWordGlobal import *
from direct.showbase.DirectObject import DirectObject
import threading
import httplib

class BanFSM(FSM):

    def __init__(self, air, avId):
        FSM.__init__(self, 'banFSM-%s' % avId)
        self.air = air
        self.avId = avId

        # Needed variables for the actual banning.
        self.DISLid = None
        self.accountId = None
        self.avName = None

    def performBan(self):
        self.ejectPlayer()
        print(self.accountId)

    def ejectPlayer(self):
        av = self.air.doId2do.get(self.avId)
        if not av:
            return

        # Send the client a 'CLIENTAGENT_EJECT' with the players name.
        datagram = PyDatagram()
        datagram.addServerHeader(
                av.GetPuppetConnectionChannel(self.avId),
                self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(152)
        datagram.addString(self.avName)
        simbase.air.send(datagram)

    def dbCallback(self, dclass, fields):
        if dclass != simbase.air.dclassesByName['AccountAI']:
            return

        self.accountId = fields.get('ACCOUNT_ID')

        if not self.accountId:
            return

        self.duration = None
        self.performBan()

    def getAvatarDetails(self):
        av = self.air.doId2do.get(self.avId)
        if not av:
            return

        self.DISLid = av.getDISLid()
        self.avName = av.getName()

    def log(self):
        simbase.air.writeServerEvent('ban', self.accountId)

    def cleanup(self):
        self.air = None
        self.avId = None

        self.DISLid = None
        self.avName = None
        self.accountId = None
        self.comment = None
        self.duration = None
        self = None

    def enterStart(self):
        self.getAvatarDetails()
        self.air.dbInterface.queryObject(self.air.dbId, self.DISLid, self.dbCallback)

    def exitStart(self):
        self.log()
        self.cleanup()

    def enterOff(self):
        pass

    def exitOff(self):
        pass


class BanManagerAI(DirectObject):
    notify = DirectNotifyGlobal.directNotify.newCategory('BanManagerAI')

    def __init__(self, air):
        self.air = air
        self.banFSMs = {}

    def ban(self, avId, comment):
        self.banFSMs[avId] = BanFSM(self.air, avId)
        self.banFSMs[avId].request('Start')

        self.acceptOnce(self.air.getAvatarExitEvent(avId), self.banDone, [avId])

    def banDone(self, avId):
        self.banFSMs[avId].request('Off')
        self.banFSMs[avId] = None


@magicWord(category=CATEGORY_MODERATOR, types=[str])
def kick(reason='No reason specified'):
    """
    Kick the target from the game server.
    """
    target = spellbook.getTarget()
    if target == spellbook.getInvoker():
        return "You can't kick yourself!"
    datagram = PyDatagram()
    datagram.addServerHeader(
        target.GetPuppetConnectionChannel(target.doId),
        simbase.air.ourChannel, CLIENTAGENT_EJECT)
    datagram.addUint16(155)
    datagram.addString('You were kicked by a moderator for the following reason: %s' % reason)
    simbase.air.send(datagram)
    return "Kicked %s from the game server!" % target.getName()

@magicWord(category=CATEGORY_MODERATOR, types=[int, str])
def kickId(id, reason='No reason specified'):
    """
    Kick the target from the game server.
    """
    target = simbase.air.doId2do.get(100000000+id)
    if target == spellbook.getInvoker():
        return "You can't kick yourself!"
    datagram = PyDatagram()
    datagram.addServerHeader(
        target.GetPuppetConnectionChannel(target.doId),
        simbase.air.ourChannel, CLIENTAGENT_EJECT)
    datagram.addUint16(155)
    datagram.addString('You were kicked by a moderator for the following reason: %s' % reason)
    simbase.air.send(datagram)
    return "Kicked %s from the game server!" % target.getName()

@magicWord(category=CATEGORY_MODERATOR, types=[str])
def ban(reason):
    """
    Ban and Kick the target from the game server.
    """
    target = spellbook.getTarget()
    if target == spellbook.getInvoker():
        return "You can't ban yourself!"
    simbase.air.banManager.ban(target.doId, reason)
    datagram = PyDatagram()
    datagram.addServerHeader(
        target.GetPuppetConnectionChannel(target.doId),
        simbase.air.ourChannel, CLIENTAGENT_EJECT)
    datagram.addUint16(155)
    datagram.addString('You were banned by a moderator for the following reason: %s' % reason)
    simbase.air.send(datagram)
    return "Kicked and Banned %s from the game server!" % target.getName()

@magicWord(category=CATEGORY_MODERATOR, types=[int, str])
def banId(id, reason):
    """
    Ban and Kick the short id from the game server.
    """
    target = simbase.air.doId2do.get(100000000+id)
    if target == spellbook.getInvoker():
        return "You can't ban yourself!"
    simbase.air.banManager.ban(target.doId, reason)
    datagram = PyDatagram()
    datagram.addServerHeader(
        target.GetPuppetConnectionChannel(target.doId),
        simbase.air.ourChannel, CLIENTAGENT_EJECT)
    datagram.addUint16(155)
    datagram.addString('You were banned by a moderator for the following reason: %s' % reason)
    simbase.air.send(datagram)
    return "Kicked and Banned %s from the game server!" % target.getName()
