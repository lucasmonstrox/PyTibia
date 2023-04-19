import pathlib
from src.repositories.actionBar.core import slotIsAvailable
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_small_health_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/smallHealthPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_small_health_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/smallHealthPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_health_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/healthPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_health_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/healthPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_strong_health_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/strongHealthPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_strong_health_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/strongHealthPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_great_health_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/greatHealthPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_great_health_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/greatHealthPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_ultimate_health_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/ultimateHealthPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_ultimate_health_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/ultimateHealthPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_supreme_health_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/supremeHealthPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_supreme_health_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/supremeHealthPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_mana_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/manaPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_mana_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/manaPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_strong_mana_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/strongManaPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_strong_mana_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/strongManaPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_great_mana_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/greatManaPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_great_mana_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/greatManaPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_ultimate_mana_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/ultimateManaPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_ultimate_mana_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/ultimateManaPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_great_spirit_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/greatSpiritPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_great_spirit_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/greatSpiritPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_antidote_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/antidotePotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_antidote_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/antidotePotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_antidote_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/antidotePotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_True_when_antidote_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/antidotePotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_mastermind_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/mastermindPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_mastermind_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/mastermindPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_berserk_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/berserkPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_berserk_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/berserkPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_berserk_potion_is_not_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/berserkPotionNotAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = False
    assert isAvailable == expectedSlotIsAvailable


def test_should_return_False_when_berserk_potion_is_available():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/berserkPotionAvailable.png')
    isAvailable = slotIsAvailable(screenshotImage, 1)
    expectedSlotIsAvailable = True
    assert isAvailable == expectedSlotIsAvailable
