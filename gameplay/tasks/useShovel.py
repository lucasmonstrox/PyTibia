import pyautogui
from time import time
import hud.core
import hud.slot


class UseShovelTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.name = 'useShovel'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, context):
        isHoleOpen = hud.core.isHoleOpen(
            context['hudImg'], context['radarCoordinate'], self.value['coordinate'])
        return isHoleOpen

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['radarCoordinate'], self.value['coordinate'])
        # TODO: replace by correct binds
        pyautogui.press('f9')
        hud.slot.clickSlot(slot, context['hudCoordinate'])
        return context

    def did(self, _):
        # TODO: check if char is in upper coordinate
        return True

    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        return context

    def onDidComplete(self, context):
        return context
