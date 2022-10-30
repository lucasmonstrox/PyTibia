from time import time
import actionBar.core


class RefillCheckerTask:
    def __init__(self, value):
        self.createdAt = time()
        self.startedAt = None
        self.delayBeforeStart = 2
        self.delayAfterComplete = 2
        self.name = 'refillChecker'
        self.status = 'notStarted'
        self.value = value

    def shouldIgnore(self, context):
        # TODO: get correct binds for health potion
        quantityOfHealthPotions = actionBar.core.getSlotCount(
            context['screenshot'], '1')
        # TODO: get correct binds for mana potion
        quantityOfManaPotions = actionBar.core.getSlotCount(
            context['screenshot'], '2')
        hasEnoughHealthPotions = quantityOfHealthPotions > context['refill'][
            'healthItem']['quantity']
        hasEnoughManaPotions = quantityOfManaPotions > context['refill'][
            'manaItem']['quantity']
        shouldIgnore = hasEnoughHealthPotions and hasEnoughManaPotions
        return shouldIgnore

    def do(self, context):
        context['waypoints']['currentIndex'] += 1
        context['waypoints']['state'] = None
        return context

    def did(self, _):
        return True

    def shouldRestart(self, _):
        return False

    def onDidNotComplete(self, context):
        context['waypoints']['currentIndex'] = 0
        context['waypoints']['state'] = None
        return context

    def onDidComplete(context):
        return context
