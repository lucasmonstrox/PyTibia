
from gameplay.tasks.walk import WalkTask


def makeWalkTask(waypoint):
    task = WalkTask(waypoint)
    return ('walk', task)