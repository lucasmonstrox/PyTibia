from src.utils.keyboard import hotkey, keyDown, keyUp, press, write


def test_should_call_hotkey(mocker):
    hotkeys = ['a', 'b']
    hotkeySpy =  mocker.patch('pyautogui.hotkey')
    hotkey(hotkeys)
    hotkeySpy.assert_called_once_with(hotkeys)

def test_should_call_keyDown(mocker):
    hotkey = 'a'
    keyDownSpy =  mocker.patch('pyautogui.keyDown')
    keyDown(hotkey)
    keyDownSpy.assert_called_once_with(hotkey)

def test_should_call_keyUp(mocker):
    hotkey = 'a'
    keyUpSpy =  mocker.patch('pyautogui.keyUp')
    keyUp(hotkey)
    keyUpSpy.assert_called_once_with(hotkey)

def test_should_call_hotkey(mocker):
    hotkeys = ['a', 'b']
    pressSpy =  mocker.patch('pyautogui.press')
    press(hotkeys)
    pressSpy.assert_called_once_with(hotkeys)

def test_should_call_write(mocker):
    phrase = 'hello world!'
    writeSpy =  mocker.patch('pyautogui.write')
    write(phrase)
    writeSpy.assert_called_once_with(phrase)
