from toontown.catalog.CatalogItem import CatalogItem
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.estate import HouseInteriorGlobals
from toontown.toontowngui import FeatureComingSoonDialog

class CatalogInteriorLayoutItem(CatalogItem):
    def makeNewItem(self, layoutId):
        self.layoutId = layoutId

        CatalogItem.makeNewItem(self)

    def decodeDatagram(self, di, versionNumber, store):
        CatalogItem.decodeDatagram(self, di, versionNumber, store)

        self.layoutId = di.getUint8()

    def encodeDatagram(self, dg, store):
        CatalogItem.encodeDatagram(self, dg, store)

        dg.addUint8(self.layoutId)

    def compareTo(self, other):
        return self.layoutId - other.layoutId

    def getHashContents(self):
        return (self.layoutId,)

    def output(self, store = -1):
        return 'CatalogInteriorLayoutItem(%s%s)' % (self.layoutId, self.formatOptionalData(store))

    def getBasePrice(self):
        return ToontownGlobals.HouseInteriorLayoutPrices[self.layoutId]

    def getTypeName(self):
        return TTLocalizer.InteriorLayoutTypeName

    def getName(self):
        return TTLocalizer.InteriorLayoutNames[self.layoutId]

    def reachedPurchaseLimit(self, avatar):
        return avatar.getInteriorLayout() == self.layoutId or self in avatar.onOrder or self in avatar.mailboxContents

    def isGift(self):
        return False

    def getPicture(self, avatar):
        self.model = loader.loadModel(HouseInteriorGlobals.Models[self.layoutId])
        frame = self.makeFrame()
        self.model.reparentTo(frame)
        self.model.setScale(0.1)
        self.model.setH(90)
        self.model.setZ(-1)
        self.hasPicture = True
        return (frame, None)

    def cleanupPicture(self):
        CatalogItem.cleanupPicture(self)

        self.model.detachNode()
        self.model = None

    def recordPurchase(self, avatar, optional):
        if avatar:
            house = simbase.air.doId2do.get(avatar.getHouseId())
            if house:
                house.b_setInteriorLayout(self.layoutId)
            avatar.b_setInteriorLayout(self.layoutId)
        return ToontownGlobals.P_ItemAvailable
        
    def acceptItem(self, mailbox, index, callback):
        FeatureComingSoonDialog.FeatureComingSoonDialog("For the new interior to apply, you will need to relog!")
        if hasattr(mailbox, 'mailboxGui') and mailbox.mailboxGui:
            mailbox.acceptItem(self, index, callback)
            mailbox.mailboxGui.justExit()
