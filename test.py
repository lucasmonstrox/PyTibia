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
import timeit

pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0


def main():
    global context

    def handleGameData(context):
        context = setTibiaWindowMiddleware(context)
        context = setScreenshotMiddleware(context)
        context = setRadarMiddleware(context)
        context = setChatTabsMiddleware(context)
        context = setBattleListMiddleware(context)
        context = setGameWindowMiddleware(context)
        context = setDirectionMiddleware(context)
        context = setGameWindowCreaturesMiddleware(context)
        # context = setHandleLootMiddleware(context)
        return context

    res = timeit.repeat(lambda: handleGameData(context), repeat=10, number=1)
    print('res', res)


if __name__ == '__main__':
    main()
