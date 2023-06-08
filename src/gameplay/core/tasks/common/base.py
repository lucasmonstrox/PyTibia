from time import time
from ....typings import Context


class BaseTask:
    def __init__(self, delayBeforeStart=0, delayAfterComplete=0, delayOfTimeout=0, isRootTask=False, manuallyTerminable=False, name='baseTask', parentTask=None):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.terminable = True
        self.delayBeforeStart = delayBeforeStart
        self.delayAfterComplete = delayAfterComplete
        self.delayOfTimeout = delayOfTimeout
        self.isRetrying = False
        self.isRootTask = isRootTask
        self.manuallyTerminable = manuallyTerminable
        self.name = name
        self.parentTask = parentTask
        self.retryCount = 0
        self.rootTask = None
        self.status = 'notStarted'
        self.statusReason = None

    def setParentTask(self, parentTask):
        self.parentTask = parentTask
        return self

    def setRootTask(self, rootTask):
        self.rootTask = rootTask
        return self

    # TODO: add unit tests
    def shouldIgnore(self, _: Context) -> bool:
        return False

    def shouldManuallyComplete(self, _: Context) -> bool:
        return False

    # TODO: add unit tests
    def shouldRestart(self, _: Context) -> bool:
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
    def onBeforeStart(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onBeforeRestart(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onIgnored(self, context: Context) -> Context:
        return context
    
    # TODO: add unit tests
    def onInterrupt(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onComplete(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onInterrupt(self, context: Context) -> Context:
        return context

    # TODO: add unit tests
    def onTimeout(self, context: Context) -> Context:
        return context
