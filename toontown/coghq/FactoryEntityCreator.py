from otp.level import EntityCreator
from toontown.coghq import FactoryLevelMgr
from toontown.coghq import PlatformEntity
from toontown.coghq import ConveyorBelt
from toontown.coghq import GearEntity
from toontown.coghq import PaintMixer
from toontown.coghq import GoonClipPlane
from toontown.coghq import MintProduct
from toontown.coghq import MintProductPallet
from toontown.coghq import MintShelf
from toontown.coghq.boardbothq import BoardOfficeProduct
from toontown.coghq.boardbothq import BoardOfficeProductPallet
from toontown.coghq.boardbothq import BoardOfficeShelf
from toontown.coghq import PathMasterEntity
from toontown.coghq import RenderingEntity

class FactoryEntityCreator(EntityCreator.EntityCreator):

    def __init__(self, level):
        EntityCreator.EntityCreator.__init__(self, level)
        nothing = EntityCreator.nothing
        nonlocal = EntityCreator.nonlocal
        self.privRegisterTypes({'activeCell': nonlocal,
         'crusherCell': nonlocal,
         'battleBlocker': nonlocal,
         'beanBarrel': nonlocal,
         'button': nonlocal,
         'conveyorBelt': ConveyorBelt.ConveyorBelt,
         'crate': nonlocal,
         'door': nonlocal,
         'directionalCell': nonlocal,
         'gagBarrel': nonlocal,
         'gear': GearEntity.GearEntity,
         'goon': nonlocal,
         'gridGoon': nonlocal,
         'golfGreenGame': nonlocal,
         'goonClipPlane': GoonClipPlane.GoonClipPlane,
         'grid': nonlocal,
         'healBarrel': nonlocal,
         'levelMgr': FactoryLevelMgr.FactoryLevelMgr,
         'lift': nonlocal,
         'mintProduct': MintProduct.MintProduct,
         'mintProductPallet': MintProductPallet.MintProductPallet,
         'mintShelf': MintShelf.MintShelf,
         'boardOfficeProduct': BoardOfficeProduct.BoardOfficeProduct,
         'boardOfficeProductPallet': BoardOfficeProductPallet.BoardOfficeProductPallet,
         'boardOfficeShelf': BoardOfficeShelf.BoardOfficeShelf,
         'mover': nonlocal,
         'paintMixer': PaintMixer.PaintMixer,
         'pathMaster': PathMasterEntity.PathMasterEntity,
         'rendering': RenderingEntity.RenderingEntity,
         'platform': PlatformEntity.PlatformEntity,
         'sinkingPlatform': nonlocal,
         'stomper': nonlocal,
         'stomperPair': nonlocal,
         'laserField': nonlocal,
         'securityCamera': nonlocal,
         'elevatorMarker': nonlocal,
         'trigger': nonlocal,
         'moleField': nonlocal,
         'maze': nonlocal})
