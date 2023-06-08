from src.gameplay.core.tasks.depositGold import DepositGoldTask
from src.gameplay.core.tasks.enableChat import EnableChatTask
from src.gameplay.core.tasks.say import SayTask
from src.gameplay.core.tasks.selectChatTab import SelectChatTabTask
from src.gameplay.core.tasks.setChatOff import SetChatOffTask
from src.gameplay.core.tasks.setNextWaypoint import SetNextWaypointTask


context = {}

def test_should_test_default_params():
    task = DepositGoldTask()
    assert task.name == 'depositGold'
    assert task.isRootTask == True
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 1

def test_onBeforeStart():
    task = DepositGoldTask()
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 9
    assert isinstance(task.tasks[0], SelectChatTabTask)
    assert task.tasks[0].tabName == 'local chat'
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], EnableChatTask)
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
    assert isinstance(task.tasks[2], SayTask)
    assert task.tasks[2].phrase == 'hi'
    assert task.tasks[2].parentTask == task
    assert task.tasks[2].rootTask == task
    assert isinstance(task.tasks[3], EnableChatTask)
    assert task.tasks[3].parentTask == task
    assert task.tasks[3].rootTask == task
    assert isinstance(task.tasks[4], SayTask)
    assert task.tasks[4].phrase == 'deposit all'
    assert task.tasks[4].parentTask == task
    assert task.tasks[4].rootTask == task
    assert isinstance(task.tasks[5], EnableChatTask)
    assert task.tasks[5].parentTask == task
    assert task.tasks[5].rootTask == task
    assert isinstance(task.tasks[6], SayTask)
    assert task.tasks[6].phrase == 'yes'
    assert task.tasks[6].parentTask == task
    assert task.tasks[6].rootTask == task
    assert isinstance(task.tasks[7], SetChatOffTask)
    assert task.tasks[7].parentTask == task
    assert task.tasks[7].rootTask == task
    assert isinstance(task.tasks[8], SetNextWaypointTask)
    assert task.tasks[8].parentTask == task
    assert task.tasks[8].rootTask == task
