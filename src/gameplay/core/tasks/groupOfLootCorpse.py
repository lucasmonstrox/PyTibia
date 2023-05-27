from src.repositories.gameWindow.typings import Creature
from ..factories.makeLootCorpse import makeLootCorpseTask
from .common.vector import VectorTask


class GroupOfLootCorpseTasks(VectorTask):
    def __init__(self, corpse: Creature):
        super().__init__()
        self.name = 'groupOfLootCorpse'
        self.tasks = self.generateTasks(corpse)
        self.value = corpse

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, corpse: Creature):
        return [
            # TODO: add walkToCoordinate to reach dead corpse
            makeLootCorpseTask(corpse)
        ]
