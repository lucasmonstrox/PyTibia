from src.gameplay.core.tasks.clickInCoordinate import ClickInCoordinateTask
from src.gameplay.core.tasks.setNextWaypoint import SetNextWaypointTask
from src.gameplay.core.tasks.useShovel import UseShovelTask
from src.gameplay.core.tasks.useShovelWaypoint import UseShovelWaypointTask


context = {}
waypoint = {'coordinate': (1, 2, 3)}

def test_should_test_default_params():
    task = UseShovelWaypointTask(waypoint)
    assert task.name == 'useShovelWaypoint'
    assert task.isRootTask == True
    assert task.waypoint == waypoint

def test_onBeforeStart():
    task = UseShovelWaypointTask(waypoint)
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 3
    assert isinstance(task.tasks[0], UseShovelTask)
    assert task.tasks[0].waypoint == waypoint
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], ClickInCoordinateTask)
    assert task.tasks[1].waypoint == waypoint
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
    assert isinstance(task.tasks[2], SetNextWaypointTask)
    assert task.tasks[2].parentTask == task
    assert task.tasks[2].rootTask == task