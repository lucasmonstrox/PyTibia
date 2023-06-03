from src.shared.typings import Waypoint
from .common.vector import VectorTask
from .useRope import UseRopeTask
from .setNextWaypoint import SetNextWaypointTask


class UseRopeWaypointTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useRopeWaypoint'
        self.isRootTask = True
        self.waypoint = waypoint

    # TODO: add unit tests
    # TODO: add typings
    def onBeforeStart(self, _):
        self.tasks = [
            UseRopeTask(self.waypoint).setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
