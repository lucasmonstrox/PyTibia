from src.gameplay.core.tasks.common.vector import VectorTask


context = {}

def test_should_test_default_params():
    baseTask = VectorTask()
    assert baseTask.currentTaskIndex == 0
    assert len(baseTask.tasks) == 0

def test_shouldRestartAfterAllChildrensComplete_return_False():
    task = VectorTask()
    assert task.shouldRestartAfterAllChildrensComplete(context) == False
