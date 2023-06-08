from src.gameplay.core.tasks.closeNpcTradeBox import CloseNpcTradeBoxTask


def test_should_test_default_params():
    task = CloseNpcTradeBoxTask()
    assert task.name == 'closeNpcTradeBox'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 0.5

def test_should_not_call_leftClick_when_getTradeTopPosition_return_None(mocker):
    context = {'screenshot': []}
    getTradeTopPositionSpy = mocker.patch('src.repositories.refill.core.getTradeTopPosition', return_value=None)
    leftClickSpy = mocker.patch('src.utils.mouse.leftClick')
    task = CloseNpcTradeBoxTask()
    assert task.do(context) == context
    getTradeTopPositionSpy.assert_called_once_with(context['screenshot'])
    leftClickSpy.assert_not_called()

def test_should_not_call_leftClick_when_getTradeTopPosition_return_None(mocker):
    context = {'screenshot': []}
    getTradeTopPositionSpy = mocker.patch('src.repositories.refill.core.getTradeTopPosition', return_value=(0, 0, 0, 0))
    leftClickSpy = mocker.patch('src.utils.mouse.leftClick')
    task = CloseNpcTradeBoxTask()
    assert task.do(context) == context
    getTradeTopPositionSpy.assert_called_once_with(context['screenshot'])
    leftClickSpy.assert_called_once_with((165, 7))
