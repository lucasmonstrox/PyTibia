from typing import Tuple
from src.shared.typings import GrayImage
from ..tasks.scrollToItem import ScrollToItemTask


# TODO: add unit tests
def makeScrollToItemTask(containerSlotImage: GrayImage, itemSlotImage: GrayImage) -> Tuple[str, ScrollToItemTask]:
    task = ScrollToItemTask(containerSlotImage, itemSlotImage)
    return ('scrollToItem', task)
