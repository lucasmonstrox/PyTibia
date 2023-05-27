from src.shared.typings import Waypoint
from ..factories.makeUseRope import makeUseRopeTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from .common.vector import VectorTask


class UseRopeWaypointTask(VectorTask):
    def __init__(self, _, waypoint: Waypoint):
        super().__init__()
        self.name = 'useRopeWaypoint'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, waypoint: Waypoint):
        return [
            makeUseRopeTask(waypoint),
            makeSetNextWaypointTask(),
        ]
