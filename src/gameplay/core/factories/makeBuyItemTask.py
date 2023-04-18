from ..tasks.buyItem import BuyItemTask


def makeBuyItemTask(itemWithQuantity):
    task = BuyItemTask(itemWithQuantity)
    return ('buyItem', task)
