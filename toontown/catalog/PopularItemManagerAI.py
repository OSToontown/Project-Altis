from toontown.catalog.CatalogItemList import CatalogItemList
from toontown.catalog.CatalogInvalidItem import CatalogInvalidItem
from toontown.catalog.CatalogFurnitureItem import CatalogFurnitureItem
from toontown.catalog.CatalogChatItem import CatalogChatItem
from toontown.catalog.CatalogClothingItem import CatalogClothingItem
from toontown.catalog.CatalogEmoteItem import CatalogEmoteItem
from toontown.catalog.CatalogWallpaperItem import CatalogWallpaperItem
from toontown.catalog.CatalogWindowItem import CatalogWindowItem
from toontown.catalog.CatalogFlooringItem import CatalogFlooringItem
from toontown.catalog.CatalogMouldingItem import CatalogMouldingItem
from toontown.catalog.CatalogWainscotingItem import CatalogWainscotingItem
from toontown.catalog.CatalogPoleItem import CatalogPoleItem
from toontown.catalog.CatalogPetTrickItem import CatalogPetTrickItem
from toontown.catalog.CatalogBeanItem import CatalogBeanItem
from toontown.catalog.CatalogGardenItem import CatalogGardenItem
from toontown.catalog.CatalogRentalItem import CatalogRentalItem
from toontown.catalog.CatalogGardenStarterItem import CatalogGardenStarterItem
from toontown.catalog.CatalogNametagItem import CatalogNametagItem
from toontown.catalog.CatalogToonStatueItem import CatalogToonStatueItem
from toontown.catalog.CatalogAnimatedFurnitureItem import CatalogAnimatedFurnitureItem
from toontown.catalog.CatalogAccessoryItem import CatalogAccessoryItem

class PopularItemManagerAI:

    def __init__(self, air):
        self.air = air

        self.popularItemDict = {}

    def avBoughtItem(self, item):
        # Load the current popularItems
        try:
            popularItems = simbase.backups.load('catalog', ('popular-items',), default=({}))
        except ValueError:
            return

        itemOutput = item.output()

        # Don't allow rental items!
        if 'CatalogRentalItem' in itemOutput:
            return

        if not itemOutput in popularItems:
            popularItems[itemOutput] = 1
        else:
            popularItems[itemOutput] += 1

        # Save it.
        try:
            simbase.backups.save('catalog', ('popular-items',), (popularItems))
        except ValueError:
            pass

    def requestPopularItems(self):
        # Load the current popularItems
        try:
            self.popularItemDict = simbase.backups.load('catalog', ('popular-items',), default=({}))
        except ValueError:
            pass

        sortedItems = [(x,y) for y,x in sorted([(y,x) for x,y in self.popularItemDict.items()],reverse=True)]

        finalItems = []
        if len(sortedItems) <= 12:
            for item in sortedItems:
                item = eval(item[0])
                finalItems.append(item)
        else:
            for i in xrange(12):
                item = eval(sortedItems[i][0])
                finalItems.append(item)

        catalog = CatalogItemList(finalItems)
        return catalog.getBlob()

