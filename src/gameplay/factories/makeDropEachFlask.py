from ..tasks.dropEachFlask import DropEachFlaskTask


def makeDropEachFlaskTask(backpack):
    task = DropEachFlaskTask(backpack)
    return ('dropEachFlask', task)
