from os.path import exists
import time
from tinydb import Query, TinyDB
from tkinter import messagebox
from src.gameplay.core.load import loadContextFromConfig
from src.repositories.chat.core import getTabs
from src.utils.core import getScreenshot


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
                    'highPriority': {
                        'healthFood': {
                            'enabled': False,
                            'hotkey': '3',
                            'hpPercentageLessThanOrEqual': 0,
                        },
                        'manaFood': {
                            'enabled': False,
                            'hotkey': '4',
                            'manaPercentageLessThanOrEqual': 0,
                        },
                        'swapRing': {
                            'enabled': False,
                            'firstRing': {
                                'hotkey': 'f11',
                                'hpPercentageLessThanOrEqual': 0
                            },
                            'secondRing': {
                                'hotkey': 'f12',
                                'hpPercentageGreaterThanOrEqual': 0
                            },
                            'ringAlwaysEquipped': ''
                        },
                        'swapAmulet': {
                            'enabled': False,
                            'firstAmulet': {
                                'hotkey': 'u',
                                'hpPercentageLessThanOrEqual': 0
                            },
                            'secondAmulet': {
                                'hotkey': 'i',
                                'hpPercentageGreaterThanOrEqual': 0
                            },
                            'amuletAlwaysEquipped': ''
                        }
                    },
                    'potions': {
                        'firstHealthPotion': {
                            'enabled': False,
                            'hotkey': '1',
                            'hpPercentageLessThanOrEqual': 0,
                            'manaPercentageGreaterThanOrEqual': 0,
                        },
                        'firstManaPotion': {
                            'enabled': False,
                            'hotkey': '2',
                            'manaPercentageLessThanOrEqual': 0,
                        },
                    },
                    'spells': {
                        'criticalHealing': {
                            'enabled': False,
                            'hotkey': '5',
                            'hpPercentageLessThanOrEqual': 0,
                            'manaPercentageGreaterThanOrEqual': 0,
                            'spell': None
                        },
                        'lightHealing': {
                            'enabled': False,
                            'hotkey': '7',
                            'hpPercentageLessThanOrEqual': 0,
                            'manaPercentageGreaterThanOrEqual': 0,
                            'spell': None
                        },
                        'utura': {
                            'enabled': False,
                            'hotkey': '8',
                            'hpPercentageLessThanOrEqual': 0,
                            'manaPercentageGreaterThanOrEqual': 0,
                            'spell': None
                        },
                        'uturaGran': {
                            'enabled': False,
                            'hotkey': '9',
                            'hpPercentageLessThanOrEqual': 0,
                            'manaPercentageGreaterThanOrEqual': 0,
                            'spell': None
                        },
                    },
                    'eatFood': {
                        'enabled': False,
                        'hotkey': '0',
                        'eatWhenFoodIslessOrEqual': 0,
                    }
                },
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

    def getAllWaypointLabels(self):
        waypointsLabels = [waypointItem['label'] for waypointItem in self.context['cavebot']
                           ['waypoints']['items'] if waypointItem['label'] != '']
        return waypointsLabels

    def hasWaypointWithLabel(self, label: str, ignoreLabel=None) -> bool:
        for waypoint in self.context['cavebot']['waypoints']['points']:
            if waypoint['label'] == label and ignoreLabel is not None:
                return True
        return False

    def updateWaypointByIndex(self, waypointIndex, label=None, options={}):
        if label is not None:
            self.context['cavebot']['waypoints']['items'][waypointIndex]['label'] = label
            self.enabledProfile['config']['cavebot']['waypoints']['items'][waypointIndex]['label'] = label
        self.context['cavebot']['waypoints']['items'][waypointIndex]['options'] = options
        self.enabledProfile['config']['cavebot']['waypoints']['items'][waypointIndex]['options'] = options
        self.db.update(self.enabledProfile)

    def removeWaypointByIndex(self, index):
        self.context['cavebot']['waypoints']['items'].pop(index)
        self.enabledProfile['config']['cavebot']['waypoints']['items'].pop(
            index)
        self.db.update(self.enabledProfile)

    def play(self):
        if self.context['window'] is None:
            messagebox.showerror(
                'Erro', 'Tibia window is not set!')
            return
        self.context['window'].activate()
        time.sleep(1)
        screenshot = getScreenshot()
        # chatTabs = getTabs(screenshot)
        # if 'loot' not in chatTabs:
        #     messagebox.showerror(
        #         'Erro', 'Loot tab must be open!')
        #     return
        self.context['pause'] = False

    def pause(self):
        self.context['pause'] = True
        self.context['tasksOrchestrator'].setRootTask(self.context, None)

    def toggleHealingPotionsByKey(self, healthPotionType, enabled):
        self.context['healing']['potions'][healthPotionType]['enabled'] = enabled
        self.enabledProfile['config']['healing']['potions'][healthPotionType]['enabled'] = enabled
        self.db.update(self.enabledProfile)

    def toggleHealingHighPriorityByKey(self, key, enabled):
        self.context['healing']['highPriority'][key]['enabled'] = enabled
        self.enabledProfile['config']['healing']['highPriority'][key]['enabled'] = enabled
        self.db.update(self.enabledProfile)

    def setHealthFoodHpPercentageLessThanOrEqual(self, hpPercentageLessThanOrEqual):
        self.context['healing']['highPriority']['healthFood']['hpPercentageLessThanOrEqual'] = hpPercentageLessThanOrEqual
        self.enabledProfile['config']['healing']['highPriority']['healthFood'][
            'hpPercentageLessThanOrEqual'] = hpPercentageLessThanOrEqual
        self.db.update(self.enabledProfile)

    def setManaFoodHpPercentageLessThanOrEqual(self, manaPercentageLessThanOrEqual):
        self.context['healing']['highPriority']['manaFood']['manaPercentageLessThanOrEqual'] = manaPercentageLessThanOrEqual
        self.enabledProfile['config']['healing']['highPriority']['manaFood'][
            'manaPercentageLessThanOrEqual'] = manaPercentageLessThanOrEqual
        self.db.update(self.enabledProfile)

    def toggleSpellByKey(self, healthPotionType, enabled):
        self.context['healing']['spells'][healthPotionType]['enabled'] = enabled
        self.enabledProfile['config']['healing']['spells'][healthPotionType]['enabled'] = enabled
        self.db.update(self.enabledProfile)

    def setHealthPotionHotkeyByKey(self, healthPotionType, hotkey):
        self.context['healing']['potions'][healthPotionType]['hotkey'] = hotkey
        self.enabledProfile['config']['healing']['potions'][healthPotionType]['hotkey'] = hotkey
        self.db.update(self.enabledProfile)

    def setSpellHotkeyByKey(self, healthPotionType, hotkey):
        self.context['healing']['spells'][healthPotionType]['hotkey'] = hotkey
        self.enabledProfile['config']['healing']['spells'][healthPotionType]['hotkey'] = hotkey
        self.db.update(self.enabledProfile)

    def setHealthPotionHpPercentageLessThanOrEqual(self, healthPotionType, hpPercentage):
        self.context['healing']['potions'][healthPotionType]['hpPercentageLessThanOrEqual'] = hpPercentage
        self.enabledProfile['config']['healing']['potions'][healthPotionType]['hpPercentageLessThanOrEqual'] = hpPercentage
        self.db.update(self.enabledProfile)

    def setSpellHpPercentageLessThanOrEqual(self, spellType, hpPercentage):
        self.context['healing']['spells'][spellType]['hpPercentageLessThanOrEqual'] = hpPercentage
        self.enabledProfile['config']['healing']['spells'][spellType]['hpPercentageLessThanOrEqual'] = hpPercentage
        self.db.update(self.enabledProfile)

    def setSpellManaPercentageGreaterThanOrEqual(self, spellType, hpPercentage):
        self.context['healing']['spells'][spellType]['manaPercentageGreaterThanOrEqual'] = hpPercentage
        self.enabledProfile['config']['healing']['spells'][spellType]['manaPercentageGreaterThanOrEqual'] = hpPercentage
        self.db.update(self.enabledProfile)

    def setSpellName(self, spellType, spell):
        self.context['healing']['spells'][spellType]['spell'] = spell
        self.enabledProfile['config']['healing']['spells'][spellType]['spell'] = spell
        self.db.update(self.enabledProfile)

    def setHealthPotionManaPercentageGreaterThanOrEqual(self, healthPotionType, hpPercentage):
        self.context['healing']['potions'][healthPotionType]['manaPercentageGreaterThanOrEqual'] = hpPercentage
        self.enabledProfile['config']['healing']['potions'][healthPotionType]['manaPercentageGreaterThanOrEqual'] = hpPercentage
        self.db.update(self.enabledProfile)

    def setHealthPotionManaPercentageLessThanOrEqual(self, healthPotionType, hpPercentage):
        self.context['healing']['potions'][healthPotionType]['manaPercentageLessThanOrEqual'] = hpPercentage
        self.enabledProfile['config']['healing']['potions'][healthPotionType]['manaPercentageLessThanOrEqual'] = hpPercentage
        self.db.update(self.enabledProfile)

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
