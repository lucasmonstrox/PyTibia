from src.repositories.inventory.core import images
from ...typings import Context
from .common.vector import VectorTask
from .dropEachFlask import DropEachFlaskTask
from .expandBackpack import ExpandBackpackTask
from .openBackpack import OpenBackpackTask
from .setNextWaypoint import SetNextWaypointTask


class DropFlasksTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'dropFlasks'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.isRootTask = True

    # TODO: add unit tests
    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            OpenBackpackTask(context['backpacks']['main']).setParentTask(self).setRootTask(self),
            ExpandBackpackTask(images['containersBars'][context['backpacks']['main']]).setParentTask(self).setRootTask(self),
            DropEachFlaskTask(context['backpacks']['main']).setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
