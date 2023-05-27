from src.gameplay.core.tasks.useHotkey import UseHotkeyVectorTask
from src.repositories.actionBar.core import slotIsAvailable, slotIsEquipped
from ...typings import Context


currentSpellHealingPriorityTask = None


# TODO: add unit tests
def healingPriorityObserver(context: Context):
    global currentSpellHealingPriorityTask
    if currentSpellHealingPriorityTask is not None:
        if currentSpellHealingPriorityTask.status == 'completed':
            currentSpellHealingPriorityTask = None
        else:
            currentSpellHealingPriorityTask.do(context)
            return
    if context['healing']['highPriority']['ssa']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['highPriority']['ssa']['hpPercentageLessThanOrEqual']:
            if not slotIsEquipped(context['screenshot'], 17) and slotIsAvailable(context['screenshot'], 17):
                currentSpellHealingPriorityTask = UseHotkeyVectorTask(context['healing']['highPriority']['ssa']['hotkey'])
        elif context['statusBar']['hpPercentage'] >= context['healing']['highPriority']['ssa']['hpPercentageGreaterThanOrEqual']:
            if slotIsEquipped(context['screenshot'], 17):
                currentSpellHealingPriorityTask = UseHotkeyVectorTask(context['healing']['highPriority']['ssa']['hotkey'])
                return
