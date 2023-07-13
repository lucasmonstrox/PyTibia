from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import slotIsAvailable
from ...typings import Context
from ..utils.potions import matchHpHealing, matchManaHealing


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def healingByPotions(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    if context['healing']['potions']['firstHealthPotion']['enabled']:
        if matchHpHealing(context['healing']['potions']['firstHealthPotion'], context['statusBar']) and slotIsAvailable(context['screenshot'], 1):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['potions']['firstHealthPotion']['hotkey'], delayAfterComplete=1))
            return
    if context['healing']['potions']['firstManaPotion']['enabled']:
        if matchManaHealing(context['healing']['potions']['firstManaPotion'], context['statusBar']) and slotIsAvailable(context['screenshot'], 2):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['potions']['firstManaPotion']['hotkey'], delayAfterComplete=1))
            return
