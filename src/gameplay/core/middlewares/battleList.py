from src.repositories.battleList.core import getCreatures, isAttackingSomeCreature
from src.repositories.battleList.extractors import getContent
from ...typings import Context


# TODO: add unit tests
def setBattleListMiddleware(gameContext: Context) -> Context:
    content = getContent(gameContext['screenshot'])
    gameContext['battleList']['creatures'] = getCreatures(content)
    hasBattleListCreatures = len(gameContext['battleList']['creatures']) > 0
    # TODO: avoid clever code
    gameContext['cavebot']['isAttackingSomeCreature'] = isAttackingSomeCreature(gameContext['battleList']['creatures']) if hasBattleListCreatures else False
    return gameContext