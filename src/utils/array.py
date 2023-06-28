from typing import List, TypeVar


def getNextArrayIndex(items: List[TypeVar['T']], currentIndex: int) -> int:
    return currentIndex + 1 if currentIndex < len(items) - 1 else 0
