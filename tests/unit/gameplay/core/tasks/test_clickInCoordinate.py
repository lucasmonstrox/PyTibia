from src.gameplay.core.tasks.clickInCoordinate import ClickInCoordinateTask


def test_should_test_default_params():
    waypoint = {}
    task = ClickInCoordinateTask(waypoint)
    assert task.name == 'clickInCoordinate'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 0.5
    assert task.waypoint == waypoint

def test_should_do(mocker):
    context = {
        'cavebot': {'targetCreature': None},
        'gameWindow': {'coordinate': (1, 2, 3)},
        'radar': {'coordinate': (4, 5, 6)},
    }
    waypoint = {'coordinate': (7, 8, 9)}
    slot = (0, 0)
    getSlotFromCoordinateSpy = mocker.patch('src.repositories.gameWindow.core.getSlotFromCoordinate', return_value=slot)
    clickSlotSpy = mocker.patch('src.repositories.gameWindow.slot.clickSlot')
    task = ClickInCoordinateTask(waypoint)
    assert task.do(context) == context
    getSlotFromCoordinateSpy.assert_called_once_with(context['radar']['coordinate'], waypoint['coordinate'])
    clickSlotSpy.assert_called_once_with(slot, context['gameWindow']['coordinate'])

def test_should_method_did_return_False_when_coordinates_are_different(mocker):
    context = {
        'cavebot': {'waypoints': {'state': {'checkInCoordinate': (1, 2, 3)}}},
        'radar': {'coordinate': (2, 2, 3)},
    }
    waypoint = {'coordinate': (7, 8, 9)}
    task = ClickInCoordinateTask(waypoint)
    coordinatesAreSameSpy = mocker.patch('src.gameplay.utils.coordinatesAreEqual', return_value=False)
    assert task.did(context) == False
    coordinatesAreSameSpy.assert_called_once_with(context['radar']['coordinate'], context['cavebot']['waypoints']['state']['checkInCoordinate'])

def test_should_method_did_return_True_when_coordinates_are_equal(mocker):
    context = {
        'cavebot': {'waypoints': {'state': {'checkInCoordinate': (1, 2, 3)}}},
        'radar': {'coordinate': (1, 2, 3)},
    }
    waypoint = {'coordinate': (7, 8, 9)}
    task = ClickInCoordinateTask(waypoint)
    coordinatesAreSameSpy = mocker.patch('src.gameplay.utils.coordinatesAreEqual', return_value=True)
    assert task.did(context) == True
    coordinatesAreSameSpy.assert_called_once_with(context['radar']['coordinate'], context['cavebot']['waypoints']['state']['checkInCoordinate'])
