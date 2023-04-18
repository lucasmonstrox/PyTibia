from ..tasks.openBackpack import OpenBackpackTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeOpenBackpackTask(backpack):
    task = OpenBackpackTask(backpack)
    return ('openBackpack', task)
