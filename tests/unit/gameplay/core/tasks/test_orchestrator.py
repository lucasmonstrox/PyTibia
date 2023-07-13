from time import sleep
from src.gameplay.core.tasks.common.base import BaseTask
from src.gameplay.core.tasks.common.vector import VectorTask
from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.typings import Context


context = {}


def test_should_do_single_task():
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, BaseTask(name='currentTask'))
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_should_do_single_task_when_task_is_done_in_second_attempt(mocker):
    baseTask = BaseTask(name='currentTask')
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, baseTask)
    mocker.patch.object(baseTask, 'did',  return_value=False)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    mocker.patch.object(baseTask, 'did',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_should_do_single_task_when_task_has_delayBeforeStart():
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, BaseTask(
        name='currentTask', delayBeforeStart=1))
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'awaitingDelayBeforeStart'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_should_do_single_task_when_task_has_delayAfterComplete():
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, BaseTask(
        name='currentTask', delayAfterComplete=1))
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'awaitingDelayToComplete'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_should_do_task_when_task_has_delayOfTimeout(mocker):
    baseTask = BaseTask(name='currentTask', delayOfTimeout=1)
    mocker.patch.object(baseTask, 'did',  return_value=False)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, baseTask)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(3)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'timeout'


def test_should_do_task_when_task_is_manuallyTerminable(mocker):
    baseTask = BaseTask(name='currentTask', manuallyTerminable=True)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, baseTask)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'awaitingManualTermination'
    assert tasksOrchestrator.rootTask.statusReason is None
    mocker.patch.object(baseTask, 'shouldManuallyComplete',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.name == 'currentTask'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_do_vector_task():
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(name='firstTask').setParentTask(vectorTask)
    secondTask = BaseTask(name='secondTask').setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert firstTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'running'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'completed'
    assert secondTask.statusReason == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_do_vector_task_when_tasks_has_delayBeforeStart():
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(
        name='firstTask', delayBeforeStart=1).setParentTask(vectorTask)
    secondTask = BaseTask(
        name='secondTask', delayBeforeStart=1).setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingDelayBeforeStart'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'awaitingDelayBeforeStart'
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'running'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'completed'
    assert secondTask.statusReason == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_do_vector_task_when_tasks_has_delayAfterComplete():
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(
        name='firstTask', delayAfterComplete=1).setParentTask(vectorTask)
    secondTask = BaseTask(
        name='secondTask', delayAfterComplete=1).setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingDelayToComplete'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'running'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'awaitingDelayToComplete'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'completed'
    assert secondTask.statusReason == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_do_vector_task_with_when_tasks_has_delayOfTimeout(mocker):
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(
        name='firstTask', delayOfTimeout=1).setParentTask(vectorTask)
    secondTask = BaseTask(
        name='secondTask', delayOfTimeout=1).setParentTask(vectorTask)
    mocker.patch.object(firstTask, 'did',  return_value=False)
    mocker.patch.object(secondTask, 'did',  return_value=False)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'timeout'
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'timeout'
    assert secondTask.status == 'running'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'timeout'
    assert secondTask.status == 'running'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    sleep(2)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'timeout'
    assert secondTask.status == 'completed'
    assert secondTask.statusReason == 'timeout'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


def test_do_vector_task_with_when_tasks_are_manuallyTerminable(mocker):
    vectorTask = VectorTask(name='vectorTask')
    firstTask = BaseTask(
        name='firstTask', manuallyTerminable=True).setParentTask(vectorTask)
    secondTask = BaseTask(
        name='secondTask', manuallyTerminable=True).setParentTask(vectorTask)
    vectorTask.tasks.append(firstTask)
    vectorTask.tasks.append(secondTask)
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, vectorTask)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'running'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingManualTermination'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert firstTask.status == 'awaitingManualTermination'
    assert firstTask.statusReason is None
    assert secondTask.status == 'notStarted'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    mocker.patch.object(
        firstTask, 'shouldManuallyComplete',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'running'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'awaitingManualTermination'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'awaitingManualTermination'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'secondTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'awaitingManualTermination'
    assert secondTask.statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    mocker.patch.object(
        secondTask, 'shouldManuallyComplete',  return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.getCurrentTask(context).name == 'vectorTask'
    assert firstTask.status == 'completed'
    assert firstTask.statusReason == 'completed'
    assert secondTask.status == 'completed'
    assert secondTask.statusReason == 'completed'
    assert tasksOrchestrator.rootTask.status == 'completed'
    assert tasksOrchestrator.rootTask.statusReason == 'completed'


class CustomTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.isRootTask = True
        self.name = 'custom'

    def onBeforeStart(self, context):
        self.tasks = [
            BaseTask(name='firstTask').setParentTask(self),
            BaseTask(name='secondTask',
                     manuallyTerminable=True).setParentTask(self),
        ]
        return context


def test_should_restart_parent_task(mocker):
    customTask = CustomTask()
    tasksOrchestrator = TasksOrchestrator()
    tasksOrchestrator.setRootTask(context, customTask)
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert len(tasksOrchestrator.rootTask.tasks) == 0
    tasksOrchestrator.do(context)
    mocker.patch.object(customTask, 'shouldRestart', return_value=False)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.getCurrentTask(context).name == 'firstTask'
    assert tasksOrchestrator.rootTask.tasks[0].status == 'running'
    assert tasksOrchestrator.rootTask.tasks[0].statusReason is None
    assert tasksOrchestrator.rootTask.tasks[1].status == 'notStarted'
    assert tasksOrchestrator.rootTask.tasks[1].statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.rootTask.tasks[0].status == 'completed'
    assert tasksOrchestrator.rootTask.tasks[0].statusReason == 'completed'
    assert tasksOrchestrator.rootTask.tasks[1].status == 'notStarted'
    assert tasksOrchestrator.rootTask.tasks[1].statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.rootTask.tasks[0].status == 'completed'
    assert tasksOrchestrator.rootTask.tasks[0].statusReason == 'completed'
    assert tasksOrchestrator.rootTask.tasks[1].status == 'running'
    assert tasksOrchestrator.rootTask.tasks[1].statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 1
    assert tasksOrchestrator.rootTask.tasks[0].status == 'completed'
    assert tasksOrchestrator.rootTask.tasks[0].statusReason == 'completed'
    assert tasksOrchestrator.rootTask.tasks[1].status == 'awaitingManualTermination'
    assert tasksOrchestrator.rootTask.tasks[1].statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None
    mocker.patch.object(customTask, 'shouldRestart', return_value=True)
    tasksOrchestrator.do(context)
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert tasksOrchestrator.rootTask.retryCount == 1
    assert tasksOrchestrator.rootTask.tasks[0].status == 'running'
    assert tasksOrchestrator.rootTask.tasks[0].statusReason is None
    assert tasksOrchestrator.rootTask.tasks[1].status == 'notStarted'
    assert tasksOrchestrator.rootTask.tasks[1].statusReason is None
    assert tasksOrchestrator.rootTask.status == 'running'
    assert tasksOrchestrator.rootTask.statusReason is None


class RootTaskWithTimeoutTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.isRootTask = True
        self.name = 'custom'

    def onBeforeStart(self, context):
        self.tasks = [
            BaseTask(name='firstTask', delayOfTimeout=1,
                     shouldTimeoutTreeWhenTimeout=True).setParentTask(self).setRootTask(self),
            BaseTask(name='secondTask').setParentTask(self).setRootTask(self),
        ]
        return context

    def onTimeout(self, context: Context) -> Context:
        return context


def test_call_all_tree_onTimeout(mocker):
    rootTask = RootTaskWithTimeoutTask()
    tasksOrchestrator = TasksOrchestrator()
    rootTaskOnTimeoutSpy = mocker.patch.object(
        rootTask, 'onTimeout', return_value=context)
    tasksOrchestrator.setRootTask(context, rootTask)
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert len(tasksOrchestrator.rootTask.tasks) == 0
    tasksOrchestrator.do(context)
    assert rootTask.tasks[0].status == 'running'
    assert rootTask.tasks[0].statusReason is None
    assert rootTask.tasks[1].status == 'notStarted'
    assert rootTask.tasks[1].statusReason is None
    firstTaskOnTimeoutSpy = mocker.patch.object(
        rootTask.tasks[0], 'onTimeout', return_value=context)
    secondTaskOnTimeoutSpy = mocker.patch.object(
        rootTask.tasks[1], 'onTimeout', return_value=context)
    sleep(2)
    tasksOrchestrator.do(context)
    firstTaskOnTimeoutSpy.assert_called_once_with(context)
    secondTaskOnTimeoutSpy.assert_not_called()
    rootTaskOnTimeoutSpy.assert_called_once_with(context)
    assert rootTask.tasks[0].status == 'completed'
    assert rootTask.tasks[0].statusReason == 'timeout'
    assert rootTask.tasks[1].status == 'notStarted'
    assert rootTask.tasks[1].statusReason is None
    assert rootTask.status == 'completed'
    assert rootTask.statusReason == 'timeout'


class RootTaskWithoutTimeoutTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.isRootTask = True
        self.name = 'custom'

    def onBeforeStart(self, context):
        self.tasks = [
            BaseTask(name='firstTask', delayOfTimeout=1).setParentTask(
                self).setRootTask(self),
            BaseTask(name='secondTask').setParentTask(self).setRootTask(self),
        ]
        return context

    def onTimeout(self, context: Context) -> Context:
        return context


def test_not_call_all_tree_onTimeout(mocker):
    rootTask = RootTaskWithoutTimeoutTask()
    tasksOrchestrator = TasksOrchestrator()
    rootTaskOnTimeoutSpy = mocker.patch.object(
        rootTask, 'onTimeout', return_value=context)
    tasksOrchestrator.setRootTask(context, rootTask)
    assert tasksOrchestrator.rootTask.status == 'notStarted'
    assert tasksOrchestrator.rootTask.currentTaskIndex == 0
    assert len(tasksOrchestrator.rootTask.tasks) == 0
    tasksOrchestrator.do(context)
    assert rootTask.tasks[0].status == 'running'
    assert rootTask.tasks[0].statusReason is None
    assert rootTask.tasks[1].status == 'notStarted'
    assert rootTask.tasks[1].statusReason is None
    firstTaskOnTimeoutSpy = mocker.patch.object(
        rootTask.tasks[0], 'onTimeout', return_value=context)
    secondTaskOnTimeoutSpy = mocker.patch.object(
        rootTask.tasks[1], 'onTimeout', return_value=context)
    sleep(2)
    tasksOrchestrator.do(context)
    firstTaskOnTimeoutSpy.assert_called_once_with(context)
    secondTaskOnTimeoutSpy.assert_not_called()
    rootTaskOnTimeoutSpy.assert_not_called()
    assert rootTask.tasks[0].status == 'completed'
    assert rootTask.tasks[0].statusReason == 'timeout'
    assert rootTask.tasks[1].status == 'notStarted'
    assert rootTask.tasks[1].statusReason is None
    assert rootTask.status == 'running'
    assert rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert rootTask.tasks[0].status == 'completed'
    assert rootTask.tasks[0].statusReason == 'timeout'
    assert rootTask.tasks[1].status == 'running'
    assert rootTask.tasks[1].statusReason is None
    assert rootTask.status == 'running'
    assert rootTask.statusReason is None
    tasksOrchestrator.do(context)
    assert rootTask.tasks[0].status == 'completed'
    assert rootTask.tasks[0].statusReason == 'timeout'
    assert rootTask.tasks[1].status == 'completed'
    assert rootTask.tasks[1].statusReason == 'completed'
    assert rootTask.status == 'completed'
    assert rootTask.statusReason == 'completed'
