from src.repositories.gameWindow.typings import Creature
from ...typings import Context
from .common.vector import VectorTask
from .collectDeadCorpse import CollectDeadCorpseTask


class LootCorpseTask(VectorTask):
    def __init__(self, creature: Creature):
        super().__init__()
        self.name = 'lootCorpse'
        self.isRootTask = True
        self.creature = creature

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            # TODO: add walkToCoordinate to reach dead creature
            CollectDeadCorpseTask(self.creature).setParentTask(self).setRootTask(self)
        ]
        return context