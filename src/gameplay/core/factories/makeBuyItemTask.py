from typing import Tuple
from ..tasks.buyItem import BuyItemTask


# TODO: add unit tests
def makeBuyItemTask(itemWithQuantity: Tuple[str, int]) -> Tuple[str, BuyItemTask]:
    task = BuyItemTask(itemWithQuantity)
    return ('buyItem', task)
