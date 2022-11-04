from time import time
from chat.core import enableChatOff


class SetChatOffTask:
    def __init__(self):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'setChatOff'
        self.status = 'notStarted'
        self.value = None

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        enableChatOff(context['screenshot'])
        return context

    def did(self, _):
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context
