from time import time
from src.gameplay.comboSpells.core import comboSpellDidMatch
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.repositories.actionBar.core import hasCooldownByName
from src.repositories.gameWindow.creatures import getNearestCreaturesCount
from src.utils.array import getNextArrayIndex
from src.wiki.spells import spells
from .core.tasks.useHotkey import UseHotkeyTask
from .typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def comboSpells(context: Context):
    # TODO: instead of making this comparison, it should be using thread and being turned off when disabled
    if not context['comboSpells']['enabled']:
        return
    if context['statusBar']['mana'] is None:
        return
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    nearestCreaturesCount = getNearestCreaturesCount(
        context['gameWindow']['monsters'])
    if nearestCreaturesCount == 0:
        return
    for key, comboSpell in enumerate(context['comboSpells']['items']):
        if comboSpell['enabled'] == False:
            continue
        if comboSpellDidMatch(comboSpell, nearestCreaturesCount):
            spell = comboSpell['spells'][comboSpell['currentSpellIndex']]
            if context['statusBar']['mana'] < spells[spell['name']]['manaNeeded']:
                return
            if hasCooldownByName(context['screenshot'], 'attack'):
                return
            if hasCooldownByName(context['screenshot'], spell['name']):
                return
            # TODO: verify if spell hotkey slot is available
            tasksOrchestrator.setRootTask(
                context, UseHotkeyTask(spell['hotkey']))
            nextIndex = getNextArrayIndex(
                comboSpell['spells'], comboSpell['currentSpellIndex'])
            # TODO: improve indexes without using context
            context['comboSpells']['items'][key]['currentSpellIndex'] = nextIndex
            context['comboSpells']['lastUsedSpell'] = spell['name']
            context['comboSpells']['lastUsedSpellAt'] = time()
            return
