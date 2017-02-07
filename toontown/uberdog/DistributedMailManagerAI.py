from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectAI import DistributedObjectAI
from otp.ai.MagicWordGlobal import *
from toontown.parties.SimpleMailBase import SimpleMailBase

class DistributedMailManagerAI(DistributedObjectAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedMailManagerAI")
    
    def __init__(self, air):
        DistributedObjectAI.__init__(self, air)

    def sendSimpleMail(self, avId, senderId, contents):
        av = self.air.doId2do[avId]
        if not av:
            return
        avMail = av.getMail()
        msgId = len(avMail) + 1
        #TODO: Actually grab the real date. 
        mail = [msgId, senderId, 1, 29, 2003, contents]
        avMail.append(mail)
        av.setMail(avMail)

    def setNumMailItems(self, avId, amount):
        av = self.air.doId2do[avId]
        if not av:
            return
        av.setNumMailItems(amount)

@magicWord(category=CATEGORY_PROGRAMMER, types=[str])
def testSimpleMail(contents):
    invoker = spellbook.getInvoker()
    simbase.air.mailManager.sendSimpleMail(invoker.doId, invoker.doId, contents)
    return("Tested Simple Mail!")