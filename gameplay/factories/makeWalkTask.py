from gameplay.tasks.walk import WalkTask


def makeWalkTask(context, waypoint):
    task = WalkTask(context, waypoint)
    return ('walk', task)