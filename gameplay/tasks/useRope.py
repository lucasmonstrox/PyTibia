import pyautogui
from time import time
import hud.core
import hud.slot


class UseRopeTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.delayOfTimeout = None
        self.name = 'useRope'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        # TODO: replace by correct bindings
        pyautogui.press('f8')
        hud.slot.clickSlot(slot, context['hudCoordinate'])
        return context

    def did(self, _):
        # TODO: check if char is in upper coordinate
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
