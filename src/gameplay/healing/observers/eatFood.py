from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import slotIsAvailable, slotIsEquipped
from src.repositories.skills.core import getFood
from ...typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def eatFood(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    if not context['healing']['eatFood']['enabled']:
        return
    food = getFood(context['screenshot'])
    if food > context['healing']['eatFood']['eatWhenFoodIslessOrEqual']:
        return
    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
        context['healing']['eatFood']['hotkey'], delayAfterComplete=2))
