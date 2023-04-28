import pathlib
from src.repositories.battleList.core import getBeingAttackedCreatures
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()


def test_should_get_no_being_attacked_creatures():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/noBeingAttackedCreatures.png')
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in getBeingAttackedCreatures(screenshotImage, 3)]
    expectedBeingAttackedCreatures = [False, False, False]
    assert beingAttackedCreatures == expectedBeingAttackedCreatures


def test_should_get_no_being_attacked_creatures_with_highlight():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/noBeingAttackedCreaturesWithHighlight.png')
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in getBeingAttackedCreatures(screenshotImage, 3)]
    expectedBeingAttackedCreatures = [False, False, False]
    assert beingAttackedCreatures == expectedBeingAttackedCreatures


def test_should_get_being_attacked_creatures():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/beingAttackedCreature.png')
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in getBeingAttackedCreatures(screenshotImage, 3)]
    expectedBeingAttackedCreatures = [True, False, False]
    assert beingAttackedCreatures == expectedBeingAttackedCreatures


def test_should_get_being_attacked_creatures_with_highlight_in_non_being_attacked_creature():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/highlightInNonBeingAttackedCreature.png')
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in getBeingAttackedCreatures(screenshotImage, 3)]
    expectedBeingAttackedCreatures = [True, False, False]
    assert beingAttackedCreatures == expectedBeingAttackedCreatures


def test_should_get_being_attacked_creatures_with_highlight_in_being_attacked_creature():
    screenshotImage = loadFromRGBToGray(f'{currentPath}/highlightInBeingAttackedCreature.png')
    beingAttackedCreatures = [beingAttackedCreature for beingAttackedCreature in getBeingAttackedCreatures(screenshotImage, 3)]
    expectedBeingAttackedCreatures = [True, False, False]
    assert beingAttackedCreatures == expectedBeingAttackedCreatures
