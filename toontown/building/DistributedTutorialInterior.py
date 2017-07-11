import random
from toontown.toonbase.ToonBaseGlobal import *
from pandac.PandaModules import *
from direct.interval.IntervalGlobal import *
from direct.gui.DirectGui import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from toontown.dna.DNAParser import *
from toontown.building import ToonInterior
from direct.directnotify import DirectNotifyGlobal
from direct.distributed import DistributedObject
from toontown.building import ToonInteriorColors
from toontown.hood import ZoneUtil
from toontown.char import Char
from toontown.suit import SuitDNA
from toontown.suit import Suit
from toontown.quest import QuestParser
from toontown.toon import DistributedNPCSpecialQuestGiver
from toontown.toonbase import TTLocalizer
from toontown.chat.ChatGlobals import CFSpeech

class DistributedTutorialInterior(DistributedObject.DistributedObject):

    def announceGenerate(self):
        DistributedObject.DistributedObject.announceGenerate(self)

        if not base.cr.doFindAllInstances(DistributedNPCSpecialQuestGiver.DistributedNPCSpecialQuestGiver):
            self.acceptOnce('doneTutorialSetup', self.setup)
        else:
            self.setup()

    def disable(self):
        self.interior.removeNode()
        del self.interior
        self.street.removeNode()
        del self.street
        self.sky.removeNode()
        del self.sky
        self.ignore('enterTutorialInterior')

        DistributedObject.DistributedObject.disable(self)

    def randomDNAItem(self, category, findFunc):
        codeCount = self.dnaStore.getNumCatalogCodes(category)
        index = self.randomGenerator.randint(0, codeCount - 1)
        code = self.dnaStore.getCatalogCode(category, index)
        return findFunc(code)

    def replaceRandomInModel(self, model):
        baseTag = 'random_'
        npc = model.findAllMatches('**/' + baseTag + '???_*')
        for i in xrange(npc.getNumPaths()):
            np = npc.getPath(i)
            name = np.getName()
            b = len(baseTag)
            category = name[b + 4:]
            key1 = name[b]
            key2 = name[b + 1]
            if key1 == 'm':
                model = self.randomDNAItem(category, self.dnaStore.findNode)
                newNP = model.copyTo(np)
                c = render.findAllMatches('**/collision')
                c.stash()
                if key2 == 'r':
                    self.replaceRandomInModel(newNP)
            elif key1 == 't':
                texture = self.randomDNAItem(category, self.dnaStore.findTexture)
                np.setTexture(texture, 100)
                newNP = np
            if key2 == 'c':
                if category == 'TI_wallpaper' or category == 'TI_wallpaper_border':
                    self.randomGenerator.seed(self.zoneId)
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))
                else:
                    newNP.setColorScale(self.randomGenerator.choice(self.colors[category]))

    def setup(self):
        self.dnaStore = base.cr.playGame.dnaStore
        self.randomGenerator = random.Random()
        self.randomGenerator.seed(self.zoneId)
        self.interior = loader.loadModel('phase_3.5/models/modules/toon_interior_tutorial')
        self.interior.reparentTo(render)
        dnaStore = DNAStorage()
        node = loader.loadDNAFile(self.cr.playGame.hood.dnaStore, 'phase_3.5/dna/tutorial_street.pdna')
        self.street = render.attachNewNode(node)
        self.street.flattenMedium()
        self.street.setPosHpr(-17, 42, -0.5, 180, 0, 0)
        self.street.find('**/tb2:toon_landmark_TT_A1_DNARoot').stash()
        self.street.find('**/tb1:toon_landmark_hqTT_DNARoot/**/door_flat_0').stash()
        self.street.findAllMatches('**/+CollisionNode').stash()
        self.skyFile = 'phase_3.5/models/props/TT_sky'
        self.sky = loader.loadModel(self.skyFile)
        self.sky.setScale(0.8)
        self.sky.reparentTo(render)
        self.sky.setDepthTest(0)
        self.sky.setDepthWrite(0)
        self.sky.setBin('background', 100)
        self.sky.find('**/Sky').reparentTo(self.sky, -1)
        self.tutMusic = base.loader.loadMusic('phase_3.5/audio/bgm/tutorial_bgm.ogg')
        hoodId = ZoneUtil.getCanonicalHoodId(self.zoneId)
        self.colors = ToonInteriorColors.colors[hoodId]
        self.replaceRandomInModel(self.interior)
        doorModelName = 'door_double_round_ul'
        if doorModelName[-1:] == 'r':
            doorModelName = doorModelName[:-1] + 'l'
        else:
            doorModelName = doorModelName[:-1] + 'r'
        door = self.dnaStore.findNode(doorModelName)
        door_origin = render.find('**/door_origin;+s')
        doorNP = door.copyTo(door_origin)
        door_origin.setScale(0.8, 0.8, 0.8)
        door_origin.setPos(door_origin, 0, -0.025, 0)
        color = self.randomGenerator.choice(self.colors['TI_door'])
        DNADoor.setupDoor(doorNP, self.interior, door_origin, self.dnaStore, str(self.block), color)
        doorFrame = doorNP.find('door_*_flat')
        doorFrame.wrtReparentTo(self.interior)
        doorFrame.setColor(color)
        del self.colors
        del self.dnaStore
        del self.randomGenerator
        self.interior.flattenMedium()
        npcOrigin = self.interior.find('**/npc_origin_' + `(self.cr.doId2do[self.npcId].posIndex)`)
        if not npcOrigin.isEmpty():
            self.cr.doId2do[self.npcId].reparentTo(npcOrigin)
            self.cr.doId2do[self.npcId].clearMat()
        base.localAvatar.setPosHpr(-2, 12, 0, -10, 0, 0)
        self.tom = self.cr.doId2do[self.npcId]
        place = base.cr.playGame.getPlace()
        if place and hasattr(place, 'fsm') and place.fsm.getCurrentState().getName():
            self.notify.info('Tutorial movie: Place ready.')
            self.playMovie()
        else:
            self.notify.info('Tutorial movie: Waiting for place=%s, has fsm=%s' % (place, hasattr(place, 'fsm')))
            if hasattr(place, 'fsm'):
                self.notify.info('Tutorial movie: place state=%s' % place.fsm.getCurrentState().getName())
            self.acceptOnce('enterTutorialInterior', self.playMovie)

    def playMovie(self):
        self.notify.info('Tutorial movie: Play.')
        avHeight = max(base.localAvatar.getHeight(), 3.0)
        scaleFactor = avHeight * 0.3333333333
        self.logo = OnscreenImage(image = 'phase_3/maps/toontown-logo.png', pos = (-0.5, 0, 0), color = (1, 1, 1, 0), scale = (0.5, 0.5, 0.25))
        self.logo.setTransparency(TransparencyAttrib.MAlpha)
        self.movie = Sequence()
        self.movie.append(Parallel(Func(base.playMusic, self.tutMusic), Func(base.cr.playGame.getPlace().setState, 'stopped'), Func(base.transitions.fadeIn, 6.4), Wait(6.6)))
        self.movie.append(Sequence(Func(camera.wrtReparentTo, render), camera.posQuatInterval(1, (5, 9, self.tom.getHeight() - 0.5), (155, -2, 0), other=self.tom, blendType='easeInOut')))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting1 % base.localAvatar.getName(), CFSpeech))
        self.movie.append(Wait(5.1))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting2, CFSpeech))
        self.movie.append(Wait(7.3))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting3, CFSpeech))
        self.movie.append(Wait(4))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting4, CFSpeech))
        self.movie.append(Wait(6.5))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting5, CFSpeech))
        self.movie.append(Parallel(Func(base.transitions.fadeIn, 2), Wait(2), LerpFunc(self.adjustTransparency, fromData=0, toData=1, duration=2.5, blendType='noBlend')))
        self.movie.append(Wait(12.5))
        self.movie.append(LerpFunc(self.adjustTransparency, fromData=1, toData=0, duration=2.5, blendType='noBlend'))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting6, CFSpeech))
        self.movie.append(Wait(4))
        self.movie.append(Func(self.tom.setChatAbsolute, TTLocalizer.TutorialGreeting7, CFSpeech))
        self.movie.append(Sequence(Func(camera.wrtReparentTo, base.localAvatar), camera.posQuatInterval(1, (0, -9 * scaleFactor, avHeight), (0, 0, 0), other=base.localAvatar, blendType='easeInOut')))
        self.movie.append(Func(base.cr.playGame.getPlace().setState, 'walk'),)
        self.movie.start()
		
    def adjustTransparency(self, transparency):
        self.logo['color'] = (1, 1,1 , transparency)

    def setZoneIdAndBlock(self, zoneId, block):
        self.zoneId = zoneId
        self.block = block

    def setTutorialNpcId(self, npcId):
        self.npcId = npcId

    def getTutorialNpc(self):
        return self.cr.doId2do[self.npcId]
