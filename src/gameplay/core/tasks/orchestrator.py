from time import time
from ...typings import Context
from .common.base import BaseTask

class TasksOrchestrator:
    rootTask = None

    # TODO: add unit tests
    def setRootTask(self, context: Context, task: BaseTask):
        currentTask = self.getCurrentTask(context)
        if currentTask is not None:
            self.interruptTasks(context, currentTask)
        if task is not None:
            task.isRootTask = True
        self.rootTask = task

    # TODO: add unit tests
    def interruptTasks(self, context: Context, task) -> Context:
        context = task.onInterrupt(context)
        if task.parentTask is not None:
            return self.interruptTasks(context, task.parentTask)
        return context

    # TODO: add unit tests
    def reset(self):
        self.rootTask = None
        # terminate all tasks in the tree

    def getCurrentTask(self, context: Context):
        return self.getNestedTask(self.rootTask, context)

    def getCurrentTaskName(self, context: Context):
        currentTask = self.getNestedTask(self.rootTask, context)
        if currentTask is None:
            return 'unknown'
        if currentTask.isRootTask:
            return currentTask.name
        return currentTask.rootTask.name

    def getNestedTask(self, task, context: Context):
        if hasattr(task, 'tasks'):
            if task.status == 'notStarted':
                context = task.onBeforeStart(context)
                task.status = 'running'
            if task.status != 'completed':
                if len(task.tasks) == 0:
                    return task
                return self.getNestedTask(task.tasks[task.currentTaskIndex], context)
        return task

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        currentTask = self.getCurrentTask(context)
        self.checkHooks(currentTask, context)
        return self.handleTasks(context)

    def checkHooks(self, currentTask, context: Context) -> Context:
        if currentTask.manuallyTerminable and currentTask.shouldManuallyComplete(context):
            currentTask.status = 'completed'
            currentTask.statusReason = 'completed'
            return self.markCurrentTaskAsFinished(currentTask, context, disableManualTermination=True)
        if currentTask.status != 'notStarted' and currentTask.shouldRestart(context):
            currentTask.status = 'notStarted'
            currentTask.retryCount += 1
            if hasattr(currentTask, 'tasks'):
                currentTask.currentTaskIndex = 0
            context = currentTask.onBeforeRestart(context)
        if currentTask.parentTask:
            self.checkHooks(currentTask.parentTask, context)
        return context

    def handleTasks(self, context: Context) -> Context:
        if self.rootTask is None:
            return context
        if self.rootTask.status == 'completed':
            return context
        currentTask = self.getCurrentTask(context)
        if currentTask.status == 'awaitingManualTermination':
            if currentTask.shouldManuallyComplete(context):
                currentTask.status = 'completed'
                currentTask.statusReason = 'completed'
                return self.markCurrentTaskAsFinished(currentTask, context, disableManualTermination=True)
            if currentTask.shouldRestart(context) and currentTask.isRestarting == False:
                currentTask.startedAt = None
                currentTask.status = 'notStarted'
                currentTask.isRestarting = True
                currentTask.retryCount += 1
                return currentTask.onBeforeRestart(context)
            return context
        if currentTask.status == 'notStarted' or currentTask.status == 'awaitingDelayBeforeStart':
            currentTask.isRestarting = False
            if currentTask.startedAt is None:
                currentTask.startedAt = time()
            context = currentTask.onBeforeStart(context)
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
                    currentTask.statusReason = 'timeout'
                    return self.markCurrentTaskAsFinished(currentTask, context)
                if currentTask.did(context):
                    currentTask.finishedAt = time()
                    if currentTask.delayAfterComplete > 0:
                        currentTask.status = 'awaitingDelayToComplete'
                        return context
                    else:
                        return self.markCurrentTaskAsFinished(currentTask, context)
                else:
                    context = currentTask.ping(context)
        if currentTask.status == 'awaitingDelayToComplete' and self.didPassedEnoughDelayAfterTaskComplete(currentTask):
            return self.markCurrentTaskAsFinished(currentTask, context)
        return context

    # TODO: add unit tests
    def markCurrentTaskAsFinished(self, task, context: Context, disableManualTermination=False):
        if task.manuallyTerminable and disableManualTermination == False:
            task.status = 'awaitingManualTermination'
            return context
        else:
            task.status = 'completed'
            if task.statusReason is None:
                task.statusReason = 'completed'
        context = task.onComplete(context)
        if task.parentTask:
            if task.parentTask.currentTaskIndex < len(task.parentTask.tasks) - 1:
                task.parentTask.currentTaskIndex += 1
            else:
                if task.parentTask.shouldRestartAfterAllChildrensComplete(context):
                    task.parentTask.status = 'notStarted'
                    task.parentTask.currentTaskIndex = 0
                    task.parentTask.retryCount += 1
                    return task.parentTask.onBeforeRestart(context)
                context = self.markCurrentTaskAsFinished(task.parentTask, context)
        return context

    def didPassedEnoughTimeToExecute(self, task):
        return time() - task.startedAt >= task.delayBeforeStart

    def didPassedEnoughDelayAfterTaskComplete(self, task):
        return time() - task.finishedAt >= task.delayAfterComplete

    def didTaskTimedout(self, task):
        return task.delayOfTimeout > 0 and time() - task.startedAt >= task.delayOfTimeout
