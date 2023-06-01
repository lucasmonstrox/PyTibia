from time import time
from ....typings import Context


class BaseTask:
    def __init__(self, parentTask=None):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.terminable = True
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.delayOfTimeout = None
        self.parentTask = parentTask
        self.status = 'notStarted'
        self.value = None

    def setParentTask(self, parentTask):
        self.parentTask = parentTask
        return self

    def initialize(self, context):
        return self

    # TODO: add unit tests
    def shouldIgnore(self, _: Context) -> bool:
        return False

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def ping(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def did(self, _: Context) -> bool:
        return True

    # TODO: add unit tests
    def shouldRestart(self, _: Context) -> bool:
        return False

    # TODO: add unit tests
    def onIgnored(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onComplete(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onTimeout(self, context: Context) -> Context:
        return context
