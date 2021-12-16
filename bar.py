import cv2
import d3dshot
from time import time
import cupy as cp
import pygetwindow as gw
from hud import hud
import pyautogui


def getScreenshot(d3):
    window = gw.getWindowsWithTitle('Tibia - ADM')[0]
    region = (window.top, window.left, window.width - 15, window.height)
    screenshot = d3.screenshot(region=region)
    screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    screenshot = cp.array(screenshot)
    return screenshot


def main():
    loop_time = time()
    d3 = d3dshot.create(capture_output='numpy')
    screenshot = cp.ascontiguousarray(
        cp.array(cv2.imread('screenshot.png', cv2.IMREAD_GRAYSCALE)))
    while True:
        screenshot = getScreenshot(d3)
        playable = screenshot[35:35 + 352, 151:151 + 480]
        playable = playable.flatten()
        creaturesBars = hud.getCreaturesBars(playable)
        hasCreaturesBars = len(creaturesBars) > 0
        if hasCreaturesBars:
            x = creaturesBars[0][0] + 152 + 5
            y = creaturesBars[0][1] + 36 + 5
            pyautogui.moveTo(x, y)
            pyautogui.rightClick()
            break
        timef = (time() - loop_time)
        timef = timef if timef else 1
        fps = 1 / timef
        print('FPS {}'.format(fps))
        loop_time = time()


if __name__ == '__main__':
    main()
