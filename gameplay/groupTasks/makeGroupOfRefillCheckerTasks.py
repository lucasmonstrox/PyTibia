import numpy as np
from gameplay.factories.makeRefillCheckerTask import makeRefillCheckerTask
from gameplay.typings import taskType


def makeGroupOfRefillCheckerTasks(waypoint):
    tasks = np.array([], dtype=taskType)
    tasksToAppend = np.array([
        makeRefillCheckerTask(waypoint),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks