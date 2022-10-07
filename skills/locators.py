import utils.core
import utils.image

capacityImage = utils.image.loadFromRGBToGray('skills/images/capacity.png')
hitPointsImage = utils.image.loadFromRGBToGray('skills/images/hitPoints.png')
speedImage = utils.image.loadFromRGBToGray('skills/images/speed.png')
staminaImage = utils.image.loadFromRGBToGray('skills/images/stamina.png')


@utils.core.cacheObjectPos
def getCapacityPosition(screenshot):
    return utils.core.locate(screenshot, capacityImage)


@utils.core.cacheObjectPos
def getHitPointsPosition(screenshot):
    return utils.core.locate(screenshot, hitPointsImage)


@utils.core.cacheObjectPos
def getSpeedPosition(screenshot):
    return utils.core.locate(screenshot, speedImage)


@utils.core.cacheObjectPos
def getStaminaPosition(screenshot):
    return utils.core.locate(screenshot, staminaImage)