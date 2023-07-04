import tkinter as tk
from tkinter import ttk
from .highPriorityTab import HighPriorityTab
from .potionsTab import PotionsTab
from .spellsTab import SpellsTab


class HealingPage(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
        self.tabControl = ttk.Notebook(self)

        self.highPriorityTab = HighPriorityTab(self.tabControl, self.context)
        self.potionsTab = PotionsTab(self.tabControl, self.context)
        self.spellsTab = SpellsTab(self.tabControl, self.context)

        self.tabControl.add(self.highPriorityTab, text='High Priority')
        self.tabControl.add(self.potionsTab, text='Potions')
        self.tabControl.add(self.spellsTab, text='Spells')
        self.tabControl.pack(expand=1, fill='both')
