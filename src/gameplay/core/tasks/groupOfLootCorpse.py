import numpy as np
from src.repositories.gameWindow.typings import Creature
from ...typings import Context
from ..factories.makeLootCorpse import makeLootCorpseTask
from ..typings import Task
from .groupTask import GroupTask


class GroupOfLootCorpseTasks(GroupTask):
    def __init__(self, context: Context, corpse: Creature):
        super().__init__()
        self.name = 'groupOfLootCorpse'
        self.tasks = self.generateTasks(corpse)
        self.value = corpse

    # TODO: add unit tests
    # TODO: add typings
    def generateTasks(self, corpse: Creature):
        return np.array([
            makeLootCorpseTask(corpse)
        ], dtype=Task)
