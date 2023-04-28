import pathlib
from src.repositories.actionBar.core import hasExoriGranCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_exori_gran_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutExoriGranCooldown.png')
    hasCooldown = hasExoriGranCooldown(screenshotImage)
    expectedHasExoriGranCooldown = False
    assert hasCooldown == expectedHasExoriGranCooldown


def test_should_return_True_when_has_exori_gran_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withExoriGranCooldown.png')
    hasCooldown = hasExoriGranCooldown(screenshotImage)
    expectedHasExoriGranCooldown = True
    assert hasCooldown == expectedHasExoriGranCooldown
