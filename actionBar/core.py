from . import extractors
import utils.core
import utils.image


attackCooldownImg = utils.image.loadFromRGBToGray(
    'actionBar/images/cooldowns/attack.png')
exoriCooldownImg = utils.image.loadFromRGBToGray(
    'actionBar/images/cooldowns/exori.png')
exoriGranCooldownImg = utils.image.loadFromRGBToGray(
    'actionBar/images/cooldowns/exoriGran.png')
exoriMasCooldownImg = utils.image.loadFromRGBToGray(
    'actionBar/images/cooldowns/exoriMas.png')
hasteCooldownImg = utils.image.loadFromRGBToGray(
    'actionBar/images/cooldowns/haste.png')
supportCooldownImg = utils.image.loadFromRGBToGray(
    'actionBar/images/cooldowns/support.png')


def hasCooldownByImg(screenshot, cooldownImg):
    listOfCooldownsImg = extractors.getCooldownsImg(screenshot)
    cooldownImgPos = utils.core.locate(listOfCooldownsImg, cooldownImg)
    cooldownImgIsntPresent = cooldownImgPos is None
    if cooldownImgIsntPresent:
        return False
    (x, _, width, _) = cooldownImgPos
    percentBar = listOfCooldownsImg[20:21, x:x+width]
    firstPixel = percentBar[0][0]
    whitePixelColor = 255
    hasCooldown = firstPixel == whitePixelColor
    return hasCooldown


def hasAttackCooldown(screenshot):
    return hasCooldownByImg(screenshot, attackCooldownImg)


def hasExoriCooldown(screenshot):
    return hasCooldownByImg(screenshot, exoriCooldownImg)


def hasExoriGranCooldown(screenshot):
    return hasCooldownByImg(screenshot, exoriGranCooldownImg)


def hasExoriMasCooldown(screenshot):
    return hasCooldownByImg(screenshot, exoriMasCooldownImg)


def hasHasteCooldown(screenshot):
    return hasCooldownByImg(screenshot, hasteCooldownImg)


def hasSupportCooldown(screenshot):
    return hasCooldownByImg(screenshot, supportCooldownImg)
