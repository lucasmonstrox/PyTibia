import pyautogui
from src.features.inventory.core import depotImage
from src.utils.core import locate
from .baseTask import BaseTask


class OpenDepotTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'openDepot'

    def do(self, context):
        depotPosition = locate(context['screenshot'], depotImage)
        pyautogui.rightClick(depotPosition[0] + 5, depotPosition[1] + 5)
        return context
    
    # TODO: check if depot is opened
    def did(self, context):
        return True
