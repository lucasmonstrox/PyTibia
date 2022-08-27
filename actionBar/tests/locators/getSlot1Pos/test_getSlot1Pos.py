import pathlib
from actionBar.locators import getSlot1Pos, getSlot2Pos, getSlot3Pos, getSlot4Pos, getSlot5Pos, getSlot6Pos, getSlot7Pos, getSlot8Pos, getSlot9Pos
from utils.image import load, RGBtoGray

currentPath = pathlib.Path(__file__).parent.parent.resolve()
screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))


def test_should_get_slot_1_pos():
    pos = getSlot1Pos(screenshotImg)
    expectedPos = (41, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_2_pos():
    pos = getSlot2Pos(screenshotImg)
    expectedPos = (77, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_3_pos():
    pos = getSlot3Pos(screenshotImg)
    expectedPos = (113, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_4_pos():
    pos = getSlot4Pos(screenshotImg)
    expectedPos = (149, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_5_pos():
    pos = getSlot5Pos(screenshotImg)
    expectedPos = (185, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_6_pos():
    pos = getSlot6Pos(screenshotImg)
    expectedPos = (221, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_7_pos():
    pos = getSlot7Pos(screenshotImg)
    expectedPos = (257, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_8_pos():
    pos = getSlot8Pos(screenshotImg)
    expectedPos = (293, 394, 11, 8)
    assert pos == expectedPos


def test_should_get_slot_9_pos():
    pos = getSlot9Pos(screenshotImg)
    expectedPos = (329, 394, 11, 8)
    assert pos == expectedPos
