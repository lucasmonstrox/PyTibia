from src.gameplay.core.tasks.collectDeadCorpse import CollectDeadCorpseTask
from src.gameplay.core.tasks.lootCorpse import LootCorpseTask


context = {}
creature = {'coordinate': (0, 0, 0)}

def test_should_test_default_params():
    task = LootCorpseTask(creature)
    assert task.name == 'lootCorpse'
    assert task.isRootTask == True
    assert task.creature == creature

def test_onBeforeStart():
    task = LootCorpseTask(creature)
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 1
    assert isinstance(task.tasks[0], CollectDeadCorpseTask)
    assert task.tasks[0].creature == creature
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task