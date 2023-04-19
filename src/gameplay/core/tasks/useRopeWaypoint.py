import numpy as np
from src.shared.typings import Waypoint
from ..factories.makeUseRope import makeUseRopeTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..typings import Task
from .groupTask import GroupTask


class UseRopeWaypointTask(GroupTask):
    def __init__(self, _, waypoint: Waypoint):
        super().__init__()
        self.name = 'useRopeWaypoint'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, waypoint: Waypoint):
        return np.array([
            makeUseRopeTask(waypoint),
            makeSetNextWaypointTask(),
        ], dtype=Task)
