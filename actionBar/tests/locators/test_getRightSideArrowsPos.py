import pathlib
from actionBar.locators import getRightSideArrowsPos
from utils.image import load, RGBtoGray


def test_should_get_right_side_arrows_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getRightSideArrowsPos(screenshotImg)
    expectedPos = (1539, 392, 17, 34)
    assert pos == expectedPos
