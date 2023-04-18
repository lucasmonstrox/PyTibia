from typing import Tuple
from ..tasks.refillChecker import RefillCheckerTask


# TODO: add unit tests
def makeRefillCheckerTask(phrase: str) -> Tuple[str, RefillCheckerTask]:
    task = RefillCheckerTask(phrase)
    return ('refillChecker', task)
