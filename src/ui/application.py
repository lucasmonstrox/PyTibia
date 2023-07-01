import tkinter as tk
from tkinter import ttk
from .pages.cavebot.cavebotPage import CavebotPage
from .pages.comboSpells import ComboSpellsPage
from .pages.config import ConfigPage
from .pages.inventory import InventoryPage
from .pages.healing import HealingPage


class Application(tk.Tk):
    def __init__(self, context):
        super().__init__()
        self.context = context
        self.title('PyTibia')
        self.geometry('920x720')
        self.resizable(False, False)

        playPauseMenu = tk.Frame(self)
        playPauseMenu.pack(side=tk.TOP)

        playButton = tk.Button(playPauseMenu, text="Play",
                               command=lambda: self.context.play(), width=10, height=3)
        playButton.pack(side=tk.LEFT, padx=10, pady=10)

        pauseButton = tk.Button(
            playPauseMenu, text="Pause", command=lambda: self.context.pause(), width=10, height=3)
        pauseButton.pack(side=tk.LEFT, padx=10, pady=10)

        self.tabControl = ttk.Notebook(self)

        self.configPage = ConfigPage(self.tabControl, self.context)
        self.inventoryPage = InventoryPage(self.tabControl, self.context)
        self.cavebotPage = CavebotPage(self.tabControl, self.context)
        self.healingPage = HealingPage(self.tabControl)
        self.comboSpellsPage = ComboSpellsPage(self.tabControl)

        self.tabControl.add(self.configPage, text='Configuration')
        self.tabControl.add(self.inventoryPage, text='Inventory')
        self.tabControl.add(self.cavebotPage, text='Cavebot')
        self.tabControl.add(self.healingPage, text='Healing')
        self.tabControl.add(self.comboSpellsPage, text='Combo Spells')

        self.tabControl.pack(expand=1, fill='both')

        self.bind('<FocusIn>', self.focusIn)

    def focusIn(self, event):
        if event.widget == self:
            self.context.pause()
