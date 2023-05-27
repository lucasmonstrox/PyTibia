from src.shared.typings import Waypoint
from ..factories.makeClickInCoordinate import makeClickInCoordinateTask
from ..factories.makeSetNextWaypoint import makeSetNextWaypointTask
from ..factories.makeUseShovel import makeUseShovelTask
from .common.vector import VectorTask


class UseShovelWaypointTask(VectorTask):
    def __init__(self, _, waypoint: Waypoint):
        super().__init__()
        self.name = 'useShovelWaypoint'
        self.tasks = self.generateTasks(waypoint)
        self.value = waypoint

    def generateTasks(self, waypoint):
        return [
            makeUseShovelTask(waypoint),
            makeClickInCoordinateTask(waypoint),
            makeSetNextWaypointTask(),
        ]
