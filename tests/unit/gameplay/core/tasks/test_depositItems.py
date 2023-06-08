import numpy as np
from src.gameplay.core.tasks.closeContainer import CloseContainerTask
from src.gameplay.core.tasks.depositItems import DepositItemsTask
from src.gameplay.core.tasks.dropBackpackIntoStash import DropBackpackIntoStashTask
from src.gameplay.core.tasks.dragItems import DragItemsTask
from src.gameplay.core.tasks.goToFreeDepot import GoToFreeDepotTask
from src.gameplay.core.tasks.openBackpack import OpenBackpackTask
from src.gameplay.core.tasks.openLocker import OpenLockerTask
from src.gameplay.core.tasks.openDepot import OpenDepotTask
from src.gameplay.core.tasks.scrollToItem import ScrollToItemTask
from src.gameplay.core.tasks.setNextWaypoint import SetNextWaypointTask
from src.repositories.inventory.core import images


context = {
    'backpacks': {
        'main': 'brocade backpack',
        'loot': 'beach backpack',
    }
}
waypoint = {'coordinate': (1, 2, 3)}

def test_should_test_default_params():
    task = DepositItemsTask(waypoint)
    assert task.name == 'depositItems'
    assert task.isRootTask == True
    assert task.delayBeforeStart == 1
    assert task.delayAfterComplete == 1

def test_onBeforeStart():
    task = DepositItemsTask(waypoint)
    assert task.onBeforeStart(context) == context
    assert len(task.tasks) == 10
    assert isinstance(task.tasks[0], GoToFreeDepotTask)
    assert task.tasks[0].parentTask == task
    assert task.tasks[0].rootTask == task
    assert isinstance(task.tasks[1], OpenLockerTask)
    assert task.tasks[1].parentTask == task
    assert task.tasks[1].rootTask == task
    assert isinstance(task.tasks[2], OpenBackpackTask)
    assert task.tasks[2].backpack == context['backpacks']['main']
    assert task.tasks[2].parentTask == task
    assert task.tasks[2].rootTask == task
    assert isinstance(task.tasks[3], ScrollToItemTask)
    assert np.array_equal(task.tasks[3].containerImage, images['containersBars'][context['backpacks']['main']]) == True
    assert np.array_equal(task.tasks[3].itemImage, images['slots'][context['backpacks']['loot']]) == True
    assert task.tasks[3].parentTask == task
    assert task.tasks[3].rootTask == task
    assert isinstance(task.tasks[4], DropBackpackIntoStashTask)
    assert task.tasks[4].backpack == context['backpacks']['loot']
    assert task.tasks[4].parentTask == task
    assert task.tasks[4].rootTask == task
    assert isinstance(task.tasks[5], OpenDepotTask)
    assert task.tasks[5].parentTask == task
    assert task.tasks[5].rootTask == task
    assert isinstance(task.tasks[6], OpenBackpackTask)
    assert task.tasks[6].backpack == context['backpacks']['loot']
    assert task.tasks[6].parentTask == task
    assert task.tasks[6].rootTask == task
    assert isinstance(task.tasks[7], DragItemsTask)
    assert np.array_equal(task.tasks[7].containerBarImage, images['containersBars'][context['backpacks']['loot']]) == True
    assert np.array_equal(task.tasks[7].targetContainerImage, images['slots']['depot chest 2']) == True
    assert task.tasks[7].parentTask == task
    assert task.tasks[7].rootTask == task
    assert isinstance(task.tasks[8], CloseContainerTask)
    assert np.array_equal(task.tasks[8].containerBarImage, images['containersBars'][context['backpacks']['loot']]) == True
    assert task.tasks[8].parentTask == task
    assert task.tasks[8].rootTask == task
    assert isinstance(task.tasks[9], SetNextWaypointTask)
    assert task.tasks[9].parentTask == task
    assert task.tasks[9].rootTask == task
