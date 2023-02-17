import pathlib
from actionBar.locators import getLeftArrowsPos
from utils.image import load, RGBtoGray


def test_should_get_left_side_arrows_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getLeftArrowsPos(screenshotImg)
    expectedPos = (0, 392, 17, 34)
    assert pos == expectedPos
