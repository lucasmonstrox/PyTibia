import pathlib
from actionBar.locators import getSlot4Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_4_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot4Pos(screenshotImg)
    expectedPos = (149, 394, 11, 8)
    assert pos == expectedPos
