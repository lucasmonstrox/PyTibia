
from ..tasks.dragItems import DragItemsTask


def makeDragItemsTask(container, item):
    task = DragItemsTask(container, item)
    return ('makeDragItems', task)
