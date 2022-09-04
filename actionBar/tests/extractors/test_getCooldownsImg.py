import numpy as np
import pathlib
from actionBar.extractors import getCooldownsImg
from utils.image import load, RGBtoGray


currentPath = pathlib.Path(__file__).parent.resolve()
screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
listOfCooldownsImg = RGBtoGray(load(f'{currentPath}/listOfCooldownsImg.png'))


def test_should_return_None_when_cannot_get_left_side_arrows_pos(mocker):
    getLeftSideArrowsPosSpy = mocker.patch(
        'actionBar.locators.getLeftSideArrowsPos', return_value=None)
    getRightSideArrowsPosSpy = mocker.patch(
        'actionBar.locators.getRightSideArrowsPos', return_value=None)
    result = getCooldownsImg(screenshotImg)
    assert result == None
    getLeftSideArrowsPosSpy.assert_called_once_with(screenshotImg)
    getRightSideArrowsPosSpy.assert_not_called()


def test_should_return_None_when_cannot_get_right_side_arrows_pos(mocker):
    getLeftSideArrowsPosSpy = mocker.patch(
        'actionBar.locators.getLeftSideArrowsPos', return_value=(0, 392, 17, 34))
    getRightSideArrowsPosSpy = mocker.patch(
        'actionBar.locators.getRightSideArrowsPos', return_value=None)
    result = getCooldownsImg(screenshotImg)
    assert result == None
    getLeftSideArrowsPosSpy.assert_called_once_with(screenshotImg)
    getRightSideArrowsPosSpy.assert_called_once_with(screenshotImg)


def test_should_get_cooldowns_img():
    cooldownsImgAfterExtraction = getCooldownsImg(screenshotImg)
    np.testing.assert_array_equal(listOfCooldownsImg, cooldownsImgAfterExtraction)
