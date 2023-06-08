from src.gameplay.core.tasks.attackClosestCreature import AttackClosestCreatureTask
from src.gameplay.core.tasks.clickInClosestCreature import ClickInClosestCreatureTask
from src.gameplay.core.tasks.walkToTargetCreature import WalkToTargetCreatureTask


context = {}

def test_should_test_default_params():
    task = AttackClosestCreatureTask()
    assert task.name == 'attackClosestCreature'
    assert task.isRootTask == 1

def test_onBeforeStart():
    task = AttackClosestCreatureTask()
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 2
    assert isinstance(task.tasks[0], ClickInClosestCreatureTask)
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], WalkToTargetCreatureTask)
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
