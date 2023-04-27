import pathlib
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
tabsImagesPath = f'{imagesPath}/tabs'
images = {
    'tabs': {
        'loot': {
            'selectedLoot': loadFromRGBToGray(f'{tabsImagesPath}/selectedLoot.png'),
            'unselectedLoot': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLoot.png'),
            'unselectedLootWithNewestMessage': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLootWithNewestMessage.png'),
            'unselectedLootWithUnreadMessage': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLootWithUnreadMessage.png'),
        }
    }
}