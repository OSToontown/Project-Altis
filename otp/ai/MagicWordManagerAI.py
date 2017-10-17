from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.ai.MagicWordGlobal import *
from direct.distributed.PyDatagram import PyDatagram
from direct.distributed.MsgTypes import *
from toontown.toon.DistributedToonAI import DistributedToonAI
import time
import datetime
import os
import raven

class MagicWordManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("MagicWordManagerAI")
    client = raven.Client('https://4e7951caa8ce4dd180a3bd032f645d71:6949b0a5d126453b92434392457d60dc@sentry.io/194824')

    def sendMagicWord(self, word, targetId):
        invokerId = self.air.getAvatarIdFromSender()
        invoker = self.air.doId2do.get(invokerId)

        if not isinstance(self.air.doId2do.get(targetId), DistributedToonAI):
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['Target is not a toon object!'])
            return

        if not invoker:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['missing invoker'])
            return
        now = time.strftime("%c")
        if invoker.getAdminAccess() < MINIMUM_MAGICWORD_ACCESS:
            self.air.writeServerEvent('suspicious', invokerId, 'Attempted to issue magic word: %s' % word)
            dg = PyDatagram()
            dg.addServerHeader(self.GetPuppetConnectionChannel(invokerId), self.air.ourChannel, CLIENTAGENT_EJECT)
            dg.addUint16(126)
            dg.addString('Magic Words are reserved for administrators only!')
            self.air.send(dg)
            return

        target = self.air.doId2do.get(targetId)
        if not target:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', ['missing target'])
            return

        response = spellbook.process(invoker, target, word)
        if response:
            self.sendUpdateToAvatarId(invokerId, 'sendMagicWordResponse', [response])

        self.air.writeServerEvent('magic-word',
                                  invokerId, invoker.getAdminAccess(),
                                  targetId, target.getAdminAccess(),
                                  word, response)

        if not os.path.exists('logs/mw'):
            os.makedirs('logs/mw')


        with open("logs/mw/magic-words.txt","a") as textFile:
            textFile.write("%s | %s : %s\n" % (now, invokerId, word))

        print("%s | %s : %s\n" % (now, invokerId, word))

        if os.getenv('DISTRICT_NAME', 'Test Canvas') == "Test Canvas":
            return
        baseword = word
        if ' ' in word:
            baseword = word.split()[0]

        self.client.tags_context({
            'WordUsed': baseword,
            'InvokerAvId': invokerId,
            'InvokerToonName': invoker.getName(),
            'TargetAvId': targetId,
            'TargetToonName': target.getName()
        })
        self.client.user_context({
            'InvokerAvId': invokerId,
            'InvokerToonName': invoker.getName(),
            'InvokerAccess': invoker.getAdminAccess(),
            'time': now,
            'TargetAvId': targetId,
            'TargetToonName': target.getName(),
            'TargetAccess': target.getAdminAccess(),
            'response': response
        })
        if invokerId != targetId:
            self.client.captureMessage('~~' + word)
        else:
            self.client.captureMessage('~' + word)

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[str])
def help(wordName=None):
    print 'help called with %s' % (wordName)
    if not wordName:
        return "What were you interested getting help for?"
    word = spellbook.words.get(wordName.lower())   # look it up by its lower case value
    if not word:
        accessLevel = spellbook.getInvoker().getAdminAccess()
        wname = wordName.lower()
        for key in spellbook.words:
            if spellbook.words.get(key).access <= accessLevel:
                if wname in key:
                    return 'Did you mean %s' % (spellbook.words.get(key).name)
        return 'I have no clue what %s is refering to' % (wordName)
    return word.doc

@magicWord(category=CATEGORY_COMMUNITY_MANAGER, types=[])
def words():
    accessLevel = spellbook.getInvoker().getAdminAccess()
    wordString = None
    for key in spellbook.words:
       word = spellbook.words.get(key)
       if word.access <= accessLevel:
           if wordString is None:
               wordString = key
           else:
               wordString += ", ";
               wordString += key;
    if wordString is None:
        return "You are chopped liver"
    else:
        return wordString
