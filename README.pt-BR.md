# Sumário
- [Descrição](#descrição)
    - [Recursos](#recursos)
    - [Metas](#metas)
- [Instalação](#instalação)
    - [Pré-requisitos](#pré-requisitos)
- [Desenvolvimento](#desenvolvimento)
    - [Executando a Aplicação](#executando-a-aplicação)
    - [Testes de execução](#testes-de-execução)
- [Inspiração](#inspiração)
- [Licença](#licença)

# Descrição
> O Robô Tibia PixelBot mais rápido, desenvolvido em python afim de um fps fluido.

*Leia também em outras línguas: [Inglês](README.md), [Português Brasileiro](README.pt-BR.md).*

Este Robô trabalha localizando imagens por toda a tela enquanto aplica o cache dessas, evitando redetecção de imagens já capturadas e uso excessivo de CPU/GPU.

Ele ainda é baseado em cálculo de matriz, incluindo o paralelismo e pré-processamento, como sendo a única maneira de obter máxima performance(em nanosegundos/microsegundos).

O PyTibia PixelBot utiliza estrutura de dados, vetores, *pathfinding*, etc. acerca de outras funcionalidades importantes para tomada de decisões inteligentes durante a *gameplay*.

Eu, Lucas, criei essa orquestra de funcionalidades para aprender a linguagem de programação python, fazer *lives* na Twitch, amigos, enquanto aplico meus conhecimentos de *deep learning*, o já mencionado *pathfinding*, matrizes e mais.

Não, eu **não** pretendo vender uma assinatura para o seu uso, porém ele funcionará no "global" e você muito provavelmente poderá usá-lo, sob sua total responsabilidade.

O robô não está finalizado e passa por constantes mudanças.

Sinta-se livre para utilizar de qualquer função, criar sua própria versão ou aguardar o lançamento de uma versão inicial.

# Recursos

Apenas disponível para cavaleiros

- Bot de Caverna :heavy_check_mark:
- Cura :heavy_check_mark:
- Magia :heavy_check_mark:
- Alvo :heavy_check_mark:
- Gameplay via teclado :heavy_check_mark:
- Interface de Usuário :warning:

# Metas

- Detecção de qualquer informação necessária no cliente em (mili/macro/nano) segundos.
- Controle total sob os píxeis do mouse para a movimentação humanizada.
- Utilizar redes neurais convolucionais para detectar empecílios relevantes como objetos bloqueadores, *loot* soltas, etc.
- Utilizar redes neurais subsequentes para o uso de linguagens naturais durante o processo de interação com outros jogadores.
- *Crack* de kernel e/ou colocar o Tibia a trabalhar em um subsistema para evitar detecções BE.
- Gameplay multijogador.
- Gameplay de guilda, iniciando guerras e dominando servidores inteiros.
- Levantar fundos e ajudar meus colegas venezuelanos quais estão passando por momentos difíceis.

# Instalação

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

# Desenvolvimento

## Executando a aplicação

```bash
poetry run python main.py

# to test last experiments with mess code
poetry run python test.py
```

## Testes de execução

```bash
# unit tests
poetry run python -m pytest
```

# TODO

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

# Autores

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Criador & Desenvolvedor
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Desenvolvedor
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Tester
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Desenvolvedor
- [**evitarafadiga**](http://github.com/evitarafadiga) - Arquiteto de Software

Veja também a lista de [contribuidores](../../graphs/contributors) participantes deste projeto.

Gostaria de fazer parte da equipe? Me contate no [**linkedin**](https://www.linkedin.com/in/lucasmonstro/).

# Inspiração

Agradecimentos especiais ao idealista [**Murilo Chianfa**](https://github.com/MuriloChianfa), responsável pelo [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). O robô inicia-se a partir do projeto [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12).

You can check the bot development at [https://twitch.tv/lucasmonstrocs](https://twitch.tv/lucasmonstrocs).

## Licença

Copyright © 2023 [**lucasmonstro**](https://github.com/lucasmonstro)  
Este projeto contém a licença [MIT](https://opensource.org/licenses/MIT).
