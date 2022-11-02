import numpy as np
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.typings import taskType


def makeWalkpointsBetweenTwoCoordinatesTasks(checkInCoordinate):
    tasks = np.array([], dtype=taskType)
    walkpointTask = makeWalkTask(checkInCoordinate)
    taskToAppend = np.array([walkpointTask], dtype=taskType)
    tasks = np.append(tasks, [taskToAppend])
    return tasks
