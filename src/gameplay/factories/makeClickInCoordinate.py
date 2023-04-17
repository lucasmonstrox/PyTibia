from ..tasks.clickInCoordinate import ClickInCoordinateTask


def makeClickInCoordinateTask(coordinate):
    task = ClickInCoordinateTask(coordinate)
    return ('clickInCoordinate', task)
