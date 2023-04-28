# 📝 Descripción

> El PixelBot de Tibia más rápido desarrollado en Python para obtener fps desbloqueados.

_Lee esto en otros idiomas: [Inglés](README.md), [Portugués de Brasil](README.pt-BR.md)._

Este BOT funciona ubicando imágenes en la pantalla y aplica caché para evitar la redetección de imágenes y, de esta manera, evitar el uso excesivo de CPU/GPU.

Este BOT se basa en cálculos matriciales, también aplica paralelismo y preprocesamiento, ya que es la única forma de obtener el máximo rendimiento (nanosegundos/microsegundos).

Este BOT también utiliza estructuras de datos, matrices, búsqueda de caminos, entre otras cosas importantes para tomar decisiones inteligentes y un juego efectivo.

El BOT se desplaza mediante el teclado y realiza movimientos del ratón similares a los humanos.

Creé este BOT para aprender Python, hacer transmisiones en Twitch, hacer amigos y aplicar mis conocimientos en aprendizaje profundo, búsqueda de caminos, matrices, etc.

No venderé suscripciones a este BOT, pero funcionará en "global" y puedes utilizarlo bajo tu propio riesgo.

Este BOT aún no está listo, se encuentra en construcción.

Siéntete libre de usar cualquier función para crear tu BOT personalizado o esperar el lanzamiento de la versión 0.

# 🗺️ Funcionalidades

Disponible únicamente para caballeros/paladines

| Funcionalidades           | Completado         |
| ------------------------- | ------------------ |
| Alertas                   | :x:                |
| Inicio de sesión automático| :x:                |
| Anillo automático         | :x:                |
| Guardado automático en servidor| :x:                |
| Cavebot                   | :heavy_check_mark: |
| Hechizos combinados       | :heavy_check_mark: |
| Desechar frascos          | :heavy_check_mark: |
| Depósito de oro           | :heavy_check_mark: |
| Depósito de objetos no apilables| :heavy_check_mark: |
| Depósito de objetos apilables| :heavy_check_mark: |
| Pescar                    | :x:                |
| Comedor de alimentos      | :heavy_check_mark: |
| Curación                  | :heavy_check_mark: |
| Selección de objetivos inteligente| :heavy_check_mark: |
| Recarga                   | :heavy_check_mark: |
| Saqueo rápido             | :heavy_check_mark: |
| Vender frascos            | :x:                |
| Vender objetos            | :x:                |
| Entrenar                  | :x:                |

# ⚽ Objetivos

- Detectar toda la información necesaria en el cliente en (mili/macro/nano)segundos
- Controlar cada píxel del ratón para realizar movimientos humanos
- Utilizar redes neuronales convolucionales para detectar elementos relevantes como objetos bloqueables, botines caídos, etc.
- Emplear redes neuronales recurrentes para procesar lenguaje natural y chatear con otros jugadores
- Romper el núcleo o hacer que Tibia funcione en un subsistema para evitar detecciones de BE
- Realizar un juego en grupo
- Desarrollar un juego de gremios, comenzar una guerra y dominar un servidor de Tibia
- Recaudar dinero y enviarlo a mis amigos venezolanos que enfrentan dificultades económicas

# 🦾 Un excelente bot en funcionamiento hasta que PyTibia esté listo

BearSharp es un bot de pago extraordinario creado por un amigo, puedes encontrarlo a través de Discord mediante el enlace https://discord.gg/kaKgkNxNtD

# 🧰 Instalación

## Prerrequisitos

- Python 3.9.13
- Poetry >=1.2.0

Instalar paquetes antes de continuar

```bash
pip install poetry
poetry install
```

# ⌨ Desarrollo

## ⚙ Ejecución de la aplicación
```bash
poetry run python main.py
```

## 🧪 Ejecución de pruebas
```bash
# pruebas unitarias
poetry run python -m pytest
```

# ✅ Pendientes

- Añadir documentación de la API
- Añadir documentación de la API (páginas de GitHub) al despliegue en CI
- Incorporar mypy
- Añadir mypy a CI
- Añadir pruebas unitarias a CI
- Añadir adaptador de captura de pantalla en Linux
- Aplicar patrón de máquina de estados para gestionar tareas

# 👷 Autores

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Propietario y Desarrollador
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Desarrollador
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Probador
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Mentor de Tibia
- [**evitarafadiga**](http://github.com/evitarafadiga) - Arquitecto de software

Consulta también la lista de [colaboradores](../../graphs/contributors) que participaron
en este proyecto.

Si deseas convertirte en colaborador, envía un mensaje a mi [**linkedin**](https://www.linkedin.com/in/lucasmonstro/).

# ❤️ Inspiración para el desarrollo

Un agradecimiento especial a [**Murilo Chianfa**](https://github.com/MuriloChianfa), propietario de [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). Comencé este bot especialmente para superar las ralentizaciones de [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12).

Puedes ver el desarrollo del bot en [https://twitch.tv/lucasmonstrocs](https://twitch.tv/lucasmonstrocs).
Disfruta de nuestro Discord a través del enlace [https://discord.gg/HpvzwvNB](https://discord.gg/HpvzwvNB)

# 📝 Licencia

Derechos de autor © 2023 [**lucasmonstro**](https://github.com/lucasmonstro)  
Este proyecto tiene licencia [MIT](https://opensource.org/licenses/MIT)



