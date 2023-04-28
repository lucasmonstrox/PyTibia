from src.repositories.skills.core import getHp, getMana
from src.repositories.statusBar.core import getManaPercentage, getHpPercentage
from ...typings import Context


# TODO: add unit tests
def setMapPlayerStatusMiddleware(gameContext: Context) -> Context:
    gameContext['statusBar']['hp'] = getHp(gameContext['screenshot'])
    gameContext['statusBar']['hpPercentage'] = getHpPercentage(gameContext['screenshot'])
    gameContext['statusBar']['mana'] = getMana(gameContext['screenshot'])
    gameContext['statusBar']['manaPercentage'] = getManaPercentage(gameContext['screenshot'])
    return gameContext
