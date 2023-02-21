import numpy as np
from time import time
from ..factories.makeUseRopeTask import makeUseRopeTask
from ..factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from ..typings import taskType
from .groupTaskExecutor import GroupTaskExecutor


class UseRopeWaypointTask(GroupTaskExecutor):
    def __init__(self, _, waypoint):
        super().__init__()
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'groupOfUseRope'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        tasks = np.array([], dtype=taskType)
        tasksToAppend = np.array([
            makeUseRopeTask(waypoint),
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
