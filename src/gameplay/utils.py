from src.utils.keyboard import keyUp


# TODO: add parameters types
def coordinatesAreEqual(firstCoordinate, secondCoordinate) -> bool:
    if firstCoordinate[0] != secondCoordinate[0]:
        return False
    if firstCoordinate[1] != secondCoordinate[1]:
        return False
    if firstCoordinate[2] != secondCoordinate[2]:
        return False
    return True

# TODO: add parameter type
def releaseKeys(context):
    if context['lastPressedKey'] is not None:
        keyUp(context['lastPressedKey'])
        context['lastPressedKey'] = None
    return context