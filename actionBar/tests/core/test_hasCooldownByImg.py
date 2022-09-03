import pathlib
from actionBar.core import hasCooldownByImg
from utils.image import load, RGBtoGray

actionBarPath = pathlib.Path(__file__).parent.parent.parent.resolve()
currentPath = pathlib.Path(__file__).parent.resolve()
screenshotImg = RGBtoGray(load(f'{currentPath}/screenshot.png'))
listOfCooldownsImg = RGBtoGray(load(f'{currentPath}/listOfCooldownsImg.png'))
cooldownImg = RGBtoGray(load(f'{actionBarPath}/images/cooldowns/exori.png'))


def test_should_return_None_when_getCooldownsImg_return_None(mocker):
    getCooldownsImgSpy = mocker.patch(
        'actionBar.extractors.getCooldownsImg', return_value=None)
    result = hasCooldownByImg(screenshotImg, cooldownImg)
    getCooldownsImgSpy.assert_called_with(screenshotImg)
    assert result == None


def test_should_return_False_when_locate_return_None(mocker):
    mocker.patch('actionBar.extractors.getCooldownsImg',
                 return_value=listOfCooldownsImg)
    locateSpy = mocker.patch('utils.core.locate', return_value=None)
    result = hasCooldownByImg(screenshotImg, cooldownImg)
    locateSpy.assert_called_with(listOfCooldownsImg, cooldownImg)
    assert result == False


def test_should_return_True_when_has_cooldown_by_img(mocker):
    mocker.patch('actionBar.extractors.getCooldownsImg',
                 return_value=listOfCooldownsImg)
    mocker.patch('utils.core.locate', return_value=(209, 0, 20, 20))
    result = hasCooldownByImg(screenshotImg, cooldownImg)
    assert result == True
