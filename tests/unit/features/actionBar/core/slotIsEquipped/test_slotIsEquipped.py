import pathlib
from src.repositories.actionBar.core import slotIsEquipped
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_slot_is_not_equipped():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/slotIsNotEquipped.png')
    isEquipped = slotIsEquipped(screenshotImage, 14)
    expectedSlotIsEquipped = False
    assert isEquipped == expectedSlotIsEquipped


def test_should_return_True_when_slot_is_equipped():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/slotIsEquipped.png')
    isEquipped = slotIsEquipped(screenshotImage, 14)
    expectedSlotIsEquipped = True
    assert isEquipped == expectedSlotIsEquipped
