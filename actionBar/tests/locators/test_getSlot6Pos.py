import pathlib
from actionBar.locators import getSlot6Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_6_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot6Pos(screenshotImg)
    expectedPos = (221, 394, 11, 8)
    assert pos == expectedPos
