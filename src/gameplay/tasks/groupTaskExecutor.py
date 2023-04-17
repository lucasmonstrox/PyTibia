from time import time
from .baseTask import BaseTask


class GroupTaskExecutor(BaseTask):
    def __init__(self):
        super().__init__()
        self.currentTaskIndex = 0
        self.tasks = []

    def do(self, context):
        if self.status == 'completed':
            return context
        alreadyPing = False
        hasTasks = len(self.tasks) > 0
        if hasTasks:
            self.status = 'running'
            _, task = self.tasks[self.currentTaskIndex]
            if task.status == 'notStarted':
                if self.tasks[self.currentTaskIndex][1].startedAt == None:
                    self.tasks[self.currentTaskIndex][1].startedAt = time()
                passedTimeSinceLastCheck = time() - self.tasks[self.currentTaskIndex][1].startedAt
                shouldExecNow = passedTimeSinceLastCheck >= self.tasks[self.currentTaskIndex][1].delayBeforeStart
                if shouldExecNow:
                    shouldExecResponse = self.tasks[self.currentTaskIndex][1].shouldIgnore(context) == False
                    shouldNotExecTask = shouldExecResponse == False and self.tasks[self.currentTaskIndex][1].status != 'running'
                    if shouldNotExecTask:
                        context = self.tasks[self.currentTaskIndex][1].onIgnored(context)
                        self.markCurrentTaskAsCompleted(context)
                    else:
                        self.tasks[self.currentTaskIndex][1].status = 'running'
                        context = self.tasks[self.currentTaskIndex][1].do(context)
                        context = self.ping(context)
                        alreadyPing = True
            elif self.tasks[self.currentTaskIndex][1].status == 'running':
                if not task.terminable:
                    context = task.ping(context)
                    return task.do(context)
                if self.tasks[self.currentTaskIndex][1].shouldRestart(context):
                    self.tasks[self.currentTaskIndex][1].status = 'notStarted'
                else:
                    hasDelayOfTimeout = self.tasks[self.currentTaskIndex][1].delayOfTimeout is not None
                    if hasDelayOfTimeout:
                        passedTimeSinceLastCheck = time() - self.tasks[self.currentTaskIndex][1].startedAt
                        didTimeout = passedTimeSinceLastCheck >= self.tasks[self.currentTaskIndex][1].delayOfTimeout
                        if didTimeout:
                            context = self.tasks[self.currentTaskIndex][1].onDidTimeout(context)
                            self.markCurrentTaskAsCompleted(context)
                            return context
                    didTask = self.tasks[self.currentTaskIndex][1].did(context)
                    if didTask:
                        self.tasks[self.currentTaskIndex][1].finishedAt = time()
                        self.tasks[self.currentTaskIndex][1].status = 'almostComplete'
                    else:
                        context = self.tasks[self.currentTaskIndex][1].ping(context)
                        context = self.ping(context)
                        alreadyPing = True
            if len(self.tasks) == 0:
                if alreadyPing == False:
                    context = self.ping(context)
                return context
            if self.tasks[self.currentTaskIndex][1].status == 'almostComplete':
                passedTimeSinceTaskCompleted = time() - self.tasks[self.currentTaskIndex][1].finishedAt
                didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > self.tasks[self.currentTaskIndex][1].delayAfterComplete
                if didPassedEnoughDelayAfterTaskComplete:
                    context = self.tasks[self.currentTaskIndex][1].onDidComplete(context)
                    self.markCurrentTaskAsCompleted(context)
        else:
            context = self.ping(context)
        return context

    def markCurrentTaskAsCompleted(self, context):
        self.tasks[self.currentTaskIndex][1].status = 'completed'
        isntLastTask = self.currentTaskIndex < len(self.tasks) - 1
        if isntLastTask:
            self.currentTaskIndex += 1
        else:
            if self.terminable:
                self.status = 'completed'
                self.onDidComplete(context)
    