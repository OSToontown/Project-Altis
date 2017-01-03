from toontown.catalog.CatalogFurnitureItem import CatalogFurnitureItem # Furniture
from toontown.catalog.CatalogChatItem import CatalogChatItem # Phrase
from toontown.catalog.CatalogClothingItem import CatalogClothingItem # Clothing
from toontown.catalog.CatalogEmoteItem import CatalogEmoteItem # Emotion
from toontown.catalog.CatalogWallpaperItem import CatalogWallpaperItem # Furniture
from toontown.catalog.CatalogWindowItem import CatalogWindowItem # Furniture
from toontown.catalog.CatalogFlooringItem import CatalogFlooringItem # Furniture
from toontown.catalog.CatalogMouldingItem import CatalogMouldingItem # Furniture
from toontown.catalog.CatalogWainscotingItem import CatalogWainscotingItem # Furniture
from toontown.catalog.CatalogPoleItem import CatalogPoleItem # Special
from toontown.catalog.CatalogPetTrickItem import CatalogPetTrickItem # Special
from toontown.catalog.CatalogBeanItem import CatalogBeanItem # Furniture
from toontown.catalog.CatalogGardenItem import CatalogGardenItem # Special
from toontown.catalog.CatalogRentalItem import CatalogRentalItem # Special
from toontown.catalog.CatalogGardenStarterItem import CatalogGardenStarterItem # Special
from toontown.catalog.CatalogNametagItem import CatalogNametagItem # Nametag
from toontown.catalog.CatalogToonStatueItem import CatalogToonStatueItem # Special
from toontown.catalog.CatalogAnimatedFurnitureItem import CatalogAnimatedFurnitureItem # Furniture
from toontown.catalog.CatalogAccessoryItem import CatalogAccessoryItem # Clothing

class CatalogItemSorter:
    SPECIAL_ITEMS = (CatalogToonStatueItem, CatalogPoleItem, CatalogGardenStarterItem,
                     CatalogGardenItem, CatalogRentalItem, CatalogPetTrickItem)
    NAMETAG_ITEMS = (CatalogNametagItem,)
    PHRASE_ITEMS = (CatalogChatItem,)
    CLOTHING_ITEMS = (CatalogAccessoryItem, CatalogClothingItem)
    EMOTION_ITEMS = (CatalogEmoteItem,)
    FURNITURE_ITEMS = (CatalogFurnitureItem, CatalogWallpaperItem, CatalogWindowItem,
                       CatalogFlooringItem, CatalogMouldingItem, CatalogWainscotingItem,
                       CatalogBeanItem, CatalogAnimatedFurnitureItem)

    def __init__(self, itemList):
        self.itemList = itemList

        self.sortedItems = {
          'UNSORTED': [],
          'SPECIAL': [],
          'CLOTHING': [],
          'PHRASES': [],
          'EMOTIONS': [],
          'FURNITURE': [],
          'NAMETAG': []
        }

    def sortItems(self):
        for item in self.itemList:
            if self.__isSpecial(item):
                self.sortedItems['SPECIAL'].append(item)
            elif self.__isNametag(item):
                self.sortedItems['NAMETAG'].append(item)
            elif self.__isClothing(item):
                self.sortedItems['CLOTHING'].append(item)
            elif self.__isPhrase(item):
                self.sortedItems['PHRASES'].append(item)
            elif self.__isEmotion(item):
                self.sortedItems['EMOTIONS'].append(item)
            elif self.__isFurniture(item):
                self.sortedItems['FURNITURE'].append(item)
            else:
                self.sortedItems['UNSORTED'].append(item)
        return self.sortedItems

    def __isSpecial(self, item):
        return isinstance(item, CatalogItemSorter.SPECIAL_ITEMS)

    def __isClothing(self, item):
        return isinstance(item, CatalogItemSorter.CLOTHING_ITEMS)

    def __isPhrase(self, item):
        return isinstance(item, CatalogItemSorter.PHRASE_ITEMS)

    def __isNametag(self, item):
        return isinstance(item, CatalogItemSorter.NAMETAG_ITEMS)

    def __isEmotion(self, item):
        return isinstance(item, CatalogItemSorter.EMOTION_ITEMS)

    def __isFurniture(self, item):
        return isinstance(item, CatalogItemSorter.FURNITURE_ITEMS)