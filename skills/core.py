from skills import config, locators
import utils.core
import utils.image


def getCapacity(screenshot):
    capacityPosition = locators.getCapacityPosition(screenshot)
    didntFoundCapacityPosition = capacityPosition is None
    if didntFoundCapacityPosition:
        return None
    count = getValuesCount(screenshot, capacityPosition)
    return count


def getHitPoints(screenshot):
    hitPointsPosition = locators.getHitPointsPosition(screenshot)
    didntFoundHitPointsPosition = hitPointsPosition is None
    if didntFoundHitPointsPosition:
        return None
    count = getValuesCount(screenshot, hitPointsPosition)
    return count


def getSpeed(screenshot):
    speedPosition = locators.getSpeedPosition(screenshot)
    didntFoundSpeedPosition = speedPosition is None
    if didntFoundSpeedPosition:
        return None
    count = getValuesCount(screenshot, speedPosition)
    return count


def getStamina(screenshot):
    staminaPosition = locators.getStaminaPosition(screenshot)
    didntFoundStaminaPosition = staminaPosition is None
    if didntFoundStaminaPosition:
        return None
    count = getMinutesCount(screenshot, staminaPosition)
    return count


def getMinutesCount(screenshot, position):
    (x, y, _, _) = position
    minutesCountsImage = screenshot[y:y + 8, x + 144 - 14:x + 144]
    minutesCountsImage = utils.image.convertGraysToBlack(minutesCountsImage)
    minutesCountsHashKey = utils.core.hashit(minutesCountsImage)
    minutesCount = 0
    if minutesCountsHashKey in config.minutesOrHoursHashes:
        minutesCount = config.minutesOrHoursHashes[minutesCountsHashKey]
    hoursCountsImage = screenshot[y:y + 8, x + 110:x + 124]
    hoursCountsImage = utils.image.convertGraysToBlack(hoursCountsImage)
    hoursCountsHashKey = utils.core.hashit(hoursCountsImage)
    hoursCount = 0
    if hoursCountsHashKey in config.minutesOrHoursHashes:
        hoursCount = config.minutesOrHoursHashes[hoursCountsHashKey]
    minutes = (hoursCount * 60) + minutesCount
    return minutes


def getValuesCount(screenshot, position):
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
