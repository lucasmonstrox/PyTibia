from src.gameplay.core.tasks.orchestrator import TasksOrchestrator
from src.gameplay.core.tasks.common.base import BaseTask
from src.gameplay.core.tasks.common.vector import VectorTask
from src.gameplay.core.tasks.walkToWaypoint import WalkToWaypoint
import timeit
import numpy as np
from src.repositories.battleList.typings import Creature as BattleListCreature
from src.repositories.gameWindow.typings import Creature as GameWindowCreature
from src.repositories.radar.typings import Coordinate, Waypoint

class SetNextWaypointTask(BaseTask):
    def __init__(self):
        super().__init__()

    def do(self, context):
        print('set next waypoint')

class SayTask(BaseTask):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def do(self, _):
        print(self.text)

    def did(self, _):
        return True

class DepositGoldTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'depositGold'

    def initialize(self, context):
        self.tasks = [
            SayTask('hi').setParentTask(self),
            SayTask('deposit all').setParentTask(self),
            SayTask('yes').setParentTask(self),
        ]
        self.initialized = True
        return self

class DepositGoldWaypointTask(VectorTask):
    def __init__(self):
        super().__init__()
        self.name = 'depositGoldWaypoint'

    def initialize(self, context):
        self.tasks = [
            DepositGoldTask().setParentTask(self),
            SetNextWaypointTask().setParentTask(self),
        ]
        self.initialized = True
        return self

tasksOrchestratorInstance = TasksOrchestrator(WalkToWaypoint([33211, 32449, 7]))

context = {
    'cavebot': {
        'enabled': True,
        'holesOrStairs': [],
        'isAttackingSomeCreature': False,
        'previousTargetCreature': None,
        'targetCreature': None,
        'waypoints': {
            'currentIndex': 0,
            'points': np.array([
                ('', 'walk', (33211, 32449, 7), {}),
                ('', 'walk', (33217, 32450, 7), {}),
                ('', 'walk', (33215, 32446, 7), {}),
            ], dtype=Waypoint)
        }
    },
    'radar': {
        'coordinate': [33206, 32447, 7],
        'lastCoordinateVisited': None
    }
}

res = timeit.repeat(lambda: tasksOrchestratorInstance.do(context), repeat=10, number=1)


# # print('11111')
# # fazer tarefa
# context = tasksOrchestratorInstance.do(context)
# # verificar se tarefa foi feita, se sim, passa para a proxima
# context = tasksOrchestratorInstance.do(context)
# # print('22222')
# # fazer tarefa
# context = tasksOrchestratorInstance.do(context)
# # verificar se tarefa foi feita, se sim, passa para a proxima
# context = tasksOrchestratorInstance.do(context)
# # print('33333')
# # fazer tarefa
# context = tasksOrchestratorInstance.do(context)
# # verificar se tarefa foi feita, se sim, passa para a proxima
# context = tasksOrchestratorInstance.do(context)
# # print('44444')
# # fazer tarefa
# context = tasksOrchestratorInstance.do(context)
# # verificar se tarefa foi feita, se sim, passa para a proxima
# context = tasksOrchestratorInstance.do(context)

# print(' ')
# print('1. tasksOrTask', tasksOrchestratorInstance.tasksOrTask, tasksOrchestratorInstance.tasksOrTask.status, tasksOrchestratorInstance.tasksOrTask.currentTaskIndex)
# print('1.1. tasksOrTask.tasks[0]', tasksOrchestratorInstance.tasksOrTask.tasks[0], tasksOrchestratorInstance.tasksOrTask.tasks[0].status, tasksOrchestratorInstance.tasksOrTask.tasks[0].currentTaskIndex)
# print('1.1.1 tasksOrTask.tasks[0].tasks[0]', tasksOrchestratorInstance.tasksOrTask.tasks[0].tasks[0], tasksOrchestratorInstance.tasksOrTask.tasks[0].tasks[0].status)
# print('1.1.2 tasksOrTask.tasks[0].tasks[1]', tasksOrchestratorInstance.tasksOrTask.tasks[0].tasks[1], tasksOrchestratorInstance.tasksOrTask.tasks[0].tasks[1].status)
# print('1.1.3 tasksOrTask.tasks[0].tasks[2]', tasksOrchestratorInstance.tasksOrTask.tasks[0].tasks[2], tasksOrchestratorInstance.tasksOrTask.tasks[0].tasks[2].status)
# print('1.2. tasksOrTask.tasks[1]', tasksOrchestratorInstance.tasksOrTask.tasks[1], tasksOrchestratorInstance.tasksOrTask.tasks[1].status)
# context = tasksOrchestratorInstance.do(context)
# print('tasksOrchestratorInstance.tasksIndexes', tasksOrchestratorInstance.tasksIndexes)


# [
#     VectorTask(
#         VectorTask(
#             SimpleTask(),
#             SimpleTask(),
#         ),
#         SimpleTask(),
#         SimpleTask(),
#     ),
#     SimpleTask()
# ]