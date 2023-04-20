# 📝 Descrição

> PyTibia es el Tibia PixelBot más rápido del mercado, desarrollado en python para lograr fps desbloqueados.

_Leer también en otros idiomas: [English](README.md), [Português Brasileiro](README.pt-BR.md), [Spanish](README.es-es.md)._

El BOT funciona al ubicar imágenes en toda la pantalla y aplica el almacenamiento en caché para omitir la reubicación de imágenes fijas que ya se han capturado, lo que evita el uso excesivo de CPU/GPU.

El BOT se basa en cálculo matricial, paralelismo, preprocesamiento y almacenamiento en caché. Fue la forma que encontré para obtener el rendimiento necesario (en nanosegundos/microsegundos) y responder de manera oportuna en comparación con Tibia.

El BOT utiliza estructura de datos, matrices, _pathfinding_, etc. y otras funciones importantes para tomar decisiones inteligentes durante el juego.

El BOT camina sobre el teclado y realiza movimientos humanos usando el mouse.

Yo, Lucas, creé esta orquesta de características para aprender el lenguaje de programación python, hacer _lives_ en Twitch, amigos, mientras aplicaba mis conocimientos de _aprendizaje profundo_, el mencionado _pathfinding_, matrices y más.

No, **no** tengo la intención de venderle una suscripción para su uso, sin embargo, funcionará "globalmente" y lo más probable es que pueda usarlo, bajo su propio riesgo.

El robot no está finalizado y sufre cambios constantes.

Siéntase libre de usar cualquier función, cree su propia versión o espere a que se lance una versión iniciale.

# 🗺️ Recursos

Solo disponible para caballero/paladín

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

# ⚽ Objetivos

- Detección de cualquier información necesaria sobre el cliente en (mili/macro/nano) segundos.
- Control total sobre los píxeles del mouse para un movimiento humanizado.
- Utilice la computación de visión para detectar objetos que bloqueen el camino del char.
- Usa el procesamiento del lenguaje natural para hablar con otros jugadores.
- _Descifrar_ el kernel y/o ejecutar Tibia en un subsistema para evitar las detecciones de BattleEye.
- Juego de fiesta.
- Juego de gremios, comienza una guerra y domina un servidor.
- Recaudar fondos y ayudar a mis compatriotas venezolanos que están pasando por momentos difíciles.

# 🦾 Otro excelente bot mientras PyTibia no está listo

BearSharp es un excelente bot hecho por un amigo y ya esta funcionando, puedes hablar con el por discord https://discord.gg/kaKgkNxNtD

# 🧰 Instalación

## requisitos previos

- Python 3.9.13
- Poetry >=1.2.0

Antes de continuar, instale los siguientes paquetes:

```bash
pip install poetry
poetry install
```

# ⌨ Desarrollo

## ⚙ Ejecutando la aplicación

```bash
poetry run python main.py
```

## 🧪 Pruebas de ejecución

```bash
# unit tests
poetry run python -m pytest
```

# ✅ TODO

- Agregar documentación de la API
- añadir mypy
- Agregar pruebas e2e en el cliente de Tibia

# 👷 Autores

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Creador y desarrollador
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Desarrollador
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/ )) - Probador
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Mentor de Tibia
- [**evitarafadiga**](http://github.com/evitarafadiga)([**linkedin**](https://www.linkedin.com/in/lazvsantos/)) - Arquitecto de software

Consulte también la lista de [colaboradores](../../graphs/contributors) que participan en este proyecto.

¿Te gustaría ser parte del equipo? Contáctame en [**linkedin**](https://www.linkedin.com/in/lucasmonstro/).

# ❤️ Inspiracción

Un agradecimiento especial a [**Murilo Chianfa**](https://github.com/MuriloChianfa), responsable de [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). Inicié el bot para resolver problemas que no se resolvieron en [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12).

Puedes seguir el desarrollo del bot en mi transmisión [https://twitch.tv/lucasmonstrocs](https://twitch.tv/lucasmonstrocs).
Puedes unirte a nuestro discordia a través del enlace [https://discord.gg/HpvzwvNB](https://discord.gg/HpvzwvNB)

## 📝 Licencia

Copyright © 2023 [**lucasmonstro**](https://github.com/lucasmonstro)  
Este proyecto está autorizado bajo la licencia [MIT](https://opensource.org/licenses/MIT).