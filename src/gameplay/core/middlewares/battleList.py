from src.features.battleList.core import getCreatures, isAttackingSomeCreature
from src.features.battleList.extractors import getContent


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def setBattleListMiddleware(gameContext):
    content = getContent(gameContext['screenshot'])
    gameContext['battleList']['creatures'] = getCreatures(content)
    hasBattleListCreatures = len(gameContext['battleList']['creatures']) > 0
    gameContext['cavebot']['isAttackingSomeCreature'] = isAttackingSomeCreature(gameContext['battleList']['creatures']) if hasBattleListCreatures else False
    return gameContext