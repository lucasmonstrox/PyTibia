from src.gameplay.core.tasks.useRope import UseRopeTask


def test_should_test_default_params():
    waypoint = ('', 'walk', (0, 0, 0), {})
    task = UseRopeTask(waypoint)
    assert task.name == 'useRope'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 1
    assert task.waypoint == waypoint


def test_should_do(mocker):
    context = {
        'gameWindow': {'coordinate': (1, 2, 3)},
        'radar': {'coordinate': (4, 5, 6)},
    }
    waypoint = {'coordinate': (7, 8, 9)}
    task = UseRopeTask(waypoint)
    slot = (0, 0)
    getSlotFromCoordinateSpy = mocker.patch(
        'src.repositories.gameWindow.core.getSlotFromCoordinate', return_value=slot)
    clickSlotSpy = mocker.patch('src.repositories.gameWindow.slot.clickSlot')
    pressSpy = mocker.patch('src.utils.keyboard.press')
    assert task.do(context) == context
    getSlotFromCoordinateSpy.assert_called_once_with(
        context['radar']['coordinate'], waypoint['coordinate'])
    clickSlotSpy.assert_called_once_with(
        slot, context['gameWindow']['coordinate'])
    pressSpy.assert_called_once_with('o')
