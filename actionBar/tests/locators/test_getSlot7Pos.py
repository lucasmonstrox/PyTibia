import pathlib
from actionBar.locators import getSlot7Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_7_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot7Pos(screenshotImg)
    expectedPos = (257, 394, 11, 8)
    assert pos == expectedPos
