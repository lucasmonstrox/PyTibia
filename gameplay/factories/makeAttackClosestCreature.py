from gameplay.tasks.attackClosestCreature import AttackClosestCreatureTask


def makeAttackClosestCreatureTask(closestCreature):
    task = AttackClosestCreatureTask(closestCreature)
    return ('attackClosestCreature', task)