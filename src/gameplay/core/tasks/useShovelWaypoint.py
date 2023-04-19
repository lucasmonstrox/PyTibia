import numpy as np
from src.shared.typings import Waypoint
from ..factories.makeClickInCoordinate import makeClickInCoordinateTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..factories.makeUseShovel import makeUseShovelTask
from ..typings import Task
from .groupTaskExecutor import GroupTask


class UseShovelWaypointTask(GroupTask):
    def __init__(self, _, waypoint: Waypoint):
        super().__init__()
        self.name = 'useShovelWaypoint'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        return np.array([
            makeUseShovelTask(waypoint),
            makeClickInCoordinateTask(waypoint),
            makeSetNextWaypointTask(),
        ], dtype=Task)
