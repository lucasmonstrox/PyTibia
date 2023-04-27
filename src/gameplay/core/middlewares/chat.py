from src.repositories.chat.core import getTabs
from ...typings import Context


# TODO: add unit tests
def setChatTabsMiddleware(gameContext: Context) -> Context:
    gameContext['chat']['tabs'] = getTabs(gameContext['screenshot'])
    return gameContext