import pathlib
from src.features.actionBar.core import hasHasteCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_haste_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutHasteCooldown.png')
    hasCooldown = hasHasteCooldown(screenshotImage)
    expectedHasHasteCooldown = False
    assert hasCooldown == expectedHasHasteCooldown


def test_should_return_True_when_has_haste_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withHasteCooldown.png')
    hasCooldown = hasHasteCooldown(screenshotImage)
    expectedHasHasteCooldown = True
    assert hasCooldown == expectedHasHasteCooldown
