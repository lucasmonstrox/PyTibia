# 📝 Description

> Fastest Tibia PixelBot developed in python to get unlocked fps.

This bot memorizes and applies cache to detect images and thus avoid excessive cpu/gpu usage.

This bot is all based on matrix calculation, applies parallelism and also pre-processing, as it is the only way to have maximum performance.

This bot also uses data structure, arrays, path finding(djkistra), among other important things to have smart gameplay.

# 🗺️ MVP Features Status

- ActionBar:
  - Counting slots :heavy_check_mark:
- BattleList:
  - [Getting monsters](battleList/docs/README.md) :heavy_check_mark:
  - [Checking if monster is being attacked](battleList/docs/README.md) :heavy_check_mark:
  - Is attacking any creature :heavy_check_mark:
- Cavebot:
  - Attacking closest creature :heavy_check_mark:
  - Ignoring non target monsters :heavy_check_mark:
  - Resume coordinate :heavy_check_mark:
  - Retarget to another creature when current target is non attackable :warning:
- Chat:
  - Check if Server Log is selected :warning:
  - Talk to NPC's to trade :warning:
- Equipment:
  - Count cap :warning:
- Loot:
  - Get dead monsters by player :warning:
    - Parse server logs message to get loot notification :warning:
  - Collect loot :warning:
    - When hunting, go to dead monster to collect :warning:
    - Detect container full :warning:
- Healing:
  - Spell :heavy_check_mark:
  - Potion :heavy_check_mark:
- HUD:
  - Getting coordinates(playable area) :heavy_check_mark:
  - Getting Monsters :heavy_check_mark:
- Radar:
  - Floor level :heavy_check_mark:
  - Tracking coordinates :heavy_check_mark:
- Refill:
  - Deposit items in depot :warning:
  - Detect trade container :warning:
  - Scroll until icon is detected :warning:
  - Buy necessary quantity of icon :warning:
- Spell:
  - Apply exori when there are a certain number of monsters around :heavy_check_mark:
  - Getting spells cooldowns :warning:
- Status:
  - Getting Life :heavy_check_mark:
  - Getting Mana :heavy_check_mark:

# ⌨ Development

## ⚙ Running the app

```bash
# main file to track basic functions output like(is burning, has helmet equipped, etc)
python main.py

# to test last experiments with mess code
python test.py
```

# 👷 Authors

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Owner & Developer
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Developer
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Tester

See also the list of [contributors](../../graphs/contributors) who participated
in this project

# ❤️ Development inspiration

A special thanks to [**Murilo Chianfa**](https://github.com/MuriloChianfa) the owner of [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). I started this bot to overcome [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12) slowdowns.

# 📝 License

Copyright © 2021 [**lucasmonstro**](https://github.com/lucasmonstro)  
This project is [MIT](https://opensource.org/licenses/MIT) licensed
