from ...typings import Context


def setCleanUpTasksMiddleware(gameContext: Context) -> Context:
    currentTask = gameContext['taskOrchestrator'].getCurrentTask(gameContext)
    if currentTask is not None:
        if currentTask.isRootTask and currentTask.status == 'completed':
            gameContext['taskOrchestrator'].reset()
        if currentTask.rootTask is not None and currentTask.rootTask.status == 'completed':
            gameContext['taskOrchestrator'].reset()
    return gameContext
