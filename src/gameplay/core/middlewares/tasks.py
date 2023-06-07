from ...typings import Context


def setCleanUpTasksMiddleware(context: Context) -> Context:
    currentTask = context['tasksOrchestrator'].getCurrentTask(context)
    if currentTask is not None:
        if currentTask.isRootTask and currentTask.status == 'completed':
            context['tasksOrchestrator'].reset()
        if currentTask.rootTask is not None:
            if currentTask.rootTask.status == 'completed':
                context['tasksOrchestrator'].reset()
    return context
