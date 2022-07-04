from utils import utils

attackCooldownImg = utils.loadImgAsArray('actionBar/images/cooldowns/attack.png')
exoriCooldownImg = utils.loadImgAsArray('actionBar/images/cooldowns/exori.png')
exoriGranCooldownImg = utils.loadImgAsArray('actionBar/images/cooldowns/exoriGran.png')
exoriMasCooldownImg = utils.loadImgAsArray('actionBar/images/cooldowns/exoriMas.png')


def hasAttackCooldown(screenshot):
    return utils.locate(screenshot, attackCooldownImg) is not None


def hasExoriCooldown(screenshot):
    return utils.locate(screenshot, exoriCooldownImg) is not None


def hasExoriGranCooldown(screenshot):
    return utils.locate(screenshot, exoriGranCooldownImg) is not None


def hasExoriMasCooldown(screenshot):
    return utils.locate(screenshot, exoriMasCooldownImg) is not None