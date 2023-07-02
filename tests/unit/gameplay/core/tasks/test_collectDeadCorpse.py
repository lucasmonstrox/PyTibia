from src.gameplay.core.tasks.collectDeadCorpse import CollectDeadCorpseTask


context = {
    'gameWindow': {'coordinate': (0, 0, 0, 0)},
    'loot': {
        'corpsesToLoot': [
            {'coordinate': (0, 0, 0)},
            {'coordinate': (1, 0, 0)},
            {'coordinate': (2, 0, 0)},
            {'coordinate': (0, 1, 0)},
            {'coordinate': (1, 1, 0)},
            {'coordinate': (2, 1, 0)},
            {'coordinate': (0, 2, 0)},
            {'coordinate': (1, 2, 0)},
            {'coordinate': (2, 2, 0)},
            {'coordinate': (3, 3, 0)},
        ]
    },
    'radar': {'coordinate': (1, 1, 0)},
}
creature = {}


def test_should_test_default_params():
    task = CollectDeadCorpseTask(creature)
    assert task.name == 'collectDeadCorpse'
    assert task.delayBeforeStart == 0.85
    assert task.creature == creature


def test_should_do(mocker):
    keyDownSpy = mocker.patch('src.utils.keyboard.keyDown')
    keyUpSpy = mocker.patch('src.utils.keyboard.keyUp')
    rightClickSlotSpy = mocker.patch(
        'src.repositories.gameWindow.slot.rightClickSlot')
    task = CollectDeadCorpseTask(creature)
    assert task.do(context) == context
    keyDownSpy.assert_called_once_with('shift')
    assert rightClickSlotSpy.call_count == 9
    rightClickSlotSpy.assert_has_calls([
        mocker.call([6, 4], context['gameWindow']['coordinate']),
        mocker.call([7, 4], context['gameWindow']['coordinate']),
        mocker.call([8, 4], context['gameWindow']['coordinate']),
        mocker.call([6, 5], context['gameWindow']['coordinate']),
        mocker.call([7, 5], context['gameWindow']['coordinate']),
        mocker.call([8, 5], context['gameWindow']['coordinate']),
        mocker.call([6, 6], context['gameWindow']['coordinate']),
        mocker.call([7, 6], context['gameWindow']['coordinate']),
        mocker.call([8, 6], context['gameWindow']['coordinate']),
    ])
    keyUpSpy.assert_called_once_with('shift')


def test_onComplete():
    task = CollectDeadCorpseTask(creature)
    assert task.onComplete(context) == context
    assert len(context['loot']['corpsesToLoot']) == 1
