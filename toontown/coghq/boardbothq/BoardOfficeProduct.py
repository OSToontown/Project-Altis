from toontown.toonbase.ToontownGlobals import *
from otp.level import BasicEntities

class BoardOfficeProduct(BasicEntities.NodePathEntity):
    Models = {BoardOfficeIntA: 'phase_10/models/cashbotHQ/MoneyBag',
     BoardOfficeIntB: 'phase_10/models/cashbotHQ/MoneyStackPallet',
     BoardOfficeIntC: 'phase_10/models/cashbotHQ/GoldBarStack'}
    Scales = {BoardOfficeIntA: 0.98,
     BoardOfficeIntB: 0.38,
     BoardOfficeIntC: 0.6}

    def __init__(self, level, entId):
        BasicEntities.NodePathEntity.__init__(self, level, entId)
        self.model = None
        self.boardofficeId = self.level.boardofficeId
        self.loadModel()

    def destroy(self):
        if self.model:
            self.model.removeNode()
            del self.model
        BasicEntities.NodePathEntity.destroy(self)

    def loadModel(self):
        if self.model:
            self.model.removeNode()
            self.model = None
        self.model = loader.loadModel(self.Models[self.boardofficeId])
        self.model.setScale(self.Scales[self.boardofficeId])
        self.model.flattenStrong()
        if self.model:
            self.model.reparentTo(self)

    if __dev__:

        def setBoardOfficeId(self, boardofficeId):
            self.boardofficeId = boardofficeId
            self.loadModel()
