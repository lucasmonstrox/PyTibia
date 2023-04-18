from ..tasks.dropEachFlask import DropEachFlaskTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeDropEachFlaskTask(backpack):
    task = DropEachFlaskTask(backpack)
    return ('dropEachFlask', task)
