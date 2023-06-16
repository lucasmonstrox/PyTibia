# import kivy.context
import pyautogui
from time import sleep, time
from src.gameplay.cavebot import resolveCavebotTasks, shouldAskForCavebotTasks
from src.gameplay.context import context
from src.gameplay.combo import comboSpellsObserver
from src.gameplay.core.load import loadConfigByJson, loadContextFromConfig
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
# from src.ui.context import GameContext
# from src.ui.app import MyApp


pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def main():
    global context

    def handleGameData(context):
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

    def handleGameplayTasks(context):
        # TODO: mover isso fora daqui
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
                currentWaypoint = context['cavebot']['waypoints']['points'][currentWaypointIndex]
                context['tasksOrchestrator'].setRootTask(
                    context, resolveTasksByWaypoint(currentWaypoint))
        context['gameWindow']['previousMonsters'] = context['gameWindow']['monsters']
        return context

    try:
        # kivy.context.register_context('game', GameContext, context)
        # MyApp().run()
        config = loadConfigByJson('config.json')
        context = loadContextFromConfig(config, context)
        while True:
            if context['pause']:
                continue
            startTime = time()
            context = handleGameData(context)
            context = handleGameplayTasks(context)
            context = context['tasksOrchestrator'].do(context)
            context['radar']['lastCoordinateVisited'] = context['radar']['coordinate']
            healingByPotionsObserver(context)
            comboSpellsObserver(context)
            endTime = time()
            diff = endTime - startTime
            sleep(max(0.045 - diff, 0))
    except KeyboardInterrupt:
        raise SystemExit


if __name__ == '__main__':
    main()
