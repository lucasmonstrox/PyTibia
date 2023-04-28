import pathlib
from src.repositories.actionBar.locators import getRightArrowsPosition
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_None_when_right_arrows_are_unlocked():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/rightArrowsLocked.png')
    rightArrowsPosition = getRightArrowsPosition(screenshotImage)
    expectedRightArrowsPosition = None
    assert rightArrowsPosition == expectedRightArrowsPosition


def test_should_get_right_arrows_position():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/rightArrowsUnlocked.png')
    rightArrowsPosition = getRightArrowsPosition(screenshotImage)
    expectedRightArrowsPosition = (1363, 744, 17, 34)
    assert rightArrowsPosition == expectedRightArrowsPosition
