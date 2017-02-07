from toontown.cogdominium import CogdoCraneGameConsts as Globals
from toontown.cogdominium.CogdoGameAudioManager import CogdoGameAudioManager

class CogdoCraneGame(DirectObject):
    notify = directNotify.newCategory('CogdoCraneGame')

    def __init__(self, distGame):
        self.distGame = distGame
        self.toonId2Player = {}
        self.players = []

    def _initAudio(self):
        self._audioMgr = CogdoGameAudioManager(Globals.MusicFiles, Globals.SfxFiles, camera, cutoff=Globals.AudioCutoff)

    def _destroyAudio(self):
        self._audioMgr.destroy()
        del self._audioMgr

    def load(self):
        self._initAudio()

    def unload(self):
        self._destroyAudio()
        del self.toonId2Player

    def onstage(self):
        pass

    def offstage(self):
        pass

    def startIntro(self):
        self._audioMgr.playMusic('normal')

    def endIntro(self):
        for player in self.players:
            self.placePlayer(player)
            if player.toon is localAvatar:
                localAvatar.sendCurrentPosition()

            player.request('Ready')

    def startFinish(self):
        pass

    def endFinish(self):
        pass

    def start(self):
        for player in self.players:
            player.handleGameStart()
            player.request('Normal')

    def exit(self):
        for player in self.players:
            player.request('Done')

    def _addPlayer(self, player):
        self.players.append(player)
        self.toonId2Player[player.toon.doId] = player

    def _removePlayer(self, player):
        if player in self.players:
            self.players.remove(player)
        else:
            for cPlayer in self.players:
                if cPlayer.toon == player.toon:
                    self.players.remove(cPlayer)
                    break

        if player.toon.doId in self.toonId2Player:
            del self.toonId2Player[player.toon.doId]

    def handleToonLeft(self, toonId):
        self._removePlayer(self.toonId2Player[toonId])