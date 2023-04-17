import numpy as np
from ..factories.makeUseRope import makeUseRopeTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..typings import taskType
from .groupTaskExecutor import GroupTaskExecutor


class UseRopeWaypointTask(GroupTaskExecutor):
    def __init__(self, _, waypoint):
        super().__init__()
        self.name = 'useRopeWaypoint'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        return np.array([
            makeUseRopeTask(waypoint),
            makeSetNextWaypointTask(),
        ], dtype=taskType)
