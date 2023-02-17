import numpy as np
import pathlib
from actionBar.extractors import getCooldownsImage
from utils.image import load, RGBtoGray


currentPath = pathlib.Path(__file__).parent.resolve()
screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
listOfCooldownsImg = RGBtoGray(load(f'{currentPath}/listOfCooldownsImg.png'))


def test_should_return_None_when_cannot_get_left_side_arrows_pos(mocker):
    getLeftArrowsPosSpy = mocker.patch(
        'actionBar.locators.getLeftArrowsPos', return_value=None)
    getRightArrowsPosSpy = mocker.patch(
        'actionBar.locators.getRightArrowsPos', return_value=None)
    result = getCooldownsImage(screenshotImg)
    assert result == None
    getLeftArrowsPosSpy.assert_called_once_with(screenshotImg)
    getRightArrowsPosSpy.assert_not_called()


def test_should_return_None_when_cannot_get_right_side_arrows_pos(mocker):
    getLeftArrowsPosSpy = mocker.patch(
        'actionBar.locators.getLeftArrowsPos', return_value=(0, 392, 17, 34))
    getRightArrowsPosSpy = mocker.patch(
        'actionBar.locators.getRightArrowsPos', return_value=None)
    result = getCooldownsImage(screenshotImg)
    assert result == None
    getLeftArrowsPosSpy.assert_called_once_with(screenshotImg)
    getRightArrowsPosSpy.assert_called_once_with(screenshotImg)


def test_should_get_cooldowns_img():
    cooldownsImgAfterExtraction = getCooldownsImage(screenshotImg)
    np.testing.assert_array_equal(listOfCooldownsImg, cooldownsImgAfterExtraction)
