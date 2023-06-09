from src.gameplay.core.tasks.walkToCoordinate import WalkToCoordinateTask


context = {'radar': {'coordinate': (1, 2, 3)}}
coordinate = (4, 5, 6)

def test_should_test_default_params():
    task = WalkToCoordinateTask(coordinate)
    assert task.name == 'walkToCoordinate'
    assert task.coordinate == coordinate

def test_should_method_onBeforeStart_call_calculateWalkpoint(mocker):
    task = WalkToCoordinateTask(coordinate)
    calculateWalkpointSpy = mocker.patch.object(task, 'calculateWalkpoint')
    assert task.onBeforeStart(context) == context
    calculateWalkpointSpy.assert_called_once_with(context)

def test_should_method_onBeforeRestart_call_onBeforeStart(mocker):
    task = WalkToCoordinateTask(coordinate)
    onBeforeStartSpy = mocker.patch.object(task, 'onBeforeStart', return_value=context)
    assert task.onBeforeRestart(context) == context
    onBeforeStartSpy.assert_called_once_with(context)

def test_should_method_onComplete_call_releaseKeys(mocker):
    task = WalkToCoordinateTask(coordinate)
    releaseKeysSpy = mocker.patch('src.gameplay.utils.releaseKeys', return_value=context)
    assert task.onComplete(context) == context
    releaseKeysSpy.assert_called_once_with(context)

def test_should_call_onComplete(mocker):
    task = WalkToCoordinateTask(coordinate)
    releaseKeysSpy = mocker.patch('src.gameplay.utils.releaseKeys', return_value=context)
    assert task.onComplete(context) == context
    releaseKeysSpy.assert_called_once_with(context)

def test_should_method_onInterrupt_call_releaseKeys(mocker):
    task = WalkToCoordinateTask(coordinate)
    releaseKeysSpy = mocker.patch('src.gameplay.utils.releaseKeys', return_value=context)
    assert task.onInterrupt(context) == context
    releaseKeysSpy.assert_called_once_with(context)

def test_should_method_shouldRestartAfterAllChildrensComplete_return_True_when_there_are_no_tasks(mocker):
    task = WalkToCoordinateTask(coordinate)
    coordinatesAreEqualSpy = mocker.patch('src.gameplay.utils.coordinatesAreEqual')
    assert task.shouldRestartAfterAllChildrensComplete(context) == True
    coordinatesAreEqualSpy.assert_not_called()

def test_should_method_shouldRestartAfterAllChildrensComplete_return_True_when_coordinates_are_different(mocker):
    task = WalkToCoordinateTask(coordinate)
    task.tasks = [1]
    coordinatesAreEqualSpy = mocker.patch('src.gameplay.utils.coordinatesAreEqual', return_value=False)
    assert task.shouldRestartAfterAllChildrensComplete(context) == True
    coordinatesAreEqualSpy.assert_called_once_with(context['radar']['coordinate'], coordinate)

def test_should_method_shouldRestartAfterAllChildrensComplete_return_False_when_coordinates_are_equal(mocker):
    task = WalkToCoordinateTask(coordinate)
    task.tasks = [1]
    coordinatesAreEqualSpy = mocker.patch('src.gameplay.utils.coordinatesAreEqual', return_value=True)
    assert task.shouldRestartAfterAllChildrensComplete(context) == False
    coordinatesAreEqualSpy.assert_called_once_with(context['radar']['coordinate'], coordinate)
