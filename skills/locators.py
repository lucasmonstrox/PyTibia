import pathlib
import utils.core
import utils.image


currentPath = pathlib.Path(__file__).parent.resolve()

capacityImage = utils.image.loadFromRGBToGray(
    f'{currentPath}/images/capacity.png')
hitPointsImage = utils.image.loadFromRGBToGray(
    f'{currentPath}/images/hitPoints.png')
manaImage = utils.image.loadFromRGBToGray(f'{currentPath}/images/mana.png')
speedImage = utils.image.loadFromRGBToGray(f'{currentPath}/images/speed.png')
staminaImage = utils.image.loadFromRGBToGray(
    f'{currentPath}/images/stamina.png')


@utils.core.cacheObjectPos
def getCapacityPosition(screenshot):
    return utils.core.locate(screenshot, capacityImage)


@utils.core.cacheObjectPos
def getHitPointsPosition(screenshot):
    return utils.core.locate(screenshot, hitPointsImage)


@utils.core.cacheObjectPos
def getManaPosition(screenshot):
    return utils.core.locate(screenshot, manaImage)


@utils.core.cacheObjectPos
def getSpeedPosition(screenshot):
    return utils.core.locate(screenshot, speedImage)


@utils.core.cacheObjectPos
def getStaminaPosition(screenshot):
    return utils.core.locate(screenshot, staminaImage)
