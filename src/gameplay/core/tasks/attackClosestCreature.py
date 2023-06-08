from ...typings import Context
from .common.vector import VectorTask
from .clickInClosestCreature import ClickInClosestCreatureTask
from .walkToTargetCreature import WalkToTargetCreature


class AttackClosestCreatureTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'attackClosestCreature'
        self.isRootTask = True

    # TODO: add unit tests
    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            # TODO: task should have like 5 retries until all tree is destroyed
            ClickInClosestCreatureTask().setParentTask(self).setRootTask(self),
            WalkToTargetCreature().setParentTask(self).setRootTask(self),
        ]
        return context
