import numpy as np
from time import sleep
import win32gui
from src.gameplay.utils import releaseKeys
from src.repositories.radar.core import getCoordinate
from src.repositories.radar.typings import Waypoint
from src.utils.core import getScreenshot


class GameContext:
    # TODO: add types
    def __init__(self, context):
        self.context = context

    def addWaypoint(self, waypoint):
        self.context['cavebot']['waypoints']['points'] = np.append(self.context['cavebot']['waypoints']['points'], np.array([waypoint], dtype=Waypoint))

    def focusInTibia(self):
        win32gui.ShowWindow(self.context['window'], 3)
        win32gui.SetForegroundWindow(self.context['window'])

    def play(self):
        self.focusInTibia()
        sleep(1)
        self.context['pause'] = False

    def pause(self):
        self.context['pause'] = True
        self.context['tasksOrchestrator'].reset()
        self.context = releaseKeys(self.context)

    def getCoordinate(self):
        screenshot = getScreenshot()
        coordinate = getCoordinate(screenshot, previousCoordinate=self.context['radar']['previousCoordinate'])
        return coordinate

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
