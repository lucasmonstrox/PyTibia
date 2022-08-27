import pathlib
from actionBar.locators import getSlot2Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_2_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot2Pos(screenshotImg)
    expectedPos = (77, 394, 11, 8)
    assert pos == expectedPos
