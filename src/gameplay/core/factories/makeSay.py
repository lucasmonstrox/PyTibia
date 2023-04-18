from typing import Tuple
from ..tasks.say import SayTask


# TODO: add unit tests
def makeSayTask(phrase: str) -> Tuple[str, SayTask]:
    task = SayTask(phrase)
    return ('say', task)
