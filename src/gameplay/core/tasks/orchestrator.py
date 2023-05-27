from time import time
from ...typings import Context
from .common.base import BaseTask
from .common.vector import VectorTask


class TasksOrchestrator:
    def __init__(self):
        super().__init__()
        self.currentTaskPath = [0]
        self.tasksOrTask = None

    def reset(self):
        self.currentTaskPath = [0]
        self.tasksOrTask = None

    def setTasksOrTask(self, tasksOrTask):
        self.tasksOrTask = tasksOrTask

    def getCurrentTask(self):
        if self.tasksOrTask is None:
            return None
        if isinstance(self.tasksOrTask, BaseTask):
            return self.tasksOrTask
        return self.tasksOrTask[tuple(self.currentTaskPath)]

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        # verificar se há tasks
        if self.tasksOrTask is None:
            return context
        # obter a task atual
        currentTask = self.getCurrentTask()
        return context
        alreadyPing = False
        if len(self.tasks) > 0:
            self.status = 'running'
            if self.tasks[self.currentTaskIndex].status == 'notStarted':
                if self.tasks[self.currentTaskIndex].startedAt is None:
                    self.tasks[self.currentTaskIndex].startedAt = time()
                passedTimeSinceLastCheck = time() - self.tasks[self.currentTaskIndex].startedAt
                shouldExecNow = passedTimeSinceLastCheck >= self.tasks[self.currentTaskIndex].delayBeforeStart
                if shouldExecNow:
                    shouldExecResponse = self.tasks[self.currentTaskIndex].shouldIgnore(context) == False
                    shouldNotExecTask = shouldExecResponse == False and self.tasks[self.currentTaskIndex].status != 'running'
                    if shouldNotExecTask:
                        context = self.tasks[self.currentTaskIndex].onIgnored(context)
                        self.markCurrentTaskAsCompleted(context)
                    else:
                        self.tasks[self.currentTaskIndex].status = 'running'
                        context = self.tasks[self.currentTaskIndex].do(context)
                        context = self.ping(context)
                        alreadyPing = True
            elif self.tasks[self.currentTaskIndex].status == 'running':
                if not self.tasks[self.currentTaskIndex].terminable:
                    context = self.tasks[self.currentTaskIndex].ping(context)
                    return self.tasks[self.currentTaskIndex].do(context)
                if self.tasks[self.currentTaskIndex].shouldRestart(context):
                    self.tasks[self.currentTaskIndex].status = 'notStarted'
                else:
                    hasDelayOfTimeout = self.tasks[self.currentTaskIndex].delayOfTimeout is not None
                    if hasDelayOfTimeout:
                        passedTimeSinceLastCheck = time() - self.tasks[self.currentTaskIndex].startedAt
                        didTimeout = passedTimeSinceLastCheck >= self.tasks[self.currentTaskIndex].delayOfTimeout
                        if didTimeout:
                            context = self.tasks[self.currentTaskIndex].onDidTimeout(context)
                            self.markCurrentTaskAsCompleted(context)
                            return context
                    didTask = self.tasks[self.currentTaskIndex].did(context)
                    if didTask:
                        self.tasks[self.currentTaskIndex].finishedAt = time()
                        self.tasks[self.currentTaskIndex].status = 'almostComplete'
                    else:
                        context = self.tasks[self.currentTaskIndex].ping(context)
                        context = self.ping(context)
                        alreadyPing = True
            if len(self.tasks) == 0:
                if alreadyPing == False:
                    context = self.ping(context)
                return context
            if self.tasks[self.currentTaskIndex].status == 'almostComplete':
                passedTimeSinceTaskCompleted = time() - self.tasks[self.currentTaskIndex].finishedAt
                didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > self.tasks[self.currentTaskIndex].delayAfterComplete
                if didPassedEnoughDelayAfterTaskComplete:
                    context = self.tasks[self.currentTaskIndex].onDidComplete(context)
                    self.markCurrentTaskAsCompleted(context)
        else:
            context = self.ping(context)
        return context

    # TODO: add unit tests
    def markCurrentTaskAsCompleted(self, context: Context):
        self.tasks[self.currentTaskIndex].status = 'completed'
        if self.currentTaskIndex < len(self.tasks) - 1:
            self.currentTaskIndex += 1
        else:
            if self.terminable:
                self.status = 'completed'
                self.onDidComplete(context)
