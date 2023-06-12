from src.utils.mouse import drag, leftClick, moveTo, rightClick, scroll


def test_should_drag(mocker):
    x0y0WindowCoordinate = (0, 0)
    x1y1WindowCoordinate = (1, 1)
    moveToSpy =  mocker.patch('pyautogui.moveTo')
    dragToSpy =  mocker.patch('pyautogui.dragTo')
    drag(x0y0WindowCoordinate, x1y1WindowCoordinate)
    moveToSpy.assert_called_once_with(x0y0WindowCoordinate[0], x0y0WindowCoordinate[1])
    dragToSpy.assert_called_once_with(x1y1WindowCoordinate[0], x1y1WindowCoordinate[1], button='left')

def test_should_call_leftClick_without_params_when_windowCoordinate_is_None(mocker):
    leftClickSpy =  mocker.patch('pyautogui.leftClick')
    leftClick()
    leftClickSpy.assert_called()

def test_should_call_leftClick_with_params_when_windowCoordinate_is_not_None(mocker):
    windowCoordinate = (0, 0)
    leftClickSpy =  mocker.patch('pyautogui.leftClick')
    leftClick(windowCoordinate)
    leftClickSpy.assert_called_once_with(windowCoordinate[0], windowCoordinate[1])

def test_should_call_moveTo_with_correct_params(mocker):
    windowCoordinate = (0, 0)
    moveToSpy =  mocker.patch('pyautogui.moveTo')
    moveTo(windowCoordinate)
    moveToSpy.assert_called_once_with(windowCoordinate[0], windowCoordinate[1])

def test_should_call_scroll_with_correct_params(mocker):
    scrolls = 5
    scrollSpy =  mocker.patch('pyautogui.scroll')
    scroll(scrolls)
    scrollSpy.assert_called_once_with(scrolls)

def test_should_call_rightClick_without_params_when_windowCoordinate_is_None(mocker):
    rightClickSpy =  mocker.patch('pyautogui.rightClick')
    rightClick()
    rightClickSpy.assert_called()

def test_should_call_rightClick_with_params_when_windowCoordinate_is_not_None(mocker):
    windowCoordinate = (0, 0)
    rightClickSpy =  mocker.patch('pyautogui.rightClick')
    rightClick(windowCoordinate)
    rightClickSpy.assert_called_once_with(windowCoordinate[0], windowCoordinate[1])
