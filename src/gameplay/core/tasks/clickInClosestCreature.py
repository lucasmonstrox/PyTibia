import src.utils.keyboard as keyboard
import src.utils.mouse as mouse
from ...typings import Context
from .common.base import BaseTask


class ClickInClosestCreatureTask(BaseTask):
    def __init__(self):
        super().__init__()
        self.name = 'clickInClosestCreature'
        self.delayOfTimeout = 1

    def shouldIgnore(self, context: Context) -> bool:
        return context['cavebot']['targetCreature'] is not None

    def do(self, context: Context) -> Context:
        # attack by mouse click when there are players on screen or ignorable creatures
        if context['gameWindow']['players'] or context['targeting']['hasIgnorableCreatures']:
            keyboard.keyDown('alt')
            mouse.leftClick(context['cavebot']
                            ['closestCreature']['windowCoordinate'])
            keyboard.keyUp('alt')
            return context
        keyboard.press('space')
        return context

    def did(self, context: Context) -> bool:
        return context['cavebot']['isAttackingSomeCreature']
