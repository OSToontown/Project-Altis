import hmac
import httplib
import urllib
import json
from direct.directnotify.DirectNotifyGlobal import directNotify
from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from pandac.PandaModules import *
from otp.distributed.PotentialAvatar import PotentialAvatar
from otp.otpbase import OTPGlobals
from toontown.chat.ChatGlobals import WTSystem
from toontown.chat.WhisperPopup import WhisperPopup

class ClientServicesManager(DistributedObjectGlobal):
    notify = directNotify.newCategory('ClientServicesManager')

    def __init__(self, air):
        DistributedObjectGlobal.__init__(self, air)

    def performLogin(self, doneEvent):
        self.doneEvent = doneEvent

        params = urllib.urlencode({'u': base.launcher.getUsername(), 'p': base.launcher.getPassword()})
        headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "application/json"}

        conn = httplib.HTTPConnection('www.projectaltis.com')
        conn.request("POST", "/api/login", params, headers)
        conn2 = httplib.HTTPConnection('ip.42.pl')
        conn2.request("GET", "/raw")
        ip = conn2.getresponse().read()
        try:
            response = json.loads(str(conn.getresponse().read()))
            conn.close()
        except:
            self.notify.error('Failed to decode json login API response!')
            try:
                response = json.loads(str(conn.getresponse().read()))
                conn.close()
            except:
                self.notify.error('Failed to decode json login API response! (Second Time)')
                try:
                    response = json.loads(str(conn.getresponse().read()))
                    conn.close()
                except:
                    self.notify.error('Failed to decode json login API response! (Third Time)')
                    try:
                        response = json.loads(str(conn.getresponse().read()))
                        conn.close()
                    except:
                        return

        if response['status'] != 'true':
            # looks like we got a hacker!
            raise SystemExit
        else:
            # the request was successful, set the login cookie and login.
            cookie = response['additional']

        key = 'ed7dfd72f2a4e146e1421cda26737abf6435gfs4'
        digest_maker = hmac.new(key)
        digest_maker.update(cookie)
        import uuid
        cookie = cookie + ("#%s" % uuid.getnode())
        del uuid
        self.sendUpdate('login', [cookie, ip, digest_maker.hexdigest()])

    def acceptLogin(self, timestamp):
        messenger.send(self.doneEvent, [{'mode': 'success', 'timestamp': timestamp}])

    def requestAvatars(self):
        self.sendUpdate('requestAvatars')

        #self.sendUpdate('requestMOTD')

    def setMOTD(self, motd):
        base.cr.motdText = motd

    def setAvatars(self, avatars):
        avList = []
        for avNum, avName, avDNA, avPosition, nameState, hp, maxHp, hat, glasses, backpack, shoes in avatars:
            nameOpen = int(nameState == 1)
            names = [avName, '', '', '']
            if nameState == 2: # PENDING
                names[1] = avName
            elif nameState == 3: # APPROVED
                names[2] = avName
            elif nameState == 4: # REJECTED
                names[3] = avName
            avList.append(PotentialAvatar(avNum, names, avDNA, avPosition, nameOpen, hp = hp, maxHp = maxHp, hat = hat, glasses = glasses, backpack = backpack, shoes = shoes))

        self.cr.handleAvatarsList(avList)

    def sendCreateAvatar(self, avDNA, _, index, uber, tracks, pg):
        self.sendUpdate('createAvatar', [avDNA.makeNetString(), index, uber, tracks, pg])

    def createAvatarResp(self, avId):
        messenger.send('nameShopCreateAvatarDone', [avId])

    def sendDeleteAvatar(self, avId):
        self.sendUpdate('deleteAvatar', [avId])

    def sendSetNameTyped(self, avId, name, callback):
        self._callback = callback
        self.sendUpdate('setNameTyped', [avId, name])

    def setNameTypedResp(self, avId, status):
        self._callback(avId, status)

    def sendSetNamePattern(self, avId, p1, f1, p2, f2, p3, f3, p4, f4, callback):
        self._callback = callback
        self.sendUpdate('setNamePattern', [avId, p1, f1, p2, f2, p3, f3, p4, f4])

    def setNamePatternResp(self, avId, status):
        self._callback(avId, status)

    def sendAcknowledgeAvatarName(self, avId, callback):
        self._callback = callback
        self.sendUpdate('acknowledgeAvatarName', [avId])

    def acknowledgeAvatarNameResp(self):
        self._callback()

    def sendChooseAvatar(self, avId):
        self.sendUpdate('chooseAvatar', [avId])

    def systemMessage(self, message):
        whisper = WhisperPopup(message, OTPGlobals.getInterfaceFont(), WTSystem)
        whisper.manage(base.marginManager)

        if hasattr(base.cr, 'chatLog'):
            base.cr.chatLog.addToLog("\1orangeText\1System Message: %s\2" %(message))

        # play the system message sound effect
        base.playSfx(base.loader.loadSfx('phase_3/audio/sfx/clock03.ogg'))
