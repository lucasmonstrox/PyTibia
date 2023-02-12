import numpy as np
from time import time
from gameplay.factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from gameplay.factories.makeWalkTask import makeWalkTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType


class GroupOfSingleWalkTasks(GroupTaskExecutor):
    def __init__(self, context, checkInCoordinate):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 2
        self.name = 'groupOfSingleWalk'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(context, checkInCoordinate)
        self.value = checkInCoordinate

    def generateTasks(self, context, checkInCoordinate):
        tasks = np.array([], dtype=taskType)
        walkpointTask = makeWalkTask(context, checkInCoordinate)
        taskToAppend = np.array([walkpointTask], dtype=taskType)
        tasks = np.append(tasks, [taskToAppend])
        tasksToAppend = np.array([
            makeSetNextWaypointTask(),
        ], dtype=taskType)
        tasks = np.append(tasks, [tasksToAppend])
        return tasks

    def shouldIgnore(self, _):
        return False

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
