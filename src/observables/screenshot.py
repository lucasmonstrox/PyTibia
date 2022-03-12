from utils import utils

def screenshotObservable(observer, _):
    while True:
        screenshot = utils.getScreenshot()
        observer.on_next(screenshot)