from .baseTask import BaseTask


class DecisionTask(BaseTask):
    def __init__(self, leftTask, rightTask):
        super().__init__()
        self.leftTask = leftTask
        self.rightTask = rightTask

    def exec(self, context):
        return context
