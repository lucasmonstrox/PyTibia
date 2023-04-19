import numpy as np
from src.features.battleList.typings import Creature as BattleListCreature
from src.features.gameWindow.typings import Creature as GameWindowCreature
from src.features.radar.typings import Coordinate, Waypoint


gameContext = {
    'backpacks': {
        'main': 'brocade backpack',
        'gold': 'crystal backpack',
        'loot': 'beach backpack',
    },
    'battleList': {
        'beingAttackedCreatureCategory': None,
        'creatures': np.array([], dtype=BattleListCreature),
    },
    'cavebot': {
        'enabled': True,
        'holesOrStairs': np.array([
            (33306, 32284, 5),
            (33306, 32284, 6),
            (33309, 32284, 6),
            (33312, 32281, 7),
            (33309, 32284, 7),
            (33312, 32281, 8),
            (33300, 32290, 8),
        ], dtype=Coordinate),
        'isAttackingSomeCreature': False,
        'targetCreature': None,
        'waypoints': {
            'currentIndex': None,
            'points': np.array([
                # werehyaena cave 1
                # ('', 'logout', (33214, 32458, 8), {}),
                ('', 'walk', (33214, 32458, 8), {}),
                ('', 'moveUpNorth', (33214, 32456, 8), {}),
                ('', 'walk', (33217, 32441, 7), {}),
                ('endOfCity', 'walk', (33215, 32406, 7), {}),
                ('', 'walk', (33218, 32377, 7), {}),
                ('', 'walk', (33212, 32359, 7), {}),
                ('', 'useShovel', (33212, 32358, 7), {}),
                ('', 'moveDownEast', (33227, 32358, 8), {}),
                ('', 'walk', (33222, 32355, 9), {}),
                ('', 'moveDownNorth', (33222, 32355, 9), {}), # 10
                ('caveStart', 'walk', (33207, 32353, 10), {}),
                ('', 'walk', (33189, 32348, 10), {}),
                ('', 'walk', (33193, 32366, 10), {}),
                ('', 'walk', (33208, 32367, 10), {}),
                ('', 'walk', (33223, 32387, 10), {}),
                ('', 'walk', (33200, 32389, 10), {}),
                ('', 'walk', (33196, 32398, 10), {}),
                ('', 'walk', (33210, 32373, 10), {}),
                ('', 'walk', (33221, 32351, 10), {}), # 18
                ('', 'dropFlasks', (33306, 32289, 7), {}),
                ('', 'refillChecker', (33306, 32289, 7), { # 20
                    'minimumOfManaPotions': 100,
                    'minimumOfHealthPotions': 200,
                    'minimumOfCapacity': 500,
                    'waypointLabelToRedirect': 'caveStart',
                }),
                ('', 'walk', (33221, 32353, 10), {}),
                ('', 'moveUpSouth', (33221, 32353, 10), {}),
                ('', 'walk', (33229, 32358, 9), {}),
                ('', 'moveUpWest', (33229, 32358, 9), {}),
                ('', 'walk', (33212, 32358, 8), {}),
                ('', 'useRope', (33212, 32358, 8), {}),
                ('', 'walk', (33220, 32378, 7), {}), # 27
                ('', 'walk', (33221, 32387, 7), {}),
                ('', 'depositGold', (33221, 32387, 7), {}),
                ('', 'walk', (33215, 32422, 7), {}),
                ('', 'walk', (33213, 32454, 7), {}),
                ('', 'moveDownSouth', (33213, 32454, 7), {}), # 32
                ('', 'depositItems', (33214, 32456, 8), {'city': 'Darashia'}),
                ('', 'walk', (33214, 32458, 8), {}),
                ('', 'moveUpNorth', (33214, 32456, 8), {}),
                ('', 'walk', (33217, 32403, 7), {}),
                ('', 'refill', (33306, 32289, 7), {
                    'waypointLabelToRedirect': 'endOfCity'
                }),
            ], dtype=Waypoint),
            'state': None
        },
    },
    'comingFromDirection': None,
    'comboSpells': {
        'enabled': True,
        'lastUsedSpell': None,
        'items': [
            {
                'enabled': True,
                'name': '3 ou -',
                'creatures': {
                    'compare': 'lessThan',
                    'value': 4
                },
                'currentSpellIndex': 0,
                'spells': [
                    {'name': 'exori', 'hotkey': 'f4', 'metadata': {'mana': 115}},
                    {'name': 'exori gran', 'hotkey': 'f5', 'metadata': {'mana': 340}},
                    {'name': 'exori', 'hotkey': 'f4', 'metadata': {'mana': 115}},
                    {'name': 'exori min', 'hotkey': 'f7', 'metadata': {'mana': 200}},
                    {'name': 'exori', 'hotkey': 'f4', 'metadata': {'mana': 115}},
                    {'name': 'exori gran', 'hotkey': 'f5', 'metadata': {'mana': 340}},
                ],
            },
            {
                'enabled': True,
                'name': '4 ou +',
                'creatures': {
                    'compare': 'greaterThanOrEqual',
                    'value': 4
                },
                'currentSpellIndex': 0,
                'spells': [
                    {'name': 'exori gran', 'hotkey': 'f5', 'metadata': {'mana': 340}},
                    {'name': 'exori mas', 'hotkey': 'f6', 'metadata': {'mana': 160}},
                    {'name': 'exori', 'hotkey': 'f4', 'metadata': {'mana': 115}},
                    {'name': 'exori gran', 'hotkey': 'f5', 'metadata': {'mana': 340}},
                    {'name': 'exori mas', 'hotkey': 'f6', 'metadata': {'mana': 160}},
                ],
            }
        ],
    },
    'currentTask': None,
    'deposit': {
        'lockerCoordinate': None
    },
    'currentPotionHealing': None,
    'currentSpellHealing': None,
    'gameWindow': {
        'coordinate': None,
        'img': None,
        'previousGameWindowImage': None,
        'walkedPixelsInSqm': 0,
        'previousMonsters': np.array([], dtype=GameWindowCreature),
        'monsters': np.array([], dtype=GameWindowCreature),
        'players': np.array([], dtype=GameWindowCreature),
    },
    'healing': {
        'enabled': True,
        'highPriority': {
            'healthFood': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
            },
            'manaFood': {
                'enabled': False,
                'hotkey': None,
                'manaPercentageLessThanOrEqual': None,
            },
        },
        'potions': {
            'firstHealthPotion': {
                'enabled': True,
                'hotkey': 'f1',
                'hpPercentageLessThanOrEqual': 50,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'secondHealthPotion': {
                'enabled': False,
                'hotkey': 'f2',
                'hpPercentageLessThanOrEqual': 70,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'thirdHealthPotion': {
                'enabled': True,
                'hotkey': 'f2',
                'hpPercentageLessThanOrEqual': 80,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'firstManaPotion': {
                'enabled': True,
                'hotkey': '2',
                'manaPercentageLessThanOrEqual': 80,
            },
            'secondManaPotion': {
                'enabled': False,
                'hotkey': None,
                'manaPercentageLessThanOrEqual': None,
            },
            'thirdManaPotion': {
                'enabled': False,
                'hotkey': None,
                'manaPercentageLessThanOrEqual': None,
            },
        },
        'spells': {
            'criticalHealing': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'spell': {
                    'name': 'exura med ico',
                    'manaNeeded': 90,
                    'cooldownInSeconds': 1
                }
            },
            'lightHealing': {
                'enabled': False,
                'hotkey': None,
                'hpPercentage': None,
                'spell': {
                    'name': 'exura ico',
                    'manaNeeded': 40,
                    'cooldownInSeconds': 1
                }
            },
            'utura': {
                'enabled': True,
                'hotkey': '3',
                'spell': {
                    'name': 'utura',
                    'manaNeeded': 40,
                    'cooldownInSeconds': 1
                }
            },
            'exuraGranIco': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': 99,
                'manaPercentageGreaterThanOrEqual': 5
            },
        },
    },
    'hotkeys': {
        'healthPotion': 'f1',
        'manaPotion': 'f2',
        'eatFood': 'f7',
        'rope': 'f8',
        'shovel': 'f9',
    },
    'hotkeysV2': {
        'f1': 'ultimate health potion',
        'f2': 'strong mana potion',
        'f3': 'exura med ico',
        'f12': 'stone skin amulet'
    },
    'loot': {
        'corpsesToLoot': np.array([], dtype=GameWindowCreature),
    },
    'lastPressedKey': None,
    'radar': {
        'coordinate': None,
        'previousCoordinate': None,
        'lastCoordinateVisited': None,
    },
    'refill': {
        'enabled': True,
        'health': {
            'item': 'supreme health potion',
            'quantity': 300,
        },
        'mana': {
            'item': 'strong mana potion',
            'quantity': 500,
        },
    },
    'resolution': 1080,
    'statusBar': {
        'hpPercentage': None,
        'hp': None,
        'manaPercentage': None,
        'mana': None,
    },
    'targeting': {
        'enabled': True,
        'creatures': {
            'Rat': {
                'ignore': True
            },
        },
        'canIgnoreCreatures': True,
        'hasIgnorableCreatures' : False,
    },
    'screenshot': None,
    'way': None,
    'window': None
}
