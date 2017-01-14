from direct.directnotify import DirectNotifyGlobal
from toontown.cogdominium.DistCogdoGameAI import DistCogdoGameAI

class DistCogdoCraneGameAI(DistCogdoGameAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistCogdoCraneGameAI")

    def __init__(self, air):
        DistCogdoGameAI.__init__(self, air)

