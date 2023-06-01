from .base import BaseTask


class VectorTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.currentTaskIndex = 0
        self.initialized = False
        self.tasks = []
