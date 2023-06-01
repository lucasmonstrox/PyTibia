from time import time
from ...typings import Context


class TasksOrchestrator:
    def __init__(self, rootTask=None):
        super().__init__()
        self.rootTask = rootTask

    def setRootTask(self, rootTask):
        self.rootTask = rootTask
    
    def reset(self):
        self.rootTask = None

    def getCurrentTask(self, context: Context):
        return self.getNestedTask(self.rootTask, context)

    def getNestedTask(self, task, context: Context):
        if hasattr(task, 'tasks'):
            if task.status == 'notStarted':
                task.initialize(context)
                task.status = 'running'
            if task.status != 'completed':
                return self.getNestedTask(task.tasks[task.currentTaskIndex], context)
        return task
    
    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        if self.rootTask is None:
            return context
        if self.rootTask.status == 'completed':
            return context
        currentTask = self.getCurrentTask(context)
        if currentTask.status == 'notStarted':
            if currentTask.startedAt is None:
                currentTask.startedAt = time()
            shouldExecNow = time() - currentTask.startedAt >= currentTask.delayBeforeStart
            if shouldExecNow:
                shouldExecResponse = currentTask.shouldIgnore(context) == False
                shouldNotExecTask = shouldExecResponse == False and currentTask.status != 'running'
                if shouldNotExecTask:
                    context = currentTask.onIgnored(context)
                    context = self.markCurrentTaskAsFinished(currentTask, context)
                else:
                    currentTask.status = 'running'
                    context = currentTask.do(context)
        elif currentTask.status == 'running':
            if not currentTask.terminable:
                context = currentTask.ping(context)
                return currentTask.do(context)
            if currentTask.shouldRestart(context):
                currentTask.status = 'notStarted'
            else:
                hasDelayOfTimeout = currentTask.delayOfTimeout is not None
                if hasDelayOfTimeout:
                    didTimeout = time() - currentTask.startedAt >= currentTask.delayOfTimeout
                    if didTimeout:
                        context = currentTask.onTimeout(context)
                        context = self.markCurrentTaskAsFinished(currentTask, context)
                        return context
                if currentTask.did(context):
                    currentTask.finishedAt = time()
                    currentTask.status = 'almostComplete'
                else:
                    context = currentTask.ping(context)
        if currentTask.status == 'almostComplete':
            didPassedEnoughDelayAfterTaskComplete = time() - currentTask.finishedAt >= currentTask.delayAfterComplete
            if didPassedEnoughDelayAfterTaskComplete:
                context = self.markCurrentTaskAsFinished(currentTask, context)
        return context
    
    # TODO: add unit tests
    def markCurrentTaskAsFinished(self, task, context: Context):
        task.status = 'completed'
        context = task.onComplete(context)
        if task.parentTask:
            isntLastTask = task.parentTask.currentTaskIndex < len(task.parentTask.tasks) - 1
            if isntLastTask:
                task.parentTask.currentTaskIndex += 1
            else:
                context = self.markCurrentTaskAsFinished(task.parentTask, context)
        return context
