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
                if len(task.tasks) == 0:
                    return task
                return self.getNestedTask(task.tasks[task.currentTaskIndex], context)
        return task

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        if self.rootTask is None:
            return context
        if self.rootTask.status == 'completed':
            return context
        currentTask = self.getCurrentTask(context)
        if currentTask.status == 'awaitingManualTermination':
            if currentTask.shouldManuallyComplete(context):
                currentTask.status = 'completed'
                return self.markCurrentTaskAsFinished(currentTask, context, disableManualTermination=True)
            if currentTask.shouldRestart(context):
                currentTask.status = 'notStarted'
                currentTask.retryCount += 1
                context = currentTask.onBeforeRestart(context)
            return context
        if currentTask.status == 'notStarted' or currentTask.status == 'awaitingDelayBeforeStart':
            if currentTask.startedAt is None:
                currentTask.startedAt = time()
            if self.didPassedEnoughTimeToExecute(currentTask):
                if currentTask.shouldIgnore(context):
                    context = currentTask.onIgnored(context)
                    return self.markCurrentTaskAsFinished(currentTask, context)
                else:
                    currentTask.status = 'running'
                    return currentTask.do(context)
            else:
                currentTask.status = 'awaitingDelayBeforeStart'
            return context
        elif currentTask.status == 'running':
            if not currentTask.terminable:
                context = currentTask.ping(context)
                return currentTask.do(context)
            if currentTask.shouldRestart(context):
                currentTask.status = 'notStarted'
                return context
            else:
                if self.didTaskTimedout(currentTask):
                    context = currentTask.onTimeout(context)
                    return self.markCurrentTaskAsFinished(currentTask, context)
                if currentTask.did(context):
                    currentTask.finishedAt = time()
                    if currentTask.delayAfterComplete > 0:
                        currentTask.status = 'awaitingDelayAfterComplete'
                        return context
                    else:
                        return self.markCurrentTaskAsFinished(currentTask, context)
                else:
                    context = currentTask.ping(context)
        if currentTask.status == 'awaitingDelayAfterComplete' and self.didPassedEnoughDelayAfterTaskComplete(currentTask):
            return self.markCurrentTaskAsFinished(currentTask, context)
        return context

    # TODO: add unit tests
    def markCurrentTaskAsFinished(self, task, context: Context, disableManualTermination=False):
        if task.manuallyTerminable and disableManualTermination == False:
            task.status = 'awaitingManualTermination'
            return context
        else:
            task.status = 'completed'
        context = task.onComplete(context)
        if task.parentTask:
            isntLastTask = task.parentTask.currentTaskIndex < len(task.parentTask.tasks) - 1
            if isntLastTask:
                task.parentTask.currentTaskIndex += 1
            else:
                context = self.markCurrentTaskAsFinished(task.parentTask, context)
        return context

    def didPassedEnoughTimeToExecute(self, task):
        return time() - task.startedAt >= task.delayBeforeStart

    def didPassedEnoughDelayAfterTaskComplete(self, task):
        return time() - task.finishedAt >= task.delayAfterComplete

    def didTaskTimedout(self, task):
        return task.delayOfTimeout > 0 and time() - task.startedAt >= task.delayOfTimeout
