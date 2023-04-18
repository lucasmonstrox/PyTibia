from ..tasks.setNextWaypoint import SetNextWaypointTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeSetNextWaypointTask():
    task = SetNextWaypointTask()
    return ('setNextWaypoint', task)