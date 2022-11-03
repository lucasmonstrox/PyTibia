import numpy as np
from time import time
from gameplay.factories.makeRefillCheckerTask import makeRefillCheckerTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType


class GroupOfRefillCheckerTasks(GroupTaskExecutor):
    def __init__(self, waypoint):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefillChecker'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        tasks = np.array([], dtype=taskType)
        tasksToAppend = np.array([
            makeRefillCheckerTask(waypoint),
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
