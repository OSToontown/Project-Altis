from otp.ai.AIBaseGlobal import *
from direct.distributed.ClockDelta import *
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from toontown.building import DistributedDoorAI
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
from toontown.coghq import CogDisguiseGlobals
from toontown.building import FADoorCodes
from toontown.building import DoorTypes

class DistributedCogHQDoorAI(DistributedDoorAI.DistributedDoorAI):
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedCogHQDoorAI')

    def __init__(self, air, blockNumber, doorType, destinationZone, doorIndex = 0, lockValue = FADoorCodes.SB_DISGUISE_INCOMPLETE, swing = 3):
        DistributedDoorAI.DistributedDoorAI.__init__(self, air, blockNumber, doorType, doorIndex, lockValue, swing)
        self.destinationZone = destinationZone

    def requestEnter(self):
        avatarId = self.air.getAvatarIdFromSender()
        dept = ToontownGlobals.cogHQZoneId2deptIndex(self.destinationZone)
        av = self.air.doId2do.get(avatarId)
        if av:
            if self.doorType == DoorTypes.EXT_COGHQ and self.isLockedDoor():
                parts = av.getCogParts()
                if CogDisguiseGlobals.isSuitComplete(parts, dept):
                    allowed = 1
                else:
                    allowed = 0
            else:
                allowed = 1
            
            if not allowed:
                self.sendReject(avatarId, self.isLockedDoor())
                return

            self.enqueueAvatarIdEnter(avatarId)
            self.sendUpdateToAvatarId(avatarId, 'setOtherZoneIdAndDoId', [self.destinationZone, self.otherDoor.getDoId()])

    def requestExit(self):
        avatarId = self.air.getAvatarIdFromSender()
        
        if avatarId in self.avatarsWhoAreEntering:
            del self.avatarsWhoAreEntering[avatarId]
        
        if avatarId not in self.avatarsWhoAreExiting:
            dept = ToontownGlobals.cogHQZoneId2deptIndex(self.destinationZone)
            self.avatarsWhoAreExiting[avatarId] = 1
            self.sendUpdate('avatarExit', [avatarId])
            self.openDoor(self.exitDoorFSM)
            if self.lockedDoor:
                av = self.air.doId2do[avatarId]
                if self.doorType == DoorTypes.EXT_COGHQ:
                    av.b_setCogIndex(-1)
                else:
                    av.b_setCogIndex(dept)