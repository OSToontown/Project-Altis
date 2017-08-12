from pandac.PandaModules import *
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.coghq import DistributedCashbotBossCraneAI
from toontown.coghq import DistributedCashbotBossSafeAI
from toontown.suit import DistributedCashbotBossGoonAI
from toontown.coghq import DistributedCashbotBossTreasureAI
from toontown.battle import BattleExperienceAI
from toontown.chat import ResistanceChat
from direct.fsm import FSM
from toontown.suit import DistributedBossCogAI
from otp.avatar import DistributedAvatarAI
from toontown.suit import SuitDNA
import random
from otp.ai.MagicWordGlobal import *
from toontown.building import SuitBuildingGlobals
import math

class DistributedCashbotBossAI(DistributedBossCogAI.DistributedBossCogAI, FSM.FSM):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCashbotBossAI')
    maxGoons = 8

    def __init__(self, air):
        DistributedBossCogAI.DistributedBossCogAI.__init__(self, air, 'm')
        FSM.FSM.__init__(self, 'DistributedCashbotBossAI')
        self.cranes = None
        self.safes = None
        self.goons = None
        self.treasures = {}
        self.grabbingTreasures = {}
        self.recycledTreasures = []
        self.battleDifficulty = 0
        self.goonMinStrength = 7
        self.goonMaxStrength = 30
        self.healAmount = 0
        self.rewardId = ResistanceChat.getRandomId()
        self.rewardedToons = []
        self.scene = NodePath('scene')
        self.reparentTo(self.scene)
        cn = CollisionNode('walls')
        cs = CollisionSphere(0, 0, 0, 13)
        cn.addSolid(cs)
        cs = CollisionInvSphere(0, 0, 0, 42)
        cn.addSolid(cs)
        self.attachNewNode(cn)
        self.heldObject = None
        self.waitingForHelmet = 0
        self.avatarHelmets = {}
        self.bossMaxDamage = ToontownGlobals.CashbotBossMaxDamage
        self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage

    def generate(self):
        DistributedBossCogAI.DistributedBossCogAI.generate(self)
        if __dev__:
            self.scene.reparentTo(self.getRender())

    def getHoodId(self):
        return ToontownGlobals.CashbotHQ

    def formatReward(self):
        return str(self.rewardId)

    def makeBattleOneBattles(self):
        self.postBattleState = 'RollToBattleTwo'
        self.initializeBattles(1, ToontownGlobals.CashbotBossBattleOnePosHpr)

    def generateSuits(self, battleNumber):
        if battleNumber == 1:
            return self.invokeSuitPlanner(SuitBuildingGlobals.SUIT_PLANNER_CFO, 0)
        else:
            return self.invokeSuitPlanner(SuitBuildingGlobals.SUIT_PLANNER_CFO_SKELECOGS, 1)

    def removeToon(self, avId):
        if self.cranes != None:
            for crane in self.cranes:
                crane.removeToon(avId)

        if self.safes != None:
            for safe in self.safes:
                safe.removeToon(avId)

        if self.goons != None:
            for goon in self.goons:
                goon.removeToon(avId)

        DistributedBossCogAI.DistributedBossCogAI.removeToon(self, avId)

    def __makeBattleThreeObjects(self):
        if self.cranes == None:
            self.cranes = []
            for index in xrange(len(ToontownGlobals.CashbotBossCranePosHprs)):
                crane = DistributedCashbotBossCraneAI.DistributedCashbotBossCraneAI(self.air, self, index)
                crane.generateWithRequired(self.zoneId)
                self.cranes.append(crane)

        if self.safes == None:
            self.safes = []
            for index in xrange(len(ToontownGlobals.CashbotBossSafePosHprs)):
                safe = DistributedCashbotBossSafeAI.DistributedCashbotBossSafeAI(self.air, self, index)
                safe.generateWithRequired(self.zoneId)
                self.safes.append(safe)

        if self.goons == None:
            self.goons = []

    def __resetBattleThreeObjects(self):
        if self.cranes != None:
            for crane in self.cranes:
                crane.request('Free')

        if self.safes != None:
            for safe in self.safes:
                safe.request('Initial')

    def __deleteBattleThreeObjects(self):
        if self.cranes != None:
            for crane in self.cranes:
                crane.request('Off')
                crane.requestDelete()

            self.cranes = None
        if self.safes != None:
            for safe in self.safes:
                safe.request('Off')
                safe.requestDelete()

            self.safes = None
        if self.goons != None:
            for goon in self.goons:
                goon.request('Off')
                goon.requestDelete()

            self.goons = None

    def doNextAttack(self, task):
        self.__doDirectedAttack()
        if self.heldObject == None and not self.waitingForHelmet:
            self.waitForNextHelmet()

    def __doDirectedAttack(self):
        if self.toonsToAttack:
            toonId = self.toonsToAttack.pop(0)
            while toonId not in self.involvedToons:
                if not self.toonsToAttack:
                    self.b_setAttackCode(ToontownGlobals.BossCogNoAttack)
                    return
                toonId = self.toonsToAttack.pop(0)

            self.toonsToAttack.append(toonId)
            self.b_setAttackCode(ToontownGlobals.BossCogSlowDirectedAttack, toonId)

    def reprieveToon(self, avId):
        if avId in self.toonsToAttack:
            i = self.toonsToAttack.index(avId)
            del self.toonsToAttack[i]
            self.toonsToAttack.append(avId)

    def makeTreasure(self, goon):
        if self.state != 'BattleThree':
            return
        pos = goon.getPos(self)
        v = Vec3(pos[0], pos[1], 0.0)
        if not v.normalize():
            v = Vec3(1, 0, 0)
        v = v * 27
        angle = random.uniform(0.0, 2.0 * math.pi)
        radius = 10
        dx = radius * math.cos(angle)
        dy = radius * math.sin(angle)
        fpos = self.scene.getRelativePoint(self, Point3(v[0] + dx, v[1] + dy, 0))
        if goon.strength <= 10:
            style = random.choice([ToontownGlobals.ToontownCentral, ToontownGlobals.DonaldsDock, ToontownGlobals.DaisyGardens, ToontownGlobals.MinniesMelodyland])
            healAmount = 4
        elif goon.strength <= 15:
            style = random.choice([ToontownGlobals.DonaldsDock, ToontownGlobals.DaisyGardens, ToontownGlobals.MinniesMelodyland])
            healAmount = 10
        else:
            style = random.choice([ToontownGlobals.TheBrrrgh, ToontownGlobals.DonaldsDreamland])
            healAmount = 12
        if self.recycledTreasures:
            treasure = self.recycledTreasures.pop(0)
            treasure.d_setGrab(0)
            treasure.b_setGoonId(goon.doId)
            treasure.b_setStyle(style)
            treasure.b_setPosition(pos[0], pos[1], 0)
            treasure.b_setFinalPosition(fpos[0], fpos[1], 0)
        else:
            treasure = DistributedCashbotBossTreasureAI.DistributedCashbotBossTreasureAI(self.air, self, goon, style, fpos[0], fpos[1], 0)  
            treasure.generateWithRequired(self.zoneId)
        treasure.healAmount = healAmount
        self.treasures[treasure.doId] = treasure

    def grabAttempt(self, avId, treasureId):
        av = self.air.doId2do.get(avId)
        if not av:
            return
        treasure = self.treasures.get(treasureId)
        if treasure:
            if treasure.validAvatar(av):
                del self.treasures[treasureId]
                treasure.d_setGrab(avId)
                self.grabbingTreasures[treasureId] = treasure
                taskMgr.doMethodLater(5, self.__recycleTreasure, treasure.uniqueName('recycleTreasure'), extraArgs=[treasure])
            else:
                treasure.d_setReject()

    def __recycleTreasure(self, treasure):
        if treasure.doId in self.grabbingTreasures:
            del self.grabbingTreasures[treasure.doId]
            self.recycledTreasures.append(treasure)

    def deleteAllTreasures(self):
        for treasure in self.treasures.values():
            treasure.requestDelete()

        self.treasures = {}
        for treasure in self.grabbingTreasures.values():
            taskMgr.remove(treasure.uniqueName('recycleTreasure'))
            treasure.requestDelete()

        self.grabbingTreasures = {}
        for treasure in self.recycledTreasures:
            treasure.requestDelete()

        self.recycledTreasures = []

    def getMaxGoons(self):
        t = self.getBattleThreeTime()
        if t <= 1.0:
            return self.maxGoons
        elif t <= 1.1:
            return self.maxGoons + 1
        elif t <= 1.2:
            return self.maxGoons + 2
        elif t <= 1.3:
            return self.maxGoons + 3
        elif t <= 1.4:
            return self.maxGoons + 4
        else:
            return self.maxGoons + 8

    def makeGoon(self, side = None):
        if side == None:
            side = random.choice(['EmergeA', 'EmergeB'])
        goon = self.__chooseOldGoon()
        if goon == None:
            if len(self.goons) >= self.getMaxGoons():
                return
            goon = DistributedCashbotBossGoonAI.DistributedCashbotBossGoonAI(self.air, self)
            goon.generateWithRequired(self.zoneId)
            self.goons.append(goon)
        if self.getBattleThreeTime() > 1.0:
            goon.STUN_TIME = 4
            goon.b_setupGoon(velocity=8, hFov=90, attackRadius=20, strength=self.goonMaxStrength, scale=2.0)
        else:
            goon.STUN_TIME = self.progressValue(30, 8)
            goon.b_setupGoon(velocity=self.progressRandomValue(3, 7), hFov=self.progressRandomValue(70, 80), attackRadius=self.progressRandomValue(6, 15), strength=int(self.progressRandomValue(self.goonMinStrength, self.goonMaxStrength)), scale=self.progressRandomValue(self.goonMinScale, self.goonMaxScale))
        goon.request(side)

    def __chooseOldGoon(self):
        for goon in self.goons:
            if goon.state == 'Off':
                return goon

    def waitForNextGoon(self, delayTime):
        currState = self.getCurrentOrNextState()
        if currState == 'BattleThree':
            taskName = self.uniqueName('NextGoon')
            taskMgr.remove(taskName)
            taskMgr.doMethodLater(delayTime, self.doNextGoon, taskName)

    def stopGoons(self):
        taskName = self.uniqueName('NextGoon')
        taskMgr.remove(taskName)

    def doNextGoon(self, task):
        if self.attackCode != ToontownGlobals.BossCogDizzy:
            self.makeGoon()
        delayTime = self.progressValue(10, 2)
        self.waitForNextGoon(delayTime)

    def waitForNextHelmet(self):
        currState = self.getCurrentOrNextState()
        if currState == 'BattleThree':
            taskName = self.uniqueName('NextHelmet')
            taskMgr.remove(taskName)
            delayTime = self.progressValue(45, 15)
            taskMgr.doMethodLater(delayTime, self.__donHelmet, taskName)
            self.waitingForHelmet = 1

    def __donHelmet(self, task):
        self.waitingForHelmet = 0
        if self.heldObject == None:
            safe = self.safes[0]
            safe.request('Grabbed', self.doId, self.doId)
            self.heldObject = safe

    def stopHelmets(self):
        self.waitingForHelmet = 0
        taskName = self.uniqueName('NextHelmet')
        taskMgr.remove(taskName)

    def acceptHelmetFrom(self, avId):
        now = globalClock.getFrameTime()
        then = self.avatarHelmets.get(avId, None)
        if then == None or now - then > 300:
            self.avatarHelmets[avId] = now
            return 1
        return 0

    def magicWordHit(self, damage, avId):
        if self.heldObject:
            self.heldObject.demand('Dropped', avId, self.doId)
            self.heldObject.avoidHelmet = 1
            self.heldObject = None
            self.waitForNextHelmet()
        else:
            self.recordHit(damage)

    def magicWordReset(self):
        if self.state == 'BattleThree':
            self.__resetBattleThreeObjects()

    def magicWordResetGoons(self):
        if self.state == 'BattleThree':
            if self.goons != None:
                for goon in self.goons:
                    goon.request('Off')
                    goon.requestDelete()

                self.goons = None
            self.__makeBattleThreeObjects()

    def recordHit(self, damage):
        avId = self.air.getAvatarIdFromSender()
        if not self.validate(avId, avId in self.involvedToons, 'recordHit from unknown avatar'):
            return
        if self.state != 'BattleThree':
            return
        self.b_setBossDamage(self.bossDamage + damage)
        healthDisp = int(self.bossMaxDamage - self.bossDamage)
        if healthDisp < 0:
           healthDisp = 0
        self.setHealthTag(str(healthDisp) + '/' + str(int(self.bossMaxDamage)))
        if self.bossDamage >= self.bossMaxDamage:
            self.b_setState('Victory')
        elif self.attackCode != ToontownGlobals.BossCogDizzy:
            if damage >= self.knockoutDamage:
                self.b_setAttackCode(ToontownGlobals.BossCogDizzy)
                self.stopHelmets()
            else:
                self.b_setAttackCode(ToontownGlobals.BossCogNoAttack)
                self.stopHelmets()
                self.waitForNextHelmet()

    def b_setBossDamage(self, bossDamage):
        self.d_setBossDamage(bossDamage)
        self.setBossDamage(bossDamage)

    def setBossDamage(self, bossDamage):
        self.reportToonHealth()
        self.bossDamage = bossDamage

    def d_setBossDamage(self, bossDamage):
        self.sendUpdate('setBossDamage', [bossDamage])

    def d_setRewardId(self, rewardId):
        self.sendUpdate('setRewardId', [rewardId])

    def applyReward(self):
        avId = self.air.getAvatarIdFromSender()
        if avId in self.involvedToons and avId not in self.rewardedToons:
            self.rewardedToons.append(avId)
            toon = self.air.doId2do.get(avId)
            if toon:
                toon.doResistanceEffect(self.rewardId)

            if simbase.config.GetBool('cfo-staff-event', False):

                withStaff = False
                for avId in self.involvedToons:
                    av = self.air.doId2do.get(avId)
                    if av:
                        if av.adminAccess > 100:
                            withStaff = True

                if withStaff:
                    participants = simbase.backups.load('cfo-staff-event', ('participants',), default={'doIds': []})
                    if avId not in participants['doIds']:
                        participants['doIds'].append(toon.doId)
                    simbase.backups.save('cfo-staff-event', ('participants',), participants)

    def enterOff(self):
        DistributedBossCogAI.DistributedBossCogAI.enterOff(self)
        self.rewardedToons = []

    def exitOff(self):
        DistributedBossCogAI.DistributedBossCogAI.exitOff(self)

    def enterIntroduction(self):
        DistributedBossCogAI.DistributedBossCogAI.enterIntroduction(self)
        self.__makeBattleThreeObjects()
        self.__resetBattleThreeObjects()
        self.calcAndSetBattleDifficulty()

    def exitIntroduction(self):
        DistributedBossCogAI.DistributedBossCogAI.exitIntroduction(self)
        self.__deleteBattleThreeObjects()
        
    def makeBattleTwoBattles(self):
        self.postBattleState = 'PrepareBattleThree'
        self.initializeBattles(2, ToontownGlobals.CashbotBossBattleThreePosHpr)
        
    def enterPrepareBattleTwo(self):
        self.barrier = self.beginBarrier('PrepareBattleTwo', self.involvedToons, 45, self.__donePrepareBattleTwo)
        self.divideToons()
        self.makeBattleTwoBattles()
        self.__makeBattleThreeObjects()
        self.__resetBattleThreeObjects()
        self.calcAndSetBattleDifficulty()
        
    def __donePrepareBattleTwo(self, avIds):
        self.b_setState('BattleTwo')

    def exitPrepareBattleTwo(self):
        self.ignoreBarrier(self.barrier)
        self.__deleteBattleThreeObjects()
		
    def enterRollToBattleTwo(self):
        self.barrier = self.beginBarrier('RollToBattleTwo', self.involvedToons, 1, self.__doneRollToBattleTwo)
        
    def __doneRollToBattleTwo(self, avIds):
        self.b_setState('PrepareBattleTwo')

    def exitRollToBattleTwo(self):
        self.ignoreBarrier(self.barrier)
        
    def enterBattleTwo(self):
        if self.battleA:
            self.battleA.startBattle(self.toonsA, self.suitsA)
        if self.battleB:
            self.battleB.startBattle(self.toonsB, self.suitsB)

    def exitBattleTwo(self):
        self.resetBattles()

    def enterPrepareBattleThree(self):
        self.resetBattles()
        self.__makeBattleThreeObjects()
        self.__resetBattleThreeObjects()
        self.calcAndSetBattleDifficulty()
        self.barrier = self.beginBarrier('PrepareBattleThree', self.involvedToons, 55, self.__donePrepareBattleThree)

    def __donePrepareBattleThree(self, avIds):
        self.b_setState('BattleThree')

    def exitPrepareBattleThree(self):
        if self.newState != 'BattleThree':
            self.__deleteBattleThreeObjects()
        self.ignoreBarrier(self.barrier)

    def enterBattleThree(self):
        self.setPosHpr(*ToontownGlobals.CashbotBossBattleThreePosHpr)
        self.__makeBattleThreeObjects()
        self.__resetBattleThreeObjects()
        self.reportToonHealth()
        self.toonsToAttack = self.involvedToons[:]
        random.shuffle(self.toonsToAttack)
        self.b_setBossDamage(0)
        self.battleThreeStart = globalClock.getFrameTime()
        self.resetBattles()
        self.waitForNextAttack(15)
        self.waitForNextHelmet()
        self.makeGoon(side='EmergeA')
        self.makeGoon(side='EmergeB')
        taskName = self.uniqueName('NextGoon')
        taskMgr.remove(taskName)
        taskMgr.doMethodLater(2, self.__doInitialGoons, taskName)
		
    def getToonDifficulty(self):
        totalCogSuitTier = 0
        totalToons = 0

        for toonId in self.involvedToons:
            toon = simbase.air.doId2do.get(toonId)
            if toon:
                totalToons += 1
                totalCogSuitTier += toon.cogTypes[2]

        averageTier = math.floor(totalCogSuitTier / totalToons) + 1
        return int(averageTier)
		
    def b_setBonusUnites(self, unites):
        self.setBonusUnites(unites)
        self.d_setBonusUnites(unites)

    def setBonusUnites(self, unites):
        self.bonusUnites = unites

    def d_setBonusUnites(self, unites):
        self.sendUpdate('setBonusUnites', [unites])

    def calcAndSetBattleDifficulty(self):
        self.toonLevels = self.getToonDifficulty()
        battleDifficulty = int(self.toonLevels)
        self.b_setBattleDifficulty(battleDifficulty)
        self.recalcDifficulty()
		
    def recalcDifficulty(self):
        if self.battleDifficulty >= 7:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage*3.2)
            self.goonMinStrength = 10
            self.goonMaxStrength = 43
            self.goonMinScale = 0.8
            self.goonMaxScale = 2.6
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage * 2
            self.b_setBonusUnites(2)
        elif self.battleDifficulty >= 6:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage*2.9)
            self.goonMinStrength = 10
            self.goonMaxStrength = 41
            self.goonMinScale = 0.8
            self.goonMaxScale = 2.5
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage * 1.8
            self.b_setBonusUnites(2)
        elif self.battleDifficulty >= 5:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage*2.5)
            self.goonMinStrength = 10
            self.goonMaxStrength = 39
            self.goonMinScale = 0.8
            self.goonMaxScale = 2.4
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage * 1.6
            self.b_setBonusUnites(1)
        elif self.battleDifficulty >= 4:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage*2)
            self.goonMinStrength = 8
            self.goonMaxStrength = 38
            self.goonMinScale = 0.6
            self.goonMaxScale = 2.4
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage * 1.4
            self.b_setBonusUnites(1)
        elif self.battleDifficulty >= 3:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage*1.5)
            self.goonMinStrength = 8
            self.goonMaxStrength = 36
            self.goonMinScale = 0.6
            self.goonMaxScale = 2.2
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage * 1.3
            self.b_setBonusUnites(1)
        elif self.battleDifficulty >= 2:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage*1.2)
            self.goonMinStrength = 5
            self.goonMaxStrength = 35
            self.goonMinScale = 0.5
            self.goonMaxScale = 2.1
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage * 1.2
            self.b_setBonusUnites(0)
        else:
            self.b_setMaxHp(ToontownGlobals.CashbotBossMaxDamage)
            self.goonMinStrength = 3
            self.goonMaxStrength = 32
            self.goonMinScale = 0.3
            self.goonMaxScale = 1.7
            self.knockoutDamage = ToontownGlobals.CashbotBossKnockoutDamage
            self.b_setBonusUnites(0)

    def b_setBattleDifficulty(self, batDiff):
        self.setBattleDifficulty(batDiff)
        self.d_setBattleDifficulty(batDiff)

    def setBattleDifficulty(self, batDiff):
        self.battleDifficulty = batDiff

    def d_setBattleDifficulty(self, batDiff):
        self.sendUpdate('setBattleDifficulty', [batDiff])

    def b_setMaxHp(self, hp):
        self.setMaxHp(hp)
        self.d_setMaxHp(hp)

    def setMaxHp(self, hp):
        self.bossMaxDamage = hp

    def d_setMaxHp(self, hp):
        self.sendUpdate('setMaxHp', [hp])        

    def __doInitialGoons(self, task):
        self.makeGoon(side='EmergeA')
        self.makeGoon(side='EmergeB')
        self.waitForNextGoon(10)

    def exitBattleThree(self):
        helmetName = self.uniqueName('helmet')
        taskMgr.remove(helmetName)
        if self.newState != 'Victory':
            self.__deleteBattleThreeObjects()
        self.deleteAllTreasures()
        self.stopAttacks()
        self.stopGoons()
        self.stopHelmets()
        self.heldObject = None

    def enterVictory(self):
        self.resetBattles()
        self.suitsKilled.append({'type': None,
         'level': None,
         'track': self.dna.dept,
         'isSkelecog': 0,
         'isForeman': 0,
         'isBoss': 1,
         'isSupervisor': 0,
         'isVirtual': 0,
         'isElite': 0,
         'activeToons': self.involvedToons[:]})
        self.barrier = self.beginBarrier('Victory', self.involvedToons, 30, self.__doneVictory)

    def __doneVictory(self, avIds):
        self.d_setBattleExperience()
        self.b_setState('Reward')
        BattleExperienceAI.assignRewards(self.involvedToons, self.toonSkillPtsGained, self.suitsKilled, ToontownGlobals.dept2cogHQ(self.dept), self.helpfulToons)
        for toonId in self.involvedToons:
            toon = self.air.doId2do.get(toonId)
            if toon:
                toon.addResistanceMessage(self.rewardId)
                if self.bonusUnites:
                    for x in xrange(self.bonusUnites):
                        toon.addResistanceMessage(ResistanceChat.getRandomId())
                toon.b_promote(self.deptIndex)
                toon.addStat(ToontownGlobals.STATS_CFO)
                simbase.air.questManager.toonDefeatedBoss(toon, ToontownGlobals.dept2cogHQ(self.dept), self.dna.dept, self.involvedToons)
            if len(self.involvedToons[:]) == 1 and self.begunSolo:
                isSolo = 1
            else:
                isSolo = 0
            self.air.achievementsManager.cfo(toonId, solo = isSolo)

    def exitVictory(self):
        self.__deleteBattleThreeObjects()

    def enterEpilogue(self):
        DistributedBossCogAI.DistributedBossCogAI.enterEpilogue(self)
        self.d_setRewardId(self.rewardId)


@magicWord(category=CATEGORY_ADMINISTRATOR)
def restartCraneRound():
    """
    Restarts the crane round in the CFO.
    """
    invoker = spellbook.getInvoker()
    boss = None
    for do in simbase.air.doId2do.values():
        if isinstance(do, DistributedCashbotBossAI):
            if invoker.doId in do.involvedToons:
                boss = do
                break
    if not boss:
        return "You aren't in a CFO!"
    boss.exitIntroduction()
    boss.b_setState('PrepareBattleThree')
    boss.b_setState('BattleThree')
    return 'Restarting the crane round...'


@magicWord(category=CATEGORY_ADMINISTRATOR)
def skipCFO():
    """
    Skips to the final round of the CFO.
    """
    invoker = spellbook.getInvoker()
    boss = None
    for do in simbase.air.doId2do.values():
        if isinstance(do, DistributedCashbotBossAI):
            if invoker.doId in do.involvedToons:
                boss = do
                break
    if not boss:
        return "You aren't in a CFO!"
    if boss.state in ('PrepareBattleThree', 'BattleThree'):
        return "You can't skip this round."
    boss.exitIntroduction()
    boss.b_setState('PrepareBattleThree')
    return 'Skipping the first round...'

@magicWord(category=CATEGORY_PROGRAMMER)
def cfo2():
    """
    Skips to the final round of the CFO.
    """
    invoker = spellbook.getInvoker()
    boss = None
    for do in simbase.air.doId2do.values():
        if isinstance(do, DistributedCashbotBossAI):
            if invoker.doId in do.involvedToons:
                boss = do
                break
    if not boss:
        return "You aren't in a CFO!"
    boss.exitIntroduction()
    boss.b_setState('PrepareBattleTwo')
    return 'Skipping the first round...'

@magicWord(category=CATEGORY_PROGRAMMER)
def killCFO():
    """
    Kills the CFO.
    """
    invoker = spellbook.getInvoker()
    boss = None
    for do in simbase.air.doId2do.values():
        if isinstance(do, DistributedCashbotBossAI):
            if invoker.doId in do.involvedToons:
                boss = do
                break
    if not boss:
        return "You aren't in a CFO!"
    boss.b_setState('Victory')
    return 'Killed CFO.'
