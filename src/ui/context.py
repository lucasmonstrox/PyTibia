from kivymd.toast import toast
import numpy as np
from time import sleep
import win32gui
from src.gameplay.typings import Context
from src.repositories.radar.core import getCoordinate
from src.repositories.radar.typings import Waypoint
from src.utils.core import getScreenshot


class GameContext:
    def __init__(self, context: Context):
        self.context = context

    def addWaypoint(self, waypoint):
        self.context['cavebot']['waypoints']['points'] = np.append(self.context['cavebot']['waypoints']['points'], np.array([waypoint], dtype=Waypoint))

    # TODO: se nao tiver nada de healing configurado, alertar
    def play(self) -> bool:
        if self.context['cavebot']['enabled'] and len(self.context['cavebot']['waypoints']['points']) <= 1:
            toast('Parece que não há waypoints configurados.')
            return False
        if self.context['window'] is None:
            toast('Parece que a window não foi encontrada.')
            return False
        win32gui.ShowWindow(self.context['window'], 3)
        win32gui.SetForegroundWindow(self.context['window'])
        sleep(1)
        self.context['pause'] = False
        return True

    def pause(self):
        if self.context['tasksOrchestrator'].getCurrentTaskName(self.context) != 'unknown':
            self.context['tasksOrchestrator'].setRootTask(None, self.context)
        sleep(1)
        self.context['pause'] = True

    def getCoordinate(self):
        screenshot = getScreenshot()
        coordinate = getCoordinate(screenshot)
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
