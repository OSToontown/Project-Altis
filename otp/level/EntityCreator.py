from otp.level import CutScene
from otp.level import EntityCreatorBase
from otp.level import BasicEntities
from direct.directnotify import DirectNotifyGlobal
from otp.level import EditMgr
from otp.level import EntrancePoint
from otp.level import LevelMgr
from otp.level import LogicGate
from otp.level import ZoneEntity
from otp.level import ModelEntity
from otp.level import PathEntity
from otp.level import VisibilityExtender
from otp.level import PropSpinner
from otp.level import AmbientSound
from otp.level import LocatorEntity
from otp.level import CollisionSolidEntity

def nothing(*args):
    return 'nothing'

def nonlocal(*args):
    return 'nonlocal'

class EntityCreator(EntityCreatorBase.EntityCreatorBase):

    def __init__(self, level):
        EntityCreatorBase.EntityCreatorBase.__init__(self, level)
        self.level = level
        self.privRegisterTypes({'attribModifier': nothing,
         'ambientSound': AmbientSound.AmbientSound,
         'collisionSolid': CollisionSolidEntity.CollisionSolidEntity,
         'cutScene': CutScene.CutScene,
         'editMgr': EditMgr.EditMgr,
         'entityGroup': nothing,
         'entrancePoint': EntrancePoint.EntrancePoint,
         'levelMgr': LevelMgr.LevelMgr,
         'locator': LocatorEntity.LocatorEntity,
         'logicGate': LogicGate.LogicGate,
         'model': ModelEntity.ModelEntity,
         'nodepath': BasicEntities.NodePathEntity,
         'path': PathEntity.PathEntity,
         'propSpinner': PropSpinner.PropSpinner,
         'visibilityExtender': VisibilityExtender.VisibilityExtender,
         'zone': ZoneEntity.ZoneEntity})

    def doCreateEntity(self, ctor, entId):
        return ctor(self.level, entId)