import time
from src.gameplay.comboSpells.core import comboSpellDidMatch
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.repositories.actionBar.core import hasCooldownByName
from src.repositories.gameWindow.creatures import getNearestCreaturesCount
from src.utils.array import getNextArrayIndex
from src.utils.keyboard import press
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
    if getNearestCreaturesCount(context['gameWindow']['monsters']) == 0:
        return
    if context['comboSpells']['enabled'] == False:
        return
    for key, comboSpell in enumerate(context['comboSpells']['items']):
        if comboSpell['enabled'] == False:
            continue
        if comboSpellDidMatch(comboSpell, nearestCreaturesCount):
            spell = comboSpell['spells'][comboSpell['currentSpellIndex']]
            hasCooldown = hasCooldownByName(context['screenshot'], spell['name'])
            if hasCooldown:
                return
            hasNoMana = context['statusBar']['mana'] < spell['metadata']['mana']
            if hasNoMana:
                continue
            press(spell['hotkey'])
            nextIndex = getNextArrayIndex(comboSpell['spells'], comboSpell['currentSpellIndex'])
            # improve indexes without using context
            context['comboSpells']['items'][key]['currentSpellIndex'] = nextIndex
            context['comboSpells']['lastUsedSpell'] = spell['name']
            time.sleep(0.5)
            break
