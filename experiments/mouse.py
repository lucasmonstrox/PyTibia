import multiprocessing
import numpy as np
import pyautogui
from rx import create, interval, operators, timer, of, from_, pipe, from_iterable
from rx.scheduler import ThreadPoolScheduler
from rx.subject import Subject
import time
from actionBar import cooldown
import battleList.core
import hud.creatures
import player.core
import radar.core
import utils.core
import utils.image
import utils.mouse
import utils.window
import datetime
from typing import cast

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def switch_map(mapper):
    mapper_ = mapper or cast(of)
    return pipe(
        operators.map(mapper_),
        operators.switch_latest(),
    )


def main():
    x = np.arange(320, 740)
    y = np.arange(120, 540)
    z = np.column_stack((x, y))
    # pyautogui.moveTo(320, 740, duration=3)
    # pyautogui.moveTo(1040, 120, duration=3)
    pixelSequence = Subject()

    def test(items):
        print('aew')
        return timer(0, 0.005).pipe(
            operators.map(lambda i: items[i]),
            operators.take(len(items))
        )

    mousePoint = pixelSequence.pipe(
        switch_map(test),
    )

    mousePoint.subscribe(
        lambda res: pyautogui.moveTo(res[0], res[1]),
        lambda err: print('err', err),
        lambda: print('complete'),
    )

    x1 = np.arange(10, 610)
    y1 = np.arange(210, 810)
    z1 = np.column_stack((x1, y1))
    # a = np.arange(320, 321)
    # pixelSequence.on_next([
    #     [0, 1],
    #     [10, 11],
    #     [20, 21],
    #     [30, 31],
    #     [40, 41],
    # ])
    pixelSequence.on_next(z)
    time.sleep(1)
    pixelSequence.on_next(z1)
    while True:

        #     pixelSequence.on_next([
        #         [100, 50],
        #         [200, 50],
        #         [300, 50],
        #     ])
        continue


if __name__ == '__main__':
    main()
