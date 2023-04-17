import pyautogui
from time import sleep
from src.gameplay.comboSpells.core import comboSpellDidMatch
from src.features.actionBar.core import hasCooldownByName
from src.features.hud.creatures import getNearestCreaturesCount
from src.utils.array import getNextArrayIndex


def comboSpellsObservable(_):
    global gameContext, hudCreatures
    if gameContext['statusBar']['mana'] is None:
        return
    nearestCreaturesCount = getNearestCreaturesCount(gameContext['monsters'])
    if nearestCreaturesCount == 0:
        return
    if gameContext['comboSpells']['enabled'] == False:
        return
    for key, comboSpell in enumerate(gameContext['comboSpells']['items']):
        if comboSpell['enabled'] == False:
            continue
        if comboSpellDidMatch(comboSpell, nearestCreaturesCount):
            spell = comboSpell['spells'][comboSpell['currentSpellIndex']]
            hasCooldown = hasCooldownByName(gameContext['screenshot'], spell['name'])
            if hasCooldown:
                return
            hasNoMana = gameContext['statusBar']['mana'] < spell['metadata']['mana']
            if hasNoMana:
                continue
            hotkey = spell['hotkey']
            pyautogui.press(hotkey)
            nextIndex = getNextArrayIndex(comboSpell['spells'], comboSpell['currentSpellIndex'])
            gameContext['comboSpells']['items'][key]['currentSpellIndex'] = nextIndex
            gameContext['comboSpells']['lastUsedSpell'] = spell['name']
            sleep(0.5)
            break