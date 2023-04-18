import numpy as np
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..factories.makeWalk import makeWalkTask
from ..typings import Task
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfSingleWalkTasks(GroupTaskExecutor):
    def __init__(self, context, checkInCoordinate):
        super().__init__()
        self.delayAfterComplete = 2
        self.name = 'groupOfSingleWalk'
        self.tasks = self.generateTasks(context, checkInCoordinate)
        self.value = checkInCoordinate

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def generateTasks(self, context, checkInCoordinate):
        return np.array([
            makeWalkTask(context, checkInCoordinate),
            makeSetNextWaypointTask(),
        ], dtype=Task)
