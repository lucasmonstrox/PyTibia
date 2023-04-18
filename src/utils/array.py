# TODO: add unit tests
# TODO: add typings
def getNextArrayIndex(items, currentIndex: int) -> int:
    lengthOfItems = len(items)
    lastItemIndex = lengthOfItems - 1
    nextArrayIndex = currentIndex + 1 if currentIndex < lastItemIndex else 0
    return nextArrayIndex
