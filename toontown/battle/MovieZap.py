from direct.interval.IntervalGlobal import *
from BattleBase import *
from BattleProps import *
from BattleSounds import *
from toontown.toon.ToonDNA import *
from toontown.suit.SuitDNA import *
import MovieUtil
import MovieNPCSOS
import MovieCamera
from direct.directnotify import DirectNotifyGlobal
import BattleParticles
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
import random
notify = DirectNotifyGlobal.directNotify.newCategory('MovieZap')
hitSoundFiles = ('AA_tesla.ogg', 'AA_carpet.ogg', 'AA_balloon.ogg', 'AA_tesla.ogg', 'AA_tesla.ogg', 'AA_tesla.ogg', 'AA_lightning.ogg')
missSoundFiles = ('AA_tesla_miss.ogg', 'AA_carpet.ogg', 'AA_balloon_miss.ogg', 'AA_tesla_miss.ogg', 'AA_tesla_miss.ogg', 'AA_tesla_miss.ogg', 'AA_lightning_miss.ogg')
sprayScales = [0.2,
 0.3,
 0.1,
 0.6,
 0.8,
 1.0,
 2.0]
WaterSprayColor = Point4(1.0, 1.0, 0, 1.0)
zapPos = Point3(0, 0, 0)
zapHpr = Vec3(0, 0, 0)

def doZaps(zaps):
    if len(zaps) == 0:
        return (None, None)

    suitZapsDict = {}
    doneUber = 0
    skip = 0
    for zap in zaps:
        skip = 0
        if skip:
            pass
        elif type(zap['target']) == type([]):
            if 1:
                target = zap['target'][0]
                suitId = target['suit'].doId
                if suitId in suitZapsDict:
                    suitZapsDict[suitId].append(zap)
                else:
                    suitZapsDict[suitId] = [zap]
        else:
            suitId = zap['target']['suit'].doId
            if suitId in suitZapsDict:
                suitZapsDict[suitId].append(zap)
            else:
                suitZapsDict[suitId] = [zap]

    suitZaps = suitZapsDict.values()

    def compFunc(a, b):
        if len(a) > len(b):
            return 1
        elif len(a) < len(b):
            return -1
        return 0
    suitZaps.sort(compFunc)

    delay = 0.0

    mtrack = Parallel()
    for st in suitZaps:
        if len(st) > 0:
            ival = __doSuitZaps(st)
            if ival:
                mtrack.append(Sequence(Wait(delay), ival))
            delay = delay + TOON_ZAP_SUIT_DELAY
    npcArrivals, npcDepartures, npcs = MovieNPCSOS.doNPCTeleports(zaps)
    enterDuration = npcArrivals.getDuration()
    exitDuration = npcDepartures.getDuration()
    camDuration = mtrack.getDuration()
    camTrack = MovieCamera.chooseLureShot(zaps, camDuration, enterDuration, exitDuration)
    return (mtrack, camTrack)


def __doSuitZaps(zaps):
    uberClone = 0
    toonTracks = Parallel()
    delay = 0.0
    if type(zaps[0]['target']) == type([]):
        for target in zaps[0]['target']:
            if len(zaps) == 1 and target['hp'] > 0:
                fShowStun = 1
            else:
                fShowStun = 0

    elif len(zaps) == 1 and zaps[0]['target']['hp'] > 0:
        fShowStun = 1
    else:
        fShowStun = 0
    for s in zaps:
        tracks = __doZap(s, delay, fShowStun, uberClone)
        if s['level'] >= ToontownBattleGlobals.UBER_GAG_LEVEL_INDEX:
            uberClone = 1
        if tracks:
            for track in tracks:
                toonTracks.append(track)

        delay = delay + TOON_ZAP_DELAY

    return toonTracks


def __doZap(zap, delay, fShowStun, uberClone = 0):
    zapSequence = Sequence(Wait(delay))
    if type(zap['target']) == type([]):
        for target in zap['target']:
            notify.debug('toon: %s zaps prop: %d at suit: %d for hp: %d' % (zap['toon'].getName(),
             zap['level'],
             target['suit'].doId,
             target['hp']))

    else:
        notify.debug('toon: %s zaps prop: %d at suit: %d for hp: %d' % (zap['toon'].getName(),
         zap['level'],
         zap['target']['suit'].doId,
         zap['target']['hp']))
    if uberClone:
        ival = zapfn_array[zap['level']](zap, delay, fShowStun, uberClone)
        if ival:
            zapSequence.append(ival)
    else:
        ival = zapfn_array[zap['level']](zap, delay, fShowStun)
        if ival:
            zapSequence.append(ival)
    return [zapSequence]


def __suitTargetPoint(suit):
    pnt = suit.getPos(render)
    pnt.setZ(pnt[2] + suit.getHeight() * 0.66)
    return Point3(pnt)

def __getSuitTrack(suit, tContact, tDodge, hp, hpbonus, kbbonus, anim, died, leftSuits, rightSuits, battle, toon, fShowStun, beforeStun = 0.5, afterStun = 1.8, geyser = 0, uberRepeat = 0, revived = 0):
    if hp > 0:
        suitTrack = Sequence()
        sival = ActorInterval(suit, anim)
        sival = []
        if fShowStun == 1:
            sival = Parallel(Func(suit.loop, anim), MovieUtil.zapCog(suit, beforeStun, afterStun))
        else:
            sival = ActorInterval(suit, anim)
        showDamage = Func(suit.showHpText, -hp, openEnded=0, attackTrack=ZAP_TRACK)
        updateHealthBar = Func(suit.updateHealthBar, hp)
        suitTrack.append(Wait(tContact))
        suitTrack.append(showDamage)
        suitTrack.append(updateHealthBar)
        if not geyser:
            suitTrack.append(sival)
        elif not uberRepeat:
            geyserMotion = Sequence(sUp, Wait(0.0), sDown)
            suitLaunch = Parallel(sival, geyserMotion)
            suitTrack.append(suitLaunch)
        else:
            suitTrack.append(Wait(5.5))
        bonusTrack = Sequence(Wait(tContact))
        if kbbonus > 0:
            bonusTrack.append(Wait(0.75))
            bonusTrack.append(Func(suit.showHpText, -kbbonus, 2, openEnded=0, attackTrack=THROW_TRACK))
            bonusTrack.append(updateHealthBar)
        if hpbonus > 0:
            bonusTrack.append(Wait(0.75))
            bonusTrack.append(Func(suit.showHpText, -hpbonus, 1, openEnded=0, attackTrack=THROW_TRACK))
            bonusTrack.append(updateHealthBar)
        if died != 0:
            suitTrack.append(MovieUtil.createSuitDeathTrack(suit, toon, battle))
        else:
            suitTrack.append(Func(suit.loop, 'neutral'))
        if revived != 0:
            suitTrack.append(MovieUtil.createSuitReviveTrack(suit, toon, battle))
        return Parallel(suitTrack, bonusTrack)
    else:
        return MovieUtil.createSuitZaplessMultiTrack(suit, 2.5)


def say(statement):
    print statement


def __getSoundTrack(level, hitSuit, delay, node = None):
    if hitSuit:
        soundEffect = globalBattleSoundCache.getSound(hitSoundFiles[level])
    else:
        soundEffect = globalBattleSoundCache.getSound(missSoundFiles[level])
    soundTrack = Sequence()
    if soundEffect:
        if level == 0:
            pass
        else:
            soundTrack.append(Wait(delay))
        soundTrack.append(SoundInterval(soundEffect, node=node))
        return soundTrack


def __doJoybuzzer(zap, delay, fShowStun):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    target = zap['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = zap['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tTotalFlowerToonAnimationTime = 2
    tFlowerFirstAppears = 1.0
    dFlowerScaleTime = 0.5
    tSprayStarts = tTotalFlowerToonAnimationTime
    dSprayScale = 0.2
    dSprayHold = 0.1
    tContact = tSprayStarts + dSprayScale
    tSuitDodges = tTotalFlowerToonAnimationTime
    tracks = Parallel()
    button = globalPropPool.getProp('joybuzz')
    button2 = MovieUtil.copyProp(button)
    buttons = [button, button2]
    hands = toon.getRightHands()
    toonTrack = Sequence(Func(MovieUtil.showProps, buttons, hands, Vec3((0.3, 0, 0)), Vec3((-10, -60 ,0))), Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'water-gun'), Func(MovieUtil.removeProps, buttons), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
    tracks.append(__getSoundTrack(level, hitSuit, tTotalFlowerToonAnimationTime, toon))
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)

    def getSprayStartPos(toon = toon):
        toon.update(0)
        p = button2.getPos(toon)
        return p

    sprayTrack = MovieUtil.getZapTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale=scale, vertScale=scale)
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, revived=revived))
    return tracks


def __doRug(zap, delay, fShowStun):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    target = zap['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = zap['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tSpray = 5.2
    sprayPoseFrame = 88
    dSprayScale = 0.1
    dSprayHold = 0.1
    tContact = tSpray + dSprayScale
    tSuitDodges = max(tSpray - 0.5, 0.0)
    tracks = Parallel()
    tracks.append(ActorInterval(toon, 'run'))
    soundTrack = __getSoundTrack(level, hitSuit, 0, toon)
    tracks.append(soundTrack)
    rug = globalPropPool.getProp('zapRug')
    rugPos = Point3(0, 0, 0.025)
    rugHpr = Point3(0, 0, 0)
    glassTrack = Sequence(Func(MovieUtil.showProp, rug, toon, rugPos, rugHpr), ActorInterval(toon, 'walk', playRate=0.7), ActorInterval(toon, 'run'), ActorInterval(toon, 'run', playRate=1.1),  ActorInterval(toon, 'run', playRate=1.2),  ActorInterval(toon, 'run', playRate=1.3),  ActorInterval(toon, 'run', playRate=1.4), ActorInterval(toon, 'water', playRate=1, startFrame=0, endFrame=36), Wait(1), Func(MovieUtil.removeProp, rug), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(glassTrack)
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)

    def getSprayStartPos(toon = toon):
        toon.update(0)
        lod0 = toon.getLOD(toon.getLODNames()[0])
        if base.config.GetBool('want-new-anims', 1):
            if not lod0.find('**/def_joint_right_hold').isEmpty():
                joint = lod0.find('**/def_joint_right_hold')
            else:
                joint = lod0.find('**/joint_Rhold')
        else:
            joint = lod0.find('**/joint_Rhold')
        p = joint.getPos(render)
        return p

    sprayTrack = MovieUtil.getZapTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale=scale, vertScale=scale)
    tracks.append(Sequence(Wait(tSpray), sprayTrack))
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, revived=revived))
    return tracks


def __doBalloon(zap, delay, fShowStun):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    target = zap['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = zap['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tPistol = 0.0
    dPistolScale = 3
    dPistolHold = 1.8
    tSpray = 3
    sprayPoseFrame = 63
    dSprayScale = 0.1
    dSprayHold = 0.3
    tContact = tSpray + dSprayScale
    tSuitDodges = 1.1
    tracks = Parallel()
    toonTrack = Sequence(Func(toon.headsUp, battle, suitPos), Func(toon.pingpong, 'smooch', fromFrame=40, toFrame=45), Wait(2.5), Func(toon.stop), Func(toon.pingpong, 'cast', fromFrame=30, toFrame=40), Wait(2), Func(toon.stop), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
    soundTrack = __getSoundTrack(level, hitSuit, 0.2, toon)
    tracks.append(soundTrack)
    pistol = globalPropPool.getProp('balloon')
    hands = toon.getRightHands()
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)

    def getSprayStartPos(pistol = pistol, toon = toon):
        toon.update(0)
        p = pistol.getPos(render)
        return p

    sprayTrack = MovieUtil.getSprayTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale=scale, vertScale=scale)
    pistolPos = Point3(0.28, 0.1, 0.08)
    pistolHpr = VBase3(85.6, -4.44, 94.43)
    pistolTrack = Sequence(Func(MovieUtil.showProp, pistol, hand_jointpath0, pistolPos, pistolHpr), LerpScaleInterval(pistol, dPistolScale, dPistolScale, startScale=MovieUtil.PNT3_NEARZERO), Wait(tSpray - dPistolScale))
    pistolTrack.append(sprayTrack)
    pistolTrack.append(Wait(dPistolHold))
    pistolTrack.append(LerpScaleInterval(pistol, 0.4, MovieUtil.PNT3_NEARZERO, dPistolScale))
    pistolTrack.append(Func(hand_jointpath1.removeNode))
    pistolTrack.append(Func(hand_jointpath0.removeNode))
    pistolTrack.append(Func(MovieUtil.removeProp, pistol))
    tracks.append(pistolTrack)
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, revived=revived))
    return tracks


def __doBattery(zap, delay, fShowStun):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    target = zap['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = zap['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    origPos = toon.getPos(battle)
    battery = globalPropPool.getProp('battery')
    runBackHpr = Vec3(0, 0, 0)
    hands = toon.getRightHands()
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    hitSuit = hp > 0
    scale = 0.3
    tAppearDelay = 0.7
    dHoseHold = 0.7
    midPos = Point3(toon.getX(battle)*.5, 0, 0)
    runDur = 1
    tSprayDelay = 2
    tSpray = 1
    dSprayScale = 0.1
    dSprayHold = 1.8
    tContact = 2
    tSuitDodges = 2.1
    tracks = Parallel()
    toonTrack = Sequence(Wait(tAppearDelay), Func(MovieUtil.showProp, battery, hand_jointpath0), Func(toon.headsUp, battle, suitPos), Func(toon.loop, 'catch-run'), Wait(1), Func(toon.loop, 'catch-neutral'), Wait(3), Func(toon.stop), Func(toon.setHpr, battle, runBackHpr), Func(toon.loop, 'catch-run'), Func(toon.loop, 'neutral'), Func(MovieUtil.removeProp, battery), Func(toon.setHpr, battle, origHpr))
    moveTrack = Sequence(Wait(tAppearDelay), LerpPosInterval(toon, runDur, midPos, other=battle), Wait(3), LerpPosInterval(toon, runDur, origPos, other=battle))
    tracks.append(toonTrack)
    tracks.append(moveTrack)
    soundTrack = __getSoundTrack(level, hitSuit, tSprayDelay, toon)
    tracks.append(soundTrack)
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)

    def getSprayStartPos(battery = battery, toon = toon):
        toon.update(0)
        p = battery.getPos(render)
        return p

    sprayTrack = Sequence()
    sprayTrack.append(Wait(tSprayDelay))
    sprayTrack.append(MovieUtil.getZapTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale=scale, vertScale=scale))
    tracks.append(sprayTrack)
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, revived=revived))
    return tracks


def __doTazer(zap, delay, fShowStun):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    target = zap['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = zap['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    origPos = toon.getPos(battle)
    tazer = globalPropPool.getProp('tazer')
    tazer.setHpr(180, 0, 0)
    runBackHpr = Vec3(0, 0, 0)
    hands = toon.getRightHands()
    hand_jointpath0 = hands[0].attachNewNode('handJoint0-path')
    hand_jointpath1 = hand_jointpath0.instanceTo(hands[1])
    hitSuit = hp > 0
    scale = 0.3
    tAppearDelay = 0.7
    dHoseHold = 0.7
    midPos = Point3(toon.getX(battle)*.5, 0, 0)
    runDur = 1
    tSprayDelay = 2
    tSpray = 1
    dSprayScale = 0.1
    dSprayHold = 1.8
    tContact = 2
    tSuitDodges = 2.1
    tracks = Parallel()
    toonTrack = Sequence(Wait(tAppearDelay), Func(MovieUtil.showProp, tazer, hand_jointpath0), Func(toon.headsUp, battle, suitPos), Func(toon.loop, 'run'), Wait(1), Func(toon.pingpong, 'cast', fromFrame=30, toFrame=40), Wait(3), Func(toon.stop), Func(toon.setHpr, battle, runBackHpr), Func(toon.loop, 'run'), Func(toon.loop, 'neutral'), Func(MovieUtil.removeProp, tazer), Func(toon.setHpr, battle, origHpr))
    moveTrack = Sequence(Wait(tAppearDelay), LerpPosInterval(toon, runDur, midPos, other=battle), Wait(3), LerpPosInterval(toon, runDur, origPos, other=battle))
    tracks.append(toonTrack)
    tracks.append(moveTrack)
    soundTrack = __getSoundTrack(level, hitSuit, tSprayDelay, toon)
    tracks.append(soundTrack)
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)

    def getSprayStartPos(tazer = tazer, toon = toon):
        toon.update(0)
        p = tazer.getPos(render)
        return p

    sprayTrack = Sequence()
    sprayTrack.append(Wait(tSprayDelay))
    sprayTrack.append(MovieUtil.getZapTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale=scale, vertScale=scale))
    tracks.append(sprayTrack)
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, revived=revived))
    return tracks


def __doTesla(zap, delay, fShowStun):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    target = zap['target']
    suit = target['suit']
    hp = target['hp']
    kbbonus = target['kbbonus']
    died = target['died']
    revived = target['revived']
    leftSuits = target['leftSuits']
    rightSuits = target['rightSuits']
    battle = zap['battle']
    suitPos = suit.getPos(battle)
    origHpr = toon.getHpr(battle)
    endPos = toon.getPos(battle)
    endPos.setY(endPos.getY() + 3)
    hitSuit = hp > 0
    scale = sprayScales[level]
    tButton = 0.0
    dButtonScale = 0.5
    dButtonHold = 3.0
    dSprayScale = 0.1
    dSprayHold = 1.8
    tContact = 2.9
    tSpray = 2.5
    tSprayDelay = 2.5
    tSuitDodges = 1.8
    shrinkDuration = 0.4
    tracks = Parallel()
    soundTrack = __getSoundTrack(level, hitSuit, 2.3, toon)
    tracks.append(soundTrack)
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [button, button2]
    hands = toon.getLeftHands()
    toonTrack = Sequence(Func(MovieUtil.showProps, buttons, hands), Func(toon.headsUp, battle, endPos), ActorInterval(toon, 'pushbutton'), Func(MovieUtil.removeProps, buttons), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
    coil = globalPropPool.getProp('tesla')
    coil.setPos(endPos)
    propTrack = Sequence()
    propTrack.append(Func(coil.show))
    propTrack.append(Func(coil.setScale, Point3(0.1, 0.1, 0.1)))
    propTrack.append(Func(coil.reparentTo, battle))
    propTrack.append(LerpScaleInterval(coil, 1.5, Point3(1.0, 1.0, 1.0)))
    propTrack.append(Wait(tSpray + 2))
    propTrack.append(LerpScaleInterval(nodePath=coil, scale=Point3(1.0, 1.0, 0.1), duration=shrinkDuration))
    propTrack.append(Func(MovieUtil.removeProp, coil))
    tracks.append(propTrack)
    targetPoint = lambda suit = suit: __suitTargetPoint(suit)

    def getSprayStartPos(coil = coil, toon = toon):
        toon.update(0)
        p = coil.getPos(render)
        p.setZ(5)
        return p

    sprayTrack = Sequence()
    sprayTrack.append(Wait(tSprayDelay))
    sprayTrack.append(MovieUtil.getZapTrack(battle, WaterSprayColor, getSprayStartPos, targetPoint, dSprayScale, dSprayHold, dSprayScale, horizScale=scale, vertScale=scale))
    tracks.append(sprayTrack)
    if hp > 0 or delay <= 0:
        tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, revived=revived))
    return tracks


def __doLightning(zap, delay, fShowStun, uberClone = 0):
    toon = zap['toon']
    level = zap['level']
    hpbonus = zap['hpbonus']
    tracks = Parallel()
    tButton = 0.0
    dButtonScale = 0.5
    dButtonHold = 3.0
    tContact = 1
    tSpray = 1
    tSuitDodges = 1.8
    button = globalPropPool.getProp('button')
    button2 = MovieUtil.copyProp(button)
    buttons = [button, button2]
    hands = toon.getLeftHands()
    battle = zap['battle']
    origHpr = toon.getHpr(battle)
    suit = zap['target'][0]['suit']
    suitPos = suit.getPos(battle)
    toonTrack = Sequence(Func(MovieUtil.showProps, buttons, hands), Func(toon.headsUp, battle, suitPos), ActorInterval(toon, 'pushbutton'), Func(MovieUtil.removeProps, buttons), Func(toon.loop, 'neutral'), Func(toon.setHpr, battle, origHpr))
    tracks.append(toonTrack)
    for target in zap['target']:
        suit = target['suit']
        hp = target['hp']
        kbbonus = target['kbbonus']
        died = target['died']
        revived = target['revived']
        leftSuits = target['leftSuits']
        rightSuits = target['rightSuits']
        battle = zap['battle']
        suitPos = suit.getPos(battle)
        origHpr = toon.getHpr(battle)
        hitSuit = hp > 0
        scale = sprayScales[level]
        soundTrack = __getSoundTrack(level, hitSuit, 2.3, toon)
        tracks.append(soundTrack)
        cloud = globalPropPool.getProp('stormcloud')
        cloudHeight = suit.height + 3
        cloudPosPoint = Point3(0, 0, cloudHeight)
        scaleUpPoint = Point3(10, 10, 10)
        rainDelay = 1
        if hp > 0:
            cloudHold = 4.7
        else:
            cloudHold = 1.7

        def getCloudTrack(cloud, suit, cloudPosPoint, scaleUpPoint, rainDelay, cloudHold, battle = battle):
            tracks = Parallel()
            track = Sequence(Func(MovieUtil.showProp, cloud, suit, cloudPosPoint), Func(cloud.pose, 'stormcloud', 0), LerpScaleInterval(cloud, 1.5, scaleUpPoint, startScale=MovieUtil.PNT3_NEARZERO), Wait(rainDelay), ActorInterval(cloud, 'stormcloud'))
            track.append(LerpScaleInterval(cloud, 0.5, MovieUtil.PNT3_NEARZERO))
            track.append(Func(MovieUtil.removeProp, cloud))
            oldcolor = render.getColorScale()
            lightTrack = Sequence(Wait(rainDelay + 1), LerpColorScaleInterval(render, 1, (0.3, 0.3, 0.3, 1)), Wait(2), LerpColorScaleInterval(render, 1, (oldcolor)))
            tracks.append(track)
            tracks.append(lightTrack)
            return tracks

        tracks.append(getCloudTrack(cloud, suit, cloudPosPoint, scaleUpPoint, rainDelay, cloudHold))
        if hp > 0 or delay <= 0:
            tracks.append(__getSuitTrack(suit, tContact, tSuitDodges, hp, hpbonus, kbbonus, 'shock', died, leftSuits, rightSuits, battle, toon, fShowStun, beforeStun=2.6, afterStun=2.3, revived=revived))
    return tracks


zapfn_array = (__doJoybuzzer,
 __doRug,
 __doBalloon,
 __doBattery,
 __doTazer,
 __doTesla,
 __doLightning)
