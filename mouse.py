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


def switch_map(mapper):
    mapper_ = mapper or cast(of)
    return pipe(
        operators.map(mapper_),
        operators.switch_latest(),
    )


def main():
    pixelSequence = Subject()
    mousePoint = pixelSequence.pipe(
        switch_map(lambda items: timer(0, 0.9).pipe(
            operators.map(lambda i: items[i]),
            operators.take(3)
        )),
    )
    mousePoint.subscribe(
        lambda res: print("Mouse set to: {}".format(res)),
        lambda err: print('err', err),
        lambda: print('complete'),
    )
    pixelSequence.on_next([
        [0, 1],
        [10, 11],
        [20, 21],
        [30, 31],
        [40, 41],
    ])
    while True:
        time.sleep(2)
        pixelSequence.on_next([
            [100, 50],
            [200, 50],
            [300, 50],
        ])
        continue


if __name__ == '__main__':
    main()
