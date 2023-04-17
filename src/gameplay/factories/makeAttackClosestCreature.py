from ..tasks.attackClosestCreature import AttackClosestCreatureTask


def makeAttackClosestCreatureTask():
    task = AttackClosestCreatureTask()
    return ('attackClosestCreature', task)