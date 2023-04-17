from .baseTask import BaseTask


class PauseBotTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.delayBeforeStart = 1
        self.delayAfterComplete = 1
        self.name = 'pauseBot'

    def do(self, context):
        context['cavebot']['enabled'] = False
        return context
    
    # TODO: check if cavebot['enabled'] is False
    def did(self, context):
        return True
