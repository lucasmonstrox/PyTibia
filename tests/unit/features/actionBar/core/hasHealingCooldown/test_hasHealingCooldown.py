import pathlib
from src.repositories.actionBar.core import hasHealingCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_healing_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutHealingCooldown.png')
    hasCooldown = hasHealingCooldown(screenshotImage)
    expectedHasHealingCooldown = False
    assert hasCooldown == expectedHasHealingCooldown


def test_should_return_True_when_has_healing_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withHealingCooldown.png')
    hasCooldown = hasHealingCooldown(screenshotImage)
    expectedHasHealingCooldown = True
    assert hasCooldown == expectedHasHealingCooldown
