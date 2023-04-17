def getNextArrayIndex(items, currentIndex):
    lengthOfItems = len(items)
    lastItemIndex = lengthOfItems - 1
    nextArrayIndex = currentIndex + 1 if currentIndex < lastItemIndex else 0
    return nextArrayIndex
