from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import slotIsAvailable
from ...typings import Context
from ..utils.potions import matchHpHealing, matchManaHealing


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def healingByPotionsObserver(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    for potionType in ['firstHealthPotion', 'secondHealthPotion', 'thirdHealthPotion']:
        if context['healing']['potions'][potionType]['enabled']:
            if matchHpHealing(context['healing']['potions'][potionType], context['statusBar']) and slotIsAvailable(context['screenshot'], context['healing']['potions'][potionType]['slotIndex']):
                tasksOrchestrator.setRootTask(context, UseHotkeyTask(context['healing']['potions'][potionType]['hotkey'], delayAfterComplete=1))
                return
    for potionType in ['firstManaPotion', 'secondManaPotion', 'thirdManaPotion']:
        if context['healing']['potions'][potionType]['enabled']:
            if matchManaHealing(context['healing']['potions'][potionType], context['statusBar']) and slotIsAvailable(context['screenshot'], context['healing']['potions'][potionType]['slotIndex']):
                tasksOrchestrator.setRootTask(context, UseHotkeyTask(context['healing']['potions'][potionType]['hotkey'], delayAfterComplete=1))
                return
