from gameplay.tasks.openBackpack import OpenBackpackTask


def makeOpenBackpackTask(backpack):
    task = OpenBackpackTask(backpack)
    return ('openBackpack', task)
