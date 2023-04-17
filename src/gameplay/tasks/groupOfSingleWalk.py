import numpy as np
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..factories.makeWalk import makeWalkTask
from ..typings import taskType
from .groupTaskExecutor import GroupTaskExecutor


class GroupOfSingleWalkTasks(GroupTaskExecutor):
    def __init__(self, context, checkInCoordinate):
        super().__init__()
        self.delayAfterComplete = 2
        self.name = 'groupOfSingleWalk'
        self.tasks = self.generateTasks(context, checkInCoordinate)
        self.value = checkInCoordinate

    def generateTasks(self, context, checkInCoordinate):
        return np.array([
            makeWalkTask(context, checkInCoordinate),
            makeSetNextWaypointTask(),
        ], dtype=taskType)
