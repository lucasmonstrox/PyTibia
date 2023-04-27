import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
imagesPath = f'{currentPath}/images'
tabsImagesPath = f'{imagesPath}/tabs'
images = {
    'tabs': {
        'localChat': {
            'selectedLocalChat': loadFromRGBToGray(f'{tabsImagesPath}/selectedLocalChat.png'),
            'unselectedLocalChat': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLocalChat.png'),
            'unselectedLocalChatWithNewestMessage': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLocalChatWithNewestMessage.png'),
            'unselectedLocalChatWithUnreadMessage': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLocalChatWithUnreadMessage.png'),
        },
        'loot': {
            'selectedLoot': loadFromRGBToGray(f'{tabsImagesPath}/selectedLoot.png'),
            'unselectedLoot': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLoot.png'),
            'unselectedLootWithNewestMessage': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLootWithNewestMessage.png'),
            'unselectedLootWithUnreadMessage': loadFromRGBToGray(f'{tabsImagesPath}/unselectedLootWithUnreadMessage.png'),
        }
    }
}
hashes = {
    'tabs': {
        hashit(images['tabs']['localChat']['selectedLocalChat']): 'local chat',
        hashit(images['tabs']['localChat']['unselectedLocalChat']): 'local chat',
        hashit(images['tabs']['localChat']['unselectedLocalChatWithNewestMessage']): 'local chat',
        hashit(images['tabs']['localChat']['unselectedLocalChatWithUnreadMessage']): 'local chat',
        hashit(images['tabs']['loot']['selectedLoot']): 'loot',
        hashit(images['tabs']['loot']['unselectedLoot']): 'loot',
        hashit(images['tabs']['loot']['unselectedLootWithNewestMessage']): 'loot',
        hashit(images['tabs']['loot']['unselectedLootWithUnreadMessage']): 'loot',
    }
}