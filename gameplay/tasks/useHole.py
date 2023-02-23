import hud.core
import hud.slot
from .base.baseTask import BaseTask


class UseHoleTask(BaseTask):
    def __init__(self, value):
        super().__init__()
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'useHole'
        self.value = value

    def exec(self, context):
        slot = hud.core.getSlotFromCoordinate(
            context['coordinate'], self.value['coordinate'])
        hud.slot.rightClickSlot(slot, context['hud']['coordinate'])
        return context
    