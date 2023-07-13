import tkinter as tk
from .spellCard import SpellCard
from .uturaCard import UturaCard
from .uturaGranCard import UturaGranCard


class SpellsTab(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.criticalHealingCard = SpellCard(
            self, context, 'criticalHealing', title='Critical healing')
        self.criticalHealingCard.grid(column=0, row=0, padx=10,
                                      pady=10, sticky='nsew')

        self.lightHealingCard = SpellCard(
            self, context, 'lightHealing', title='Light healing')
        self.lightHealingCard.grid(column=1, row=0, padx=10,
                                   pady=10, sticky='nsew')

        self.uturaCard = UturaCard(self, context)
        self.uturaCard.grid(column=0, row=1, padx=10,
                            pady=10, sticky='nsew')

        self.uturaGranCard = UturaGranCard(
            self, context)
        self.uturaGranCard.grid(column=1, row=1, padx=10,
                                pady=10, sticky='nsew')
