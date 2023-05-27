import pyautogui
from .common.base import BaseTask


class SelectChatTabTask(BaseTask):
    def __init__(self, name):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'selectChatTab'
        self.value = name

    def do(self, context):
        tab = context['chat']['tabs'].get(self.value)
        cannotGetTab = tab is None
        if cannotGetTab:
            return context
        tabPosition = context['chat']['tabs'][self.value]['position']
        pyautogui.click(tabPosition[0] + 10, tabPosition[1] + 5)
        return context
