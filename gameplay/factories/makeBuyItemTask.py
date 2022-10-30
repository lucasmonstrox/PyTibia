from gameplay.tasks.buyItem import BuyItemTask


def makeBuyItemTask(phrase):
    task = BuyItemTask(phrase)
    return ('say', task)
