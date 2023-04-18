from ..tasks.attackClosestCreature import AttackClosestCreatureTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeAttackClosestCreatureTask():
    task = AttackClosestCreatureTask()
    return ('attackClosestCreature', task)