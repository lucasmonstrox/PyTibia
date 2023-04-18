from ..tasks.buyItem import BuyItemTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeBuyItemTask(itemWithQuantity):
    task = BuyItemTask(itemWithQuantity)
    return ('buyItem', task)
