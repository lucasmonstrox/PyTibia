import src.repositories.gameWindow.core as gameWindowCore
import src.repositories.gameWindow.slot as gameWindowSlot
from src.shared.typings import Waypoint
import src.utils.keyboard as keyboard
from ...typings import Context
from .common.base import BaseTask


class UseShovelTask(BaseTask):
    def __init__(self, waypoint: Waypoint):
        super().__init__()
        self.name = 'useShovel'
        self.delayBeforeStart = 1
        self.delayAfterComplete = 0.5
        self.waypoint = waypoint

    def shouldIgnore(self, context: Context) -> bool:
        return gameWindowCore.isHoleOpen(
            context['gameWindow']['image'], gameWindowCore.images[context['resolution']]['holeOpen'], context['radar']['coordinate'], self.waypoint['coordinate'])

    def do(self, context: Context) -> Context:
        slot = gameWindowCore.getSlotFromCoordinate(
            context['radar']['coordinate'], self.waypoint['coordinate'])
        keyboard.press(context['hotkeys']['shovel'])
        gameWindowSlot.clickSlot(slot, context['gameWindow']['coordinate'])
        return context

    def did(self, context: Context) -> bool:
        return self.shouldIgnore(context)
