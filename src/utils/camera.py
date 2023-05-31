
import pyautogui
import cv2
import numpy as np

class PyCamera():
    is_capturing = True

    def get_latest_frame(self, path='screen.png'):
        img = pyautogui.screenshot()
        img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)
        if path:
            # import cv2; cv2.imwrite('screen_test.png', screenshot)
            cv2.imwrite(path, img)
        return img
        