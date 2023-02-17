from .locators import getLeftArrowsPos, getRightArrowsPos


def getCooldownsImage(screenshot):
    leftArrowsPos = getLeftArrowsPos(screenshot)
    cannotGetLeftArrowsPos = leftArrowsPos is None
    if cannotGetLeftArrowsPos:
        return None
    rightArrowsPos = getRightArrowsPos(screenshot)
    cannotGetRightArrowsPos = rightArrowsPos is None
    if cannotGetRightArrowsPos:
        return None
    x0, y0, _, _ = leftArrowsPos
    x1, _, _, _ = rightArrowsPos
    cooldownsImage = screenshot[y0 + 37: y0 + 37 + 22, x0:x1]
    return cooldownsImage
