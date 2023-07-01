from src.gameplay.core.tasks.orchestrator import TasksOrchestrator


context = {
    'backpacks': {
        'main': 'brocade backpack',
        'loot': 'beach backpack',
    },
    'battleList': {
        'beingAttackedCreatureCategory': None,
        'creatures': [],
    },
    'cavebot': {
        'enabled': True,
        'holesOrStairs': [],
        'isAttackingSomeCreature': False,
        'previousTargetCreature': None,
        'targetCreature': None,
        'waypoints': {
            'currentIndex': None,
            'items': [],
            'state': None
        },
    },
    'chat': {
        'tabs': {}
    },
    'comingFromDirection': None,
    'comboSpells': {
        'enabled': True,
        'lastUsedSpell': None,
        'items': [],
    },
    'deposit': {
        'lockerCoordinate': None
    },
    'gameWindow': {
        'coordinate': None,
        'image': None,
        'previousGameWindowImage': None,
        'previousMonsters': [],
        'monsters': [],
        'players': [],
        'walkedPixelsInSqm': 0,
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
            'ssa': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'hpPercentageGreaterThanOrEqual': None,
            }
        },
        'potions': {
            'firstHealthPotion': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'secondHealthPotion': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'thirdHealthPotion': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'manaPercentageGreaterThanOrEqual': None,
            },
            'firstManaPotion': {
                'enabled': False,
                'hotkey': None,
                'manaPercentageLessThanOrEqual': None,
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
                'spell': None
            },
            'lightHealing': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'spell': None
            },
            'utura': {
                'enabled': False,
                'hotkey': None,
                'spell': None
            },
            'exuraGranIco': {
                'enabled': False,
                'hotkey': None,
                'hpPercentageLessThanOrEqual': None,
                'manaPercentageGreaterThanOrEqual': None,
                'spell': None
            },
        },
        'eatFood': {
            'enabled': True,
            'hotkey': '5',
            'eatWhenFoodIslessOrEqual': 5,
        }
    },
    'hotkeys': {},
    'loot': {
        'corpsesToLoot': [],
    },
    'lastPressedKey': None,
    'pause': True,
    'radar': {
        'coordinate': None,
        'previousCoordinate': None,
        'lastCoordinateVisited': None,
    },
    'resolution': 1080,
    'statusBar': {
        'hpPercentage': None,
        'hp': None,
        'manaPercentage': None,
        'mana': None,
    },
    'targeting': {
        'enabled': False,
        'creatures': {},
        'canIgnoreCreatures': True,
        'hasIgnorableCreatures': False,
    },
    'tasksOrchestrator': TasksOrchestrator(),
    'screenshot': None,
    'way': None,
    'window': None
}
