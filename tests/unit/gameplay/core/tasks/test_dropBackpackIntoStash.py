from src.gameplay.core.tasks.dropBackpackIntoStash import DropBackpackIntoStashTask
from src.repositories.inventory.core import images


backpack = 'Beach Backpack'


def test_should_test_default_params():
    task = DropBackpackIntoStashTask(backpack)
    assert task.name == 'dropBackpackIntoStash'
    assert task.delayAfterComplete == 1
    assert task.backpack == backpack


def test_should_do(mocker):
    context = {'screenshot': []}
    locateSpy = mocker.patch('src.utils.core.locate',
                             return_value=(0, 0, 0, 0))
    dragSpy = mocker.patch('src.utils.mouse.drag')
    task = DropBackpackIntoStashTask(backpack)
    assert task.do(context) == context
    assert locateSpy.call_count == 2
    locateSpy.assert_has_calls([
        mocker.call(context['screenshot'], images['slots']
                    [backpack], confidence=0.8),
        mocker.call(context['screenshot'], images['slots']['stash'])
    ])
    dragSpy.assert_called_once_with((0, 0), (0, 0))
