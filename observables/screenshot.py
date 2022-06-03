from utils import utils
import time

def screenshotObservable(observer, _):
    # while True:
    screenshot = utils.getScreenshot()
    observer.on_next(screenshot)
    # time.sleep(0.033)