from src.shared.typings import GrayImage
from src.utils.core import locate
from src.utils.mouse import leftClick
from ...typings import Context
from .common.base import BaseTask
import pyautogui

# TODO: check if container bar is hide
class CloseContainerTask(BaseTask):
    def __init__(self, containerBarImage: GrayImage):
        super().__init__()
        self.name = 'closeContainer'
        self.delayAfterComplete = 1
        self.containerBarImage = containerBarImage

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        containerPosition = locate(
            context['screenshot'], self.containerBarImage, confidence=0.8)
        currentMouseCoordinate = pyautogui.position()
        if containerPosition is not None:
            leftClick((containerPosition[0] + 165, containerPosition[1] + 5))
        pyautogui.moveTo(currentMouseCoordinate)
        return context
