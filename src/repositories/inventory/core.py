from src.shared.typings import GrayImage
from src.utils.core import locate
from .config import images


# TODO: add unit tests
# TODO: add perf
def isBackpackOpen(screenshot: GrayImage, name: str) -> bool:
    backpackBarImage = images['containersBars'][name]
    backpackBarPos = locate(screenshot, backpackBarImage)
    isOpen = backpackBarPos is not None
    return isOpen


# TODO: add unit tests
# TODO: add perf
def isLockerOpen(screenshot: GrayImage) -> bool:
    lockerImage = images['containersBars']['locker']
    lockerPosition = locate(screenshot, lockerImage)
    isOpen = lockerPosition is not None
    return isOpen
