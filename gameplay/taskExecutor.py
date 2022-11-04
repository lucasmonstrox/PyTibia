from time import time


class TaskExecutor:
    def exec(self, context):
        if context['currentGroupTask'] is not None:
            if context['currentGroupTask'].status == 'notStarted':
                if context['currentGroupTask'].startedAt == None:
                    context['currentGroupTask'].startedAt = time()
                passedTimeSinceLastCheck = time(
                ) - context['currentGroupTask'].startedAt
                shouldExecNow = passedTimeSinceLastCheck >= context['currentGroupTask'].delayBeforeStart
                if shouldExecNow:
                    shouldExecResponse = context['currentGroupTask'].shouldIgnore(
                        context) == False
                    shouldNotExecTask = shouldExecResponse == False and context[
                        'currentGroupTask'].status != 'running'
                    if shouldNotExecTask:
                        context = context['currentGroupTask'].onIgnored(
                            context)
                        context['currentGroupTask'] = None
                    else:
                        context['currentGroupTask'].status = 'running'
                        context = context['currentGroupTask'].do(context)
            elif context['currentGroupTask'].status == 'running':
                context = context['currentGroupTask'].do(context)
                shouldNotRestart = not context['currentGroupTask'].shouldRestart(
                    context)
                if shouldNotRestart:
                    didTask = context['currentGroupTask'].did(context)
                    if didTask:
                        context['currentGroupTask'].finishedAt = time()
                        context['currentGroupTask'].status = 'completed'
            if context['currentGroupTask'].status == 'completed':
                passedTimeSinceTaskCompleted = time(
                ) - context['currentGroupTask'].finishedAt
                didPassedEnoughDelayAfterTaskComplete = passedTimeSinceTaskCompleted > context[
                    'currentGroupTask'].delayAfterComplete
                if didPassedEnoughDelayAfterTaskComplete:
                    context = context['currentGroupTask'].onDidComplete(
                        context)
                    context['currentGroupTask'] = None
        return context
