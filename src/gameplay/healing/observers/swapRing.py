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
    if context['healing']['highPriority']['swapRing']['enabled'] == False:
        return
    tankRingSlotIsEquipped = slotIsEquipped(context['screenshot'], 21)
    tankRingSlotIsAvailable = slotIsAvailable(context['screenshot'], 21)
    if context['statusBar']['hpPercentage'] <= context['healing']['highPriority']['swapRing']['tankRing']['hpPercentageLessThanOrEqual']:
        if not tankRingSlotIsEquipped and tankRingSlotIsAvailable:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
        return
    mainRingSlotIsEquipped = slotIsEquipped(context['screenshot'], 22)
    mainRingSlotIsAvailable = slotIsAvailable(context['screenshot'], 22)
    if context['statusBar']['hpPercentage'] > context['healing']['highPriority']['swapRing']['mainRing']['hpPercentageGreaterThan']:
        if not mainRingSlotIsEquipped and mainRingSlotIsAvailable:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapRing']['mainRing']['hotkey'], delayAfterComplete=2))
        return
    if context['healing']['highPriority']['swapRing']['tankRingAlwaysEquipped']:
        if not tankRingSlotIsEquipped and tankRingSlotIsAvailable:
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
        return
    if tankRingSlotIsEquipped:
        tasksOrchestrator.setRootTask(context, UseHotkeyTask(
            context['healing']['highPriority']['swapRing']['tankRing']['hotkey'], delayAfterComplete=2))
        return
    if mainRingSlotIsEquipped:
        tasksOrchestrator.setRootTask(context, UseHotkeyTask(
            context['healing']['highPriority']['swapRing']['mainRing']['hotkey'], delayAfterComplete=2))
