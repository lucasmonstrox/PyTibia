import pathlib
from src.repositories.actionBar.locators import getLeftArrowsPosition
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_None_when_left_arrows_are_unlocked():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/leftArrowsUnlocked.png')
    leftArrowsPosition = getLeftArrowsPosition(screenshotImage)
    expectedLeftArrowsPosition = None
    assert leftArrowsPosition == expectedLeftArrowsPosition


def test_should_get_left_arrows_position():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/leftArrowsLocked.png')
    leftArrowsPosition = getLeftArrowsPosition(screenshotImage)
    expectedLeftArrowsPosition = (0, 392, 17, 34)
    assert leftArrowsPosition == expectedLeftArrowsPosition