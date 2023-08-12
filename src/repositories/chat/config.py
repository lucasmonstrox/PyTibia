import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
tabsImagesPath = f'{imagesPath}/tabs'
images = {
    'tabs': {
        'localChat': {
            'selected': loadFromRGBToGray(f'{tabsImagesPath}/localChat/selected.png'),
            'unselected': loadFromRGBToGray(f'{tabsImagesPath}/localChat/unselected.png'),
            'newestMessage': loadFromRGBToGray(f'{tabsImagesPath}/localChat/newestMessage.png'),
            'unreadMessage': loadFromRGBToGray(f'{tabsImagesPath}/localChat/unreadMessage.png'),
        },
        'loot': {
            'selected': loadFromRGBToGray(f'{tabsImagesPath}/loot/selected.png'),
            'unselected': loadFromRGBToGray(f'{tabsImagesPath}/loot/unselected.png'),
            'newestMessage': loadFromRGBToGray(f'{tabsImagesPath}/loot/newestMessage.png'),
            'unreadMessage': loadFromRGBToGray(f'{tabsImagesPath}/loot/unreadMessage.png'),
        },
        'npcs': {
            'selected': loadFromRGBToGray(f'{tabsImagesPath}/npcs/selected.png'),
            'unselected': loadFromRGBToGray(f'{tabsImagesPath}/npcs/unselected.png'),
        }
    }
}
hashes = {
    'tabs': {
        hashit(images['tabs']['localChat']['selected']): 'local chat',
        hashit(images['tabs']['localChat']['unselected']): 'local chat',
        hashit(images['tabs']['localChat']['newestMessage']): 'local chat',
        hashit(images['tabs']['localChat']['unreadMessage']): 'local chat',
        hashit(images['tabs']['loot']['selected']): 'loot',
        hashit(images['tabs']['loot']['unselected']): 'loot',
        hashit(images['tabs']['loot']['newestMessage']): 'loot',
        hashit(images['tabs']['loot']['unreadMessage']): 'loot',
        hashit(images['tabs']['npcs']['selected']): 'npcs',
        hashit(images['tabs']['npcs']['unselected']): 'npcs',
    }
}
