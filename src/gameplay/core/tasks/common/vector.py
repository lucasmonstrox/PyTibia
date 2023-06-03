from .base import BaseTask


class VectorTask(BaseTask):
    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.currentTaskIndex = 0
        self.initialized = False
        self.tasks = []
