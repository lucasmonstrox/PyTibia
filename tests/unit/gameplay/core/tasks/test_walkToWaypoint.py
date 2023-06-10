from src.gameplay.core.tasks.setNextWaypoint import SetNextWaypointTask
from src.gameplay.core.tasks.walkToCoordinate import WalkToCoordinateTask
from src.gameplay.core.tasks.walkToWaypoint import WalkToWaypointTask


context = {}
coordinate = (1, 2, 3) 

def test_should_test_default_params():
    task = WalkToWaypointTask(coordinate)
    assert task.name == 'walkToWaypoint'
    assert task.delayAfterComplete == 1
    assert task.isRootTask == True
    assert task.coordinate == coordinate

def test_onBeforeStart():
    task = WalkToWaypointTask(coordinate)
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 2
    assert isinstance(task.tasks[0], WalkToCoordinateTask)
    assert task.tasks[0].coordinate == coordinate
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], SetNextWaypointTask)
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
