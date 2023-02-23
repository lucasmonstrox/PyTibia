from time import time
from .baseTask import BaseTask


class DecisionTask(BaseTask):
    def __init__(self, leftTask, rightTask):
        super().__init__()
        self.currentTask = leftTask
        self.leftTask = leftTask
        self.rightTask = rightTask
        self.result = False
    
    def exec(self, context):
        if self.status == 'finished':
            return context
        if self.currentTask.status == 'notStarted':
            if self.currentTask.startedAt == None:
                self.currentTask.startedAt = time()
            passedTimeSinceLastCheck = time() - self.currentTask.startedAt
            shouldExecNow = passedTimeSinceLastCheck >= self.currentTask.delayBeforeStart
            if shouldExecNow:
                shouldExecResponse = self.currentTask.shouldIgnore(context) == False
                shouldNotExecTask = shouldExecResponse == False and self.currentTask.status != 'running'
                if shouldNotExecTask:
                    context = self.currentTask.onIgnored(context)
                else:
                    self.currentTask.status = 'running'
                    context = self.currentTask.exec(context)
        elif self.currentTask.status == 'running':
            if self.currentTask.shouldRestart(context):
                self.currentTask.status = 'notStarted'
            else:
                hasDelayOfTimeout = self.currentTask.delayOfTimeout is not None
                if hasDelayOfTimeout:
                    passedTimeSinceLastCheck = time() - self.currentTask.startedAt
                    didTimeout = passedTimeSinceLastCheck >= self.currentTask.delayOfTimeout
                    if didTimeout:
                        # TODO: o que fazer quando há timeout? Qual o resultado?
                        context = self.currentTask.onDidTimeout(context)
                        return context
                if self.currentTask.did(context):
                    self.currentTask.finishedAt = time()
                    self.currentTask.status = 'almostComplete'
                    self.result = True
        if self.currentTask.status == 'almostComplete':
            passedTimeSinceTaskCompleted = time() - self.currentTask.finishedAt
            didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > self.currentTask.delayAfterComplete
            if didPassedEnoughDelayAfterTaskComplete:
                context = self.currentTask.onDidComplete(context)
                if self.currentTask == self.leftTask:
                    self.onLeftTaskFinished()
                elif self.currentTask == self.rightTask:
                    self.onRightTaskFinished()
        return context

    def onLeftTaskFinished(self):
        self.leftTask.status = 'finished'
        if self.result:
            self.currentTask = self.rightTask
            return
        self.status = 'finished'

    def onRightTaskFinished(self):
        self.rightTask.status = 'finished'
        self.status = 'finished'