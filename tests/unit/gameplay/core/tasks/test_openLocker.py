from src.gameplay.core.tasks.openLocker import OpenLockerTask


def test_should_test_default_params():
    task = OpenLockerTask()
    assert task.name == 'openLocker'
    assert task.delayAfterComplete == 1


def test_should_method_shouldIgnore_return_False_when_isContainerOpen_return_False(mocker):
    context = {'screenshot': []}
    task = OpenLockerTask()
    isContainerOpenSpy = mocker.patch(
        'src.repositories.inventory.core.isContainerOpen', return_value=False)
    assert task.shouldIgnore(context) == False
    isContainerOpenSpy.assert_called_once_with(context['screenshot'], 'locker')


def test_should_method_shouldIgnore_return_True_when_isContainerOpen_return_True(mocker):
    context = {'screenshot': []}
    task = OpenLockerTask()
    isContainerOpenSpy = mocker.patch(
        'src.repositories.inventory.core.isContainerOpen', return_value=True)
    assert task.shouldIgnore(context) == True
    isContainerOpenSpy.assert_called_once_with(context['screenshot'], 'locker')


def test_should_do(mocker):
    context = {
        'deposit': {'lockerCoordinate': [1, 2, 3]},
        'gameWindow': {'coordinate': [4, 5, 6]},
        'radar': {'coordinate': [7, 8, 9]}
    }
    task = OpenLockerTask()
    slot = (0, 0)
    getSlotFromCoordinateSpy = mocker.patch(
        'src.repositories.gameWindow.core.getSlotFromCoordinate', return_value=slot)
    rightClickSlotSpy = mocker.patch(
        'src.repositories.gameWindow.slot.rightClickSlot')
    assert task.do(context) == context
    getSlotFromCoordinateSpy.assert_called_once_with(
        context['radar']['coordinate'], context['deposit']['lockerCoordinate'])
    rightClickSlotSpy.assert_called_once_with(
        slot, context['gameWindow']['coordinate'])


def test_should_method_did_return_False_when_shouldIgnore_return_False(mocker):
    context = {'screenshot': []}
    task = OpenLockerTask()
    shouldIgnoreSpy = mocker.patch.object(
        task, 'shouldIgnore', return_value=False)
    assert task.did(context) == False
    shouldIgnoreSpy.assert_called_once_with(context)


def test_should_method_did_return_True_when_shouldIgnore_return_True(mocker):
    context = {'screenshot': []}
    task = OpenLockerTask()
    shouldIgnoreSpy = mocker.patch.object(
        task, 'shouldIgnore', return_value=True)
    assert task.did(context) == True
    shouldIgnoreSpy.assert_called_once_with(context)
