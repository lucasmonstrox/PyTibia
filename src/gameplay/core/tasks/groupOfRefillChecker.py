import numpy as np
from ..factories.makeRefillChecker import makeRefillCheckerTask
from ..typings import Task
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfRefillCheckerTasks(GroupTaskExecutor):
    def __init__(self, waypoint):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'groupOfRefillChecker'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def generateTasks(self, waypoint):
        return np.array([makeRefillCheckerTask(waypoint)], dtype=Task)
