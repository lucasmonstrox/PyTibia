from src.repositories.battleList.core import getBeingAttackedCreatureCategory
from src.repositories.chat.core import hasNewLoot
from src.repositories.gameWindow.config import gameWindowSizes
from src.repositories.gameWindow.core import getCoordinate, getImageByCoordinate
from src.repositories.gameWindow.creatures import getCreatures, getCreaturesByType, getDifferentCreaturesBySlots, getTargetCreature
from ...comboSpells.core import spellsPath
from ...typings import Context
from ..tasks.selectChatTab import SelectChatTabTask


# TODO: add unit tests
def setDirectionMiddleware(context: Context) -> Context:
    if context['radar']['previousCoordinate'] is None:
        context['radar']['previousCoordinate'] = context['radar']['coordinate']
    if context['radar']['coordinate'][0] != context['radar']['previousCoordinate'][0] or context['radar']['coordinate'][1] != context['radar']['previousCoordinate'][1] or context['radar']['coordinate'][2] != context['radar']['previousCoordinate'][2]:
        comingFromDirection = None
        if context['radar']['coordinate'][2] != context['radar']['previousCoordinate'][2]:
            comingFromDirection = None
        elif context['radar']['coordinate'][0] != context['radar']['previousCoordinate'][0] and context['radar']['coordinate'][1] != context['radar']['previousCoordinate'][1]:
            comingFromDirection = None
        elif context['radar']['coordinate'][0] != context['radar']['previousCoordinate'][0]:
            comingFromDirection = 'left' if context['radar']['coordinate'][
                0] > context['radar']['previousCoordinate'][0] else 'right'
        elif context['radar']['coordinate'][1] != context['radar']['previousCoordinate'][1]:
            comingFromDirection = 'top' if context['radar']['coordinate'][
                1] > context['radar']['previousCoordinate'][1] else 'bottom'
        context['comingFromDirection'] = comingFromDirection
    # if context['gameWindow']['previousGameWindowImage'] is not None:
    #     context['gameWindow']['walkedPixelsInSqm'] = getWalkedPixels(context)
    context['gameWindow']['previousGameWindowImage'] = context['gameWindow']['image']
    context['radar']['previousCoordinate'] = context['radar']['coordinate']
    return context


# TODO: add unit tests
def setHandleLootMiddleware(context: Context) -> Context:
    currentTaskName = context['tasksOrchestrator'].getCurrentTaskName(context)
    if (currentTaskName not in ['depositGold', 'refill', 'selectChatTab']):
        lootTab = context['chat']['tabs'].get('loot')
        if lootTab is not None and not lootTab['isSelected']:
            context['tasksOrchestrator'].setRootTask(
                context, SelectChatTabTask('loot'))
    if hasNewLoot(context['screenshot']):
        if context['cavebot']['previousTargetCreature'] is not None:
            context['loot']['corpsesToLoot'].append(
                context['cavebot']['previousTargetCreature'])
            context['cavebot']['previousTargetCreature'] = None
        # has spelled exori category
        if context['comboSpells']['lastUsedSpell'] is not None and context['comboSpells']['lastUsedSpell'] in ['exori', 'exori gran', 'exori mas']:
            spellPath = spellsPath.get(
                context['comboSpells']['lastUsedSpell'], [])
            if len(spellPath) > 0:
                differentCreatures = getDifferentCreaturesBySlots(
                    context['gameWindow']['previousMonsters'], context['gameWindow']['monsters'], spellPath)
                for creature in differentCreatures:
                    context['loot']['corpsesToLoot'].append(creature)
            context['comboSpells']['lastUsedSpell'] = None
            context['comboSpells']['lastUsedSpellAt'] = None
    context['cavebot']['targetCreature'] = getTargetCreature(
        context['gameWindow']['monsters'])
    if context['cavebot']['targetCreature'] is not None:
        context['cavebot']['previousTargetCreature'] = context['cavebot']['targetCreature']
    return context


# TODO: add unit tests
def setGameWindowMiddleware(context: Context) -> Context:
    context['gameWindow']['coordinate'] = getCoordinate(
        context['screenshot'], gameWindowSizes[context['resolution']])
    context['gameWindow']['image'] = getImageByCoordinate(
        context['screenshot'], context['gameWindow']['coordinate'], gameWindowSizes[context['resolution']])
    return context


# TODO: add unit tests
def setGameWindowCreaturesMiddleware(context: Context) -> Context:
    context['battleList']['beingAttackedCreatureCategory'] = getBeingAttackedCreatureCategory(
        context['battleList']['creatures'])
    context['gameWindow']['creatures'] = getCreatures(
        context['battleList']['creatures'], context['comingFromDirection'], context['gameWindow']['coordinate'], context['gameWindow']['image'], context['radar']['coordinate'], beingAttackedCreatureCategory=context['battleList']['beingAttackedCreatureCategory'], walkedPixelsInSqm=context['gameWindow']['walkedPixelsInSqm'])
    if len(context['gameWindow']['creatures']) == 0:
        context['gameWindow']['monsters'] = []
        context['gameWindow']['players'] = []
        return context
    context['gameWindow']['monsters'] = getCreaturesByType(
        context['gameWindow']['creatures'], 'monster')
    context['gameWindow']['players'] = getCreaturesByType(
        context['gameWindow']['creatures'], 'player')
    return context
