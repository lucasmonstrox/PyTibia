# 📝 Description

> Fastest Tibia PixelBot developed in python to get unlocked fps.

This bot memorizes and applies cache to detect images and thus avoid excessive cpu/gpu usage.

This bot is all based on matrix calculation, applies parallelism and also pre-processing, as it is the only way to have maximum performance.

This bot also uses data structure, arrays, path finding(djkistra), among other important things to have smart gameplay.

# 🗺️ MVP Features Status

- ActionBar:
  - Counting slots :heavy_check_mark:
  - Getting cooldowns for knight:
    - attack :heavy_check_mark:
    - exori :heavy_check_mark:
    - exori mas :heavy_check_mark:
    - exori gran :heavy_check_mark:
- BattleList:
  - [Getting monsters](battleList/docs/README.md) :heavy_check_mark:
  - [Checking if monster is being attacked](battleList/docs/README.md) :heavy_check_mark:
  - Is attacking any creature :heavy_check_mark:
- Cavebot:
  - Attacking closest creature :heavy_check_mark:
  - Ignoring non target monsters :heavy_check_mark:
  - Resume coordinate :heavy_check_mark:
  - Retarget to another creature when current target is non attackable :heavy_check_mark:
  - Start attacking creature with less life :warning:
- Chat:
  - Check if Server Log is selected :heavy_check_mark:
  - Talk to NPC's to trade :heavy_check_mark:
- Equipment:
  - Count cap :heavy_check_mark:
  - Auto ring :heavy_check_mark:
- Loot:
  - Get dead monsters by player
    - Parse server logs message to get loot notification :heavy_check_mark:
    - Get dead monster by target :heavy_check_mark:
    - Get dead monster by exori :heavy_check_mark:
  - Collect loot :warning:
    - When hunting, go to dead monster to collect :warning:
    - Detect container full :heavy_check_mark:
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
  - Deposit items in depot :heavy_check_mark:
  - Detect trade container :heavy_check_mark:
  - Scroll until icon is detected :heavy_check_mark:
  - Buy necessary quantity of icon :heavy_check_mark:
- Spell:
  - Apply exori when there are a certain number of monsters around :heavy_check_mark:
- Status:
  - Getting Life :heavy_check_mark:
  - Getting Mana :heavy_check_mark:

# ⚙ Tibia Client Settings

<p align="center">
      This SDK needs Tibia's screen to be as clean as possible, as it works by searching every pixel on the screen.
      First of all, open the tibia menu and select the enable the option "Show Advanced Option".
  </p><br />
  <details>
  <summary><strong>Menu Setup</strong></summary><br />
    <strong>Go for Interface option and set change as image below</strong>
    <ul>
      <li>Disable "Use Native Mouse Cursor".</li>
      <li>Disable "Show Big Mouse Cursor".</li>
    </ul>
    <p align="center">
      <img src="/docs/images/foto1.png " alt="Image from interface"  width="600" />
    </p><br />
        <strong>Now you to go on Interface/HUD option and set change as image below</strong>
    <ul>
      <li>Disable "Show HUD for own character".</li>
      <li>Disable "Show Costumisable Bars".</li>
    </ul>
    <p align="center">
      <img src="/docs/images/foto2.png " alt="Image from HUD"  width="600" />
    </p><br />
    <strong>Go for Game Window option and set change as image below</strong>
    <ul>
      <li>Disable "Show Textual Effects".</li>
      <li>Disable "Show Messages".</li>
      <li>Disable "Show Private Messages".</li>
      <li>Disable "Show Potion Sound Effects".</li>
      <li>Disable "Show Spells Of Others".</li>
      <li>Disable "Show Hotkey Usage Notifications".</li>
      <li>Disable  "Show Loot Messages".</li>
      <li>Disable  "Show Boosted Creature".</li>
      <li>Disable  "Show Offiline Tranning Progress".</li>
      <li>Disable  "Show Store Notifications in Combat Tranning".</li>
      <li>Enable "Show Combat Frames".</li>
      <li>Enable "Show PvP Frames".</li>
      <li>Enable "Scale Using Only Integral Mutiples".</li>
    </ul>
    <strong> YOU NEED HAVE ATTENCTION ON THIS FEATURE, YOU NEED THIS FOR SET RIGHT RESOLUTION, WHO SDK WORK</strong>.
    <p align="center">
      <img src="/docs/images/foto3.png " alt="Image from Game Window"  width="600" />
    </p><br />
    <strong>Now you to go on Interface/Action Bars option and set change as image below</strong>
    <ul>
      <li>Disable "Show Coldown in Seconds".</li>
      <li>Disable "Show Action Button Toltip".</li>
    </ul>
    <p align="center">
      <img src="/docs/images/foto4.png " alt="Image from Action"  width="600" />
    </p><br />
  </details> 
  <details>
    <summary><strong>Screen Setup</strong></summary><br />
    <p align="center">
      <strong>This Show how you setup your screen for SDK working correct</strong>
    </p>
    <p align="center">
      <img src="/docs/images/foto5.png " alt="Image from Battlelist"  width="300" />
    </p><br />
    <p align="center">
      <strong>Set your BattleList to show only monsters like you see on image below.</strong>
    </p>
    <p align="center">
      <img src="/docs/images/foto6.png " alt="Image from Battlelist sort"  width="300" />
    </p><br />
    <p align="center">
      <strong>Set your BattleList to sort Ascending by distance.</strong>
    </p><br />
    <strong>Final Setup - Resolution</strong><br />
    <ul>
      <li>This SDK only Support 1920 x 1080 pixels.</li>
      <li>For the next step to complete, you need to do all the menu setup before getting here.</li>
      <li>For SDK work you need to reduce tibia original scale by one like you see on gif below.</li>
    </ul>
    <p align="center">
      <img src="/docs/images/gif1.gif" alt="gif from resolution"  width="600" />
    </p>
  </details>

# ⌨ Development

## ⚙ Running the app

```bash
# main file to track basic functions output like(is burning, has helmet equipped, etc)
python main.py

# to test last experiments with mess code
python test.py
```

# ✅ TODO

- Add python typings
- Add way to make unit tests
- Add way to make e2e tests into the tibia client

# 👷 Authors

- [**lucasmonstro**](http://github.com/lucasmonstro)([**linkedin**](https://www.linkedin.com/in/lucasmonstro/)) - Owner & Developer
- [**augustocrmattos**](http://github.com/augustocrmattos)([**linkedin**](https://www.linkedin.com/in/augustocrmattos/)) - Developer
- [**GuizinhoYT**](http://github.com/GuizinhoYT)([**linkedin**](https://www.linkedin.com/in/guilherme-gra%C3%A7a-3953231a2/)) - Tester
- [**lelec0**](https://github.com/lelec0)([**linkedin**](https://www.linkedin.com/in/max-miranda/)) - Developer

See also the list of [contributors](../../graphs/contributors) who participated
in this project.

# ❤️ Development inspiration

A special thanks to [**Murilo Chianfa**](https://github.com/MuriloChianfa), the owner of [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12). I started this bot to learn python and especially overcome [**TibiaAuto12**](https://github.com/MuriloChianfa/TibiaAuto12) slowdowns.

# 📝 License

Copyright © 2021 [**lucasmonstro**](https://github.com/lucasmonstro)  
This project is [MIT](https://opensource.org/licenses/MIT) licensed
