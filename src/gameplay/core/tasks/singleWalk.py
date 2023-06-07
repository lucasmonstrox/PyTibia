from ...typings import Context
from .common.vector import VectorTask
from .moveDown import MoveDown
from .moveUp import MoveUp
from .setNextWaypoint import SetNextWaypointTask


class SingleWalkTask(VectorTask):
    # TODO: add types
    def __init__(self, waypointType: str, direction: str):
        super().__init__()
        self.name = 'singleWalk'
        self.delayAfterComplete = 2
        self.isRootTask = True
        self.direction = direction
        self.waypointType = waypointType

    # TODO: add unit tests
    def onBeforeStart(self, context: Context) -> Context:
        moveDownOrUp = MoveDown(context, self.direction) if self.waypointType == 'moveDown' else MoveUp(context, self.direction)
        self.tasks = [
            moveDownOrUp.setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
