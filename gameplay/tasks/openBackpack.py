from inventory.core import isBackpackOpen, openBackpack
from .base.baseTask import BaseTask


class OpenBackpackTask(BaseTask):
    def __init__(self, backpack):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'openBackpack'
        self.value = backpack

    def shouldIgnore(self, context):
        shouldIgnore = isBackpackOpen(context['screenshot'], self.value)
        return shouldIgnore

    def exec(self, context):
        openBackpack(context['screenshot'], self.value)
        return context
    
    def did(self, context):
        did = isBackpackOpen(context['screenshot'], self.value)
        return did
