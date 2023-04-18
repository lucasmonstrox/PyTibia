from time import time


class BaseTask:
    def __init__(self):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.terminable = True
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.delayOfTimeout = None
        self.status = 'notStarted'
        self.value = None

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def shouldIgnore(self, _):
        return False

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        return context

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def ping(self, context):
        return context

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def did(self, _):
        return True

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def shouldRestart(self, _):
        return False

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def onIgnored(self, context):
        return context

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def onDidComplete(self, context):
        return context

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def onDidTimeout(self, context):
        return context
