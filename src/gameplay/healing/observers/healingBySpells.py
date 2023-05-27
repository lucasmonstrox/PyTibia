from src.gameplay.core.tasks.useHotkey import UseHotkeyVectorTask
from src.repositories.actionBar.core import hasCooldownByName
from ...typings import Context


currentSpellHealingTask = None


# TODO: add unit tests
def healingBySpellsObserver(context: Context):
    global currentSpellHealingTask
    if currentSpellHealingTask is not None:
        if currentSpellHealingTask.status == 'completed':
            currentSpellHealingTask = None
        else:
            currentSpellHealingTask.do(context)
            return
    if context['healing']['spells']['criticalHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['criticalHealing']['hpPercentageLessThanOrEqual'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['criticalHealing']['spell']['name']):
            currentSpellHealingTask = UseHotkeyVectorTask(context['healing']['spells']['criticalHealing']['hotkey'])
            return
    if context['healing']['spells']['lightHealing']['enabled']:
        if context['statusBar']['hpPercentage'] <= context['healing']['spells']['lightHealing']['hpPercentageLessThanOrEqual'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['lightHealing']['spell']['name']):
            currentSpellHealingTask = UseHotkeyVectorTask(context['healing']['spells']['lightHealing']['hotkey'])
            return
    if context['healing']['spells']['utura']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['utura']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['utura']['spell']['name']):
            currentSpellHealingTask = UseHotkeyVectorTask(context['healing']['spells']['utura']['hotkey'])
            return
    if context['healing']['spells']['exuraGranIco']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['exuraGranIco']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'exura gran ico'):
            currentSpellHealingTask = UseHotkeyVectorTask(context['healing']['spells']['exuraGranIco']['hotkey'])
            return
