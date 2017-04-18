from toontown.toonbase.ToontownGlobals import *
from toontown.coghq.boardbothq import BoardOfficeProduct

class BoardOfficeShelf(BoardOfficeProduct.BoardOfficeProduct):
    Models = {BoardOfficeIntA: 'phase_10/models/cashbotHQ/shelf_A1MoneyBags',
     BoardOfficeIntB: 'phase_10/models/cashbotHQ/shelf_A1Money',
     BoardOfficeIntC: 'phase_10/models/cashbotHQ/shelf_A1Gold'}
    Scales = {BoardOfficeIntA: 1.0,
     BoardOfficeIntB: 1.0,
     BoardOfficeIntC: 1.0}
