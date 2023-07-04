from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import hasCooldownByName
from ...typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def healingBySpellsObserver(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    if context['healing']['spells']['criticalHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['criticalHealing']['hpPercentageLessThanOrEqual'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['criticalHealing']['spell']['name']):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['criticalHealing']['hotkey']))
            return
    if context['healing']['spells']['criticalHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['mediumHealing']['hpPercentageLessThanOrEqual'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['mediumHealing']['spell']['name']):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['mediumHealing']['hotkey']))
            return
    if context['healing']['spells']['lightHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['lightHealing']['hpPercentageLessThanOrEqual'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['lightHealing']['spell']['name']):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['lightHealing']['hotkey']))
            return
    if context['healing']['spells']['uturaGran']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['uturaGran']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'utura gran'):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['uturaGran']['hotkey']))
            return
    if context['healing']['spells']['utura']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['utura']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'utura'):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['utura']['hotkey']))
            return
    if context['healing']['spells']['exuraGranIco']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['exuraGranIco']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'exura gran ico'):
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(
                context['healing']['spells']['exuraGranIco']['hotkey']))
            return
