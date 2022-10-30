from gameplay.tasks.setNextWaypoint import SetNextWaypointTask


def makeSetNextWaypointTask(waypoint):
    task = SetNextWaypointTask(waypoint)
    return ('setNextWaypoint', task)