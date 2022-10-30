import numpy as np
import gameplay.baseTasks
from gameplay.factories.makeClickInCoordinateTask import makeClickInCoordinateTask
from gameplay.factories.makeUseShovelTask import makeUseShovelTask


def makeUseShovelTasks(context, goalCoordinate, waypoint):
    tasks = np.array([], dtype=gameplay.baseTasks.taskType)
    floorTasks = gameplay.baseTasks.makeWalkpointTasks(context, goalCoordinate)
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=gameplay.baseTasks.taskType)
        tasks = np.append(tasks, [taskToAppend])
    tasksToAppend = np.array([
        makeUseShovelTask(waypoint),
        makeClickInCoordinateTask(waypoint),
    ], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [tasksToAppend])
    return tasks
