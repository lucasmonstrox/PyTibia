from os.path import exists
from tinydb import Query, TinyDB
from src.gameplay.core.load import loadContextFromConfig


class Context:
    filePath: str = 'file.json'

    def __init__(self, context):
        shouldInsertProfile = not exists(self.filePath)
        self.db = TinyDB(self.filePath)
        if shouldInsertProfile:
            self.insertProfile()
        self.enabledProfile = self.getEnabledProfile()
        self.context = loadContextFromConfig(
            self.enabledProfile['config'], context)

    def updateMainBackpack(self, backpack: str):
        self.context['backpacks']['main'] = backpack
        self.enabledProfile['config']['backpacks']['main'] = backpack
        self.db.update(self.enabledProfile)

    def insertProfile(self):
        self.db.insert({
            'enabled': True,
            'config': {
                'backpacks': {
                    'main': None,
                    'loot': None
                },
                'cavebot': {
                    'enabled': False,
                    'waypoints': {
                        'items': []
                    }
                },
                'comboSpells': {
                    'enabled': False,
                    'items': []
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
                'hotkeys': {}
            }
        })

    def getEnabledProfile(self):
        return self.db.search(Query().enabled == True)[0]

    def updateLootBackpack(self, backpack: str):
        self.context['backpacks']['loot'] = backpack
        self.enabledProfile['config']['backpacks']['loot'] = backpack
        self.db.update(self.enabledProfile)

    def addWaypoint(self, waypoint):
        self.context['cavebot']['waypoints']['items'].append(waypoint)
        self.enabledProfile['config']['cavebot']['waypoints']['items'].append(
            waypoint)
        self.db.update(self.enabledProfile)

    def updateWaypointByIndex(self, waypointIndex, options):
        self.context['cavebot']['waypoints']['items'][waypointIndex]['options'] = options
        self.enabledProfile['config']['cavebot']['waypoints']['items'][waypointIndex]['options'] = options
        self.db.update(self.enabledProfile)

    def removeWaypointByIndex(self, index):
        self.context['cavebot']['waypoints']['items'].pop(index)
        self.enabledProfile['config']['cavebot']['waypoints']['items'].pop(
            index)
        self.db.update(self.enabledProfile)

    def focusInTibia(self):
        pass
        # win32gui.ShowWindow(self.context['window'], 3)
        # win32gui.SetForegroundWindow(self.context['window'])

    def play(self):
        self.focusInTibia()
        # sleep(1)
        self.context['pause'] = False

    def pause(self):
        self.context['pause'] = True
        self.context['tasksOrchestrator'].setRootTask(None, self.context)
        # self.context = releaseKeys(self.context)

    # def getCoordinate(self):
    #     screenshot = getScreenshot()
    #     coordinate = getCoordinate(
    #         screenshot, previousCoordinate=self.context['radar']['previousCoordinate'])
    #     return coordinate

    def toggleHealingPotionsByKey(self, healthPotionType, enabled):
        self.context['healing']['potions'][healthPotionType]['enabled'] = enabled

    def setHealthPotionHotkeyByKey(self, healthPotionType, hotkey):
        self.context['healing']['potions'][healthPotionType]['hotkey'] = hotkey

    def setHealthPotionHpPercentageLessThanOrEqual(self, healthPotionType, hpPercentage):
        self.context['healing']['potions'][healthPotionType]['hpPercentageLessThanOrEqual'] = hpPercentage

    def toggleManaPotionsByKey(self, manaPotionType, enabled):
        self.context['healing']['potions'][manaPotionType]['enabled'] = enabled

    def setManaPotionManaPercentageLessThanOrEqual(self, manaPotionType, manaPercentage):
        self.context['healing']['potions'][manaPotionType]['manaPercentageLessThanOrEqual'] = manaPercentage

    def toggleHealingSpellsByKey(self, contextKey, enabled):
        self.context['healing']['spells'][contextKey]['enabled'] = enabled

    def setHealingSpellsHpPercentage(self, contextKey, hpPercentage):
        self.context['healing']['spells'][contextKey]['hpPercentageLessThanOrEqual'] = hpPercentage

    def setHealingSpellsHotkey(self, contextKey, hotkey):
        self.context['healing']['spells'][contextKey]['hotkey'] = hotkey
