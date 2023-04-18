import pyautogui
from src.utils.core import locate
from .baseTask import BaseTask


# TODO: check if container bar is hide
class CloseContainerTask(BaseTask):
    def __init__(self, containerBarImage):
        super().__init__()
        self.delayAfterComplete = 1
        self.name = 'closeContainer'
        self.value = containerBarImage

    # TODO: add unit tests
    # TODO: add perf
    # TODO: add typings
    def do(self, context):
        containerPosition = locate(context['screenshot'], self.value, confidence=0.8)
        x, y = containerPosition[0] + 165, containerPosition[1] + 5
        pyautogui.click(x, y)
        return context
