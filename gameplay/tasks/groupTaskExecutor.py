from time import time


class GroupTaskExecutor:
    def __init__(self):
        self.currentTaskIndex = 0
        self.status = 'notStarted'

    def exec(self, context):
        hasTasks = len(self.tasks) > 0
        if hasTasks:
            self.status = 'running'
            taskName, task = self.tasks[self.currentTaskIndex]
            if task.status == 'notStarted':
                if task.startedAt == None:
                    task.startedAt = time()
                passedTimeSinceLastCheck = time() - task.startedAt
                shouldExecNow = passedTimeSinceLastCheck >= task.delayBeforeStart
                if shouldExecNow:
                    shouldExecResponse = task.shouldIgnore(context) == False
                    shouldNotExecTask = shouldExecResponse == False and task.status != 'running'
                    if shouldNotExecTask:
                        context = task.onIgnored(context)
                        self.markCurrentTaskAsCompleted()
                    else:
                        task.status = 'running'
                        context = task.do(context)
                    self.tasks[self.currentTaskIndex] = (taskName, task)
            elif task.status == 'running':
                if task.shouldRestart(context):
                    self.tasks[self.currentTaskIndex][1].status = 'notStarted'
                else:
                    hasDelayOfTimeout = task.delayOfTimeout is not None
                    if hasDelayOfTimeout:
                        passedTimeSinceLastCheck = time() - task.startedAt
                        didTimeout = passedTimeSinceLastCheck >= task.delayOfTimeout
                        if didTimeout:
                            context = task.onDidTimeout(context)
                            self.markCurrentTaskAsCompleted()
                            return context
                    didTask = task.did(context)
                    if didTask:
                        task.finishedAt = time()
                        self.tasks[self.currentTaskIndex][1].status = 'almostComplete'
                    else:
                        context = task.ping(context)
            if task.status == 'almostComplete':
                passedTimeSinceTaskCompleted = time() - task.finishedAt
                didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > task.delayAfterComplete
                if didPassedEnoughDelayAfterTaskComplete:
                    context = task.onDidComplete(context)
                    self.markCurrentTaskAsCompleted()
        return context

    def markCurrentTaskAsCompleted(self):
        self.tasks[self.currentTaskIndex][1].status = 'completed'
        isntLastTask = self.currentTaskIndex < len(self.tasks) - 1
        if isntLastTask:
            self.currentTaskIndex += 1
        else:
            self.status = 'completed'
