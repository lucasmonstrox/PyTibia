from src.gameplay.core.tasks.openBackpack import OpenBackpackTask
from src.repositories.inventory.config import images


backpack = 'fur backpack'
context = {'screenshot': []}


def test_should_test_default_params():
    task = OpenBackpackTask(backpack)
    assert task.name == 'openBackpack'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 1
    assert task.backpack == backpack


def test_should_call_method_shouldIgnore_and_return_False_when_backpack_is_not_open(mocker):
    task = OpenBackpackTask(backpack)
    mocker.patch('src.repositories.inventory.core.isContainerOpen',
                 return_value=False)
    assert task.shouldIgnore(context) == False


def test_should_call_method_shouldIgnore_and_return_True_when_backpack_is_not_open(mocker):
    task = OpenBackpackTask(backpack)
    mocker.patch('src.repositories.inventory.core.isContainerOpen',
                 return_value=True)
    assert task.shouldIgnore(context) == True


def test_should_call_method_do_and_ignore_leftClick(mocker):
    task = OpenBackpackTask(backpack)
    locateSpy = mocker.patch('src.utils.core.locate', return_value=None)
    rightClickSpy = mocker.patch('src.utils.mouse.rightClick')
    assert task.do(context) == context
    locateSpy.assert_called_once_with(
        context['screenshot'], images['slots'][backpack], confidence=0.8)
    rightClickSpy.assert_not_called()


def test_should_call_method_do_and_call_rightClick(mocker):
    task = OpenBackpackTask(backpack)
    locateSpy = mocker.patch('src.utils.core.locate',
                             return_value=(0, 0, 0, 0))
    rightClickSpy = mocker.patch('src.utils.mouse.rightClick')
    assert task.do(context) == context
    locateSpy.assert_called_once_with(
        context['screenshot'], images['slots'][backpack], confidence=0.8)
    rightClickSpy.assert_called_once_with((5, 5))


def test_should_call_method_did_and_return_False_when_shouldIgnore_return_False(mocker):
    task = OpenBackpackTask(backpack)
    shouldIgnoreSpy = mocker.patch.object(
        task, 'shouldIgnore', return_value=False)
    assert task.did(context) == False
    shouldIgnoreSpy.assert_called_once_with(context)


def test_should_call_method_did_and_return_True_when_shouldIgnore_return_True(mocker):
    task = OpenBackpackTask(backpack)
    shouldIgnoreSpy = mocker.patch.object(
        task, 'shouldIgnore', return_value=True)
    assert task.did(context) == True
    shouldIgnoreSpy.assert_called_once_with(context)
