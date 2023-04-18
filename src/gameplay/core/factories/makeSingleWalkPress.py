from ..tasks.singleWalkPress import SingleWalkPressTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeSingleWalkPress(context, waypoint):
    task = SingleWalkPressTask(context, waypoint)
    return ('singleWalkPress', task)