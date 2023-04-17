from src.utils.core import getScreenshot


def setScreenshot(gameContext):
    gameContext['screenshot'] = getScreenshot()
    return gameContext