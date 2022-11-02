import numpy as np
from gameplay.factories.makeClickInCoordinateTask import makeClickInCoordinateTask
from gameplay.factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from gameplay.factories.makeUseShovelTask import makeUseShovelTask
from gameplay.typings import taskType


def makeGroupOfUseShovelTasks(_, __, waypoint):
    tasks = np.array([], dtype=taskType)
    tasksToAppend = np.array([
        makeUseShovelTask(waypoint),
        makeClickInCoordinateTask(waypoint),
        makeSetNextWaypointTask(waypoint),
    ], dtype=taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks
