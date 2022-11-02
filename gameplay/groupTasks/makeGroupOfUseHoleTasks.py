import numpy as np
from gameplay.factories.makeClickInCoordinateTask import makeClickInCoordinateTask
from gameplay.factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from gameplay.factories.makeUseHoleTask import makeUseHoleTask
from gameplay.typings import taskType


def makeGroupOfUseHoleTasks(_, __, waypoint):
    tasks = np.array([], dtype=taskType)
    tasksToAppend = np.array([
        makeUseHoleTask(waypoint),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks
