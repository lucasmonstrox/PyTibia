import pyautogui
from time import time
import hud.core
import hud.slot


class UseShovelTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.delayOfTimeout = None
        self.name = 'useShovel'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, context):
        holeOpenImg = hud.core.images[context['resolution']]['holeOpen']
        isHoleOpen = hud.core.isHoleOpen(
            context['hudImg'], holeOpenImg, context['coordinate'], self.value['coordinate'])
        return isHoleOpen

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        pyautogui.press(context['hotkeys']['shovel'])
        hud.slot.clickSlot(slot, context['hud']['coordinate'])
        return context

    def did(self, context):
        holeOpenImg = hud.core.images[context['resolution']]['holeOpen']
        did = hud.core.isHoleOpen(
            context['hudImg'], holeOpenImg, context['coordinate'], self.value['coordinate'])
        return did

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        return context

    def onDidTimeout(self, context):
        return context
