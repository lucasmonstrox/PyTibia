from gameplay.tasks.depositItems import DepositItemsTask


def makeDepositItemsTask(phrase):
    task = DepositItemsTask(phrase)
    return ('depositItems', task)
