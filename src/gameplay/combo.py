import pyautogui
import time
from src.gameplay.comboSpells.core import comboSpellDidMatch
from src.features.actionBar.core import hasCooldownByName
from src.features.gameWindow.creatures import getNearestCreaturesCount
from src.utils.array import getNextArrayIndex


def comboSpellsObservable(context):
    if context['statusBar']['mana'] is None:
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
            hasCooldown = hasCooldownByName(context['screenshot'], spell['name'])
            if hasCooldown:
                return
            hasNoMana = context['statusBar']['mana'] < spell['metadata']['mana']
            if hasNoMana:
                continue
            hotkey = spell['hotkey']
            pyautogui.press(hotkey)
            nextIndex = getNextArrayIndex(comboSpell['spells'], comboSpell['currentSpellIndex'])
            # improve indexes without using context
            context['comboSpells']['items'][key]['currentSpellIndex'] = nextIndex
            context['comboSpells']['lastUsedSpell'] = spell['name']
            time.sleep(0.5)
            break