from time import time


class GroupTaskExecutor:
    def exec(self, context):
        if len(self.tasks) > 0:
            freeTaskIndex = None
            for taskIndex, taskWithName in enumerate(self.tasks):
                _, possibleFreeTask = taskWithName
                # print('possibleFreeTask.name', possibleFreeTask.name)
                # print('possibleFreeTask.status', possibleFreeTask.status)
                if possibleFreeTask.status != 'completed':
                    freeTaskIndex = taskIndex
                    break
            # print('freeTaskIndex', freeTaskIndex)
            if freeTaskIndex == None:
                return context
            # TODO: se estiver tudo feito, dar como terminado
            taskName, task = self.tasks[freeTaskIndex]
            if task.status == 'notStarted':
                if task.startedAt == None:
                    task.startedAt = time()
                passedTimeSinceLastCheck = time() - task.startedAt
                shouldExecNow = passedTimeSinceLastCheck >= task.delayBeforeStart
                if shouldExecNow:
                    shouldExecResponse = task.shouldIgnore(context) == False
                    shouldNotExecTask = shouldExecResponse == False and task.status != 'running'
                    if shouldNotExecTask:
                        task.status = 'completed'
                        context = task.onIgnored(context)
                    else:
                        task.status = 'running'
                        context = task.do(context)
                    self.tasks[freeTaskIndex] = (taskName, task)
            elif task.status == 'running':
                shouldNotRestart = not task.shouldRestart(context)
                if shouldNotRestart:
                    didTask = task.did(context)
                    if didTask:
                        task.finishedAt = time()
                        task.status = 'almostComplete'
                        self.tasks[freeTaskIndex] = (taskName, task)
            if task.status == 'almostComplete':
                passedTimeSinceTaskCompleted = time() - task.finishedAt
                didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > task.delayAfterComplete
                if didPassedEnoughDelayAfterTaskComplete:
                    context = task.onDidComplete(context)
                    task.status = 'completed'
                    self.tasks[freeTaskIndex] = (taskName, task)
        return context

    def do(self, context):
        context = self.exec(context)
        return context

    def did(self, _):
        for taskWithName in self.tasks:
            _, task = taskWithName
            if task.status != 'completed':
                return False
        return True
