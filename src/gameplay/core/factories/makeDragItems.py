from typing import Tuple
from src.shared.typings import GrayImage
from ..tasks.dragItems import DragItemsTask


# TODO: add unit tests
def makeDragItemsTask(containerImage: GrayImage, itemImage: GrayImage) -> Tuple[str, DragItemsTask]:
    task = DragItemsTask(containerImage, itemImage)
    return ('makeDragItems', task)
