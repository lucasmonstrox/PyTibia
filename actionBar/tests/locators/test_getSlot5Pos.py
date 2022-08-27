import pathlib
from actionBar.locators import getSlot5Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_5_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot5Pos(screenshotImg)
    expectedPos = (185, 394, 11, 8)
    assert pos == expectedPos
