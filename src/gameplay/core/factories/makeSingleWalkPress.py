from ..tasks.singleWalkPress import SingleWalkPressTask


def makeSingleWalkPress(context, waypoint):
    task = SingleWalkPressTask(context, waypoint)
    return ('singleWalkPress', task)