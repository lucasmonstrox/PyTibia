import src.repositories.gameWindow.core as gameWindowCore
from src.gameplay.core.tasks.useShovel import UseShovelTask


waypoint = {'coordinate': (0, 0, 0)}


def test_should_test_default_params():
    task = UseShovelTask(waypoint)
    assert task.name == 'useShovel'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 0.5
    assert task.waypoint == waypoint


def test_should_method_shouldIgnore_return_False_when_hole_is_not_open(mocker):
    context = {
        'gameWindow': {'image': []},
        'resolution': 1080,
        'radar': {'coordinate': (4, 5, 6)},
    }
    task = UseShovelTask(waypoint)
    isHoleOpenSpy = mocker.patch(
        'src.repositories.gameWindow.core.isHoleOpen', return_value=False)
    assert task.shouldIgnore(context) == False
    isHoleOpenSpy.assert_called_once_with(context['gameWindow']['image'], gameWindowCore.images[context['resolution']]
                                          ['holeOpen'], context['radar']['coordinate'], waypoint['coordinate'])


def test_should_method_shouldIgnore_return_False_when_hole_is_open(mocker):
    context = {
        'gameWindow': {'image': []},
        'resolution': 1080,
        'radar': {'coordinate': (4, 5, 6)},
    }
    task = UseShovelTask(waypoint)
    isHoleOpenSpy = mocker.patch(
        'src.repositories.gameWindow.core.isHoleOpen', return_value=True)
    assert task.shouldIgnore(context) == True
    isHoleOpenSpy.assert_called_once_with(context['gameWindow']['image'], gameWindowCore.images[context['resolution']]
                                          ['holeOpen'], context['radar']['coordinate'], waypoint['coordinate'])


def test_should_do(mocker):
    context = {
        'gameWindow': {'coordinate': (4, 5, 6), 'image': []},
        'resolution': 1080,
        'radar': {'coordinate': (4, 5, 6)},
    }
    slot = (0, 0)
    task = UseShovelTask(waypoint)
    getSlotFromCoordinateSpy = mocker.patch(
        'src.repositories.gameWindow.core.getSlotFromCoordinate', return_value=slot)
    pressSpy = mocker.patch('src.utils.keyboard.press')
    clickSlotSpy = mocker.patch(
        'src.repositories.gameWindow.slot.clickSlot', return_value=True)
    assert task.do(context) == context
    getSlotFromCoordinateSpy.assert_called_once_with(
        context['radar']['coordinate'], waypoint['coordinate'])
    pressSpy.assert_called_once_with('p')
    clickSlotSpy.assert_called_once_with(
        slot, context['gameWindow']['coordinate'])


def test_should_method_did_return_False_when_shouldIgnore_return_False(mocker):
    context = {
        'gameWindow': {'image': []},
        'resolution': 1080,
        'radar': {'coordinate': (4, 5, 6)},
    }
    task = UseShovelTask(waypoint)
    shouldIgnoreSpy = mocker.patch.object(
        task, 'shouldIgnore', return_value=False)
    assert task.did(context) == False
    shouldIgnoreSpy.assert_called_once_with(context)


def test_should_method_did_return_True_when_shouldIgnore_return_True(mocker):
    context = {
        'gameWindow': {'image': []},
        'resolution': 1080,
        'radar': {'coordinate': (4, 5, 6)},
    }
    task = UseShovelTask(waypoint)
    shouldIgnoreSpy = mocker.patch.object(
        task, 'shouldIgnore', return_value=True)
    assert task.did(context) == True
    shouldIgnoreSpy.assert_called_once_with(context)
