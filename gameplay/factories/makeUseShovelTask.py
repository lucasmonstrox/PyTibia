
from gameplay.tasks.useShovel import UseShovelTask


def makeUseShovelTask(waypoint):
    task = UseShovelTask(waypoint)
    return ('useShovel', task)