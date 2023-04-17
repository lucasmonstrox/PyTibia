import numpy as np
import pathlib
import pyautogui
from time import sleep
from src.utils.core import cacheObjectPos, locate
from src.utils.image import loadAsGrey


currentPath = pathlib.Path(__file__).parent.resolve()
accessoriesEquippedImg = loadAsGrey('src/features/radar/images/radar-tools.png')
bleedingImg = loadAsGrey(f'{currentPath}/images/bleeding.png')
cursedImg = loadAsGrey(f'{currentPath}/images/cursed.png')
burningImg = loadAsGrey(f'{currentPath}/images/burning.png')
fightImg = loadAsGrey(f'{currentPath}/images/fight.png')
hungryImg = loadAsGrey(f'{currentPath}/images/hungry.png')
poisonedImg = loadAsGrey(f'{currentPath}/images/poisoned.png')
pzImg = loadAsGrey(f'{currentPath}/images/pz.png')
restingAreaImg = loadAsGrey(f'{currentPath}/images/resting-area.png')
stopImg = loadAsGrey(f'{currentPath}/images/stop.png')
emptyArmorImg = loadAsGrey(f'{currentPath}/images/empty-armor.png')
emptyBeltImg = loadAsGrey(f'{currentPath}/images/empty-arrow.png')
emptyBackPackImg = loadAsGrey(f'{currentPath}/images/empty-backpack.png')
emptyBootsImg = loadAsGrey(f'{currentPath}/images/empty-boots.png')
emptyHelmetImg = loadAsGrey(f'{currentPath}/images/empty-helmet.png')
emptyLegsIms = loadAsGrey(f'{currentPath}/images/empty-legs.png')
emptyNecklaceImg = loadAsGrey(f'{currentPath}/images/empty-necklace.png')
emptyRingImg = loadAsGrey(f'{currentPath}/images/empty-ring.png')
emptyShieldImg = loadAsGrey(f'{currentPath}/images/empty-shield.png')
emptyWeaponImg = loadAsGrey(f'{currentPath}/images/empty-weapon.png')
followingAttackDisImg = loadAsGrey(
    f'{currentPath}/images/following-attack-disabled.png')
balancedAttackImg = loadAsGrey(f'{currentPath}/images/balanced-attack.png')
defensiveAttackImg = loadAsGrey(
    f'{currentPath}/images/defensive-attack.png')
fullAttackImg = loadAsGrey(f'{currentPath}/images/full-attack.png')
drunkImg = loadAsGrey(f'{currentPath}/images/drunk.png')
electrifiedImg = loadAsGrey(f'{currentPath}/images/eletrified.png')
followingAttackImg = loadAsGrey(
    f'{currentPath}/images/following-attack.png')
hasteImg = loadAsGrey(f'{currentPath}/images/haste.png')
holdingAttackImg = loadAsGrey(f'{currentPath}/images/holding-attack.png')
inventoryHiddenImg = loadAsGrey(
    f'{currentPath}/images/inventory-hidden.png')
logoutBlockImg = loadAsGrey(f'{currentPath}/images/logout-block.png')
readyForPvpImg = loadAsGrey(f'{currentPath}/images/ready-for-pvp.png')
slowedImg = loadAsGrey(f'{currentPath}/images/slowed.png')
# storeImg = loadAsGrey(f'{currentPath}/images/store.png')

hpBarAllowedPixelsColors = np.array([79, 118, 121, 110, 62])
hpBarSize = 94

manaBarAllowedPixelsColors = np.array([68, 95, 97, 89, 52])
manaBarSize = 94


@cacheObjectPos
def getStopPos(screenshot):
    return locate(screenshot, stopImg)


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
    pos = locate(container, statusImg)
    if pos is None:
        pyautogui.click(x + 10, y + 10)


def getReadyForPvpContainer(screenshot):
    (left, top, _, _) = getStopPos(screenshot)
    top -= 72
    return screenshot[top: top + 20, left:left + 42], left, top


def setReadyForPvp(screenshot, condition):

    (pvpBtn, left, top) = getReadyForPvpContainer(screenshot)
    pos = locate(pvpBtn, readyForPvpImg, 0.5)
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
    pos = locate(container, emptyImg)
    cond = pos is None
    return cond


def getSpecialConditionsContainer(screenshot):
    stopPos = getStopPos(screenshot)
    if stopPos is None:
        return None
    (left, top, _, _) = stopPos
    return screenshot[top:top + 12, left - 118:left - 118 + 107]


def hasSpecialCondition(screenshot, condition):
    specialConditionsContainer = getSpecialConditionsContainer(screenshot)
    cannotGetSpecialConditionsContainer = specialConditionsContainer is None
    if cannotGetSpecialConditionsContainer:
        return None
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
    conditionImg = condList.get(condition, None)
    pos = locate(specialConditionsContainer, conditionImg)
    cond = pos is not None
    return cond


# def setInventoryVisible(screenshot, condition):
#     pos = locate(screenshot, storeImg)
#     inventoryVisible = pos is not None
#     if inventoryVisible == condition:
#         return
#     if pos is None:
#         (left, top, _, _) = src.features.radar.core.getRadarToolsPos(screenshot)
#         left -= 118
#         top += 64
#         pyautogui.click(x=left + 6, y=top + 6)
#     else:
#         pyautogui.click(x=pos[0] - 74, y=pos[1] + 6)


def stop(seconds=1):
    pyautogui.press('esc')
    sleep(seconds)
