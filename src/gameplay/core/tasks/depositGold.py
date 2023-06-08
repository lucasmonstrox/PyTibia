from ...typings import Context
from .common.vector import VectorTask
from .enableChat import EnableChatTask
from .say import SayTask
from .selectChatTab import SelectChatTabTask
from .setChatOff import SetChatOffTask
from .setNextWaypoint import SetNextWaypointTask


# TODO: check if gold was deposited successfully by shouldRestartAfterAllChildrensComplete
class DepositGoldTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'depositGold'
        self.isRootTask = True
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1

    def onBeforeStart(self, context: Context) -> Context:
        self.tasks = [
            SelectChatTabTask('local chat').setParentTask(self).setRootTask(self),
            EnableChatTask().setParentTask(self).setRootTask(self),
            SayTask('hi').setParentTask(self).setRootTask(self),
            EnableChatTask().setParentTask(self).setRootTask(self),
            SayTask('deposit all').setParentTask(self).setRootTask(self),
            EnableChatTask().setParentTask(self).setRootTask(self),
            SayTask('yes').setParentTask(self).setRootTask(self),
            SetChatOffTask().setParentTask(self).setRootTask(self),
            SetNextWaypointTask().setParentTask(self).setRootTask(self),
        ]
        return context
