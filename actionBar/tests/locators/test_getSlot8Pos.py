import pathlib
from actionBar.locators import getSlot8Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_8_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot8Pos(screenshotImg)
    expectedPos = (293, 394, 11, 8)
    assert pos == expectedPos
