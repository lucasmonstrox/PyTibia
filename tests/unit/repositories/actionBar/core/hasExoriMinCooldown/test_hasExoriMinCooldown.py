import pathlib
from src.repositories.actionBar.core import hasExoriMinCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_exori_min_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutExoriMinCooldown.png')
    hasCooldown = hasExoriMinCooldown(screenshotImage)
    expectedHasExoriMinCooldown = False
    assert hasCooldown == expectedHasExoriMinCooldown


def test_should_return_True_when_has_exori_min_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withExoriMinCooldown.png')
    hasCooldown = hasExoriMinCooldown(screenshotImage)
    expectedHasExoriMinCooldown = True
    assert hasCooldown == expectedHasExoriMinCooldown
