from src.repositories.battleList.core import getCreatures, isAttackingSomeCreature
from src.repositories.battleList.extractors import getContent
from ...typings import Context


# TODO: add unit tests
def setBattleListMiddleware(context: Context) -> Context:
    content = getContent(context['screenshot'])
    context['battleList']['creatures'] = getCreatures(content)
    context['cavebot']['isAttackingSomeCreature'] = isAttackingSomeCreature(context['battleList']['creatures'])
    return context