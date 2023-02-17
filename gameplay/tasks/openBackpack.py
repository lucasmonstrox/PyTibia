from time import time
from inventory.core import isBackpackOpen, openBackpack


class OpenBackpackTask:
    def __init__(self, backpack):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.delayOfTimeout = None
        self.name = 'openBackpack'
        self.status = 'notStarted'
        self.value = backpack

    def shouldIgnore(self, context):
        shouldIgnore = isBackpackOpen(context['screenshot'], self.value)
        return shouldIgnore

    def do(self, context):
        openBackpack(context['screenshot'], self.value)
        return context
    
    def ping(self, context):
        return context

    def did(self, context):
        did = isBackpackOpen(context['screenshot'], self.value)
        return did
    
    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
