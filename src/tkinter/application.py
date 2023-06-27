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

        self.tabControl = ttk.Notebook(self)

        self.configPage = ConfigPage(self.tabControl)
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
        pass
        # if event.widget == self:
        #     print('Janela principal recebeu foco')
