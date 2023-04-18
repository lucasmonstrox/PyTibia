from ..tasks.walk import WalkTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeWalkTask(context, waypoint):
    task = WalkTask(context, waypoint)
    return ('walk', task)