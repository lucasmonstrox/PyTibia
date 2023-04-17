from ..tasks.useRope import UseRopeTask


def makeUseRopeTask(waypoint):
    task = UseRopeTask(waypoint)
    return ('useRope', task)
