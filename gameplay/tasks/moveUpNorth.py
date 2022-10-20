import numpy as np
import gameplay.baseTasks


def makeMoveUpNorthTasks(context, goalCoordinate, waypointRadarCoordinate):
    tasks = gameplay.baseTasks.makeWalkpointTasks(
        context, context['waypoints']['state']['goalCoordinate'])
    walkpointTask = gameplay.baseTasks.makeWalkpointTask(
        context['waypoints']['state']['checkInCoordinate'])
    taskToAppend = np.array([walkpointTask], dtype=gameplay.baseTasks.taskType)
    tasks = np.append(tasks, [taskToAppend])
    return tasks
