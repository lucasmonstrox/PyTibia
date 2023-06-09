import pathlib
from src.repositories.actionBar.core import hasCooldownByImage
from src.utils.image import loadFromRGBToGray


actionBarPath = 'src/repositories/actionBar'
currentPath = pathlib.Path(__file__).parent.resolve()
screenshotImage = loadFromRGBToGray(f'{currentPath}/screenshot.png')
listOfCooldownsImage = loadFromRGBToGray(f'{currentPath}/listOfCooldownsImage.png')
cooldownImage = loadFromRGBToGray(f'{actionBarPath}/images/cooldowns/exori.png')


def test_should_return_None_when_getCooldownsImage_return_None(mocker):
    getCooldownsImageSpy = mocker.patch('src.repositories.actionBar.extractors.getCooldownsImage', return_value=None)
    locateSpy = mocker.patch('src.utils.core.locate', return_value=None)
    hasCooldown = hasCooldownByImage(screenshotImage, cooldownImage)
    expectedHasCooldownByImage = None
    assert hasCooldown == expectedHasCooldownByImage
    getCooldownsImageSpy.assert_called_with(screenshotImage)
    locateSpy.assert_not_called()


def test_should_return_False_when_locate_return_None(mocker):
    getCooldownsImageSpy = mocker.patch('src.repositories.actionBar.extractors.getCooldownsImage', return_value=listOfCooldownsImage)
    locateSpy = mocker.patch('src.utils.core.locate', return_value=None)
    hasCooldown = hasCooldownByImage(screenshotImage, cooldownImage)
    expectedHasCooldownByImage = False
    assert hasCooldown == expectedHasCooldownByImage
    getCooldownsImageSpy.assert_called_with(screenshotImage)
    locateSpy.assert_called_with(listOfCooldownsImage, cooldownImage)


def test_should_return_True_when_has_cooldown_by_image(mocker):
    mocker.patch('src.repositories.actionBar.extractors.getCooldownsImage',
                 return_value=listOfCooldownsImage)
    mocker.patch('src.utils.core.locate', return_value=(209, 0, 20, 20))
    hasCooldown = hasCooldownByImage(screenshotImage, cooldownImage)
    expectedHasCooldownByImage = True
    assert hasCooldown == expectedHasCooldownByImage
