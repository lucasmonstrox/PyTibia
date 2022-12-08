# 📝 Descrição
> O PyTibia é o Tibia PixelBot mais rápido do mercado, desenvolvido em python para atingir unlocked fps.

*Leia também em outras línguas: [Inglês](README.md), [Português Brasileiro](README.pt-BR.md).*

O BOT trabalha localizando imagens por toda a tela e aplica o cache para ignorar a relocalização de imagens estáticas que já foram capturadas, evitando o uso excessivo de CPU/GPU.

O BOT é baseado em cálculo matricial, paralelismo, pré-processamento e cacheamento. Foi a maneira que eu encontrei para obter a performance(em nanosegundos/microsegundos) necessária e responder em tempo útil em relação ao Tibia.

O BOT utiliza estrutura de dados, vetores, *pathfinding*, etc. e outras funcionalidades importantes para tomada de decisões inteligentes durante a *gameplay*.

Eu, Lucas, criei essa orquestra de funcionalidades para aprender a linguagem de programação python, fazer *lives* na Twitch, amigos, enquanto aplico meus conhecimentos de *deep learning*, o já mencionado *pathfinding*, matrizes e mais.

Não, eu **não** pretendo vender uma assinatura para o seu uso, porém ele funcionará no "global" e você muito provavelmente poderá usá-lo, sob sua total responsabilidade.

O robô não está finalizado e passa por constantes mudanças.

Sinta-se livre para utilizar de qualquer função, criar sua própria versão ou aguardar o lançamento de uma versão inicial.

# 🗺️ Recursos

Apenas disponível para cavaleiros

- Bot de Caverna :heavy_check_mark:
- Cura :heavy_check_mark:
- Spell :heavy_check_mark:
- Target :heavy_check_mark:
- Jogabilidade pelo teclado :heavy_check_mark:
- Interface de Usuário :warning:

# ⚽ Metas

- Detecção de qualquer informação necessária no cliente em (mili/macro/nano) segundos
- Controle total sob os píxeis do mouse para a movimentação humanizada.
- Utilizar redes neurais convolucionais para detectar empecílios relevantes como objetos bloqueadores, *loot* soltas, etc.
- Utilizar redes neurais subsequentes para o uso de linguagens naturais durante o processo de interação com outros jogadores.
- *Crack* de kernel e/ou colocar o Tibia a trabalhar em um subsistema para evitar detecções BE.
- Party gameplay
- Guild gameplay, iniciar uma guerra e dominar um servidor
- Levantar fundos e ajudar meus colegas venezuelanos que estão passando por momentos difíceis

# 🧰 Instalação

## Pré-requisitos

- Python 3.9.13
- Poetry >=1.2.0

Antes de continuar instale os seguintes pacotes:

```bash
pip install poetry
poetry install
poetry run task add-torch
poetry run task add-easyocr
```

# ⌨ Desenvolvimento

## ⚙ Executando a aplicação

```bash
poetry run python main.py

# to test last experiments with mess code
poetry run python test.py
```

## 🧪 Testes de execução

```bash
# unit tests
poetry run python -m pytest
```

# ✅ TODO

- Adicionar combos de magia
- Adicionar *thread* para comer
- Adicionar método de treino
- Adicionar método de pesca
- Traduzir o README para a língua espanhola
- Adicionar a documentação da API
- Adicionar mypy
- Adicionar e2e testes no cliente Tibia
- Adicionar pytest-cov
- Adicionar python typings

# 👷 Autores

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Criador & Desenvolvedor
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Desenvolvedor
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Tester
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Desenvolvedor
- [**evitarafadiga**](http://github.com/evitarafadiga)([**linkedin**](https://www.linkedin.com/in/lazvsantos/)) - Arquiteto de Software

Veja também a lista de [contribuidores](../../graphs/contributors) participantes deste projeto.

Gostaria de fazer parte da equipe? Me contate no [**linkedin**](https://www.linkedin.com/in/lucasmonstro/).

# ❤️ Inspiração

Agradecimentos especiais ao idealista [**Murilo Chianfa**](https://github.com/MuriloChianfa), responsável pelo [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). O robô inicia-se a partir do projeto [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12).

You can check the bot development at [https://twitch.tv/lucasmonstrocs](https://twitch.tv/lucasmonstrocs).

## 📝 Licença

Copyright © 2023 [**lucasmonstro**](https://github.com/lucasmonstro)  
Este projeto contém a licença [MIT](https://opensource.org/licenses/MIT).
