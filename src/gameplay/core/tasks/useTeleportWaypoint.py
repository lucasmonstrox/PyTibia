from src.shared.typings import Waypoint
from ...typings import Context
from .common.vector import VectorTask
from .rightClickInCoordinate import RightClickInCoordinateTask
from .setNextWaypoint import SetNextWaypointTask


class UseTeleportWaypointTask(VectorTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useTeleportWaypoint'
        self.isRootTask = True
        self.waypoint = waypoint

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            RightClickInCoordinateTask(self.waypoint).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
