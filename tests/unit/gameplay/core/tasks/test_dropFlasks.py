from src.gameplay.core.tasks.dropEachFlask import DropEachFlaskTask
from src.gameplay.core.tasks.dropFlasks import DropFlasksTask
from src.gameplay.core.tasks.expandBackpack import ExpandBackpackTask
from src.gameplay.core.tasks.openBackpack import OpenBackpackTask
from src.gameplay.core.tasks.setNextWaypoint import SetNextWaypointTask


context = {'backpacks': {'main': 'beach backpack'}}

def test_should_test_default_params():
    task = DropFlasksTask()
    assert task.name == 'dropFlasks'
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == True
    assert task.isRootTask == True

def test_onBeforeStart():
    task = DropFlasksTask()
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 4
    assert isinstance(task.tasks[0], OpenBackpackTask)
    assert task.tasks[0].backpack == context['backpacks']['main']
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], ExpandBackpackTask)
    assert task.tasks[1].backpack == context['backpacks']['main']
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
    assert isinstance(task.tasks[2], DropEachFlaskTask)
    assert task.tasks[2].backpack == context['backpacks']['main']
    assert task.tasks[2].parentTask == task
    assert task.tasks[2].rootTask == task
    assert isinstance(task.tasks[3], SetNextWaypointTask)
    assert task.tasks[3].parentTask == task
    assert task.tasks[3].rootTask == task
