import numpy as np
from time import time
from ..factories.makeRefillCheckerTask import makeRefillCheckerTask
from ..typings import taskType
from .base.vector import VectorTask


class RefillCheckerWaypointTask(VectorTask):
    def __init__(self, waypoint):
        super().__init__()
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefillChecker'
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
