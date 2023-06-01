from ...typings import Context


def setCleanUpTasksMiddleware(gameContext: Context) -> Context:
    currentTask = gameContext['taskOrchestrator'].getCurrentTask(gameContext)
    if currentTask is not None and (currentTask.status == 'completed' or (hasattr(currentTask, 'tasks') and len(currentTask.tasks) == 0)):
        gameContext['taskOrchestrator'].reset()
    return gameContext
