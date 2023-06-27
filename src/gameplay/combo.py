from src.gameplay.comboSpells.core import comboSpellDidMatch
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.repositories.actionBar.core import hasCooldownByName
from src.repositories.gameWindow.creatures import getNearestCreaturesCount
from src.utils.array import getNextArrayIndex
from .core.tasks.useHotkey import UseHotkeyTask
from .typings import Context


tasksOrchestrator = TasksOrchestrator()


# TODO: add unit tests
def comboSpellsObserver(context: Context):
    if context['statusBar']['mana'] is None:
        return
    currentTask = tasksOrchestrator.getCurrentTask(context)
    if currentTask is not None:
        if currentTask.status == 'completed':
            tasksOrchestrator.reset()
        else:
            tasksOrchestrator.do(context)
            return
    nearestCreaturesCount = getNearestCreaturesCount(context['gameWindow']['monsters'])
    if nearestCreaturesCount == 0:
        return
    if context['comboSpells']['enabled'] == False:
        return
    for key, comboSpell in enumerate(context['comboSpells']['items']):
        if comboSpell['enabled'] == False:
            continue
        if comboSpellDidMatch(comboSpell, nearestCreaturesCount):
            spell = comboSpell['spells'][comboSpell['currentSpellIndex']]
            if hasCooldownByName(context['screenshot'], spell['name']):
                return
            if context['statusBar']['mana'] < spell['metadata']['mana']:
                continue
            tasksOrchestrator.setRootTask(context, UseHotkeyTask(spell['hotkey'], delayAfterComplete=0.1))
            nextIndex = getNextArrayIndex(comboSpell['spells'], comboSpell['currentSpellIndex'])
            # TODO: improve indexes without using context
            context['comboSpells']['items'][key]['currentSpellIndex'] = nextIndex
            context['comboSpells']['lastUsedSpell'] = spell['name']
            break
