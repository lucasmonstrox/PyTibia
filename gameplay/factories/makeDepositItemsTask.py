from gameplay.tasks.depositItems import DepositItemsTask


def makeDepositItemsTask():
    task = DepositItemsTask()
    return ('depositItems', task)
