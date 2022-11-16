import numpy as np
import pyautogui
from time import time
import hud.core
import hud.slot


class LootCorpseTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.finishedAt = None
        self.delayBeforeStart = 0.25
        self.delayAfterComplete = 0.25
        self.delayOfTimeout = None
        self.name = 'lootCorpse'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, _):
        return False

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        pyautogui.keyDown('shift')
        hud.slot.rightClickSlot(slot, context['hud']['coordinate'])
        pyautogui.keyUp('shift')
        return context

    def did(self, _):
        # TODO: verificar se apareceu a msg de bicho lootead
        return True

    def shouldRestart(self, _):
        return False

    def onIgnored(self, context):
        return context

    def onDidComplete(self, context):
        context['corpsesToLoot'] = np.delete(context['corpsesToLoot'], 0)
        return context

    def onDidTimeout(self, context):
        return context
