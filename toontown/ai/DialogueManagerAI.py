from panda3d.core import *
from direct.directnotify import DirectNotifyGlobal 
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.chat.ChatGlobals import *
from otp.ai.MagicWordGlobal import *

class DialogueManagerAI():
    notify = DirectNotifyGlobal.directNotify.newCategory("DialogueManagerAI")

    def __init__(self, air):
        self.air = air
        self.currentNPCId = 0
        self.index = 0
        self.maxIndex = 1
        self.npc = None
        self.topic = None
        self.chat = None
        
    def requestDialogue(self, npc, topic, endPause=30):
        self.notify.info("Got dialouge request!")
        self.npc = npc
        self.maxIndex = len(TTLocalizer.toontownDialogues[topic][1, 2020])
        self.topic = topic
        self.loopChat()
        
    def loopChat(self):
        while self.index != self.maxIndex:
            self.setNPCDialouge(self.index)
            self.incrementIndex()
            continue
        
    def incrementIndex(self):
        self.notify.info("Increasing Index!")
        if self.index >= self.maxIndex:
            self.index = 0
        else:
            self.index += 1
        
    def setNPCDialouge(self, index):
        self.npc.b_setChat(self.topic, 1, 2020, index, CFSpeech | CFTimeout)
        
    def leaveDialogue(self, topic):
        if self.chat:
            self.notify.info("Ending Chat Sequence!")
            self.chat.finish()
            self.chat = None
    
    def testNPCChat(self):
        if self.npc:
            self.npc.b_setChat(self.topic, 1, 2020, 0, CFSpeech | CFTimeout)
            return "Test Worked!"
            
     
@magicWord(category=CATEGORY_PROGRAMMER)
def testDialouge():
    simbase.air.dialogueManager.testNPCChat()