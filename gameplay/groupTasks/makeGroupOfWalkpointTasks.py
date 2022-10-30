import numpy as np
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.typings import taskType
from gameplay.waypoint import generateFloorWalkpoints


def makeGroupOfWalkpointTasks(context, waypointRadarCoordinate):
    walkpoints = generateFloorWalkpoints(context['radarCoordinate'], waypointRadarCoordinate)
    tasks = np.array([], dtype=taskType)
    for walkpoint in walkpoints:
        walkpointTask = makeWalkTask(walkpoint)
        taskToAppend = np.array([walkpointTask], dtype=taskType)
        tasks = np.append(tasks, [taskToAppend])
    return tasks
