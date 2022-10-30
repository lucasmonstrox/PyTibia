import numpy as np
from gameplay.factories.makeAttackClosestCreature import makeAttackClosestCreatureTask
from gameplay.groupTasks.makeGroupOfWalkpointTasks import makeGroupOfWalkpointTasks
from gameplay.typings import taskType


def makeAttackClosestCreatureTasks(context, closestCreature):
    tasksArray = np.array([], dtype=taskType)
    tasksToAppend = np.array([
        makeAttackClosestCreatureTask(closestCreature),
    ], dtype=taskType)
    tasksArray = np.append(tasksArray, [tasksToAppend])
    floorTasks = makeGroupOfWalkpointTasks(
        context, closestCreature['radarCoordinate'])
    for floorTask in floorTasks:
        taskToAppend = np.array([floorTask], dtype=taskType)
        tasksArray = np.append(tasksArray, [taskToAppend])
    return tasksArray
