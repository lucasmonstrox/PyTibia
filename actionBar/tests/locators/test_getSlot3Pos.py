import pathlib
from actionBar.locators import getSlot3Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_3_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot3Pos(screenshotImg)
    expectedPos = (113, 394, 11, 8)
    assert pos == expectedPos
