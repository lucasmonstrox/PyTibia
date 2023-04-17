import numpy as np
from src.features.battleList.core import getBeingAttackedCreatureCategory
from src.features.hud.core import getCoordinate, getImgByCoordinate, hudSizes
from src.features.hud.creatures import getCreatures, getCreaturesByType, getTargetCreature
from features.hud.typings import creatureType


def setDirection(gameContext):
    if gameContext['radar']['previousCoordinate'] is None:
        gameContext['radar']['previousCoordinate'] = gameContext['radar']['coordinate']
    coordinate = gameContext['radar']['coordinate']
    previousCoordinate = gameContext['radar']['previousCoordinate']
    coordinateDidChange = coordinate[0] != previousCoordinate[0] or coordinate[1] != previousCoordinate[1] or coordinate[2] != previousCoordinate[2]
    if coordinateDidChange:
        comingFromDirection = None
        if coordinate[2] != previousCoordinate[2]:
            comingFromDirection = None
        elif coordinate[0] != previousCoordinate[0] and coordinate[1] != previousCoordinate[1]:
            comingFromDirection = None
        elif coordinate[0] != previousCoordinate[0]:
            comingFromDirection = 'left' if coordinate[0] > previousCoordinate[0] else 'right'
        elif coordinate[1] != previousCoordinate[1]:
            comingFromDirection = 'top' if coordinate[1] > previousCoordinate[1] else 'bottom'
        gameContext['comingFromDirection'] = comingFromDirection
    # if gameContext['hud']['previousHudImage'] is not None:
    #     gameContext['hud']['walkedPixelsInSqm'] = getWalkedPixels(gameContext)
    gameContext['hud']['previousHudImage'] = gameContext['hud']['img']
    gameContext['radar']['previousCoordinate'] = gameContext['radar']['coordinate']
    return gameContext


def setHandleLoot(gameContext):
    # if chat.core.hasNewLoot(gameContext['screenshot']):
    #     if gameContext['cavebot']['targetCreature'] is not None:
    #         gameContext['loot']['corpsesToLoot'] = np.append(gameContext['loot']['corpsesToLoot'], [gameContext['cavebot']['targetCreature']], axis=0)
    #     hasSpelledExoriCategory = gameContext['comboSpells']['lastUsedSpell'] is not None and gameContext['comboSpells']['lastUsedSpell'] in ['exori', 'exori gran', 'exori mas']
    #     if hasSpelledExoriCategory:
    #         spellPath = getSpellPath(gameContext['comboSpells']['lastUsedSpell'])
    #         if len(spellPath) > 0:
    #             differentCreatures = src.features.hud.creatures.getDifferentCreaturesBySlots(gameContext['hud']['previousMonsters'], gameContext['monsters'], spellPath)
    #             gameContext['loot']['corpsesToLoot'] = np.append(gameContext['loot']['corpsesToLoot'], differentCreatures, axis=0)
    #         gameContext['comboSpells']['lastUsedSpell'] = None
    gameContext['cavebot']['targetCreature'] = getTargetCreature(gameContext['monsters'])
    return gameContext


def setHudMiddleware(gameContext):
    hudSize = hudSizes[gameContext['resolution']]
    gameContext['hud']['coordinate'] = getCoordinate(
        gameContext['screenshot'], hudSize)
    gameContext['hud']['img'] = getImgByCoordinate(
        gameContext['screenshot'], gameContext['hud']['coordinate'], hudSize)
    return gameContext


def setHudCreatures(gameContext):
    beingAttackedCreatureCategory = getBeingAttackedCreatureCategory(gameContext['battleList']['creatures'])
    gameContext['battleList']['beingAttackedCreatureCategory'] = beingAttackedCreatureCategory
    hudCreatures = getCreatures(
        gameContext['battleList']['creatures'], gameContext['comingFromDirection'], gameContext['hud']['coordinate'], gameContext['hud']['img'], gameContext['radar']['coordinate'], beingAttackedCreatureCategory=beingAttackedCreatureCategory, walkedPixelsInSqm=gameContext['hud']['walkedPixelsInSqm'])
    hasNoHudCreatures = len(hudCreatures) == 0
    gameContext['monsters'] = np.array([], dtype=creatureType) if hasNoHudCreatures else getCreaturesByType(hudCreatures, 'monster')
    gameContext['players'] = np.array([], dtype=creatureType) if hasNoHudCreatures else getCreaturesByType(hudCreatures, 'player')
    return gameContext