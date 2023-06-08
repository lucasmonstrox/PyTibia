from typing import Union
from src.shared.typings import BBox, GrayImage
from src.utils.core import locate
from src.utils.mouse import moveTo, scroll
from ...typings import Context
from .common.base import BaseTask


class ScrollToItemTask(BaseTask):
    def __init__(self, containerImage: GrayImage, itemImage: GrayImage):
        super().__init__()
        self.name = 'scrollToItem'
        self.terminable = False
        self.containerImage = containerImage
        self.itemImage = itemImage

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        shouldIgnoreTask = self.getItemPosition(context['screenshot']) is not None
        return shouldIgnoreTask

    # TODO: add unit tests
    def do(self, context: Context) -> Context:
        containerPosition = locate(context['screenshot'], self.containerImage, confidence=0.8)
        moveTo((containerPosition[0] + 10, containerPosition[1] + 15))
        scroll(-10)
        return context

    # TODO: add unit tests
    def ping(self, context: Context) -> Context:
        itemPosition = self.getItemPosition(context['screenshot'])
        if itemPosition is not None:
            self.terminable = True
        return context

    # TODO: add unit tests
    def getItemPosition(self, screenshot: GrayImage) -> Union[BBox, None]:
        return locate(screenshot, self.itemImage, confidence=0.8)
