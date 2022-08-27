import actionBar.locators
import utils.core
import utils.image


attackCooldownImg = utils.image.loadAsGrey(
    'actionBar/images/cooldowns/attack.png')
exoriCooldownImg = utils.image.loadAsGrey(
    'actionBar/images/cooldowns/exori.png')
exoriGranCooldownImg = utils.image.loadAsGrey(
    'actionBar/images/cooldowns/exoriGran.png')
exoriMasCooldownImg = utils.image.loadAsGrey(
    'actionBar/images/cooldowns/exoriMas.png')
supportCooldownImg = utils.image.loadAsGrey(
    'actionBar/images/cooldowns/support.png')
hasteCooldownImg = utils.image.loadAsGrey(
    'actionBar/images/cooldowns/haste.png')


def getCooldownsImg(screenshot):
    (x0, y0, _, _) = actionBar.locators.getLeftSideArrowsPos(screenshot)
    (x1, _, _, _) = actionBar.locators.getRightSideArrowsPos(screenshot)
    cooldownsImg = screenshot[y0+37:y0+37+22, x0:x1]
    return cooldownsImg


def hasCooldownByImg(screenshot, cooldownImg):
    listOfCooldownsImg = getCooldownsImg(screenshot)
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


def hasSupportCooldown(screenshot):
    return hasCooldownByImg(screenshot, supportCooldownImg)


def hasHasteCooldown(screenshot):
    return hasCooldownByImg(screenshot, hasteCooldownImg)
