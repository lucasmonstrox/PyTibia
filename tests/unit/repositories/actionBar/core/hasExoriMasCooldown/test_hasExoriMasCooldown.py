import pathlib
from src.repositories.actionBar.core import hasExoriMasCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_exori_mas_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutExoriMasCooldown.png')
    hasCooldown = hasExoriMasCooldown(screenshotImage)
    expectedHasExoriMasCooldown = False
    assert hasCooldown == expectedHasExoriMasCooldown


def test_should_return_True_when_has_exori_mas_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withExoriMasCooldown.png')
    hasCooldown = hasExoriMasCooldown(screenshotImage)
    expectedHasExoriMasCooldown = True
    assert hasCooldown == expectedHasExoriMasCooldown
