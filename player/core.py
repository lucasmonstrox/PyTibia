import cv2
import numpy as np
from time import sleep
import pyautogui
import utils.core, utils.image


accessoriesEquipedImg = utils.image.loadAsArray('radar/images/radar-tools.png')
hpImg = utils.image.loadAsArray('player/images/heart.png')
manaImg = utils.image.loadAsArray('player/images/mana.png')
bleedingImg = utils.image.loadAsArray('player/images/bleeding.png')
cursedImg = utils.image.loadAsArray('player/images/cursed.png')
burningImg = utils.image.loadAsArray('player/images/burning.png')
fightImg = utils.image.loadAsArray('player/images/fight.png')
hungryImg = utils.image.loadAsArray('player/images/hungry.png')
poisonedImg = utils.image.loadAsArray('player/images/poisoned.png')
pzImg = utils.image.loadAsArray('player/images/pz.png')
restingAreaImg = utils.image.loadAsArray('player/images/resting-area.png')
stopImg = utils.image.loadAsArray('player/images/stop.png')

hpBarAllowedPixelsColors = np.array([79, 118, 121, 110, 62])
hpBarSize=94

manaBarAllowedPixelsColors = np.array([68, 95, 97, 89, 52])
manaBarSize=94


def getFilledBarPercentage(bar, size=100, allowedPixelsColors=[]):
    bar = np.where(np.isin(bar, allowedPixelsColors), 0, bar)
    barPercent = np.count_nonzero(bar == 0)
    percent = (barPercent * 100 // size)
    return percent


@utils.core.cacheObjectPos
def getHeartPos(screenshot):
    return utils.core.locate(screenshot, hpImg)


def getHealthPercentage(screenshot):
    heartPos = getHeartPos(screenshot)
    didntGetHpPos = heartPos == None
    if didntGetHpPos:
        return None
    bar = getHealthBar(screenshot, heartPos)
    percent = getFilledBarPercentage(bar, size=hpBarSize, 
                               allowedPixelsColors=hpBarAllowedPixelsColors)
    return percent


def getHealthBar(screenshot, heartPos):
    (left, top, _, _) = heartPos
    y0 = top + 5
    y1 = y0 + 1
    x0 = left + 13
    x1 = x0 + hpBarSize
    bar = screenshot[y0:y1, x0:x1][0]
    return bar


@utils.core.cacheObjectPos
def getManaPos(screenshot):
    return utils.core.locate(screenshot, manaImg)


def getManaPercentage(screenshot):
    manaPos = getManaPos(screenshot)
    didntGetHpPos = manaPos == None
    if didntGetHpPos:
        return None
    bar = getManaBar(screenshot, manaPos)
    percent = getFilledBarPercentage(bar, size=manaBarSize, 
                               allowedPixelsColors=manaBarAllowedPixelsColors)
    return percent


def getManaBar(screenshot, heartPos):
    (left, top, _, _) = heartPos
    y0 = top + 5
    y1 = y0 + 1
    x0 = left + 14
    x1 = x0 + manaBarSize
    bar = screenshot[y0:y1, x0:x1][0]
    return bar


@utils.core.cacheObjectPos
def getStopPos(screenshot):
    return utils.core.locate(screenshot, stopImg)


def getSpecialConditionsContainer(screenshot):
    (left, top, _, _) = getStopPos(screenshot)
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
    hungry = utils.core.locate(hungryImg, container) is not None
    return hungry


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


def getPlayerWindowCoordinate():
    # TODO: detect game window automatically
    playerWindowCoordinateX = 6 + (736 / 2)
    # TODO: detect game window automatically
    playerWindowCoordinateY = 90 + (539 / 2)
    return (playerWindowCoordinateX, playerWindowCoordinateY)


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
    pos = utils.core.locate(accessoriesEquipedImg, screenshot)
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


def stop(seconds=1):
    pyautogui.press('esc')
    sleep(seconds)
