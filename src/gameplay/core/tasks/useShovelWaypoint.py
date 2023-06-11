from src.shared.typings import Waypoint
from ...typings import Context
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

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            UseShovelTask(self.waypoint).setParentTask(self).setRootTask(self),
            ClickInCoordinateTask(self.waypoint).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
