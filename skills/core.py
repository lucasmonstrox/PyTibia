from skills import config, locators
import utils.core
import utils.image


def getCapacity(screenshot):
    capacityPosition = locators.getCapacityPosition(screenshot)
    didntFoundCapacityPosition = capacityPosition is None
    if didntFoundCapacityPosition:
        return None
    count = getCount(screenshot, capacityPosition)
    return count


def getHitPoints(screenshot):
    hitPointsPosition = locators.getHitPointsPosition(screenshot)
    didntFoundHitPointsPosition = hitPointsPosition is None
    if didntFoundHitPointsPosition:
        return None
    count = getCount(screenshot, hitPointsPosition)
    return count


def getSpeed(screenshot):
    speedPosition = locators.getSpeedPosition(screenshot)
    didntFoundSpeedPosition = speedPosition is None
    if didntFoundSpeedPosition:
        return None
    count = getCount(screenshot, speedPosition)
    return count


def getCount(screenshot, position):
    (x, y, _, _) = position
    capacityHundredsCountsImage = screenshot[y:y + 8, x + 144 - 22:x + 144]
    capacityHundredsCountsImage = utils.image.convertGraysToBlack(
        capacityHundredsCountsImage)
    capacityHundredsCountsHashKey = utils.core.hashit(
        capacityHundredsCountsImage)
    capacityHundredsCount = 0
    if capacityHundredsCountsHashKey in config.numbersHashes:
        capacityHundredsCount = config.numbersHashes[capacityHundredsCountsHashKey]
    capacityThousandsCountsImage = screenshot[y:y + 8, x + 116 - 22:x + 116]
    capacityThousandsCountsImage = utils.image.convertGraysToBlack(
        capacityThousandsCountsImage)
    capacityThousandsCountsHashKey = utils.core.hashit(
        capacityThousandsCountsImage)
    capacityThousandsCount = 0
    if capacityThousandsCountsHashKey in config.numbersHashes:
        capacityThousandsCount = config.numbersHashes[capacityThousandsCountsHashKey] * 1000
    capacity = capacityThousandsCount + capacityHundredsCount
    return capacity
