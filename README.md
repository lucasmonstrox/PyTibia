# 📝 Description

> Fastest Tibia PixelBot developed in python to get unlocked fps.

_Read this in other languages: [English](README.md), [Brazilian Portuguese](README.pt-BR.md)._

This BOT works locating image around the screen and applies cache to avoid image redetection and thus avoid excessive cpu/gpu usage.

This BOT is all based on matrix calculation, also applies parallelism and also pre-processing, as it is the only way to have maximum performance(nanoseconds/microseconds).

This BOT also uses data structure, arrays, path finding, among other important things to have smart decisions and gameplay.

This BOT walks by keyboard and make human mouse movimentation.

I created this BOT to learn python, to stream on twitch, to make friends, to apply my knowledgments in deep learning, path finding, matrix, etc.

I'm not going to sell subscription to this BOT, but it will work on "global" and you can use it, it's at your own risk.

This BOT ins't ready yet, this BOT still under construction.

Be free to use any function to create your custom BOT or wait for the release of v0.

# 🗺️ Features

Only available for knight/paladin

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

# ⚽ Goals

- Detect every necessary information in the client in (milli/macro/nano)seconds
- Control every pixel of the mouse to make human movements
- Use convolutionals neural networks to detect relevant stuffs like blockable objects, dropped loots, etc
- Use recurrent neural networks to use natural language processing to chat with others players
- Crack kernel or put tibia working in a sub system to avoid BE detections
- Make party gameplay
- Make a guild gameplay, start a war and dominate a tibia server
- Raise money and send $ to help my Venezuelan friends who are experiencing economic difficulties

# 🦾 A great working bot until PyTibia is ready

BearSharp is an excellent paid bot made by a friend, you can find him via discord through the link https://discord.gg/kaKgkNxNtD

# 🧰 Installation

## Prerequisites

- Python 3.9.13
- Poetry >=1.2.0

Install packages before continue

```bash
pip install poetry
poetry install
```

# ⌨ Development

## ⚙ Running the app

```bash
poetry run python main.py
```

## 🧪 Running tests

```bash
# unit tests
poetry run python -m pytest
```

# ✅ TODO

- Translate README for Spanish language
- Add api docs
- Publish api docs to github pages
- Add mypy
- Add mypy to CI
- Add unit tests to CI

# 👷 Authors

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Owner & Developer
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Developer
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Tester
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Tibia mentor
- [**evitarafadiga**](http://github.com/evitarafadiga) - Software Architect

See also the list of [contributors](../../graphs/contributors) who participated
in this project.

If you want to become a contributor, send a message to my [**linkedin**](https://www.linkedin.com/in/lucasmonstro/).

# ❤️ Development inspiration

A special thanks to [**Murilo Chianfa**](https://github.com/MuriloChianfa), the owner of [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). I started this bot especially to overcome [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12) slowdowns.

You can check the bot development at [https://twitch.tv/lucasmonstrocs](https://twitch.tv/lucasmonstrocs).
You can enjoy our discord through the link [https://discord.gg/HpvzwvNB](https://discord.gg/HpvzwvNB)

# 📝 License

Copyright © 2023 [**lucasmonstro**](https://github.com/lucasmonstro)  
This project is [MIT](https://opensource.org/licenses/MIT) licensed
