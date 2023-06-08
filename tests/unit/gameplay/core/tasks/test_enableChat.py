from src.gameplay.core.tasks.enableChat import EnableChatTask


def test_should_test_default_params():
    task = EnableChatTask()
    assert task.name == 'enableChat'
    assert task.delayBeforeStart == 2
    assert task.delayAfterComplete == 2

def test_should_method_shouldIgnore_return_False_when_chat_is_off(mocker):
    context = {'screenshot': []}
    getChatStatusSpy = mocker.patch('src.repositories.chat.core.getChatStatus', return_value=((0, 0, 0, 0), False))
    task = EnableChatTask()
    assert task.shouldIgnore(context) == False
    getChatStatusSpy.assert_called_once_with(context['screenshot'])

def test_should_method_shouldIgnore_return_True_when_chat_is_off(mocker):
    context = {'screenshot': []}
    getChatStatusSpy = mocker.patch('src.repositories.chat.core.getChatStatus', return_value=((0, 0, 0, 0), True))
    task = EnableChatTask()
    assert task.shouldIgnore(context) == True
    getChatStatusSpy.assert_called_once_with(context['screenshot'])

def test_should_do(mocker):
    context = {'screenshot': []}
    task = EnableChatTask()
    pressSpy = mocker.patch('src.utils.keyboard.press')
    assert task.do(context) == context
    pressSpy.assert_called_once_with('enter')
