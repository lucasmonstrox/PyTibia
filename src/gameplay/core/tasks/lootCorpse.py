from src.repositories.gameWindow.typings import Creature
from .common.vector import VectorTask
from .collectDeadCorpse import CollectDeadCorpseTask


class LootCorpseTask(VectorTask):
    def __init__(self, corpse: Creature):
        super().__init__()
        self.name = 'lootCorpse'
        self.isRootTask = True
        self.corpse = corpse

    # TODO: add unit tests
    # TODO: add typings
    def onBeforeStart(self, _):
        self.tasks = [
            # TODO: add walkToCoordinate to reach dead corpse
            CollectDeadCorpseTask(self.corpse).setParentTask(self)
        ]
        self.initialized = True
        return self
