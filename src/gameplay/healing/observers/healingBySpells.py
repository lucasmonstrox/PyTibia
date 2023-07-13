from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.useHotkey import UseHotkeyTask
from src.repositories.actionBar.core import hasCooldownByName
from src.wiki.spells import spells
from ...typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def healingBySpells(context: Context):
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    if context['healing']['spells']['criticalHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['criticalHealing']['hpPercentageLessThanOrEqual'] and context['statusBar']['mana'] >= spells[context['healing']['spells']['lightHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['criticalHealing']['spell']):
            tasksOrchestrator.setRootTask(
                context, UseHotkeyTask('5'))
            return
    if context['healing']['spells']['lightHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['lightHealing']['hpPercentageLessThanOrEqual'] and context['statusBar']['mana'] >= spells[context['healing']['spells']['lightHealing']['spell']]['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['lightHealing']['spell']):
            tasksOrchestrator.setRootTask(
                context, UseHotkeyTask('6'))
            return
    if context['healing']['spells']['utura']['enabled']:
        if context['statusBar']['mana'] >= spells['utura']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'utura'):
            tasksOrchestrator.setRootTask(
                context, UseHotkeyTask('7'))
            return
    if context['healing']['spells']['uturaGran']['enabled']:
        if context['statusBar']['mana'] >= spells['utura gran']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'utura gran'):
            tasksOrchestrator.setRootTask(
                context, UseHotkeyTask('8'))
            return
