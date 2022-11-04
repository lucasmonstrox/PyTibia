from gameplay.tasks.useHole import UseHoleTask


def makeUseHoleTask(waypoint):
    task = UseHoleTask(waypoint)
    return ('useHole', task)
