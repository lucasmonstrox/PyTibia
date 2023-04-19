from src.repositories.skills.core import getHp, getMana
from src.repositories.statusBar.core import getManaPercentage, getHpPercentage


def setMapPlayerStatusMiddleware(context):
    hpPercentage = getHpPercentage(context['screenshot'])
    context['statusBar']['hpPercentage'] = hpPercentage
    hp = getHp(context['screenshot'])
    context['statusBar']['hp'] = hp
    manaPercentage = getManaPercentage(context['screenshot'])
    context['statusBar']['manaPercentage'] = manaPercentage
    mana = getMana(context['screenshot'])
    context['statusBar']['mana'] = mana
    gameContext = context
    return gameContext
