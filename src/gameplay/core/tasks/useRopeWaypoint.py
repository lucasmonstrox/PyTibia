from src.shared.typings import Waypoint
from ...typings import Context
from .common.vector import VectorTask
from .useRope import UseRopeTask
from .setNextWaypoint import SetNextWaypointTask


class UseRopeWaypointTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useRopeWaypoint'
        self.isRootTask = True
        self.waypoint = waypoint

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            UseRopeTask(self.waypoint).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
