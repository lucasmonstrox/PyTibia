import json
import numpy as np
from src.repositories.radar.typings import Waypoint


# TODO: add types
# TODO: add unit tests
def loadConfigByJson(filePath: str):
    with open(filePath) as d:
        return json.load(d)


# TODO: add types
# TODO: add unit tests
def loadContextFromConfig(config, context):
    # backpacks
    context['backpacks'] = config['backpacks']
    # cavebot
    context['cavebot']['enabled'] = config['cavebot']['enabled']
    context['cavebot']['waypoints']['points'] = np.array([], dtype=Waypoint)
    for waypoint in config['cavebot']['waypoints']['points']:
        waypoint = np.array(
            (waypoint['label'], waypoint['type'], tuple(waypoint['coordinate']), waypoint['options']), dtype=Waypoint)
        context['cavebot']['waypoints']['points'] = np.append(
            context['cavebot']['waypoints']['points'], [waypoint], axis=0)
    # comboSpells
    context['comboSpells']['enabled'] = config['comboSpells']['enabled']
    for comboSpellsItem in config['comboSpells']['items']:
        comboSpellsItem['currentSpellIndex'] = 0
        context['comboSpells']['items'].append(comboSpellsItem)
    # healing
    context['healing'] = config['healing']
    # hotkeys
    context['hotkeys'] = config['hotkeys']
    return context
