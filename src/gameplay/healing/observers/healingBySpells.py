from src.features.actionBar.core import hasCooldownByName
from src.gameplay.core.tasks.useHotkey import UseHotkeyGroupTask
from ...typings import Context


currentSpellHealingTask = None


# TODO: add unit tests
def healingBySpellsObserver(context: Context):
    global currentSpellHealingTask
    if currentSpellHealingTask is not None:
        if currentSpellHealingTask.status == 'completed':
            currentSpellHealingTask = None
        else:
            if currentSpellHealingTask.status == 'notStarted':
                currentSpellHealingTask.do(context)
            return
    if context['healing']['spells']['utura']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['utura']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], context['healing']['spells']['utura']['spell']['name']):
            currentSpellHealingTask = UseHotkeyGroupTask(context['healing']['spells']['utura']['hotkey'])
            return
    if context['healing']['spells']['exuraGranIco']['enabled']:
        if context['statusBar']['mana'] >= context['healing']['spells']['exuraGranIco']['spell']['manaNeeded'] and not hasCooldownByName(context['screenshot'], 'exura gran ico'):
            currentSpellHealingTask = UseHotkeyGroupTask(context['healing']['spells']['exuraGranIco']['hotkey'])
            return
