import pyautogui
from time import sleep, time
from src.gameplay.cavebot import resolveCavebotTasks, shouldAskForCavebotTasks
from src.gameplay.context import context
from src.gameplay.combo import comboSpellsObserver
from src.gameplay.core.middlewares.battleList import setBattleListMiddleware
from src.gameplay.core.middlewares.chat import setChatTabsMiddleware
from src.gameplay.core.middlewares.gameWindow import setDirectionMiddleware, setHandleLootMiddleware, setGameWindowCreaturesMiddleware, setGameWindowMiddleware
from src.gameplay.core.middlewares.playerStatus import setMapPlayerStatusMiddleware
from src.gameplay.core.middlewares.radar import setRadarMiddleware, setWaypointIndexMiddleware
from src.gameplay.core.middlewares.screenshot import setScreenshotMiddleware
from src.gameplay.core.middlewares.tasks import setCleanUpTasksMiddleware
from src.gameplay.core.middlewares.window import setTibiaWindowMiddleware
from src.gameplay.core.tasks.lootCorpse import LootCorpseTask
from src.gameplay.resolvers import resolveTasksByWaypoint
from src.gameplay.healing.observers.eatFood import eatFoodObserver
from src.gameplay.healing.observers.healingBySpells import healingBySpellsObserver
from src.gameplay.healing.observers.healingByPotions import healingByPotionsObserver
from src.gameplay.healing.observers.healingPriority import healingPriorityObserver
from src.gameplay.targeting import hasCreaturesToAttack
from src.repositories.gameWindow.creatures import getClosestCreature


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


class PyTibiaThread:
    # TODO: add typings
    def __init__(self, context):
        self.context = context

    def mainloop(self):
        while True:
            if self.context.context['pause']:
                continue
            startTime = time()
            self.context.context = self.handleGameData(self.context.context)
            self.context.context = self.handleGameplayTasks(
                self.context.context)
            self.context.context = self.context.context['tasksOrchestrator'].do(
                self.context.context)
            self.context.context['radar']['lastCoordinateVisited'] = self.context.context['radar']['coordinate']
            healingByPotionsObserver(self.context.context)
            comboSpellsObserver(self.context.context)
            endTime = time()
            diff = endTime - startTime
            sleep(max(0.045 - diff, 0))

    def handleGameData(self, context):
        context = setTibiaWindowMiddleware(context)
        if context['pause']:
            return context
        context = setScreenshotMiddleware(context)
        context = setRadarMiddleware(context)
        context = setChatTabsMiddleware(context)
        context = setBattleListMiddleware(context)
        context = setGameWindowMiddleware(context)
        context = setDirectionMiddleware(context)
        context = setGameWindowCreaturesMiddleware(context)
        context = setHandleLootMiddleware(context)
        context = setWaypointIndexMiddleware(context)
        context = setMapPlayerStatusMiddleware(context)
        context = setCleanUpTasksMiddleware(context)
        return context

    def handleGameplayTasks(self, context):
        context['cavebot']['closestCreature'] = getClosestCreature(
            context['gameWindow']['monsters'], context['radar']['coordinate'])
        currentTask = context['tasksOrchestrator'].getCurrentTask(context)
        if currentTask is not None and currentTask.name == 'selectChatTab':
            return context
        if len(context['loot']['corpsesToLoot']) > 0:
            context['way'] = 'lootCorpses'
            if currentTask is not None and currentTask.rootTask is not None and currentTask.rootTask.name != 'lootCorpse':
                context['tasksOrchestrator'].setRootTask(context, None)
            if context['tasksOrchestrator'].getCurrentTask(context) is None:
                # TODO: get closest dead corpse
                firstDeadCorpse = context['loot']['corpsesToLoot'][0]
                context['tasksOrchestrator'].setRootTask(
                    context, LootCorpseTask(firstDeadCorpse))
            context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
            return context
        hasCreaturesToAttackAfterCheck = hasCreaturesToAttack(context)
        if hasCreaturesToAttackAfterCheck:
            if context['cavebot']['closestCreature'] is not None:
                context['way'] = 'cavebot'
            else:
                context['way'] = 'waypoint'
        else:
            context['way'] = 'waypoint'
        if hasCreaturesToAttackAfterCheck and shouldAskForCavebotTasks(context):
            currentRootTask = currentTask.rootTask if currentTask is not None else None
            isTryingToAttackClosestCreature = currentRootTask is not None and (
                currentRootTask.name == 'attackClosestCreature')
            if not isTryingToAttackClosestCreature:
                context = resolveCavebotTasks(context)
        elif context['way'] == 'waypoint':
            if context['tasksOrchestrator'].getCurrentTask(context) is None:
                currentWaypointIndex = context['cavebot']['waypoints']['currentIndex']
                currentWaypoint = context['cavebot']['waypoints']['items'][currentWaypointIndex]
                context['tasksOrchestrator'].setRootTask(
                    context, resolveTasksByWaypoint(currentWaypoint))
        context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
        return context
