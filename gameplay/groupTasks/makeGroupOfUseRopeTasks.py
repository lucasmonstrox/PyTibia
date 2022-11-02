import numpy as np
from gameplay.typings import taskType
from gameplay.factories.makeUseRopeTask import makeUseRopeTask


def makeGroupOfUseRopeTasks(_, __, waypoint):
    tasks = np.array([], dtype=taskType)
    tasksToAppend = np.array([
        makeUseRopeTask(waypoint),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks