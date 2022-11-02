from time import time
import chat.core


class SayTask:
    def __init__(self, phrase):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'say'
        self.status = 'notStarted'
        self.value = phrase

    def shouldIgnore(self, context):
        return True

    def do(self, context):
        chat.core.sendMessage(context['screenshot'], self.value)
        return context

    def did(self, context):
        # TODO: check if phrase is spelled in the chat
        return True

    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        return context
