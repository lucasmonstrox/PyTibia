from src.shared.typings import Waypoint
from .common.vector import VectorTask
from .clickInCoordinate import ClickInCoordinateTask
from .setNextWaypoint import SetNextWaypointTask
from .useShovel import UseShovelTask


class UseShovelWaypointTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useShovelWaypoint'
        self.isRootTask = True
        self.waypoint = waypoint

    # TODO: add parameters type
    def initialize(self, _):
        self.tasks = [
            UseShovelTask(self.waypoint).setParentTask(self),
            ClickInCoordinateTask(self.waypoint).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
