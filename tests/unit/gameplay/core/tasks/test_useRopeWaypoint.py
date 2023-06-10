from src.gameplay.core.tasks.setNextWaypoint import SetNextWaypointTask
from src.gameplay.core.tasks.useRope import UseRopeTask
from src.gameplay.core.tasks.useRopeWaypoint import UseRopeWaypointTask


context = {}
waypoint = {'coordinate': (1, 2, 3)}

def test_should_test_default_params():
    task = UseRopeWaypointTask(waypoint)
    assert task.name == 'useRopeWaypoint'
    assert task.isRootTask == True
    assert task.waypoint == waypoint

def test_onBeforeStart():
    task = UseRopeWaypointTask(waypoint)
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 2
    assert isinstance(task.tasks[0], UseRopeTask)
    assert task.tasks[0].waypoint == waypoint
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], SetNextWaypointTask)
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
