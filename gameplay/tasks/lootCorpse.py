import numpy as np
import pyautogui
import hud.core
import hud.slot
from .baseTask import BaseTask


class LootCorpseTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 0.25
        self.delayAfterComplete = 0.25
        self.name = 'lootCorpse'
        self.value = value

    def do(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        pyautogui.keyDown('shift')
        hud.slot.rightClickSlot(slot, context['hud']['coordinate'])
        pyautogui.keyUp('shift')
        return context
    
    def onDidComplete(self, context):
        context['corpsesToLoot'] = np.delete(context['corpsesToLoot'], 0)
        return context
