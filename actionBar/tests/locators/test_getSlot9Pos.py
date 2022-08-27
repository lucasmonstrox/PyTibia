import pathlib
from actionBar.locators import getSlot9Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_9_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot9Pos(screenshotImg)
    expectedPos = (329, 394, 11, 8)
    assert pos == expectedPos
