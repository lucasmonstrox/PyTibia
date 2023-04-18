# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def getNextArrayIndex(items, currentIndex):
    lengthOfItems = len(items)
    lastItemIndex = lengthOfItems - 1
    nextArrayIndex = currentIndex + 1 if currentIndex < lastItemIndex else 0
    return nextArrayIndex
