import pathlib
from src.utils.core import hashit, locate
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
images = {
    'arrows': {
        'leftHud01': loadFromRGBToGray(f'{currentPath}/images/arrows/leftHud01.png'),
        'leftHud10': loadFromRGBToGray(f'{currentPath}/images/arrows/leftHud10.png'),
        'leftHud11': loadFromRGBToGray(f'{currentPath}/images/arrows/leftHud11.png'),
        'rightHud01': loadFromRGBToGray(f'{currentPath}/images/arrows/rightHud01.png'),
        'rightHud10': loadFromRGBToGray(f'{currentPath}/images/arrows/rightHud10.png'),
        'rightHud11': loadFromRGBToGray(f'{currentPath}/images/arrows/rightHud11.png'),
    },
    720: {
        'holeOpen': loadFromRGBToGray(f'{currentPath}/images/waypoint/holeOpen720.png')
    },
    1080: {
        'holeOpen': loadFromRGBToGray(f'{currentPath}/images/waypoint/holeOpen1080.png')
    }
}
arrowsImagesHashes = {
    hashit(images['arrows']['leftHud01']): 'leftHud01',
    hashit(images['arrows']['leftHud10']): 'leftHud10',
    hashit(images['arrows']['leftHud11']): 'leftHud11',
    hashit(images['arrows']['rightHud01']): 'rightHud01',
    hashit(images['arrows']['rightHud10']): 'rightHud10',
    hashit(images['arrows']['rightHud11']): 'rightHud11',
}
hudSizes = {
    720: (480, 352),
    1080: (960, 704)
}
hudCache = {
    'left': {'arrow': None, 'position': None},
    'right': {'arrow': None, 'position': None},
}

def getLeftArrowPosition(screenshot):
    global hudCache
    if hudCache['left']['position'] is not None:
        images['arrows'][hudCache['left']['arrow']]
        leftArrowImage = images['arrows'][hudCache['left']['arrow']]
        leftArrowImageHash = hashit(leftArrowImage)
        if arrowsImagesHashes.get(leftArrowImageHash, None) is not None:
            return hudCache['left']['position']
    leftHud01Position = locate(screenshot, images['arrows']['leftHud01'])
    if leftHud01Position is not None:
        hudCache['left']['arrow'] = 'leftHud01'
        hudCache['left']['position'] = leftHud01Position
        return leftHud01Position
    leftHud11Position = locate(screenshot, images['arrows']['leftHud11'])
    if leftHud11Position is not None:
        hudCache['left']['arrow'] = 'leftHud11'
        hudCache['left']['position'] = leftHud11Position
        return leftHud11Position
    leftHud10Position = locate(screenshot, images['arrows']['leftHud10'])
    if leftHud10Position is not None:
        hudCache['left']['arrow'] = 'leftHud10'
        hudCache['left']['position'] = leftHud10Position
        return leftHud10Position


def getRightArrowPosition(screenshot):
    global hudCache
    if hudCache['right']['position'] is not None:
        images['arrows'][hudCache['right']['arrow']]
        rightArrowImage = images['arrows'][hudCache['right']['arrow']]
        rightArrowImageHash = hashit(rightArrowImage)
        if arrowsImagesHashes.get(rightArrowImageHash, None) is not None:
            return hudCache['right']['position']
    rightHud01Position = locate(screenshot, images['arrows']['rightHud01'])
    if rightHud01Position is not None:
        hudCache['right']['arrow'] = 'rightHud01'
        hudCache['right']['position'] = rightHud01Position
        return rightHud01Position
    rightHud11Position = locate(screenshot, images['arrows']['rightHud11'])
    if rightHud11Position is not None:
        hudCache['right']['arrow'] = 'rightHud11'
        hudCache['right']['position'] = rightHud11Position
        return rightHud11Position
    rightHud10Position = locate(screenshot, images['arrows']['rightHud10'])
    if rightHud10Position is not None:
        hudCache['right']['arrow'] = 'rightHud10'
        hudCache['right']['position'] = rightHud10Position
        return rightHud10Position


def getCoordinate(screenshot, _):
    global hudCache
    leftArrowPosition = getLeftArrowPosition(screenshot)
    if leftArrowPosition is None:
        return None
    rightArrowPosition = getRightArrowPosition(screenshot)
    if rightArrowPosition is None:
        return None
    x = ((leftArrowPosition[0] + 7 + rightArrowPosition[0]) // 2) - 480
    y = leftArrowPosition[1] + 5
    return (x, y, 960, 704)


def getImgByCoordinate(screenshot, coordinates, hudSize):
    return screenshot[coordinates[1]:coordinates[1] +
                     hudSize[1], coordinates[0]:coordinates[0] + hudSize[0]]


def getSlotFromCoordinate(currentCoordinate, coordinate):
    diffX = coordinate[0] - currentCoordinate[0]
    diffXAbs = abs(diffX)
    if diffXAbs > 7:
        return None
    diffY = coordinate[1] - currentCoordinate[1]
    diffYAbs = abs(diffY)
    if diffYAbs > 5:
        return None
    hudCoordinateX = 7 + diffX
    hudCoordinateY = 5 + diffY
    return hudCoordinateX, hudCoordinateY


def getSlotImg(hudImg, slot, slotWidth):
    xOfSlot, yOfSlot = slot
    x = xOfSlot * slotWidth
    y = yOfSlot * slotWidth
    slotImg = hudImg[y:y + slotWidth, x:x + slotWidth]
    return slotImg


def isHoleOpen(hudImg, holeOpenImg, coordinate, targetCoordinate):
    slotWidth = len(hudImg[1]) // 15
    slot = getSlotFromCoordinate(coordinate, targetCoordinate)
    slotImg = getSlotImg(hudImg, slot, slotWidth)
    holeOpenLocation = locate(slotImg, holeOpenImg)
    isOpen = holeOpenLocation is not None
    return isOpen
