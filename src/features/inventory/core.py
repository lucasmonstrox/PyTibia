from src.utils.core import locate
from .config import images


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def isBackpackOpen(screenshot, name) -> bool:
    backpackBarImg = images['backpacks'][name]
    backpackBarPos = locate(screenshot, backpackBarImg)
    isOpen = backpackBarPos is not None
    return isOpen


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def isLockerOpen(screenshot) -> bool:
    lockerPosition = locate(screenshot, images['containersBars']['locker'])
    isOpen = lockerPosition is not None
    return isOpen
