from ..tasks.useRope import UseRopeTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeUseRopeTask(waypoint):
    task = UseRopeTask(waypoint)
    return ('useRope', task)
