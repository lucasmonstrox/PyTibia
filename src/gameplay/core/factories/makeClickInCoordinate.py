from ..tasks.clickInCoordinate import ClickInCoordinateTask


# TODO: add unit tests
# TODO: add perf
# TODO: add typings
def makeClickInCoordinateTask(coordinate):
    task = ClickInCoordinateTask(coordinate)
    return ('clickInCoordinate', task)
