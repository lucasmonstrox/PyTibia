import cv2
import numpy as np
from PIL import Image, ImageGrab
from PIL.ImageOps import grayscale
from radar import radar
import skimage
from time import sleep
from utils import utils
import pyautogui


accessoriesEquipedImg = np.array(cv2.imread('radar/images/radar-tools.png'))
hpImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/hp.png'), cv2.COLOR_RGB2GRAY))
manaImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/mana.png'), cv2.COLOR_RGB2GRAY))
bleedingImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/bleeding.png'), cv2.COLOR_RGB2GRAY))
cursedImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/cursed.png'), cv2.COLOR_RGB2GRAY))
burningImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/burning.png'), cv2.COLOR_RGB2GRAY))
fightImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/fight.png'), cv2.COLOR_RGB2GRAY))
hungryImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/hungry.png'), cv2.COLOR_RGB2GRAY))
poisonedImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/poisoned.png'), cv2.COLOR_RGB2GRAY))
pzImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/pz.png'), cv2.COLOR_RGB2GRAY))
restingAreaImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/resting-area.png'), cv2.COLOR_RGB2GRAY))
stopImg = np.array(cv2.cvtColor(cv2.imread(
    'player/images/stop.png'), cv2.COLOR_RGB2GRAY))


@utils.cacheObjectPos
def getHpPos(screenshot):
    return utils.locate(screenshot, hpImg)


def getHp(screenshot):
    (left, top, width, height) = getHpPos(screenshot)
    statusBar = screenshot[top + 5:top + 6, left + 13:left + 107][0]
    pixelOf100Percent = statusBar[93]
    contains100Percent = pixelOf100Percent == 62
    if contains100Percent:
        return 100
    pixelOf90Percent = statusBar[84]
    contains90Percent = pixelOf90Percent == 121
    if contains90Percent:
        return 90
    pixelOf80Percent = statusBar[75]
    contains80Percent = pixelOf80Percent == 121
    if contains80Percent:
        return 80
    pixelOf70Percent = statusBar[65]
    pixelOf70Percent = pixelOf70Percent == 121
    if pixelOf70Percent:
        return 70
    pixelOf60Percent = statusBar[56]
    pixelOf60Percent = pixelOf60Percent == 121
    if pixelOf60Percent:
        return 60
    pixelOf50Percent = statusBar[47]
    pixelOf50Percent = pixelOf50Percent == 121
    if pixelOf50Percent:
        return 50
    pixelOf40Percent = statusBar[37]
    pixelOf40Percent = pixelOf40Percent == 121
    if pixelOf40Percent:
        return 40
    pixelOf30Percent = statusBar[28]
    pixelOf30Percent = pixelOf30Percent == 121
    if pixelOf30Percent:
        return 30
    pixelOf20Percent = statusBar[18]
    pixelOf20Percent = pixelOf20Percent == 121
    if pixelOf20Percent:
        return 20
    pixelOf10Percent = statusBar[9]
    pixelOf10Percent = pixelOf10Percent == 121
    if pixelOf10Percent:
        return 10
    pixelOf5Percent = statusBar[4]
    pixelOf5Percent = pixelOf5Percent == 121
    if pixelOf5Percent:
        return 5
    pixelOf1Percent = statusBar[0]
    pixelOf1Percent = pixelOf1Percent == 60
    if pixelOf1Percent:
        return 1
    return 0


@utils.cacheObjectPos
def getManaPos(screenshot):
    return utils.locate(screenshot, manaImg)


@utils.cacheObjectPos
def getStopPos(screenshot):
    return utils.locate(screenshot, stopImg)


def getSpecialConditionsContainer(screenshot):
    (left, top, width, height) = getStopPos(screenshot)
    container = screenshot[top:top+12, left-118:left-118+107]
    return container


def isBleeding(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, bleedingImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isBleeding = res[1] >= 0.9
    return isBleeding


def isBurning(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, burningImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isBurning = res[1] >= 0.9
    return isBurning


def isCursed(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, cursedImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isCursed = res[1] >= 0.9
    return isCursed


def isHungry(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    Image.fromarray(container).save('xavier.png')
    match = cv2.matchTemplate(container, hungryImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    print(res)
    isHungry = res[1] >= 0.9
    return isHungry


def isInFight(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, fightImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isInFight = res[1] >= 0.9
    return isInFight


def isInPz(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, pzImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isInPz = res[1] >= 0.9
    return isInPz


def isInRestingArea(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, restingAreaImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isInRestingArea = res[1] >= 0.9
    return isInRestingArea


def isPoisoned(screenshot):
    container = getSpecialConditionsContainer(screenshot)
    match = cv2.matchTemplate(container, poisonedImg, cv2.TM_CCOEFF_NORMED)
    res = cv2.minMaxLoc(match)
    isPoisoned = res[1] >= 0.9
    return isPoisoned


def getMana(screenshot):
    (left, top, width, height) = getManaPos(screenshot)
    statusBar = screenshot[top + 5:top + 6, left + 14:left + 108][0]
    pixelOf100Percent = statusBar[93]
    contains100Percent = pixelOf100Percent == 52
    if contains100Percent:
        return 100
    pixelOf90Percent = statusBar[84]
    contains90Percent = pixelOf90Percent == 97
    if contains90Percent:
        return 90
    pixelOf80Percent = statusBar[75]
    contains80Percent = pixelOf80Percent == 97
    if contains80Percent:
        return 80
    pixelOf70Percent = statusBar[65]
    contains70Percent = pixelOf70Percent == 97
    if contains70Percent:
        return 70
    pixelOf60Percent = statusBar[56]
    contains60Percent = pixelOf60Percent == 97
    if contains60Percent:
        return 60
    pixelOf50Percent = statusBar[47]
    contains50Percent = pixelOf50Percent == 97
    if contains50Percent:
        return 50
    pixelOf40Percent = statusBar[37]
    contains40Percent = pixelOf40Percent == 97
    if contains40Percent:
        return 40
    pixelOf30Percent = statusBar[28]
    contains30Percent = pixelOf30Percent == 97
    if contains30Percent:
        return 30
    pixelOf20Percent = statusBar[18]
    contains20Percent = pixelOf20Percent == 97
    if contains20Percent:
        return 20
    pixelOf10Percent = statusBar[9]
    contains10Percent = pixelOf10Percent == 97
    if contains10Percent:
        return 10
    pixelOf5Percent = statusBar[4]
    contains5Percent = pixelOf5Percent == 97
    if contains5Percent:
        return 5
    pixelOf1Percent = statusBar[0]
    contains1Percent = pixelOf1Percent == 68
    if contains1Percent:
        return 1
    return 0


def getPlayerWindowCoordinate():
    # TODO: detect game window automatically
    playerWindowCoordinateX = 6 + (736 / 2)
    # TODO: detect game window automatically
    playerWindowCoordinateY = 90 + (539 / 2)
    return (playerWindowCoordinateX, playerWindowCoordinateY)


def goToCoordinate(currentCoordinate, destinationCoordinate):
    # currentCoordinate = getCoordinate()
    currentPixelCoordinate = utils.getPixelFromCoordinate(currentCoordinate)
    destinationPixelCoordinate = utils.getPixelFromCoordinate(
        destinationCoordinate)
    currentFloor = radar.getFloorLevel()
    paths, cost = skimage.graph.route_through_array(
        radar.floorsAsBoolean[currentFloor], start=currentPixelCoordinate, end=destinationPixelCoordinate, fully_connected=False)
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
    mouseClickX = playerWindowCoordinateX + \
        ((destinationX - playerCoordinateX) * squareMeterSize)
    # TODO: avoid battleye detection clicking in a random pixel inside squaremeter
    mouseClickY = playerWindowCoordinateY + \
        ((destinationY - playerCoordinateY) * squareMeterSize)
    # TODO: avoid battleye detection adding humanoid movementation
    pyautogui.moveTo(mouseClickX, mouseClickY, duration=0.75)
    pyautogui.click(mouseClickX, mouseClickY)


def goToCoordinateByRadarClick(coordinate):
    (radarCenterX, radarCenterY) = radar.getCenterBounds()
    playerCoordinate = getCoordinate()
    (playerCoordinatePixelY, playerCoordinatePixelX) = utils.getPixelFromCoordinate(
        playerCoordinate)
    (destinationCoordinatePixelY,
     destinationCoordinatePixelX) = utils.getPixelFromCoordinate(coordinate)
    x = destinationCoordinatePixelX - playerCoordinatePixelX + radarCenterX
    y = destinationCoordinatePixelY - playerCoordinatePixelY + radarCenterY
    pyautogui.moveTo(x, y)
    pyautogui.click()


def enableFollowingAttack():
    pos = pyautogui.locateOnScreen(
        'player/images/following-attack-disabled.png', confidence=0.9)
    if pos == None:
        # TODO: throw an exception
        return
    pyautogui.click(pos.left, pos.top)


def hasAccessoriesEquiped(screenshot):
    screenshotLen = len(screenshot)
    screenshot = screenshot[:, screenshotLen-200:screenshotLen]
    pos = utils.locate(accessoriesEquipedImg, screenshot)
    hasAccessoriesEquiped = pos == None
    return hasAccessoriesEquiped


def hasArmorEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-armor.png', confidence=0.9)
    hasArmorEquipped = pos == None
    return hasArmorEquipped


def hasBackpackEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-backpack.png', confidence=0.9)
    hasBackpackEquipped = pos == None
    return hasBackpackEquipped


def hasBalancedAttack():
    pos = pyautogui.locateOnScreen(
        'player/images/balanced-attack.png', confidence=0.9)
    hasBalancedAttack = pos != None
    return hasBalancedAttack


def hasBootsEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-boots.png', confidence=0.9)
    hasBootsEquipped = pos == None
    return hasBootsEquipped


def hasDefensiveAttack():
    pos = pyautogui.locateOnScreen(
        'player/images/defensive-attack.png', confidence=0.9)
    hasDefensiveAttack = pos != None
    return hasDefensiveAttack


def hasFullAttack():
    pos = pyautogui.locateOnScreen(
        'player/images/full-attack.png', confidence=0.9)
    hasFullAttack = pos != None
    return hasFullAttack


def hasHelmetEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-helmet.png', confidence=0.9)
    hasHelmetEquipped = pos == None
    return hasHelmetEquipped


def hasLegsEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-legs.png', confidence=0.9)
    hasLegsEquipped = pos == None
    return hasLegsEquipped


def hasNecklaceEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-necklace.png', confidence=0.9)
    hasNecklaceEquipped = pos == None
    return hasNecklaceEquipped


def hasRingEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-ring.png', confidence=0.9)
    hasRingEquipped = pos == None
    return hasRingEquipped


def hasShieldEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-shield.png', confidence=0.9)
    hasShieldEquipped = pos == None
    return hasShieldEquipped


def hasWeaponEquipped():
    pos = pyautogui.locateOnScreen(
        'player/images/empty-weapon.png', confidence=0.9)
    hasWeaponEquipped = pos == None
    return hasWeaponEquipped


def isDrunk():
    pos = pyautogui.locateOnScreen('player/images/drunk.png', confidence=0.9)
    isDrunk = pos != None
    return isDrunk


def isEletrified():
    pos = pyautogui.locateOnScreen(
        'player/images/eletrified.png', confidence=0.9)
    isEletrified = pos != None
    return isEletrified


def isFollowingAttack():
    pos = pyautogui.locateOnScreen(
        'player/images/following-attack.png', confidence=0.9)
    isFollowingAttack = pos != None
    return isFollowingAttack


def isHaste():
    pos = pyautogui.locateOnScreen('player/images/haste.png', confidence=0.9)
    isHaste = pos != None
    return isHaste


def isHoldingAttack():
    pos = pyautogui.locateOnScreen(
        'player/images/holding-attack.png', confidence=0.9)
    isHoldingAttack = pos != None
    return isHoldingAttack


def isInventoryVisible():
    pos = pyautogui.locateOnScreen(
        'player/images/inventory-hidden.png', confidence=0.9)
    isInventoryVisible = pos == None
    return isInventoryVisible


def isLogoutBlock():
    pos = pyautogui.locateOnScreen(
        'player/images/logout-block.png', confidence=0.9)
    isLogoutBlock = pos != None
    return isLogoutBlock


def isReadyForPvp():
    pos = pyautogui.locateOnScreen(
        'player/images/ready-for-pvp.png', confidence=0.9)
    isReadyForPvp = pos != None
    return isReadyForPvp


def isSlowed():
    pos = pyautogui.locateOnScreen('player/images/slowed.png', confidence=0.9)
    isSlowed = pos != None
    return isSlowed
