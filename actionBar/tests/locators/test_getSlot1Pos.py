import pathlib
from actionBar.locators import getSlot1Pos
from utils.image import load, RGBtoGray


def test_should_get_slot_1_pos():
    currentPath = pathlib.Path(__file__).parent.resolve()
    screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
    pos = getSlot1Pos(screenshotImg)
    expectedPos = (41, 394, 11, 8)
    assert pos == expectedPos
