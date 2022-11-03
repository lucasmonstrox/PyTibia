import numpy as np
from gameplay.factories.makeDepositItemsTask import makeDepositItemsTask
from gameplay.typings import taskType


def makeGroupOfDepositItemsTasks(waypoint):
    tasks = np.array([], dtype=taskType)
    tasksToAppend = np.array([
        makeDepositItemsTask(waypoint),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks
