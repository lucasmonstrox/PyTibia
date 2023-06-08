from src.gameplay.core.tasks.useHole import UseHoleTask


def test_should_test_default_params():
    task = UseHoleTask(('', 'walk', (0, 0, 0), {}))
    assert task.name == 'useHole'
    assert task.delayBeforeStart == 2
    assert task.delayAfterComplete == 2

def test_should_do(mocker):
    context = {
        'gameWindow': {'coordinate': (1, 2, 3)},
        'radar': {'coordinate': (4, 5, 6)},
    }
    waypoint = {'coordinate': (7, 8, 9)}
    task = UseHoleTask(waypoint)
    slot = (0, 0)
    getSlotFromCoordinateSpy = mocker.patch('src.repositories.gameWindow.core.getSlotFromCoordinate', return_value=slot)
    rightClickSlotSpy = mocker.patch('src.repositories.gameWindow.slot.rightClickSlot')
    assert task.do(context) == context
    getSlotFromCoordinateSpy.assert_called_once_with(context['radar']['coordinate'], waypoint['coordinate'])
    rightClickSlotSpy.assert_called_once_with(slot, context['gameWindow']['coordinate'])
