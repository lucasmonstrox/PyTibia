from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import slotIsAvailable, slotIsEquipped
from ...typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def swapAmulet(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    if context['healing']['highPriority']['swapAmulet']['enabled']:
        firstSlotIsEquipped = slotIsEquipped(context['screenshot'], 23)
        firstSlotIsAvailable = slotIsAvailable(context['screenshot'], 23)
        secondSlotIsEquipped = slotIsEquipped(context['screenshot'], 24)
        secondSlotIsAvailable = slotIsAvailable(context['screenshot'], 24)
        if context['statusBar']['hpPercentage'] <= context['healing']['highPriority']['swapAmulet']['tankAmulet']['hpPercentageLessThanOrEqual']:
            if not firstSlotIsEquipped and firstSlotIsAvailable:
                tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                    context['healing']['highPriority']['swapAmulet']['tankAmulet']['hotkey'], delayAfterComplete=2))
            return
        if context['statusBar']['hpPercentage'] > context['healing']['highPriority']['swapAmulet']['mainAmulet']['hpPercentageGreaterThan']:
            if not secondSlotIsEquipped and secondSlotIsAvailable:
                tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                    context['healing']['highPriority']['swapAmulet']['mainAmulet']['hotkey'], delayAfterComplete=2))
            return
        if context['healing']['highPriority']['swapAmulet']['amuletAlwaysEquipped']:
            amuletType = context['healing']['highPriority']['swapAmulet']['amuletAlwaysEquipped']
            if amuletType == 'tankAmulet' and secondSlotIsEquipped:
                if firstSlotIsAvailable:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapAmulet']['tankAmulet']['hotkey'], delayAfterComplete=2))
                else:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapAmulet']['mainAmulet']['hotkey'], delayAfterComplete=2))
                return
            if amuletType == 'mainAmulet' and firstSlotIsEquipped:
                if secondSlotIsAvailable:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapAmulet']['mainAmulet']['hotkey'], delayAfterComplete=2))
                else:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapAmulet']['tankAmulet']['hotkey'], delayAfterComplete=2))
                return
            return
        if firstSlotIsEquipped:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapAmulet']['tankAmulet']['hotkey'], delayAfterComplete=2))
            return
        if secondSlotIsEquipped:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapAmulet']['mainAmulet']['hotkey'], delayAfterComplete=2))
            return
