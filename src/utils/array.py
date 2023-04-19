from typing import List, TypeVar


# TODO: add unit tests
def getNextArrayIndex(items: List[TypeVar('T')], currentIndex: int) -> int:
    lengthOfItems = len(items)
    lastItemIndex = lengthOfItems - 1
    nextArrayIndex = currentIndex + 1 if currentIndex < lastItemIndex else 0
    return nextArrayIndex
