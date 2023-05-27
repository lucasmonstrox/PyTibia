from ...typings import Context


def setCleanUpTasksMiddleware(gameContext: Context) -> Context:
    currentTask = gameContext['taskOrchestrator'].getCurrentTask()
    if currentTask is not None and (currentTask.status == 'completed' or len(currentTask.tasks) == 0):
        gameContext['taskOrchestrator'].reset()
    return gameContext
