import pathlib
from src.repositories.actionBar.core import hasExoriCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_exori_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutExoriCooldown.png')
    hasCooldown = hasExoriCooldown(screenshotImage)
    expectedHasExoriCooldown = False
    assert hasCooldown == expectedHasExoriCooldown


def test_should_return_True_when_has_exori_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withExoriCooldown.png')
    hasCooldown = hasExoriCooldown(screenshotImage)
    expectedHasExoriCooldown = True
    assert hasCooldown == expectedHasExoriCooldown
