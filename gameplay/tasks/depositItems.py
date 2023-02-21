from ..factories.makeOpenBackpackTask import makeOpenBackpackTask
from .decisionTask import DecisionTask


# abrir backpack principal
# -- se nao abrir em x tentativas, deve alertar o usuário
# expandir backpack principal até encontrar a backpack de loot
# -- se nao encontrar, deve alertar o usuário
# abrir a backpack de loot
# verificar se tem loot, e se tiver loot:
#  - iterar até encontrar um depot vazio
#  -- caso nao encontre, dar um delay ou verificar se alguém sai do depot
#  - abrir locker
#  - abrir depot
#  - iterar nos itens de loot e jogar um de cada vez no depot selecionado
#  - fechar backpack de loot
#  - fechar backpack principal
#  - marcar waypoint como concluido
# se não tiver loot:
#  - marcar waypoint como concluído
class DepositItemsTask(DecisionTask):
    def __init__(self, context, waypoint):
        super().__init__(
            makeOpenBackpackTask(context['backpacks']['main']),
            makeOpenBackpackTask(context['backpacks']['loot']),
        )
        self.name = 'depositItems'
        self.value = waypoint

    def exec(self, context):
        return super().exec(context)