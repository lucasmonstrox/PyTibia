from ...typings import Context


def setCleanUpTasksMiddleware(gameContext: Context) -> Context:
    currentTask = gameContext['taskOrchestrator'].getCurrentTask(gameContext)
    if currentTask is not None:
        if currentTask.isRootTask:
            if currentTask.status == 'completed':
                gameContext['taskOrchestrator'].reset()
        if currentTask.rootTask is not None:
            if currentTask.rootTask.status == 'completed':
                gameContext['taskOrchestrator'].reset()
    return gameContext
