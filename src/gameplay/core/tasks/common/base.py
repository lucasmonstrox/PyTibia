from time import time
from ....typings import Context


class BaseTask:
    def __init__(self, delayBeforeStart=0, delayAfterComplete=0, delayOfTimeout=0, isRootTask=False, manuallyTerminable=False, name='baseTask', parentTask=None, shouldTimeoutTreeWhenTimeout=False):
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
        self.shouldTimeoutTreeWhenTimeout = shouldTimeoutTreeWhenTimeout
        self.status = 'notStarted'
        self.statusReason = None

    def setParentTask(self, parentTask):
        self.parentTask = parentTask
        return self

    def setRootTask(self, rootTask):
        self.rootTask = rootTask
        return self

    def shouldIgnore(self, _: Context) -> bool:
        return False

    def shouldManuallyComplete(self, _: Context) -> bool:
        return False

    def shouldRestart(self, _: Context) -> bool:
        return False

    def do(self, context: Context) -> Context:
        return context

    def did(self, _: Context) -> bool:
        return True

    def ping(self, context: Context) -> Context:
        return context

    def onBeforeStart(self, context: Context) -> Context:
        return context

    def onBeforeRestart(self, context: Context) -> Context:
        return context

    def onIgnored(self, context: Context) -> Context:
        return context

    def onInterrupt(self, context: Context) -> Context:
        return context

    def onComplete(self, context: Context) -> Context:
        return context

    def onTimeout(self, context: Context) -> Context:
        return context
