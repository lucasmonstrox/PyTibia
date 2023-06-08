from src.gameplay.core.tasks.buyItem import BuyItemTask


itemName = 'mana potion'
context = {'screenshot': []}

def test_should_test_default_params():
    itemQuantity = 1
    task = BuyItemTask(itemName, itemQuantity)
    assert task.name == 'buyItem'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 1
    assert task.itemName == itemName
    assert task.itemQuantity == itemQuantity

def test_should_method_shouldIgnore_return_False_when_itemQuantity_is_greater_than_0():
    itemQuantity = 1
    task = BuyItemTask(itemName, itemQuantity)
    assert task.shouldIgnore(context) == False

def test_should_method_shouldIgnore_return_True_when_itemQuantity_is_equal_0():
    itemQuantity = 0
    task = BuyItemTask(itemName, itemQuantity)
    assert task.shouldIgnore(context) == True

def test_should_do(mocker):
    itemQuantity = 1
    task = BuyItemTask(itemName, itemQuantity)
    buyItemSpy = mocker.patch('src.repositories.refill.core.buyItem')
    assert task.do(context) == context
    buyItemSpy.assert_called_once_with(context['screenshot'], itemName, itemQuantity)
