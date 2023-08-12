from src.gameplay.typings import Context
from src.utils.mouse import leftClick
from .common.base import BaseTask


# TODO: implement should ignore if tab already selected
class SelectChatTabTask(BaseTask):
    def __init__(self, name):
        super().__init__()
        self.name = 'selectChatTab'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.tabName = name

    # TODO: add unit tests
    def shouldIgnore(self, context: Context) -> bool:
        tab = context['chat']['tabs'].get(self.tabName)
        if tab is None:
            return False
        return tab['isSelected']

    # TODO: add unit tests
    def do(self, context):
        tabPosition = context['chat']['tabs'][self.tabName]['position']
        # TODO: implement random click in BBox
        leftClick((tabPosition[0] + 10, tabPosition[1] + 5))
        return context
