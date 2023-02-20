from time import time


class BaseTask:
    def __init__(self):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0
        self.delayAfterComplete = 0
        self.delayOfTimeout = None
        self.status = 'notStarted'
        self.value = None

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        return context
    
    def ping(self, context):
        return context

    def did(self, _):
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
