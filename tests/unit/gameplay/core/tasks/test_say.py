from src.gameplay.core.tasks.say import SayTask

context = {}

def test_should_test_default_params():
    task = SayTask('hello')
    assert task.name == 'say'
    assert task.delayBeforeStart == 2
    assert task.delayAfterComplete == 2
    assert task.phrase == 'hello'

def test_should_do(mocker):
    writeSpy = mocker.patch('src.utils.keyboard.write')
    pressSpy = mocker.patch('src.utils.keyboard.press')
    phrase = 'hello'
    task = SayTask(phrase)
    assert task.do(context) == context
    writeSpy.assert_called_once_with(phrase)
    pressSpy.assert_called_once_with('enter')
