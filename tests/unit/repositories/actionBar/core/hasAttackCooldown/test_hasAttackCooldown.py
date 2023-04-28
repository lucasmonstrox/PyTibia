import pathlib
from src.repositories.actionBar.core import hasAttackCooldown
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_return_False_when_has_no_attack_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withoutAttackCooldown.png')
    hasCooldown = hasAttackCooldown(screenshotImage)
    expectedHasAttackCooldown = False
    assert hasCooldown == expectedHasAttackCooldown


def test_should_return_True_when_has_attack_cooldown():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/withAttackCooldown.png')
    hasCooldown = hasAttackCooldown(screenshotImage)
    expectedHasAttackCooldown = True
    assert hasCooldown == expectedHasAttackCooldown
