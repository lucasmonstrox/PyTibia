from src.utils.core import hashit, locate
from .config import arrowsImagesHashes, gameWindowCache, images


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getLeftArrowPosition(screenshot):
    global gameWindowCache
    if gameWindowCache['left']['position'] is not None:
        images['arrows'][gameWindowCache['left']['arrow']]
        leftArrowImage = images['arrows'][gameWindowCache['left']['arrow']]
        leftArrowImageHash = hashit(leftArrowImage)
        if arrowsImagesHashes.get(leftArrowImageHash, None) is not None:
            return gameWindowCache['left']['position']
    leftGameWindow01Position = locate(screenshot, images['arrows']['leftGameWindow01'])
    if leftGameWindow01Position is not None:
        gameWindowCache['left']['arrow'] = 'leftGameWindow01'
        gameWindowCache['left']['position'] = leftGameWindow01Position
        return leftGameWindow01Position
    leftGameWindow11Position = locate(screenshot, images['arrows']['leftGameWindow11'])
    if leftGameWindow11Position is not None:
        gameWindowCache['left']['arrow'] = 'leftGameWindow11'
        gameWindowCache['left']['position'] = leftGameWindow11Position
        return leftGameWindow11Position
    leftGameWindow10Position = locate(screenshot, images['arrows']['leftGameWindow10'])
    if leftGameWindow10Position is not None:
        gameWindowCache['left']['arrow'] = 'leftGameWindow10'
        gameWindowCache['left']['position'] = leftGameWindow10Position
        return leftGameWindow10Position


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getRightArrowPosition(screenshot):
    global gameWindowCache
    if gameWindowCache['right']['position'] is not None:
        images['arrows'][gameWindowCache['right']['arrow']]
        rightArrowImage = images['arrows'][gameWindowCache['right']['arrow']]
        rightArrowImageHash = hashit(rightArrowImage)
        if arrowsImagesHashes.get(rightArrowImageHash, None) is not None:
            return gameWindowCache['right']['position']
    rightGameWindow01Position = locate(screenshot, images['arrows']['rightGameWindow01'])
    if rightGameWindow01Position is not None:
        gameWindowCache['right']['arrow'] = 'rightGameWindow01'
        gameWindowCache['right']['position'] = rightGameWindow01Position
        return rightGameWindow01Position
    rightGameWindow11Position = locate(screenshot, images['arrows']['rightGameWindow11'])
    if rightGameWindow11Position is not None:
        gameWindowCache['right']['arrow'] = 'rightGameWindow11'
        gameWindowCache['right']['position'] = rightGameWindow11Position
        return rightGameWindow11Position
    rightGameWindow10Position = locate(screenshot, images['arrows']['rightGameWindow10'])
    if rightGameWindow10Position is not None:
        gameWindowCache['right']['arrow'] = 'rightGameWindow10'
        gameWindowCache['right']['position'] = rightGameWindow10Position
        return rightGameWindow10Position


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getCoordinate(screenshot, _):
    global gameWindowCache
    leftArrowPosition = getLeftArrowPosition(screenshot)
    if leftArrowPosition is None:
        return None
    rightArrowPosition = getRightArrowPosition(screenshot)
    if rightArrowPosition is None:
        return None
    x = ((leftArrowPosition[0] + 7 + rightArrowPosition[0]) // 2) - 480
    y = leftArrowPosition[1] + 5
    return (x, y, 960, 704)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getImageByCoordinate(screenshot, coordinates, gameWindowSize):
    return screenshot[coordinates[1]:coordinates[1] +
                     gameWindowSize[1], coordinates[0]:coordinates[0] + gameWindowSize[0]]


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getSlotFromCoordinate(currentCoordinate, coordinate):
    diffX = coordinate[0] - currentCoordinate[0]
    diffXAbs = abs(diffX)
    if diffXAbs > 7:
        return None
    diffY = coordinate[1] - currentCoordinate[1]
    diffYAbs = abs(diffY)
    if diffYAbs > 5:
        return None
    gameWindowCoordinateX = 7 + diffX
    gameWindowCoordinateY = 5 + diffY
    return gameWindowCoordinateX, gameWindowCoordinateY


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getSlotImg(gameWindowImg, slot, slotWidth):
    xOfSlot, yOfSlot = slot
    x = xOfSlot * slotWidth
    y = yOfSlot * slotWidth
    slotImg = gameWindowImg[y:y + slotWidth, x:x + slotWidth]
    return slotImg


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def isHoleOpen(gameWindowImg, holeOpenImg, coordinate, targetCoordinate):
    slotWidth = len(gameWindowImg[1]) // 15
    slot = getSlotFromCoordinate(coordinate, targetCoordinate)
    slotImg = getSlotImg(gameWindowImg, slot, slotWidth)
    holeOpenLocation = locate(slotImg, holeOpenImg)
    isOpen = holeOpenLocation is not None
    return isOpen
