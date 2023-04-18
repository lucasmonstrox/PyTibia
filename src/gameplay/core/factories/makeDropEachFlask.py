from typing import Tuple
from ..tasks.dropEachFlask import DropEachFlaskTask


# TODO: add unit tests
def makeDropEachFlaskTask(backpack: str) -> Tuple[str, DropEachFlaskTask]:
    task = DropEachFlaskTask(backpack)
    return ('dropEachFlask', task)
