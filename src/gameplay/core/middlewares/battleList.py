from src.features.battleList.core import getCreatures, isAttackingSomeCreature
from src.features.battleList.extractors import getContent
from ...typings import Context


# TODO: add unit tests
def setBattleListMiddleware(gameContext: Context) -> Context:
    content = getContent(gameContext['screenshot'])
    gameContext['battleList']['creatures'] = getCreatures(content)
    hasBattleListCreatures = len(gameContext['battleList']['creatures']) > 0
    gameContext['cavebot']['isAttackingSomeCreature'] = isAttackingSomeCreature(gameContext['battleList']['creatures']) if hasBattleListCreatures else False
    return gameContext