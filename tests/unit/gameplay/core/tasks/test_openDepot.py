from src.gameplay.core.tasks.openDepot import OpenDepotTask
from src.repositories.inventory.core import images


def test_should_test_default_params():
    task = OpenDepotTask()
    assert task.name == 'openDepot'
    assert task.delayAfterComplete == 1
    assert task.delayBeforeStart == 1


def test_should_do(mocker):
    context = {'screenshot': []}
    task = OpenDepotTask()
    depotPosition = (0, 0, 0, 0)
    locateSpy = mocker.patch('src.utils.core.locate', return_value=(0, 0, 0, 0))
    rightClickSpy = mocker.patch('src.utils.mouse.rightClick')
    assert task.do(context) == context
    locateSpy.assert_called_once_with(context['screenshot'], images['slots']['depot'])
    rightClickSpy.assert_called_once_with((depotPosition[0] + 5, depotPosition[1] + 5))
