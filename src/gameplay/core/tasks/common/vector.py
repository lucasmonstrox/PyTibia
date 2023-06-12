from ....typings import Context
from .base import BaseTask


class VectorTask(BaseTask):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.currentTaskIndex = 0
        self.tasks = []

    def shouldRestartAfterAllChildrensComplete(self, _: Context) -> bool:
        return False
