import anydbm
import base64
import hashlib
import hmac
import json
import time
import random
import urllib2
import httplib
import traceback
import requests
import six
from datetime import datetime
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobalUD import DistributedObjectGlobalUD
from direct.distributed.PyDatagram import *
from direct.fsm.FSM import FSM
from pandac.PandaModules import *
from otp.ai.MagicWordGlobal import *
from otp.distributed import OtpDoGlobals
from toontown.makeatoon.NameGenerator import NameGenerator
from toontown.toon.ToonDNA import ToonDNA
from toontown.toon.Experience import Experience
from toontown.toonbase import TTLocalizer

# Import from PyCrypto only if we are using a database that requires it. This
# allows local hosted and developer builds of the game to run without it:
accountDBType = "local"

# Sometimes we'll want to force a specific access level, such as on the
# developer server:
minAccessLevel = simbase.config.GetInt('min-access-level', 100)

accountServerEndpoint = simbase.config.GetString(
    'account-server-endpoint', 'https://projectaltis.com/api/')
accountServerSecret = simbase.config.GetString(
    'account-server-secret', 'sjHgh43h43ZMcHnJ')

http = HTTPClient()
http.setVerifySsl(0)

def executeHttpRequest(url, **extras):
    timestamp = str(int(time.time()))
    signature = hmac.new(accountServerSecret, timestamp, hashlib.sha256)
    request = urllib2.Request(accountServerEndpoint + url)
    request.add_header('User-Agent', 'TTA-CSM')
    request.add_header('X-CSM-Timestamp', timestamp)
    request.add_header('X-CSM-Signature', signature.hexdigest())
    for k, v in extras.items():
        request.add_header('X-CSM-' + k, v)

    try:
        return urllib2.urlopen(request).read()
    except:
        return None

blacklist = executeHttpRequest('names/blacklist.json')
if blacklist:
    blacklist = json.loads(blacklist)

def judgeName(name): #All of this gunction is just fuckrd
    if not name:
        return False

    if blacklist:
        for namePart in name.split(' '):
            namePart = namePart.lower()
            if len(namePart) < 1:
                return False

            for banned in blacklist.get(namePart[0], []):
                if banned in namePart:
                    return False
    # Use Google's API for checking badword list
    return True

def to_bool(boolorstr):
    if isinstance(boolorstr, six.string_types):
        return boolorstr.lower() == 'true'
    if isinstance(boolorstr, bool):
        return boolorstr
    else:
        return False

class AccountDB:
    notify = directNotify.newCategory('AccountDB')

    def __init__(self, csm):
        self.csm = csm

        filename = simbase.config.GetString(
            'account-bridge-filename', 'account-bridge')
        self.dbm = anydbm.open(filename, 'c')

    def addNameRequest(self, avId, name):
        return 'Success'

    def getNameStatus(self, avId):
        return 'APPROVED'

    def removeNameRequest(self, avId):
        return 'Success'

    def lookup(self, username, ip, callback):
        pass  # Inheritors should override this.

    def storeAccountID(self, userId, accountId, callback):
        self.dbm[str(userId)] = str(accountId)
        if getattr(self.dbm, 'sync', None):
            self.dbm.sync()
            callback(True)
        else:
            self.notify.warning('Unable to associate user %s with account %d!' % (userId, accountId))
            callback(False)

class LocalAccountDB(AccountDB):
    notify = directNotify.newCategory('LocalAccountDB')

    def lookup(self, cookie, ip, callback):
        if len(cookie) != 64: # Cookies should be exactly 64 Characters long!
            callback({'success': False,
                      'reason': 'FATAL ERROR IN COOKIE RESPONSE [%s]!'%cookie})
            return

        apiKey = str(ConfigVariableString('ws-key', 'secretkey'))
        sanityChecks = httplib.HTTPConnection('www.projectaltis.com')
        sanityChecks.request('GET', '/api/sanitycheck/%s/%s/%s' % (apiKey, cookie, ip))

        try:
            XYZ = sanityChecks.getresponse().read()
            print str(XYZ)
            response = json.loads(XYZ)
            # If response["isbanned"] is true
            if to_bool(response["isbanned"]):
                callback({
                    'success': False,
                    'reason': 'Your account has been banned!'
                })
                return
            if to_bool(response["whitelistissue"]):
                callback({
                    'success': False,
                    'reason': 'Please go to your account page to whitelist your IP address!'
                })
                return
            # If response["error"] is true
            if to_bool(response["error"]):
                callback({
                    'success': False,
                    'reason': 'There was an unknown error when processing your login.'
                })
                return
        except:
            print traceback.format_exc()
            callback({'success': False,
                      'reason': 'Account Server is down. Please Try Again Later!'})
            return
        # Let's check if this user's ID is in your account database bridge:
        if str(cookie) not in self.dbm:
            # Nope. Let's associate them with a brand new Account object!
            response = {
                'success': True,
                'userId': cookie,
                'accountId': 0,
                'accessLevel': 100
            }
            callback(response)
            return response
        else:
            try:
                # We have an account already, let's return what we've got:
                response = {
                    'success': True,
                    'userId': cookie,
                    'accountId': int(self.dbm[str(cookie)]),
                    'accessLevel': int(response['powerlevel'])
                }
            except:
                # We have an account already, but power level isn't an int. Let's give them 150
                response = {
                    'success': True,
                    'userId': cookie,
                    'accountId': int(self.dbm[str(cookie)]),
                    'accessLevel': int(150)
                }

            callback(response)
            return response


    def addNameRequest(self, avId, name):
        # add type a name
        self.notify.debug("name for avid %s requested: `%s`" %(avId, name))
        try:
            domain = str(ConfigVariableString('ws-domain', 'localhost'))
            key = str(ConfigVariableString('ws-key', 'secretkey'))
            nameCheck = httplib.HTTPSConnection(domain)
            nameCheck.request('GET', '/api/addtypeaname2/%s/%s/%s' % (key, avId, name))
            resp = json.loads(nameCheck.getresponse().read())
            self.sendWebhook(avId, name)
        except:
            self.notify.debug("Unable to add name request from %s (%s)" %(avId, name))
        return 'Success'

    def getNameStatus(self, avId):
        # check type a name
        self.notify.debug("debug: checking name from %s" %(avId))
        try:
            domain = str(ConfigVariableString('ws-domain', 'localhost'))
            key = str(ConfigVariableString('ws-key', 'secretkey'))
            nameCheck = httplib.HTTPSConnection(domain)
            nameCheck.request('GET', '/api/checktypeaname/%s/avid/%s' % (key, avId)) # this should just use avid
            resp = json.loads(nameCheck.getresponse().read())

            if resp[u"error"] == "true":
                state = "ERROR"

            status = resp[u"status"]
            if status == -1:
                state = "REJECTED"
            elif status == 0:
                state = "PENDING"
            elif status == 1:
                state = "APPROVED"
            else:
                self.notify.debug("Get name status for av %s didnt return an expected value, got %s, setting to PENDING" % (avId, str(status)))
                state = "REJECTED"
        except:
            self.notify.debug("Get name status failed for av %s, setting to pending" % avId)
            state = "ERROR"
        self.notify.debug("Get name status for av %s returned state %s" % (avId, state))
        return state

    @staticmethod
    def sendWebhook(avid, requestedname):
        title = str(ConfigVariableString('nwh-title'))
        displayname = str(ConfigVariableString('nwh-displayname'))
        avatarurl = str(ConfigVariableString('nws-avatarurl'))
        urllink = str(ConfigVariableString('nwh-urllink'))
        content = {
            "username": displayname,
            "avatar_url": avatarurl,
            "embeds": [
                {
                    "title": title,
                    "url": urllink,
                    "timestamp": datetime.utcnow().isoformat(),
                    "color": 3447003,
                    "provider": {
                        "name": "Project Altis",
                        "url": "https://projectaltis.com"
                    },
                    "fields": [
                        {
                            "name": "Avid",
                            "value": str(avid)
                        },
                        {
                            "name": "Requested Name",
                            "value": requestedname
                        }
                    ]
                }
            ]}
        headers = {"Content-type": "application/json"}
        conn = requests.post("https://discordapp.com/api/webhooks/360528244350648321/3qErsLnMXJaZd2JWf9QGinQCnIXU0E8lm3JuwDPwsirk_QU9Uk1QiPRhd9Fs_CQnaQej", data=json.dumps(content), headers=headers)
        if conn.status_code != 204:
            print 'Discord webhook returned ' + str(conn.status_code) + ' instead of 204 with message ' + conn.text


# --- FSMs ---
class OperationFSM(FSM):
    TARGET_CONNECTION = False

    def __init__(self, csm, target):
        self.csm = csm
        self.target = target

        FSM.__init__(self, self.__class__.__name__)

    def enterKill(self, reason=''):
        if self.TARGET_CONNECTION:
            self.csm.killConnection(self.target, reason)
        else:
            self.csm.killAccount(self.target, reason)
        self.demand('Off')

    def enterOff(self):
        if self.TARGET_CONNECTION:
            del self.csm.connection2fsm[self.target]
        else:
            del self.csm.account2fsm[self.target]


class LoginAccountFSM(OperationFSM):
    notify = directNotify.newCategory('LoginAccountFSM')
    TARGET_CONNECTION = True

    def enterStart(self, token, ip):
        self.token = token
        self.ip = ip
        self.demand('QueryAccountDB')

    def enterQueryAccountDB(self):
        self.csm.accountDB.lookup(self.token, self.ip, self.__handleLookup)

    def __handleLookup(self, result):
        if not result.get('success'):
            self.csm.air.writeServerEvent('tokenRejected', self.target, self.token)
            self.demand('Kill', result.get('reason', 'The account server rejected your token.'))
            return

        self.userId = result.get('userId', 0)
        self.accountId = result.get('accountId', 0)
        self.accessLevel = result.get('accessLevel', 0)
        if self.accountId:
            self.demand('RetrieveAccount')
        else:
            self.demand('CreateAccount')

    def enterRetrieveAccount(self):
        self.csm.air.dbInterface.queryObject(
            self.csm.air.dbId, self.accountId, self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['AccountUD']:
            self.demand('Kill', 'Your account object was not found in the database!')
            return

        self.account = fields
        self.demand('SetAccount')

    def enterCreateAccount(self):
        self.account = {
            'ACCOUNT_AV_SET': [0] * 6,
            'ESTATE_ID': 0,
            'ACCOUNT_AV_SET_DEL': [],
            'CREATED': time.ctime(),
            'LAST_LOGIN': time.ctime(),
            'ACCOUNT_ID': str(self.userId),
            'ACCESS_LEVEL': self.accessLevel,
            'MONEY': 0
        }
        self.csm.air.dbInterface.createObject(
            self.csm.air.dbId,
            self.csm.air.dclassesByName['AccountUD'],
            self.account,
            self.__handleCreate)

    def __handleCreate(self, accountId):
        if self.state != 'CreateAccount':
            self.notify.warning('Received a create account response outside of the CreateAccount state.')
            return

        if not accountId:
            self.notify.warning('Database failed to construct an account object!')
            self.demand('Kill', 'Your account object could not be created in the game database.')
            return

        self.accountId = accountId
        self.csm.air.writeServerEvent('accountCreated', accountId)
        self.demand('StoreAccountID')

    def enterStoreAccountID(self):
        self.csm.accountDB.storeAccountID(
            self.userId,
            self.accountId,
            self.__handleStored)

    def __handleStored(self, success=True):
        if not success:
            self.demand('Kill', 'The account server could not save your user ID!')
            return

        self.demand('SetAccount')

    def enterSetAccount(self):
        # If necessary, update their account information:
        if self.accessLevel:
            self.csm.air.dbInterface.updateObject(
                self.csm.air.dbId,
                self.accountId,
                self.csm.air.dclassesByName['AccountUD'],
                {'ACCESS_LEVEL': self.accessLevel})

        # If there's anybody on the account, kill them for redundant login:
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.csm.GetAccountConnectionChannel(self.accountId),
            self.csm.air.ourChannel,
            CLIENTAGENT_EJECT)
        datagram.addUint16(100)
        datagram.addString('This account has been logged in from elsewhere.')
        self.csm.air.send(datagram)

        # Next, add this connection to the account channel.
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.target,
            self.csm.air.ourChannel,
            CLIENTAGENT_OPEN_CHANNEL)
        datagram.addChannel(self.csm.GetAccountConnectionChannel(self.accountId))
        self.csm.air.send(datagram)

        # Subscribe to any "staff" channels that the account has access to.
        access = self.account.get('ACCESS_LEVEL', 0)
        if access >= 200:
            # Subscribe to the moderator channel.
            dg = PyDatagram()
            dg.addServerHeader(self.target, self.csm.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
            dg.addChannel(OtpDoGlobals.OTP_MOD_CHANNEL)
            self.csm.air.send(dg)
        if access >= 400:
            # Subscribe to the administrator channel.
            dg = PyDatagram()
            dg.addServerHeader(self.target, self.csm.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
            dg.addChannel(OtpDoGlobals.OTP_ADMIN_CHANNEL)
            self.csm.air.send(dg)
        if access >= 500:
            # Subscribe to the system administrator channel.
            dg = PyDatagram()
            dg.addServerHeader(self.target, self.csm.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
            dg.addChannel(OtpDoGlobals.OTP_SYSADMIN_CHANNEL)
            self.csm.air.send(dg)

        # Now set their sender channel to represent their account affiliation:
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.target,
            self.csm.air.ourChannel,
            CLIENTAGENT_SET_CLIENT_ID)
        # Account ID in high 32 bits, 0 in low (no avatar):
        datagram.addChannel(self.accountId << 32)
        self.csm.air.send(datagram)

        # Un-sandbox them!
        datagram = PyDatagram()
        datagram.addServerHeader(
            self.target,
            self.csm.air.ourChannel,
            CLIENTAGENT_SET_STATE)
        datagram.addUint16(2)  # ESTABLISHED
        self.csm.air.send(datagram)

        # Update the last login timestamp:
        self.csm.air.dbInterface.updateObject(
            self.csm.air.dbId,
            self.accountId,
            self.csm.air.dclassesByName['AccountUD'],
            {'LAST_LOGIN': time.ctime(),
             'ACCOUNT_ID': str(self.userId)})

        # We're done.
        self.csm.air.writeServerEvent('accountLogin', self.target, self.accountId, self.userId)
        self.csm.sendUpdateToChannel(self.target, 'acceptLogin', [int(time.time())])
        self.demand('Off')

class CreateAvatarFSM(OperationFSM):
    notify = directNotify.newCategory('CreateAvatarFSM')

    def enterStart(self, dna, index, uber, tracks, pg):
        # Basic sanity-checking:
        if index >= 6:
            self.demand('Kill', 'Invalid index specified!')
            return

        if not ToonDNA().isValidNetString(dna):
            self.demand('Kill', 'Invalid DNA specified!')
            return

        self.index = index
        self.dna = dna
        self.uber = uber
        self.pg = pg
        self.trackAccess = [0,0,0,0,1,1,0,0]
        if pg ==1:
           self.trackAccess[tracks[0]] = 1
        elif pg ==2:
            for track in tracks:
                self.trackAccess[track] = 1


        # Okay, we're good to go, let's query their account.
        self.demand('RetrieveAccount')

    def enterRetrieveAccount(self):
        self.csm.air.dbInterface.queryObject(
            self.csm.air.dbId, self.target, self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['AccountUD']:
            self.demand('Kill', 'Your account object was not found in the database!')
            return

        self.account = fields

        self.avList = self.account['ACCOUNT_AV_SET']
        # Sanitize:
        self.avList = self.avList[:6]
        self.avList += [0] * (6-len(self.avList))

        # Make sure the index is open:
        if self.avList[self.index]:
            self.demand('Kill', 'This avatar slot is already taken by another avatar!')
            return

        # Okay, there's space. Let's create the avatar!
        self.demand('CreateAvatar')

    def enterCreateAvatar(self):
        dna = ToonDNA()
        dna.makeFromNetString(self.dna)
        try:
            colorString = TTLocalizer.NumToColor[dna.headColor]
        except:
            colorString = "Colorful"
        animalType = TTLocalizer.AnimalToSpecies[dna.getAnimal()]
        name = ' '.join((colorString, animalType))

        toonFields = {
            'setName': (name,),
            'WishNameState': ('OPEN',),
            'WishName': ('',),
            'setDNAString': (self.dna,),
            'setDISLid': (self.target,),
            'setUber': (self.uber,)
        }

        if self.pg > 0:
            if self.pg == 1:
                maxMoney = 50
                maxCarry = 25
                startingHood = 1000
                prevZones = [2000]
                questLimit = 3
                questTier = 4
                if self.uber == 1:
                    hp = 15
                else:
                    hp = 25
                experience = [600, 800]

            elif self.pg == 2:
                maxMoney = 60
                maxCarry = 30
                startingHood = 5000
                prevZones = [1000, 2000]
                questLimit = 3
                questTier = 7
                if self.uber == 1:
                    hp = 15
                elif self.uber == 2:
                    hp = 25
                else:
                    hp = 34
                experience = [1000, 2400]

            exp = Experience()

            for i, t in enumerate(self.trackAccess):
                if t:
                    chosenExp = random.randint(experience[0], experience[1])
                    exp.setExp(i, chosenExp)

            toonFields['setExperience'] = (exp.makeNetString(),)

            toonFields['setMaxMoney'] = (maxMoney,)
            toonFields['setMaxCarry'] = (maxCarry,)
            toonFields['setTrackAccess'] = (self.trackAccess,)
            toonFields['setDefaultZone'] = (startingHood,)
            toonFields['setHoodsVisited'] = (prevZones + [startingHood],)
            toonFields['setZonesVisited'] = (prevZones + [startingHood],)
            toonFields['setTeleportAccess'] = (prevZones,)
            toonFields['setQuestCarryLimit'] = (questLimit,)
            toonFields['setRewardHistory'] = (questTier, [])
            toonFields['setHp'] = (hp,)
            toonFields['setMaxHp'] = (hp,)
            toonFields['setTutorialAck'] = (1,)

        self.csm.air.dbInterface.createObject(
            self.csm.air.dbId,
            self.csm.air.dclassesByName['DistributedToonUD'],
            toonFields,
            self.__handleCreate)

    def __handleCreate(self, avId):
        if not avId:
            self.demand('Kill', 'Database failed to create the new avatar object!')
            return

        self.avId = avId
        self.demand('StoreAvatar')

    def enterStoreAvatar(self):
        # Associate the avatar with the account...
        self.avList[self.index] = self.avId
        self.csm.air.dbInterface.updateObject(
            self.csm.air.dbId,
            self.target,
            self.csm.air.dclassesByName['AccountUD'],
            {'ACCOUNT_AV_SET': self.avList},
            {'ACCOUNT_AV_SET': self.account['ACCOUNT_AV_SET']},
            self.__handleStoreAvatar)

    def __handleStoreAvatar(self, fields):
        if fields:
            self.demand('Kill', 'Database failed to associate the new avatar to your account!')
            return

        # Otherwise, we're done!
        self.csm.air.writeServerEvent('avatarCreated', self.avId, self.target, self.dna.encode('hex'), self.index)
        self.csm.sendUpdateToAccountId(self.target, 'createAvatarResp', [self.avId])
        self.demand('Off')


class AvatarOperationFSM(OperationFSM):
    POST_ACCOUNT_STATE = 'Off'  # This needs to be overridden.

    def enterRetrieveAccount(self):
        # Query the account:
        self.csm.air.dbInterface.queryObject(
            self.csm.air.dbId, self.target, self.__handleRetrieve)

    def __handleRetrieve(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['AccountUD']:
            self.demand('Kill', 'Your account object was not found in the database!')
            return

        self.account = fields

        self.avList = self.account['ACCOUNT_AV_SET']
        # Sanitize:
        self.avList = self.avList[:6]
        self.avList += [0] * (6-len(self.avList))

        self.demand(self.POST_ACCOUNT_STATE)


class GetAvatarsFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('GetAvatarsFSM')
    POST_ACCOUNT_STATE = 'QueryAvatars'

    def enterStart(self):
        self.demand('RetrieveAccount')

    def enterQueryAvatars(self):
        self.pendingAvatars = set()
        self.avatarFields = {}
        for avId in self.avList:
            if avId:
                self.pendingAvatars.add(avId)

                def response(dclass, fields, avId=avId):
                    if self.state != 'QueryAvatars':
                        return
                    if dclass != self.csm.air.dclassesByName['DistributedToonUD']:
                        self.demand('Kill', "One of the account's avatars is invalid!")
                        return
                    self.avatarFields[avId] = fields
                    self.pendingAvatars.remove(avId)
                    if not self.pendingAvatars:
                        self.demand('SendAvatars')

                self.csm.air.dbInterface.queryObject(
                    self.csm.air.dbId,
                    avId,
                    response)

        if not self.pendingAvatars:
            self.demand('SendAvatars')

    def enterSendAvatars(self):
        potentialAvs = []

        for avId, fields in self.avatarFields.items():
            index = self.avList.index(avId)
            wishNameState = fields.get('WishNameState', [''])[0]
            name = fields['setName'][0]
            nameState = 0

            if wishNameState == 'OPEN':
                nameState = 1
            elif wishNameState == 'PENDING':
                actualNameState = self.csm.accountDB.getNameStatus(avId)
                self.csm.air.dbInterface.updateObject(
                    self.csm.air.dbId,
                    avId,
                    self.csm.air.dclassesByName['DistributedToonUD'],
                    {'WishNameState': [actualNameState]}
                )
                if actualNameState == 'PENDING':
                    nameState = 2
                if actualNameState == 'APPROVED':
                    nameState = 3
                    name = fields['WishName'][0]
                elif actualNameState == 'REJECTED':
                    nameState = 4
                elif actualNameState == 'ERROR':
                    nameState = 2

                    self.csm.accountDB.addNameRequest(avId, fields['WishName'][0])
            elif wishNameState == 'APPROVED':
                nameState = 3
            elif wishNameState == 'REJECTED':
                nameState = 4

            potentialAvs.append([avId, name, fields['setDNAString'][0], index, nameState, fields['setHp'][0], fields['setMaxHp'][0], fields['setHat'], fields['setGlasses'], fields['setBackpack'], fields['setShoes']])

        self.csm.sendUpdateToAccountId(self.target, 'setAvatars', [potentialAvs])
        self.demand('Off')

# This inherits from GetAvatarsFSM, because the delete operation ends in a
# setAvatars message being sent to the client.
class DeleteAvatarFSM(GetAvatarsFSM):
    notify = directNotify.newCategory('DeleteAvatarFSM')
    POST_ACCOUNT_STATE = 'ProcessDelete'

    def enterStart(self, avId):
        self.avId = avId
        GetAvatarsFSM.enterStart(self)

    def enterProcessDelete(self):
        if self.avId not in self.avList:
            self.demand('Kill', 'Tried to delete an avatar not in the account!')
            return

        index = self.avList.index(self.avId)
        self.avList[index] = 0

        avsDeleted = list(self.account.get('ACCOUNT_AV_SET_DEL', []))
        avsDeleted.append([self.avId, int(time.time())])

        estateId = self.account.get('ESTATE_ID', 0)

        if estateId != 0:
            # This assumes that the house already exists, but it shouldn't
            # be a problem if it doesn't.
            self.csm.air.dbInterface.updateObject(
                self.csm.air.dbId,
                estateId,
                self.csm.air.dclassesByName['DistributedEstateAI'],
                {'setSlot%dToonId' % index: [0],
                 'setSlot%dGarden' % index: [[]]}
            )

        self.csm.air.dbInterface.updateObject(
            self.csm.air.dbId,
            self.target,
            self.csm.air.dclassesByName['AccountUD'],
            {'ACCOUNT_AV_SET': self.avList,
             'ACCOUNT_AV_SET_DEL': avsDeleted},
            {'ACCOUNT_AV_SET': self.account['ACCOUNT_AV_SET'],
             'ACCOUNT_AV_SET_DEL': self.account['ACCOUNT_AV_SET_DEL']},
            self.__handleDelete)
        self.csm.accountDB.removeNameRequest(self.avId)

    def __handleDelete(self, fields):
        if fields:
            self.demand('Kill', 'Database failed to mark the avatar as deleted!')
            return

        self.csm.air.friendsManager.clearList(self.avId)
        self.csm.air.writeServerEvent('avatarDeleted', self.avId, self.target)
        self.demand('QueryAvatars')

class SetNameTypedFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('SetNameTypedFSM')
    POST_ACCOUNT_STATE = 'RetrieveAvatar'

    def enterStart(self, avId, name):
        self.avId = avId
        self.name = name

        if self.avId:
            self.demand('RetrieveAccount')
            return

        # Hmm, self.avId was 0. Okay, let's just cut to the judging:
        self.demand('JudgeName')

    def enterRetrieveAvatar(self):
        if self.avId and self.avId not in self.avList:
            self.demand('Kill', 'Tried to name an avatar not in the account!')
            return

        self.csm.air.dbInterface.queryObject(self.csm.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        if fields['WishNameState'][0] != 'OPEN':
            self.demand('Kill', 'Avatar is not in a namable state!')
            return

        self.demand('JudgeName')

    def enterJudgeName(self):
        # Let's see if the name is valid:
        status = judgeName(self.name)

        if self.avId and status:
            resp = self.csm.accountDB.addNameRequest(self.avId, self.name)
            if resp != 'Success':
                status = False
            else:
                self.csm.air.dbInterface.updateObject(
                    self.csm.air.dbId,
                    self.avId,
                    self.csm.air.dclassesByName['DistributedToonUD'],
                    {'WishNameState': ('PENDING',),
                     'WishName': (self.name,)})

        if self.avId:
            self.csm.air.writeServerEvent('avatarWishname', self.avId, self.name)

        self.csm.sendUpdateToAccountId(self.target, 'setNameTypedResp', [self.avId, status])
        self.demand('Off')

class SetNamePatternFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('SetNamePatternFSM')
    POST_ACCOUNT_STATE = 'RetrieveAvatar'

    def enterStart(self, avId, pattern):
        self.avId = avId
        self.pattern = pattern

        self.demand('RetrieveAccount')

    def enterRetrieveAvatar(self):
        if self.avId and self.avId not in self.avList:
            self.demand('Kill', 'Tried to name an avatar not in the account!')
            return

        self.csm.air.dbInterface.queryObject(self.csm.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        if fields['WishNameState'][0] != 'OPEN':
            self.demand('Kill', 'Avatar is not in a namable state!')
            return

        self.demand('SetName')

    def enterSetName(self):
        # Render the pattern into a string:
        parts = []
        for p, f in self.pattern:
            part = self.csm.nameGenerator.nameDictionary.get(p, ('', ''))[1]
            if f:
                part = part[:1].upper() + part[1:]
            else:
                part = part.lower()
            parts.append(part)

        parts[2] += parts.pop(3) # Merge 2&3 (the last name) as there should be no space.
        while '' in parts:
            parts.remove('')
        name = ' '.join(parts)

        self.csm.air.dbInterface.updateObject(
            self.csm.air.dbId,
            self.avId,
            self.csm.air.dclassesByName['DistributedToonUD'],
            {'WishNameState': ('',),
             'WishName': ('',),
             'setName': (name,)})

        self.csm.air.writeServerEvent('avatarNamed', self.avId, name)
        self.csm.sendUpdateToAccountId(self.target, 'setNamePatternResp', [self.avId, 1])
        self.demand('Off')


class AcknowledgeNameFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('AcknowledgeNameFSM')
    POST_ACCOUNT_STATE = 'GetTargetAvatar'

    def enterStart(self, avId):
        self.avId = avId
        self.demand('RetrieveAccount')

    def enterGetTargetAvatar(self):
        # Make sure the target avatar is part of the account:
        if self.avId not in self.avList:
            self.demand('Kill', 'Tried to acknowledge name on an avatar not in the account!')
            return

        self.csm.air.dbInterface.queryObject(self.csm.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        # Process the WishNameState change.
        wishNameState = fields['WishNameState'][0]
        wishName = fields['WishName'][0]
        name = fields['setName'][0]

        if wishNameState == 'APPROVED':
            wishNameState = ''
            name = wishName
            wishName = ''
            self.csm.accountDB.removeNameRequest(self.avId)
        elif wishNameState == 'REJECTED':
            wishNameState = 'OPEN'
            wishName = ''
            self.csm.accountDB.removeNameRequest(self.avId)
        else:
            self.demand('Kill', "Tried to acknowledge name on an avatar in %s state!" % wishNameState)
            return

        # Push the change back through:
        self.csm.air.dbInterface.updateObject(
            self.csm.air.dbId,
            self.avId,
            self.csm.air.dclassesByName['DistributedToonUD'],
            {'WishNameState': (wishNameState,),
             'WishName': (wishName,),
             'setName': (name,)},
            {'WishNameState': fields['WishNameState'],
             'WishName': fields['WishName'],
             'setName': fields['setName']})

        self.csm.sendUpdateToAccountId(self.target, 'acknowledgeAvatarNameResp', [])
        self.demand('Off')


class LoadAvatarFSM(AvatarOperationFSM):
    notify = directNotify.newCategory('LoadAvatarFSM')
    POST_ACCOUNT_STATE = 'GetTargetAvatar'

    def enterStart(self, avId):
        self.avId = avId
        self.demand('RetrieveAccount')

    def enterGetTargetAvatar(self):
        # Make sure the target avatar is part of the account:
        if self.avId not in self.avList:
            self.demand('Kill', 'Tried to play an avatar not in the account!')
            return

        self.csm.air.dbInterface.queryObject(self.csm.air.dbId, self.avId,
                                             self.__handleAvatar)

    def __handleAvatar(self, dclass, fields):
        if dclass != self.csm.air.dclassesByName['DistributedToonUD']:
            self.demand('Kill', "One of the account's avatars is invalid!")
            return

        self.avatar = fields
        self.demand('SetAvatar')

    def enterSetAvatarTask(self, channel, task):
        # Finally, grant ownership and shut down.
        datagram = PyDatagram()
        datagram.addServerHeader(self.avId, self.csm.air.ourChannel, STATESERVER_OBJECT_SET_OWNER)
        datagram.addChannel(self.target<<32 | self.avId)
        self.csm.air.send(datagram)

        self.csm.air.writeServerEvent('avatarChosen', self.avId, self.target)
        self.demand('Off')
        return task.done

    def enterSetAvatar(self):
        channel = self.csm.GetAccountConnectionChannel(self.target)

        # First, give them a POSTREMOVE to unload the avatar, just in case they
        # disconnect while we're working.
        datagramCleanup = PyDatagram()
        datagramCleanup.addServerHeader(self.avId, channel, STATESERVER_OBJECT_DELETE_RAM)
        datagramCleanup.addUint32(self.avId)
        datagram = PyDatagram()
        datagram.addServerHeader( channel, self.csm.air.ourChannel, CLIENTAGENT_ADD_POST_REMOVE)
        datagram.addString(datagramCleanup.getMessage())
        self.csm.air.send(datagram)

        # Activate the avatar on the DBSS:
        self.csm.air.sendActivate(self.avId, 0, 0, self.csm.air.dclassesByName['DistributedToonUD'], {'setAdminAccess': \
            [self.account.get('ACCESS_LEVEL', 100)]})

        # Next, add them to the avatar channel:
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.csm.air.ourChannel, CLIENTAGENT_OPEN_CHANNEL)
        datagram.addChannel(self.csm.GetPuppetConnectionChannel(self.avId))
        self.csm.air.send(datagram)

        # Now set their sender channel to represent their account affiliation:
        datagram = PyDatagram()
        datagram.addServerHeader( channel, self.csm.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.target<<32 | self.avId)
        self.csm.air.send(datagram)

        # Eliminate race conditions.
        taskMgr.doMethodLater(0.2, self.enterSetAvatarTask, 'avatarTask-%s' % (self.avId), extraArgs=[channel],
            appendTask=True)

class UnloadAvatarFSM(OperationFSM):
    notify = directNotify.newCategory('UnloadAvatarFSM')

    def enterStart(self, avId):
        self.avId = avId

        # We don't even need to query the account, we know the avatar is being played!
        self.demand('UnloadAvatar')

    def enterUnloadAvatar(self):
        channel = self.csm.GetAccountConnectionChannel(self.target)

        self.csm.air.friendsManager.toonOffline(self.avId)

        # Clear off POSTREMOVE:
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.csm.air.ourChannel, CLIENTAGENT_CLEAR_POST_REMOVES)
        self.csm.air.send(datagram)

        # Remove avatar channel:
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.csm.air.ourChannel, CLIENTAGENT_CLOSE_CHANNEL)
        datagram.addChannel(self.csm.GetPuppetConnectionChannel(self.avId))
        self.csm.air.send(datagram)

        # Reset sender channel:
        datagram = PyDatagram()
        datagram.addServerHeader(channel, self.csm.air.ourChannel, CLIENTAGENT_SET_CLIENT_ID)
        datagram.addChannel(self.target<<32)
        self.csm.air.send(datagram)

        # Unload avatar object:
        datagram = PyDatagram()
        datagram.addServerHeader(self.avId, channel, STATESERVER_OBJECT_DELETE_RAM)
        datagram.addUint32(self.avId)
        self.csm.air.send(datagram)

        # Done!
        self.csm.air.writeServerEvent('avatarUnload', self.avId)
        self.demand('Off')

class ClientServicesManagerUD(DistributedObjectGlobalUD):
    notify = directNotify.newCategory('ClientServicesManagerUD')

    def __init__(self, air):
        DistributedObjectGlobalUD.__init__(self, air)

        # For processing name patterns.
        self.nameGenerator = NameGenerator()

        # Temporary HMAC key:
        self.key = 'oa1qt8fwc0r750gkse3fgt6k3scyhzptudk422u5'

        self.blacklistedHWIDs = []

    def announceGenerate(self):
        DistributedObjectGlobalUD.announceGenerate(self)

        # These keep track of the connection/account IDs currently undergoing an
        # operation on the CSM. This is to prevent (hacked) clients from firing up more
        # than one operation at a time, which could potentially lead to exploitation
        # of race conditions.
        self.connection2fsm = {}
        self.account2fsm = {}
        self.pendingLogins = {}

        # Instantiate our account DB interface:
        self.accountDB = LocalAccountDB(self)

    def killConnection(self, connId, reason):
        datagram = PyDatagram()
        datagram.addServerHeader(connId, self.air.ourChannel, CLIENTAGENT_EJECT)
        datagram.addUint16(122)
        datagram.addString(reason)
        self.air.send(datagram)

    def killConnectionFSM(self, connId):
        fsm = self.connection2fsm.get(connId)

        if not fsm:
            self.notify.warning('Tried to kill connection %d for duplicate FSM, but none exists!' % connId)
            return

        self.killConnection(connId, 'An operation is already underway')

    def killAccount(self, accountId, reason):
        self.killConnection(self.GetAccountConnectionChannel(accountId), reason)

    def killAccountFSM(self, accountId):
        fsm = self.account2fsm.get(accountId)
        if not fsm:
            self.notify.warning('Tried to kill account %d for duplicate FSM, but none exists!' % (accountId))
            return

        self.killAccount(accountId, 'An operation is already underway')

    def runAccountFSM(self, fsmtype, *args):
        sender = self.air.getAccountIdFromSender()

        if not sender:
            self.killAccount(sender, 'Client is not logged in.')

        if sender in self.account2fsm:
            self.killAccountFSM(sender)
            return

        self.account2fsm[sender] = fsmtype(self, sender)
        self.account2fsm[sender].request('Start', *args)

    def login(self, cookie, authKey):
        sender = self.air.getMsgSender()
        hwid = cookie.split("#")[1]
        backupCookie = cookie.split("#")[0]
        cookie = cookie.split("#")[0]
        self.pendingLogins[sender] = (sender, hwid, backupCookie, cookie, authKey)

        # CLIENTAGENT_GET_NETWORK_ADDRESS is defined in OtpDoGlobals for backwards compatibility with old versions of Panda3D
        datagram = PyDatagram()
        datagram.addServerHeader(sender, self.air.ourChannel, OtpDoGlobals.CLIENTAGENT_GET_NETWORK_ADDRESS)
        datagram.addUint32(sender)
        self.air.send(datagram)

    def completeLogin(self, context, ip):
        login = self.pendingLogins.get(context)
        if not login:
            return

        sender = login[0]
        hwid = login[1]
        backupCookie = login[2]
        cookie = login[3]
        authKey = login[4]
        apiKey = str(ConfigVariableString('ws-key', 'secretkey'))
        del self.pendingLogins[context]

        # Check if Current HWID Is Already Banned, or has a Ban assigned to it
        try:
            hwidCheck = httplib.HTTPSConnection('www.projectaltis.com')
            hwidCheck.request('GET', '/api/hwid/check/%s' % hwid)
            resp = json.loads(hwidCheck.getresponse().read())
            if resp["isBanned"] == "true":
                self.notify.debug("Banned HWID Has Tried Logging In!")
                if hwid not in self.blacklistedHWIDs:
                    self.killConnection(sender, "HWID Has been Banned Previously!")
                    self.blacklistedHWIDs.append(hwid)
                else:
                    return False
        except:
            self.notify.debug("Fatal Error during HWID Check")
            if hwid not in self.blacklistedHWIDs:
                self.killConnection(sender, "Fatal Error during HWID Check")
                self.blacklistedHWIDs.append(hwid)
            else:
                return False

        # Grab real token not one time fake token
        getRealToken = httplib.HTTPSConnection('www.projectaltis.com')
        getRealToken.request('GET', '/api/validatetoken?key=%s&t=%s' % (apiKey, cookie))
        try:
            getRealTokenResp = json.loads(getRealToken.getresponse().read())
            cookie = getRealTokenResp['additional']
        except:
            self.notify.debug("Fatal Error during Playtoken Resolve")
            self.killConnection(sender, "Fatal Error during Playtoken Resolve")
            return

        # Update the given token's HWID, as it's not banned
        try:
            hwidUpgradation = httplib.HTTPSConnection('www.projectaltis.com')
            hwidUpgradation.request('GET', '/api/hwid/setid/%s/%s/%s' % (apiKey, cookie, hwid))
            resp = json.loads(hwidUpgradation.getresponse().read())
        except:
            self.notify.debug("Fatal Error during HWID Upgradation")
            self.killConnection(sender, "Fatal Error during HWID Upgradation")

        self.notify.debug('Received login cookie %r from %d' % (cookie, sender))

        # Time to check this login to see if its authentic
        digest_maker = hmac.new(self.key)
        digest_maker.update(backupCookie)

        if not hmac.compare_digest(digest_maker.hexdigest(), authKey):
            # recieved a bad authentication key from the client, drop there connection!
            self.killConnection(sender, 'Failed to login, recieved a bad login cookie %s!' % (cookie))
            return

        if sender >> 32:
            self.killConnection(sender, 'Failed to login, client is already logged in.')
            return

        if sender in self.connection2fsm:
            self.killConnectionFSM(sender)
            return

        self.connection2fsm[sender] = LoginAccountFSM(self, sender)
        self.connection2fsm[sender].request('Start', cookie, ip)

    def requestAvatars(self):
        self.notify.debug('Received avatar list request from %d' % (self.air.getMsgSender()))
        self.runAccountFSM(GetAvatarsFSM)

    def requestMOTD(self):
        acc = self.air.getAccountIdFromSender()
        motd = '[SHOULD NOT SEE]'
        self.sendUpdateToAccountId(acc, 'setMOTD', [motd])

    def createAvatar(self, dna, index, uber, tracks, pg):
        self.runAccountFSM(CreateAvatarFSM, dna, index, uber, tracks, pg)

    def deleteAvatar(self, avId):
        self.runAccountFSM(DeleteAvatarFSM, avId)

    def setNameTyped(self, avId, name):
        self.runAccountFSM(SetNameTypedFSM, avId, name)

    def setNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4):
        self.runAccountFSM(SetNamePatternFSM, avId, [(p1, f1), (p2, f2), (p3, f3), (p4, f4)])

    def acknowledgeAvatarName(self, avId):
        self.runAccountFSM(AcknowledgeNameFSM, avId)

    def chooseAvatar(self, avId):
        currentAvId = self.air.getAvatarIdFromSender()
        accountId = self.air.getAccountIdFromSender()
        if currentAvId and avId:
            self.killAccount(accountId, 'A Toon is already chosen!')
            return
        elif not currentAvId and not avId:
            # This isn't really an error, the client is probably just making sure
            # none of its Toons are active.
            return

        if avId:
            self.runAccountFSM(LoadAvatarFSM, avId)
        else:
            self.runAccountFSM(UnloadAvatarFSM, currentAvId)
