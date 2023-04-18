import pathlib
from src.utils.core import cacheObjectPosition, locate
from src.utils.image import loadFromRGBToGray


currentPath = pathlib.Path(__file__).parent.resolve()
accessoriesEquippedImg = loadFromRGBToGray('src/features/radar/images/radar-tools.png')
bleedingImg = loadFromRGBToGray(f'{currentPath}/images/bleeding.png')
cursedImg = loadFromRGBToGray(f'{currentPath}/images/cursed.png')
burningImg = loadFromRGBToGray(f'{currentPath}/images/burning.png')
fightImg = loadFromRGBToGray(f'{currentPath}/images/fight.png')
hungryImg = loadFromRGBToGray(f'{currentPath}/images/hungry.png')
poisonedImg = loadFromRGBToGray(f'{currentPath}/images/poisoned.png')
pzImg = loadFromRGBToGray(f'{currentPath}/images/pz.png')
restingAreaImg = loadFromRGBToGray(f'{currentPath}/images/resting-area.png')
stopImg = loadFromRGBToGray(f'{currentPath}/images/stop.png')
emptyArmorImg = loadFromRGBToGray(f'{currentPath}/images/empty-armor.png')
emptyBeltImg = loadFromRGBToGray(f'{currentPath}/images/empty-arrow.png')
emptyBackPackImg = loadFromRGBToGray(f'{currentPath}/images/empty-backpack.png')
emptyBootsImg = loadFromRGBToGray(f'{currentPath}/images/empty-boots.png')
emptyHelmetImg = loadFromRGBToGray(f'{currentPath}/images/empty-helmet.png')
emptyLegsIms = loadFromRGBToGray(f'{currentPath}/images/empty-legs.png')
emptyNecklaceImg = loadFromRGBToGray(f'{currentPath}/images/empty-necklace.png')
emptyRingImg = loadFromRGBToGray(f'{currentPath}/images/empty-ring.png')
emptyShieldImg = loadFromRGBToGray(f'{currentPath}/images/empty-shield.png')
emptyWeaponImg = loadFromRGBToGray(f'{currentPath}/images/empty-weapon.png')
followingAttackDisImg = loadFromRGBToGray(
    f'{currentPath}/images/following-attack-disabled.png')
balancedAttackImg = loadFromRGBToGray(f'{currentPath}/images/balanced-attack.png')
defensiveAttackImg = loadFromRGBToGray(
    f'{currentPath}/images/defensive-attack.png')
fullAttackImg = loadFromRGBToGray(f'{currentPath}/images/full-attack.png')
drunkImg = loadFromRGBToGray(f'{currentPath}/images/drunk.png')
electrifiedImg = loadFromRGBToGray(f'{currentPath}/images/eletrified.png')
followingAttackImg = loadFromRGBToGray(
    f'{currentPath}/images/following-attack.png')
hasteImg = loadFromRGBToGray(f'{currentPath}/images/haste.png')
holdingAttackImg = loadFromRGBToGray(f'{currentPath}/images/holding-attack.png')
inventoryHiddenImg = loadFromRGBToGray(
    f'{currentPath}/images/inventory-hidden.png')
logoutBlockImg = loadFromRGBToGray(f'{currentPath}/images/logout-block.png')
readyForPvpImg = loadFromRGBToGray(f'{currentPath}/images/ready-for-pvp.png')
slowedImg = loadFromRGBToGray(f'{currentPath}/images/slowed.png')


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
@cacheObjectPosition
def getStopButtonPosition(screenshot):
    return locate(screenshot, stopImg)


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getFightStatusContainer(screenshot, slotName):
    (left, top, _, _) = getStopButtonPosition(screenshot)
    fightStatusImgList = {
        'defensive-attack': (screenshot[top - 98: top - 98 + 30, left:left + 30], left, top - 98),
        'balanced-attack': (screenshot[top - 123: top - 123 + 30, left:left + 30], left, top - 123),
        'full-attack': (screenshot[top - 144: top - 144 + 30, left:left + 30], left, top - 144),
        'holding-attack': (screenshot[top - 144: top - 144 + 30, left + 22: left + 22 + 30], left + 22, top - 144),
        'following-attack': (screenshot[top - 123: top - 123 + 30, left + 22: left + 22 + 30], left + 22, top - 123)
    }

    fightStatusImg = fightStatusImgList.get(slotName, None)
    return fightStatusImg


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getReadyForPvpContainer(screenshot):
    (left, top, _, _) = getStopButtonPosition(screenshot)
    top -= 72
    return screenshot[top: top + 20, left:left + 42], left, top


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getEquipmentContainer(screenshot, slotName):
    (left, top, _, _) = getStopButtonPosition(screenshot)
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


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
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


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getSpecialConditionsContainer(screenshot):
    stopPos = getStopButtonPosition(screenshot)
    if stopPos is None:
        return None
    (left, top, _, _) = stopPos
    return screenshot[top:top + 12, left - 118:left - 118 + 107]


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
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
