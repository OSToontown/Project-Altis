from toontown.toonbase.ToontownGlobals import *
from toontown.coghq.boardbothq import BoardOfficeProduct

class BoardOfficeProductPallet(BoardOfficeProduct.BoardOfficeProduct):
    Models = {BoardOfficeIntA: 'phase_10/models/cashbotHQ/DoubleCoinStack.bam',
     BoardOfficeIntB: 'phase_10/models/cogHQ/DoubleMoneyStack.bam',
     BoardOfficeIntC: 'phase_10/models/cashbotHQ/DoubleGoldStack.bam'}
    Scales = {BoardOfficeIntA: 1.0,
     BoardOfficeIntB: 1.0,
     BoardOfficeIntC: 1.0}
