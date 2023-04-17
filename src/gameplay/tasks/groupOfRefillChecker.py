import numpy as np
from ..factories.makeRefillChecker import makeRefillCheckerTask
from ..typings import taskType
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfRefillCheckerTasks(GroupTaskExecutor):
    def __init__(self, waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefillChecker'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        return np.array([makeRefillCheckerTask(waypoint)], dtype=taskType)
