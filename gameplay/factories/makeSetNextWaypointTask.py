from gameplay.tasks.setNextWaypoint import SetNextWaypointTask


def makeSetNextWaypointTask():
    task = SetNextWaypointTask()
    return ('setNextWaypoint', task)