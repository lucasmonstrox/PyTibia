from src.gameplay.core.tasks.orchestrator import TasksOrchestrator


context = {
    'backpacks': {
        'main': '',
        'loot': '',
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
        'lastUsedSpellAt': None,
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
            'swapRing': {
                'enabled': False,
                'tankRing': {
                    'hotkey': None,
                    'hpPercentageLessThanOrEqual': 0
                },
                'mainRing': {
                    'hotkey': None,
                    'hpPercentageGreaterThanOrEqual': 0
                },
                'ringAlwaysEquipped': ''
            },
            'swapAmulet': {
                'enabled': False,
                'tankAmulet': {
                    'hotkey': None,
                    'hpPercentageLessThanOrEqual': 0
                },
                'mainAmulet': {
                    'hotkey': None,
                    'hpPercentageGreaterThan': 0
                },
                'amuletAlwaysEquipped': ''
            }
        },
        'potions': {
            'firstHealthPotion': {
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
                'spell': {
                    'name': 'utura',
                    'manaNeeded': '75'
                }
            },
            'uturaGran': {
                'enabled': False,
                'hotkey': None,
                'spell': {
                    'name': 'utura gran',
                    'manaNeeded': '165'
                }
            },
        },
        'eatFood': {
            'enabled': False,
            'hotkey': '',
            'eatWhenFoodIslessOrEqual': 0,
        }
    },
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
