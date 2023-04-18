from src.utils.core import getScreenshot


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def setScreenshot(gameContext):
    gameContext['screenshot'] = getScreenshot()
    return gameContext
