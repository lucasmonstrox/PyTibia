from ..tasks.expandBackpack import ExpandBackpackTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeExpandBackpackTask(backpack):
    task = ExpandBackpackTask(backpack)
    return ('expandBackpack', task)
