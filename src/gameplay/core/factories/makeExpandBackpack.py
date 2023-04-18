from ..tasks.expandBackpack import ExpandBackpackTask


def makeExpandBackpackTask(backpack):
    task = ExpandBackpackTask(backpack)
    return ('expandBackpack', task)


