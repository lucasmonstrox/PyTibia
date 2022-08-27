import actionBar.locators


def getCooldownsImg(screenshot):
    (x0, y0, _, _) = actionBar.locators.getLeftSideArrowsPos(screenshot)
    (x1, _, _, _) = actionBar.locators.getRightSideArrowsPos(screenshot)
    cooldownsImg = screenshot[y0+37:y0+37+22, x0:x1]
    return cooldownsImg
