import pathlib
from src.repositories.actionBar.core import hasSupportCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_support_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutSupportCooldown.png')
    hasCooldown = hasSupportCooldown(screenshotImage)
    expectedHasSupportCooldown = False
    assert hasCooldown == expectedHasSupportCooldown


def test_should_return_True_when_has_support_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withSupportCooldown.png')
    hasCooldown = hasSupportCooldown(screenshotImage)
    expectedHasSupportCooldown = True
    assert hasCooldown == expectedHasSupportCooldown
