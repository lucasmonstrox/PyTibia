from src.features.statusBar.core import getManaPercentage, getHpPercentage
from src.features.skills.core import getHp, getMana


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
