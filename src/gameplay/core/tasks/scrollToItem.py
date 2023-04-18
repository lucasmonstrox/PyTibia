import pyautogui
from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import locate
from ...typings import Context
from .baseTask import BaseTask


class ScrollToItemTask(BaseTask):
    def __init__(self, containerImage, itemImage):
        super().__init__()
        self.name = 'scrollToItem'
        self.terminable = False
        self.value = (containerImage, itemImage)
        self.itemPosition = None

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        itemPosition = self.getItemPosition(context['screenshot'])
        isItemVisible = itemPosition is not None
        return isItemVisible

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        containerPosition = locate(context['screenshot'], self.value[0], confidence=0.8)
        x = containerPosition[0] + 10
        y = containerPosition[1] + 15
        pyautogui.moveTo(x, y)
        pyautogui.scroll(-10)
        return context

    # TODO: add unit tests
    def ping(self, context: Context) -> Context:
        itemPosition = self.getItemPosition(context['screenshot'])
        isItemVisible = itemPosition is not None
        if isItemVisible:
            self.terminable = True
        return context

    # TODO: add unit tests
    def getItemPosition(self, screenshot: GrayImage) -> Union[BBox, None]:
        return locate(screenshot, self.value[1], confidence=0.8)
