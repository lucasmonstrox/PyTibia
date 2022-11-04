import numpy as np
from time import time
from gameplay.factories.makeClickInCoordinateTask import makeClickInCoordinateTask
from gameplay.factories.makeSetNextWaypointTask import makeSetNextWaypointTask
from gameplay.factories.makeUseShovelTask import makeUseShovelTask
from gameplay.groupTasks.groupTaskExecutor import GroupTaskExecutor
from gameplay.typings import taskType


class GroupOfUseShovelTasks(GroupTaskExecutor):
    def __init__(self, _, waypoint):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.name = 'groupOfUseShovel'
        self.status = 'notStarted'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        tasks = np.array([], dtype=taskType)
        tasksToAppend = np.array([
            makeUseShovelTask(waypoint),
            makeClickInCoordinateTask(waypoint),
            makeSetNextWaypointTask(waypoint),
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
