import pathlib
from src.utils.core import hashit
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
smallEmptyPotionFlaskImage = loadFromRGBToGray(f'{currentPath}/images/items/potions/smallEmptyPotionFlask.png')
mediumEmptyPotionFlaskImage = loadFromRGBToGray(f'{currentPath}/images/items/potions/mediumEmptyPotionFlask.png')
bigEmptyPotionFlaskImage = loadFromRGBToGray(f'{currentPath}/images/items/potions/bigEmptyPotionFlask.png')
emptySlotImage = loadFromRGBToGray(f'{currentPath}/images/emptySlot.png')
itemsImagesHashes = {
    hashit(smallEmptyPotionFlaskImage): 'empty potion flask',
    hashit(mediumEmptyPotionFlaskImage): 'empty potion flask',
    hashit(bigEmptyPotionFlaskImage): 'empty potion flask',
    hashit(emptySlotImage): 'empty slot',
}