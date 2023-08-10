from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import slotIsAvailable, slotIsEquipped
from ...typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def swapRing(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    if context['healing']['highPriority']['swapRing']['enabled']:
        firstSlotIsEquipped = slotIsEquipped(context['screenshot'], 21)
        firstSlotIsAvailable = slotIsAvailable(context['screenshot'], 21)
        secondSlotIsEquipped = slotIsEquipped(context['screenshot'], 22)
        secondSlotIsAvailable = slotIsAvailable(context['screenshot'], 22)
        if context['statusBar']['hpPercentage'] <= context['healing']['highPriority']['swapRing']['tankRing']['hpPercentageLessThanOrEqual']:
            if not firstSlotIsEquipped and firstSlotIsAvailable:
                tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                    context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
            return
        if context['statusBar']['hpPercentage'] > context['healing']['highPriority']['swapRing']['mainRing']['hpPercentageGreaterThan']:
            if not secondSlotIsEquipped and secondSlotIsAvailable:
                tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                    context['healing']['highPriority']['swapRing']['mainRing']['hotkey'], delayAfterComplete=2))
            return
        if context['healing']['highPriority']['swapRing']['ringAlwaysEquipped']:
            ringType = context['healing']['highPriority']['swapRing']['ringAlwaysEquipped']
            if ringType == 'tankRing' and secondSlotIsEquipped:
                if firstSlotIsAvailable:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
                else:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapRing']['mainRing']['hotkey'], delayAfterComplete=2))
                return
            if ringType == 'mainRing' and firstSlotIsEquipped:
                if secondSlotIsAvailable:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapRing']['mainRing']['hotkey'], delayAfterComplete=2))
                else:
                    tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                        context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
                return
            return
        if firstSlotIsEquipped:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
            return
        if secondSlotIsEquipped:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapRing']['mainRing']['hotkey'], delayAfterComplete=2))
            return
