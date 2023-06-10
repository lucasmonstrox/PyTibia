from src.shared.typings import Coordinate
from src.utils.keyboard import keyUp
from .typings import Context


def coordinatesAreEqual(firstCoordinate: Coordinate, secondCoordinate: Coordinate) -> bool:
    if firstCoordinate[0] != secondCoordinate[0]:
        return False
    if firstCoordinate[1] != secondCoordinate[1]:
        return False
    if firstCoordinate[2] != secondCoordinate[2]:
        return False
    return True

# TODO: add unit tests
def releaseKeys(context: Context) -> Context:
    if context['lastPressedKey'] is not None:
        keyUp(context['lastPressedKey'])
        context['lastPressedKey'] = None
    return context