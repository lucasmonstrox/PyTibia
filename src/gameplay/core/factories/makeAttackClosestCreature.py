from typing import Tuple
from ..tasks.attackClosestCreature import AttackClosestCreatureTask


# TODO: add unit tests
def makeAttackClosestCreatureTask() -> Tuple[str, AttackClosestCreatureTask]:
    task = AttackClosestCreatureTask()
    return ('attackClosestCreature', task)