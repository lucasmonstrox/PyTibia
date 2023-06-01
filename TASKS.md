# Orquestrador de tarefas

## Tipos de tarefa:

- Simples
- Sequencia(Vetor estático) vs Sequencia(Vetor estático porém calculado na hora de instanciar a tarefa)
- Repetição

As tarefas em sequencia podem ter sub tarefas de todos os tipos, simples, sequencia tambem e repetição.

## As tarefas podem ter alguns hooks e métodos:

- shouldIgnore(Verificar se é para ignorar a tarefa)
- do(método que executa a tarefa)
- did(verifica se a tarefa foi feita)
- shouldRestart(verifica se é preciso reiniciar a tarefa)
- afterRestart(método que executa depois de reiniciar a tarefa)
- onIgnore(callback quando a tarefa é ignorada)
- onFinish(callback quando a tarefa é completada)
- onTimeout(callback quando a tarefa é timedout)
- onRestart(callback quando a tarefa é reiniciada)
- onInterrupt(callback quando a tarefa é interrompida)

## Atributos de tarefas pode ter alguns atributos:

- createdAt(data de criação)
- startedAt(data de início)
- finishedAt(data de finalização)
- delayBeforeStart(delay antes de iniciar a tarefa)
- delayAfterComplete(delay depois de completar a tarefa, aqui só passa para a próxima tarefa depois do delay)
- delayAfterCheck(delay para verificar se a tarefa foi concluida)
- status(notStarted, almostComplete, finished, ignored, timedout, restarted)
- terminable(Se a tarefa pode ser concluida e movida para a próxima)
- shouldAborTree(Se a tarefa deve abortar a árvore de tarefas)

## Extras

- As tarefas podem ser interrompidas(pensar como implementar isso)
- O que fazer quando as tarefas precisam ser recalculadas(ex: FollowCreature, GoToCoordinate)?
  R: Usar o shouldRestart para isso e o afterRestart para recalcular
- As tasks pode saber quem são as tasks irmãs da esquerda e as tasks irmãs da direita
- Se a task filha der timeout, todas as pais/avos/bisavos irão dar timeout também
- A task em forma de vector nao tem "do", uma vez que as sub tarefas tem "do"

## Exemplo de tarefa simples:

- use
- clickInCoordinate(herdar de "use". Mesmo que clicar num slot)
- moveDown/moveUp(herdar de singleWalk?)
- openBackpack
- openDepot(herdar de "use")
- openDoor(herdar de "use")
- openLocker(herdar de "use")
- pauseBot
- pressLogoutKeys
- refillChecker
- selectChatTab
- setChatOff
- singleWalkPress(herdar de useHotkey?)
- useHole(herdar de "use")
- useHotkey
- useHole(herdar de "use")
- useRope(clicar na hotkey + slot = Deveria ser sequencial)
- useShovel(clicar na hotkey + slot = Deveria ser sequencial)

## Exemplo de tarefa sequencial:

- buyItem
- depoitGold(say("hi"), say("deposit all"), say("yes")) 3 tarefas
- say -> A escrita de cada letra é uma tarefa -> N tarefas, mas em sequência
- lootCorpse(walkToCoordinate(), rightClickInCoordinate) - 2 tarefas sendo a primeiro uma sequencia de tarefas, ou seja, task multidimensional
- walkToCoordinate -> Cada passo é uma tarefa, porém é possível recalcular a rota caso algum obstáculo apareça.
- useRopeWaypoint(useRope, setNextWaypoint) 2 tarefas
- useShovelWaypoint(useShovel, clickInCoordinate, setNextWaypoint) 3 tarefas

## Exemplo de tarefas de repetição:

- scrollToItem

- cenário atual que até o depot pode estar cheio
  -- ter um hook a qualquer momento que consiga saber os depots que estão visiveis e livres e mudar a rota
  -- gerar caminho até avistar a proxima coordenada e andar
  -- ha qualquer momento alguem pode entrar na coordenada que estou indo, entao abortar e marcar coordenada como ocupada

  SimpleTask

  VetorTask [
  say('hi'),
  say('deposit all'),
  say('yes'),
  ]

  RepetitiveTask
