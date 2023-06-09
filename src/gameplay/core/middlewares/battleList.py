from src.repositories.battleList.core import getCreatures, isAttackingSomeCreature
from src.repositories.battleList.extractors import getContent
from ...typings import Context


# TODO: add unit tests
def setBattleListMiddleware(gameContext: Context) -> Context:
    content = getContent(gameContext['screenshot'])
    gameContext['battleList']['creatures'] = getCreatures(content)
    gameContext['cavebot']['isAttackingSomeCreature'] = isAttackingSomeCreature(gameContext['battleList']['creatures'])
    return gameContext