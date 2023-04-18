
from ..tasks.dragItems import DragItemsTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeDragItemsTask(container, item):
    task = DragItemsTask(container, item)
    return ('makeDragItems', task)
