import numpy as np
import pathlib
from src.repositories.actionBar.extractors import getCooldownsImage
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
screenshotImage = loadFromRGBToGray(f'{currentPath}/screenshot.png')
listOfCooldownsImage = loadFromRGBToGray(
    f'{currentPath}/listOfCooldownsImage.png')


def test_should_return_None_when_cannot_get_left_arrows_position(mocker):
    getLeftArrowsPositionSpy = mocker.patch(
        'src.repositories.actionBar.locators.getLeftArrowsPosition', return_value=None)
    getRightArrowsPositionSpy = mocker.patch(
        'src.repositories.actionBar.locators.getRightArrowsPosition', return_value=None)
    cooldownsImage = getCooldownsImage(screenshotImage)
    expectedCooldownsImage = None
    assert cooldownsImage is expectedCooldownsImage
    getLeftArrowsPositionSpy.assert_called_once_with(screenshotImage)
    getRightArrowsPositionSpy.assert_not_called()


def test_should_return_None_when_cannot_get_right_arrows_position(mocker):
    getLeftArrowsPositionSpy = mocker.patch(
        'src.repositories.actionBar.locators.getLeftArrowsPosition', return_value=(0, 392, 17, 34))
    getRightArrowsPositionSpy = mocker.patch(
        'src.repositories.actionBar.locators.getRightArrowsPosition', return_value=None)
    result = getCooldownsImage(screenshotImage)
    assert result is None
    getLeftArrowsPositionSpy.assert_called_once_with(screenshotImage)
    getRightArrowsPositionSpy.assert_called_once_with(screenshotImage)


def test_should_get_cooldowns_image():
    cooldownsImageAfterExtraction = getCooldownsImage(screenshotImage)
    np.testing.assert_array_equal(
        listOfCooldownsImage, cooldownsImageAfterExtraction)
