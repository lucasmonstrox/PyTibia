# 📝 Descrição

> O PyTibia é o Tibia PixelBot mais rápido do mercado, desenvolvido em python para atingir unlocked fps.

_Leia também em outras línguas: [Inglês](README.md), [Português Brasileiro](README.pt-BR.md)._

O BOT trabalha localizando imagens por toda a tela e aplica o cache para ignorar a relocalização de imagens estáticas que já foram capturadas, evitando o uso excessivo de CPU/GPU.

O BOT é baseado em cálculo matricial, paralelismo, pré-processamento e cacheamento. Foi a maneira que eu encontrei para obter a performance(em nanosegundos/microsegundos) necessária e responder em tempo útil em relação ao Tibia.

O BOT utiliza estrutura de dados, vetores, _pathfinding_, etc. e outras funcionalidades importantes para tomada de decisões inteligentes durante a _gameplay_.

O BOT anda pelo teclado e faz movimentação humana através do mouse.

Eu, Lucas, criei essa orquestra de funcionalidades para aprender a linguagem de programação python, fazer _lives_ na Twitch, amigos, enquanto aplico meus conhecimentos de _deep learning_, o já mencionado _pathfinding_, matrizes e mais.

Não, eu **não** pretendo vender uma assinatura para o seu uso, porém ele funcionará no "global" e você muito provavelmente poderá usá-lo, sob sua total responsabilidade.

O BOT não está finalizado e passa por constantes mudanças.

Sinta-se livre para utilizar de qualquer função, criar sua própria versão ou aguardar o lançamento de uma versão inicial.

# 🗺️ Recursos

Apenas disponível para knight/palaldin

| Features                  | Done               |
| ------------------------- | ------------------ |
| Alerts                    | :x:                |
| Auto login                | :x:                |
| Auto ring                 | :x:                |
| Auto server save          | :x:                |
| Cavebot                   | :heavy_check_mark: |
| Combo Spells              | :heavy_check_mark: |
| Drop flasks               | :heavy_check_mark: |
| Deposit gold              | :heavy_check_mark: |
| Deposit non stacked items | :heavy_check_mark: |
| Deposit stacked items     | :heavy_check_mark: |
| Fish                      | :x:                |
| Food eater                | :heavy_check_mark: |
| Healing                   | :heavy_check_mark: |
| Smart Targeting           | :heavy_check_mark: |
| Refill                    | :heavy_check_mark: |
| Quick loot                | :heavy_check_mark: |
| Sell flasks               | :x:                |
| Sell items                | :x:                |
| Train                     | :x:                |

# ⚽ Metas

- Detecção de qualquer informação necessária no cliente em (mili/macro/nano) segundos.
- Controle total sob os píxeis do mouse para a movimentação humanizada.
- Utilizar computação visional para detectar objetos que bloqueiam o caminho do char.
- Utilizar processamento de linguagem natural para falar com outros jogadores.
- _Crackear_ o kernel e/ou colocar o Tibia a trabalhar em um subsistema para evitar detecções do BattleEye.
- Party gameplay.
- Guild gameplay, iniciar uma guerra e dominar um servidor.
- Levantar fundos e ajudar meus colegas venezuelanos que estão passando por momentos difíceis.

# 🧰 Instalação

## Pré-requisitos

- [`Python`](https://www.python.org/downloads/release/python-3913) 3.9.13
- [`Poetry`](https://python-poetry.org/docs/#installation) >=1.2.0

Antes de continuar instale os seguintes pacotes:

```bash
poetry install
```

# ⌨ Desenvolvimento

## ⚙ Executando a aplicação

```bash
poetry run python main.py
```

## 🧪 Testes de execução

```bash
# testes unitários
poetry run python -m pytest

# testes unitários com cobertura de teste
poetry run python -m pytest --cov=src
```

# ✅ TODO

- Traduzir o README para a língua espanhola
- Adicionar api docs
- Adicionar deploy da apidocs(github pages) no CI
- Adicionar mypy
- Adicionar mypy na CI
- Adicionar testes unitários na CI
- Adicionar adaptador de screenshot no linux

# 👷 Autores

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Criador & Desenvolvedor
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Desenvolvedor
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Tester
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Tibia mentor
- [**evitarafadiga**](http://github.com/evitarafadiga)([**linkedin**](https://www.linkedin.com/in/lazvsantos/)) - Arquiteto de Software

Veja também a lista de [contribuidores](../../graphs/contributors) participantes deste projeto.

Gostaria de fazer parte da equipe? Me contate no [**linkedin**](https://www.linkedin.com/in/lucasmonstro/).

# ❤️ Inspiração

Agradecimentos especiais ao [**Murilo Chianfa**](https://github.com/MuriloChianfa), responsável pelo [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). Eu iniciei o bot para resolver problemas que não foram resolvidos no [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12).

Você pode acompanhar o desenvolvimento do bot na minha stream [https://twitch.tv/lucasmonstrocs](https://twitch.tv/lucasmonstrocs).
Você pode entrar no nosso discord através do link [https://discord.gg/TP4axAca6a](https://discord.gg/TP4axAca6a)

## 📝 Licença

Copyright © 2023 [**lucasmonstro**](https://github.com/lucasmonstro)  
Este projeto contém a licença [MIT](https://opensource.org/licenses/MIT).
