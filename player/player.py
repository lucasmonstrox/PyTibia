import pyautogui
import skimage.graph
from radar import radar
from time import sleep
from utils import utils

healthBar = {
    "dimensions": {
        "width": 89,
        "height": 11
    },
    "percentValues": {
        "100": { "distance": 89, "pixelColor": (100, 46, 49) },
        "80": { "distance": 71, "pixelColor": (219, 79, 79) },
        "60": { "distance": 53, "pixelColor": (219, 79, 79) },
        "40": { "distance": 36, "pixelColor": (219, 79, 79) },
        "20": { "distance": 18, "pixelColor": (219, 79, 79) },
        "10": { "distance": 9, "pixelColor": (219, 79, 79) },
        "5": { "distance": 4, "pixelColor": (219, 79, 79) }
    }
}

manaBar = {
    "dimensions": {
        "width": 89,
        "height": 11
    },
    "percentValues": {
        "100": { "distance": 89, "pixelColor": (45, 45, 105) },
        "80": { "distance": 71, "pixelColor": (83, 80, 218) },
        "60": { "distance": 53, "pixelColor": (83, 80, 218) },
        "40": { "distance": 36, "pixelColor": (83, 80, 218) },
        "20": { "distance": 18, "pixelColor": (83, 80, 218) },
        "10": { "distance": 10, "pixelColor": (83, 80, 218) },
        "5": { "distance": 4, "pixelColor": (83, 80, 218) }
    }
}

def getBarPercentValue(bar, barPos):
    if barPos == None:
        # TODO: throw a custom exception
        return None
    # TODO: export current screenshot from observable function to gain performance
    im = pyautogui.screenshot()
    for percentValue in bar['percentValues'].keys():
        # pixel to check if bar contains current value
        currentValueLeft = barPos['left'] + bar['percentValues'][percentValue]['distance']
        # middle of bar
        middleOfBar = barPos['top'] + int(barPos['height'] / 2)
        pixelCoordinate = (currentValueLeft, middleOfBar)
        pixelColor = im.getpixel(pixelCoordinate)
        hasCurrentPercentValue = pixelColor == bar['percentValues'][percentValue]['pixelColor']
        if hasCurrentPercentValue:
            return percentValue
    # its really hard to determinate when player has 0 or 1 of bar percent
    return 0

def getCoordinate():
    # TODO: cache it if window coordinates doesn't change
    radarPos = radar.getPos()
    if not radarPos:
        # TODO: throw a custom exception
        return None
    radarPosX, radarPosY = radarPos
    floorLevel = radar.getFloorLevel()
    radarScreenshot = pyautogui.screenshot(region=(radarPosX, radarPosY, 106, 109))
    # load directly into numpy array to gain performance all possible radar center with radius
    currentPositionBounds = pyautogui.locate(
        radarScreenshot,
        radar.floorsAreaImgs[floorLevel],
        confidence=radar.floorsConfidence[floorLevel]
    )
    currentX, currentY = utils.getCenterOfBounds(currentPositionBounds)
    currentMapPixelCoordinate = (int(currentY), int(currentX))
    (playerCoordinateX, playerCoordinateY) = utils.getCoordinateFromPixel(currentMapPixelCoordinate)
    playerCoordinate = (playerCoordinateX, playerCoordinateY, floorLevel)
    return playerCoordinate

def getHealthPercent():
    global healthBar
    healthBarPos = getHealthBarPos()
    healthPercent = getBarPercentValue(healthBar, healthBarPos)
    return healthPercent

def getHealthBarPos():
    global healthBar
    symbolPos = getHearthSymbolPos()
    distanceBetweenSymbolAndBar = 16
    extraYBetweenSymbolAndBar = 1
    pos = {
        "left": symbolPos.left + distanceBetweenSymbolAndBar,
        "top": symbolPos.top - extraYBetweenSymbolAndBar,
        "width": healthBar['dimensions']['width'],
        "height": healthBar['dimensions']['height']
    }
    return pos

def getHearthSymbolPos():
    pos = pyautogui.locateOnScreen('player/images/health.png', confidence=0.85)
    return pos

def getManaBarPos():
    global manaBar
    symbolPos = getManaSymbolPos()
    distanceBetweenSymbolAndBar = 17
    extraYBetweenSymbolAndBar = 1
    pos = {
        "left": symbolPos.left + distanceBetweenSymbolAndBar,
        "top": symbolPos.top - extraYBetweenSymbolAndBar,
        "width": manaBar['dimensions']['width'],
        "height": manaBar['dimensions']['height']
    }
    return pos

def getManaPercent():
    global manaBar
    manaBarPos = getManaBarPos()
    manaPercent = getBarPercentValue(manaBar, manaBarPos)
    return manaPercent

def getManaSymbolPos():
    pos = pyautogui.locateOnScreen('player/images/mana.png', confidence=0.85)
    return pos

def getPlayerWindowCoordinate():
    # TODO: detect game window automatically
    playerWindowCoordinateX = 6 +(736 / 2)
    # TODO: detect game window automatically
    playerWindowCoordinateY = 90 + (539 / 2)
    return (playerWindowCoordinateX, playerWindowCoordinateY)

# this is a experimental function
def goToCoordinate(destinationCoordinate):
    currentCoordinate = getCoordinate()
    currentPixelCoordinate = utils.getPixelFromCoordinate(currentCoordinate)
    destinationPixelCoordinate = utils.getPixelFromCoordinate(destinationCoordinate)
    currentFloor = radar.getFloorLevel()
    paths, cost = skimage.graph.route_through_array(radar.floorsAsBoolean[currentFloor], start=currentPixelCoordinate, end=destinationPixelCoordinate, fully_connected=False)
    pathsLength = len(paths)
    for index, currentPosition in enumerate(paths):
        isLastPosition = index + 1 == pathsLength
        if isLastPosition:
            break
        nextPosition = paths[index + 1]
        nextPositionX, nextPositionY = nextPosition
        currentPositionX, currentPositionY = currentPosition
        shouldMoveUp = currentPositionX > nextPositionX
        if shouldMoveUp:
            pyautogui.press('up')
            sleep(0.25)
            continue
        shouldMoveDown = currentPositionX < nextPositionX
        if shouldMoveDown:
            pyautogui.press('down')
            sleep(0.25)
            continue
        shouldMoveLeft = currentPositionY > nextPositionY
        if shouldMoveLeft:
            pyautogui.press('left')
            sleep(0.25)
            continue
        shouldMoveRight = currentPositionY < nextPositionY
        if shouldMoveRight:
            pyautogui.press('right')
            sleep(0.25)
            continue

def goToCoordinateByScreenClick(coordinate):
    playerCoordinateX, playerCoordinateY, playerCoordinateZ = getCoordinate()
    playerWindowCoordinateX, playerWindowCoordinateY = getPlayerWindowCoordinate()
    destinationX, destinationY, destinationZ = coordinate
    squareMeterSize = utils.getSquareMeterSize()
    # TODO: avoid battleye detection clicking in a random pixel inside squaremeter
    mouseClickX = playerWindowCoordinateX + ((destinationX - playerCoordinateX) * squareMeterSize)
    # TODO: avoid battleye detection clicking in a random pixel inside squaremeter
    mouseClickY = playerWindowCoordinateY + ((destinationY - playerCoordinateY) * squareMeterSize)
    # TODO: avoid battleye detection adding humanoid movementation
    pyautogui.moveTo(mouseClickX, mouseClickY, duration=0.15)
    pyautogui.click(mouseClickX, mouseClickY)

# TODO: do not click in same pixel to avoid batleeye detection, click near by
def goToCoordinateByRadarClick(coordinate):
    (radarCenterX, radarCenterY) = radar.getCenterBounds()
    playerCoordinate = getCoordinate()
    (playerCoordinatePixelY, playerCoordinatePixelX) = utils.getPixelFromCoordinate(playerCoordinate)
    (destinationCoordinatePixelY, destinationCoordinatePixelX) = utils.getPixelFromCoordinate(coordinate)
    x = destinationCoordinatePixelX - playerCoordinatePixelX + radarCenterX
    y = destinationCoordinatePixelY - playerCoordinatePixelY + radarCenterY
    pyautogui.moveTo(x, y)
    pyautogui.click()

def hasAccessoriesEquiped():
    pos = pyautogui.locateOnScreen('player/images/empty-arrow.png', confidence=0.9)
    hasAccessoriesEquiped = pos == None
    return hasAccessoriesEquiped

def hasArmorEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-armor.png', confidence=0.9)
    hasArmorEquipped = pos == None
    return hasArmorEquipped

def hasBackpackEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-backpack.png', confidence=0.9)
    hasBackpackEquipped = pos == None
    return hasBackpackEquipped

def hasBalancedAttack():
    pos = pyautogui.locateOnScreen('player/images/balanced-attack.png', confidence=0.9)
    hasBalancedAttack = pos != None
    return hasBalancedAttack

def hasBootsEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-boots.png', confidence=0.9)
    hasBootsEquipped = pos == None
    return hasBootsEquipped

def hasDefensiveAttack():
    pos = pyautogui.locateOnScreen('player/images/defensive-attack.png', confidence=0.9)
    hasDefensiveAttack = pos != None
    return hasDefensiveAttack

def hasFullAttack():
    pos = pyautogui.locateOnScreen('player/images/full-attack.png', confidence=0.9)
    hasFullAttack = pos != None
    return hasFullAttack

def hasHelmetEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-helmet.png', confidence=0.9)
    hasHelmetEquipped = pos == None
    return hasHelmetEquipped

def hasLegsEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-legs.png', confidence=0.9)
    hasLegsEquipped = pos == None
    return hasLegsEquipped

def hasNecklaceEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-necklace.png', confidence=0.9)
    hasNecklaceEquipped = pos == None
    return hasNecklaceEquipped

def hasRingEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-ring.png', confidence=0.9)
    hasRingEquipped = pos == None
    return hasRingEquipped

def hasShieldEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-shield.png', confidence=0.9)
    hasShieldEquipped = pos == None
    return hasShieldEquipped

def hasWeaponEquipped():
    pos = pyautogui.locateOnScreen('player/images/empty-weapon.png', confidence=0.9)
    hasWeaponEquipped = pos == None
    return hasWeaponEquipped

def isBleeding():
    pos = pyautogui.locateOnScreen('player/images/bleeding.png', confidence=0.9)
    isBleeding = pos != None
    return isBleeding

def isBurning():
    pos = pyautogui.locateOnScreen('player/images/burning.png', confidence=0.9)
    isBurning = pos != None
    return isBurning

def isDrunk():
    pos = pyautogui.locateOnScreen('player/images/drunk.png', confidence=0.9)
    isDrunk = pos != None
    return isDrunk

def isEletrified():
    pos = pyautogui.locateOnScreen('player/images/eletrified.png', confidence=0.9)
    isEletrified = pos != None
    return isEletrified

def isFollowingAttack():
    pos = pyautogui.locateOnScreen('player/images/following-attack.png', confidence=0.9)
    isFollowingAttack = pos != None
    return isFollowingAttack

def isHaste():
    pos = pyautogui.locateOnScreen('player/images/haste.png', confidence=0.9)
    isHaste = pos != None
    return isHaste

def isHoldingAttack():
    pos = pyautogui.locateOnScreen('player/images/holding-attack.png', confidence=0.9)
    isHoldingAttack = pos != None
    return isHoldingAttack

def isInventoryVisible():
    pos = pyautogui.locateOnScreen('player/images/inventory-hidden.png', confidence=0.9)
    isInventoryVisible = pos == None
    return isInventoryVisible

def isInPz():
    pos = pyautogui.locateOnScreen('player/images/pz.png', confidence=0.9)
    isPz = pos != None
    return isPz

def isLogoutBlock():
    pos = pyautogui.locateOnScreen('player/images/logout-block.png', confidence=0.9)
    isLogoutBlock = pos != None
    return isLogoutBlock

def isPoisoned():
    pos = pyautogui.locateOnScreen('player/images/poisoned.png', confidence=0.9)
    isPoisoned = pos != None
    return isPoisoned

def isReadyForPvp():
    pos = pyautogui.locateOnScreen('player/images/ready-for-pvp.png', confidence=0.9)
    isReadyForPvp = pos != None
    return isReadyForPvp

def isSlowed():
    pos = pyautogui.locateOnScreen('player/images/slowed.png', confidence=0.9)
    isSlowed = pos != None
    return isSlowed