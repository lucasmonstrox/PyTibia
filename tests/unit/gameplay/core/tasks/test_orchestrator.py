from time import sleep
from src.gameplay.core.tasks.common.base import BaseTask
from src.gameplay.core.tasks.common.vector import VectorTask
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator


context = {}

def test_get_root_task():
    baseTask = BaseTask()
    tasksOrchestrator = TasksOrchestrator(baseTask)
    currentTask = tasksOrchestrator.getCurrentTask(context)
    assert currentTask.name == baseTask.name

def test_should_do_task_when_did_in_first_time():
    tasksOrchestrator = TasksOrchestrator(BaseTask(name='currentTask'))
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_should_do_task_when_did_in_second_time(mocker):
    baseTask = BaseTask(name='currentTask')
    tasksOrchestrator = TasksOrchestrator(baseTask)
    mocker.patch.object(baseTask, 'did',  return_value=False)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    mocker.patch.object(baseTask, 'did',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_should_do_task_when_task_has_delayBeforeStart():
    tasksOrchestrator = TasksOrchestrator(BaseTask(name='currentTask', delayBeforeStart=1))
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'awaitingDelayBeforeStart'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_should_do_task_when_task_has_delayAfterComplete():
    tasksOrchestrator = TasksOrchestrator(BaseTask(name='currentTask', delayAfterComplete=1))
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'awaitingDelayAfterComplete'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_should_do_task_when_task_has_delayOfTimeout(mocker):
    baseTask = BaseTask(name='currentTask', delayOfTimeout=1)
    mocker.patch.object(baseTask, 'did',  return_value=False)
    tasksOrchestrator = TasksOrchestrator(baseTask)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(3)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_should_do_task_when_task_is_manuallyTerminable(mocker):
    baseTask = BaseTask(name='currentTask', manuallyTerminable=True)
    mocker.patch.object(baseTask, 'shouldManuallyComplete',  return_value=True)
    tasksOrchestrator = TasksOrchestrator(baseTask)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'awaitingManualTermination'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_do_vector_task():
    context = {}
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(name='firstTask').setParentTask(vectorTask)
    secondTask = BaseTask(name='secondTask').setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator(vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'running'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_do_vector_task_when_tasks_has_delayBeforeStart():
    context = {}
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(name='firstTask', delayBeforeStart=1).setParentTask(vectorTask)
    secondTask = BaseTask(name='secondTask', delayBeforeStart=1).setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator(vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingDelayBeforeStart'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'awaitingDelayBeforeStart'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'running'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_do_vector_task_when_tasks_has_delayAfterComplete():
    context = {}
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(name='firstTask', delayAfterComplete=1).setParentTask(vectorTask)
    secondTask = BaseTask(name='secondTask', delayAfterComplete=1).setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator(vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingDelayAfterComplete'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'running'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'awaitingDelayAfterComplete'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_do_vector_task_with_when_tasks_has_delayOfTimeout(mocker):
    context = {}
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(name='firstTask', delayOfTimeout=1).setParentTask(vectorTask)
    secondTask = BaseTask(name='secondTask', delayOfTimeout=1).setParentTask(vectorTask)
    mocker.patch.object(firstTask, 'did',  return_value=False)
    mocker.patch.object(secondTask, 'did',  return_value=False)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator(vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'running'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'running'
    assert tasksOrchestrator.rootTask.status == 'running'
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'

def test_do_vector_task_with_when_tasks_are_manuallyTerminable(mocker):
    context = {}
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(name='firstTask', manuallyTerminable=True).setParentTask(vectorTask)
    secondTask = BaseTask(name='secondTask', manuallyTerminable=True).setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator(vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingManualTermination'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingManualTermination'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    mocker.patch.object(firstTask, 'shouldManuallyComplete',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'running'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'awaitingManualTermination'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'awaitingManualTermination'
    assert tasksOrchestrator.rootTask.status == 'running'
    mocker.patch.object(secondTask, 'shouldManuallyComplete',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert secondTask.status == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'
