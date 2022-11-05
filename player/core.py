import numpy as np
import pathlib
import pyautogui
from time import sleep
import utils.core
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()
accessoriesEquippedImg = utils.image.loadAsGrey('radar/images/radar-tools.png')
hpImg = utils.image.loadAsGrey(f'{currentPath}/images/heart.png')
manaImg = utils.image.loadAsGrey(f'{currentPath}/images/mana.png')
bleedingImg = utils.image.loadAsGrey(f'{currentPath}/images/bleeding.png')
cursedImg = utils.image.loadAsGrey(f'{currentPath}/images/cursed.png')
burningImg = utils.image.loadAsGrey(f'{currentPath}/images/burning.png')
fightImg = utils.image.loadAsGrey(f'{currentPath}/images/fight.png')
hungryImg = utils.image.loadAsGrey(f'{currentPath}/images/hungry.png')
poisonedImg = utils.image.loadAsGrey(f'{currentPath}/images/poisoned.png')
pzImg = utils.image.loadAsGrey(f'{currentPath}/images/pz.png')
restingAreaImg = utils.image.loadAsGrey(f'{currentPath}/images/resting-area.png')
stopImg = utils.image.loadAsGrey(f'{currentPath}/images/stop.png')
emptyArmorImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-armor.png')
emptyBeltImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-arrow.png')
emptyBackPackImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-backpack.png')
emptyBootsImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-boots.png')
emptyHelmetImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-helmet.png')
emptyLegsIms = utils.image.loadAsGrey(f'{currentPath}/images/empty-legs.png')
emptyNecklaceImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-necklace.png')
emptyRingImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-ring.png')
emptyShieldImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-shield.png')
emptyWeaponImg = utils.image.loadAsGrey(f'{currentPath}/images/empty-weapon.png')
followingAttackDisImg = utils.image.loadAsGrey(
    f'{currentPath}/images/following-attack-disabled.png')
balancedAttackImg = utils.image.loadAsGrey(f'{currentPath}/images/balanced-attack.png')
defensiveAttackImg = utils.image.loadAsGrey(
    f'{currentPath}/images/defensive-attack.png')
fullAttackImg = utils.image.loadAsGrey(f'{currentPath}/images/full-attack.png')
drunkImg = utils.image.loadAsGrey(f'{currentPath}/images/drunk.png')
electrifiedImg = utils.image.loadAsGrey(f'{currentPath}/images/eletrified.png')
followingAttackImg = utils.image.loadAsGrey(
    f'{currentPath}/images/following-attack.png')
hasteImg = utils.image.loadAsGrey(f'{currentPath}/images/haste.png')
holdingAttackImg = utils.image.loadAsGrey(f'{currentPath}/images/holding-attack.png')
inventoryHiddenImg = utils.image.loadAsGrey(
    f'{currentPath}/images/inventory-hidden.png')
logoutBlockImg = utils.image.loadAsGrey(f'{currentPath}/images/logout-block.png')
readyForPvpImg = utils.image.loadAsGrey(f'{currentPath}/images/ready-for-pvp.png')
slowedImg = utils.image.loadAsGrey(f'{currentPath}/images/slowed.png')
# storeImg = utils.image.loadAsGrey(f'{currentPath}/images/store.png')

hpBarAllowedPixelsColors = np.array([79, 118, 121, 110, 62])
hpBarSize = 94

manaBarAllowedPixelsColors = np.array([68, 95, 97, 89, 52])
manaBarSize = 94


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


def getFightStatusContainer(screenshot, slotName):
    (left, top, _, _) = getStopPos(screenshot)
    fightStatusImgList = {
        'defensive-attack': (screenshot[top - 98: top - 98 + 30, left:left + 30], left, top - 98),
        'balanced-attack': (screenshot[top - 123: top - 123 + 30, left:left + 30], left, top - 123),
        'full-attack': (screenshot[top - 144: top - 144 + 30, left:left + 30], left, top - 144),
        'holding-attack': (screenshot[top - 144: top - 144 + 30, left + 22: left + 22 + 30], left + 22, top - 144),
        'following-attack': (screenshot[top - 123: top - 123 + 30, left + 22: left + 22 + 30], left + 22, top - 123)
    }

    fightStatusImg = fightStatusImgList.get(slotName, None)
    return fightStatusImg


def setFightStatus(screenshot, statusName):
    (container, x, y) = getFightStatusContainer(screenshot, statusName)

    fightStatusList = {
        'defensive-attack': defensiveAttackImg,
        'balanced-attack': balancedAttackImg,
        'full-attack': fullAttackImg,
        'holding-attack': holdingAttackImg,
        'following-attack': followingAttackImg
    }

    statusImg = fightStatusList.get(statusName, None)
    pos = utils.core.locate(container, statusImg)
    if pos is None:
        pyautogui.click(x + 10, y + 10)


def getReadyForPvpContainer(screenshot):
    (left, top, _, _) = getStopPos(screenshot)
    top -= 72
    return screenshot[top: top + 20, left:left + 42], left, top


def setReadyForPvp(screenshot, condition):

    (pvpBtn, left, top) = getReadyForPvpContainer(screenshot)
    pos = utils.core.locate(pvpBtn, readyForPvpImg, 0.5)
    actualStatus = pos is not None

    if condition != actualStatus:
        pyautogui.click(left + 10, top + 10)


def getEquipmentContainer(screenshot, slotName):
    (left, top, _, _) = getStopPos(screenshot)
    equipList = {
        'backpack': (left - 42, top - 128),
        'helmet': (left - 79, top - 142),
        'necklace': (left - 116, top - 128),
        'weapon': (left - 116, top - 92),
        'shield': (left - 42, top - 92),
        'armor': (left - 79, top - 106),
        'ring': (left - 116, top - 56),
        'legs': (left - 79, top - 70),
        'boots': (left - 79, top - 34),
        'belt': (left - 42, top - 56)
    }
    (x, y) = equipList.get(slotName, None)
    return screenshot[y:y + 30, x:x + 30]


def isEquipmentEquipped(screenshot, equipment):
    container = getEquipmentContainer(screenshot, equipment)
    emptyImgList = {
        'backpack': emptyBackPackImg,
        'helmet': emptyHelmetImg,
        'necklace': emptyNecklaceImg,
        'weapon': emptyWeaponImg,
        'shield': emptyShieldImg,
        'armor': emptyArmorImg,
        'ring': emptyRingImg,
        'legs': emptyLegsIms,
        'boots': emptyBootsImg,
        'belt': emptyBeltImg
    }

    emptyImg = emptyImgList.get(equipment, None)
    pos = utils.core.locate(container, emptyImg)
    cond = pos is None
    return cond


def getSpecialConditionsContainer(screenshot):
    (left, top, _, _) = getStopPos(screenshot)
    container = screenshot[top:top + 12, left - 118:left - 118 + 107]
    return container


def hasSpecialCondition(screenshot, condition):
    container = getSpecialConditionsContainer(screenshot)

    condList = {
        'bleeding': bleedingImg,
        'burning': burningImg,
        'cursed': cursedImg,
        'hungry': hungryImg,
        'fight': fightImg,
        'pz': pzImg,
        'restingArea': restingAreaImg,
        'poisoned': poisonedImg,
        'drunk': drunkImg,
        'electrified': electrifiedImg,
        'haste': hasteImg,
        'slowed': slowedImg,
        'logoutBlock': logoutBlockImg
    }

    compareImg = condList.get(condition, None)
    pos = utils.core.locate(container, compareImg)
    cond = pos is not None
    return cond


# def setInventoryVisible(screenshot, condition):
#     pos = utils.core.locate(screenshot, storeImg)
#     inventoryVisible = pos is not None
#     if inventoryVisible == condition:
#         return
#     if pos is None:
#         (left, top, _, _) = radar.core.getRadarToolsPos(screenshot)
#         left -= 118
#         top += 64
#         pyautogui.click(x=left + 6, y=top + 6)
#     else:
#         pyautogui.click(x=pos[0] - 74, y=pos[1] + 6)


def stop(seconds=1):
    pyautogui.press('esc')
    sleep(seconds)
