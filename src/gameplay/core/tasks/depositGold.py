from .common.vector import VectorTask
from .say import SayTask
from .selectChatTab import SelectChatTabTask
from .setChatOff import SetChatOffTask
from .setNextWaypoint import SetNextWaypointTask


# TODO: check if gold was deposited successfully
class DepositGoldTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'depositGold'
        self.isRootTask = True
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1

    # TODO: add unit tests
    # TODO: add typings
    def onBeforeStart(self, context):
        self.tasks = [
            SelectChatTabTask('local chat').setParentTask(self),
            SayTask('hi').setParentTask(self),
            SayTask('deposit all').setParentTask(self),
            SayTask('yes').setParentTask(self),
            SetChatOffTask().setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self
