from ..tasks.useHole import UseHoleTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeUseHoleTask(waypoint):
    task = UseHoleTask(waypoint)
    return ('useHole', task)
