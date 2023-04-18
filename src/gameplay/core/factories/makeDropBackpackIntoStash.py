from typing import Tuple
from ..tasks.dropBackpackIntoStash import DropBackpackIntoStashTask


# TODO: add unit tests
def makeDropBackpackIntoStashTask(backpack: str) -> Tuple[str, DropBackpackIntoStashTask]:
    task = DropBackpackIntoStashTask(backpack)
    return ('dropBackpackIntoStash', task)
