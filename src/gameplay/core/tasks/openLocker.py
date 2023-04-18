from src.features.gameWindow.core import getSlotFromCoordinate
from src.features.gameWindow.slot import rightClickSlot
from src.features.inventory.core import isLockerOpen
from .baseTask import BaseTask


class OpenLockerTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayAfterComplete = 1
        self.name = 'openLockerTask'
    
    def shouldIgnore(self, context):
        return isLockerOpen(context['screenshot'])
    
    def do(self, context):
        lockerCoordinate = context['deposit']['lockerCoordinate']
        slot = getSlotFromCoordinate(context['radar']['coordinate'], lockerCoordinate)
        rightClickSlot(slot, context['gameWindow']['coordinate'])
        return context
    
    def did(self, context):
        return isLockerOpen(context['screenshot'])
