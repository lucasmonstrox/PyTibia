from ..tasks.scrollToItem import ScrollToItemTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeScrollToItemTask(containerSlotImage, itemSlotImage):
    task = ScrollToItemTask(containerSlotImage, itemSlotImage)
    return ('scrollToItem', task)
