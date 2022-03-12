from time import sleep
from threading import Thread
from src.observables import cavebot, healing, screenshot, waypoint 
from radar import radar
from utils import utils
from threading import current_thread
import rx
from rx import operators


def main():
    screenshotObserver = rx.create(screenshot.screenshotObservable)
    # coordinateObserver = rx.create(waypoint.coordinateObservable)
    # screenshotObserver.subscribe(
    #     lambda screenshot: print(screenshot),
    # )
    
    waypointObserver = screenshotObserver.pipe(
        operators.map(lambda screenshot: (screenshot, radar.getCoordinate(screenshot)))
    )
    waypointObserver.subscribe(lambda value: waypoint.waypoint(value))
    
    cavebotObserver = screenshotObserver.pipe(
        operators.map(lambda screenshot: (screenshot, radar.getCoordinate(screenshot)))
    )
    
    # rx.create(obs).subscribe(
    #     lambda a: print(a),
    # )
    
    # Observar a screenshot
    
    # waypointObserver = rx.create(waypoint.waypointObservable)
    # waypointObserver.subscribe(
    #     lambda waypoint: makeTime(5),
    # )
    # waypointObserver.subscribe(
    #     lambda waypoint: makeTime(2),
    # )

    
    # screenshotObserver.subscribe(
    #     lambda screenshot: makeTime(5),
    # )
    # screenshotObserver.subscribe(
    #     lambda screenshot: makeTime(2),
    # )
    # healingThread = Thread(target=healing.healingThread)
    # healingThread.start()
    # waypointThreadInstance = Thread(target=waypoint.waypointThread)
    # waypointThreadInstance.start()
    # cavebotThread = Thread(target=cavebot.cavebotThread)
    # cavebotThread.start()


if __name__ == '__main__':
    main()
