from ..tasks.scrollToItem import ScrollToItemTask


def makeScrollToItemTask(containerSlotImage, itemSlotImage):
    task = ScrollToItemTask(containerSlotImage, itemSlotImage)
    return ('scrollToItem', task)
