import tkinter as tk
from .spellCard import SpellCard


class SpellsTab(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.criticalHealingCard = SpellCard(
            self, context, 'criticalHealing', title='Utura gran')
        self.criticalHealingCard.grid(column=0, row=0, padx=10,
                                      pady=10, sticky='nsew')

        self.mediumHealingCard = SpellCard(
            self, context, 'mediumHealing', title='Utura gran')
        self.mediumHealingCard.grid(column=1, row=0, padx=10,
                                    pady=10, sticky='nsew')

        self.lightHealingCard = SpellCard(
            self, context, 'lightHealing', title='Utura gran')
        self.lightHealingCard.grid(column=2, row=0, padx=10,
                                   pady=10, sticky='nsew')

        self.uturaGranCard = SpellCard(
            self, context, 'uturaGran', title='Utura gran')
        self.uturaGranCard.grid(column=0, row=1, padx=10,
                                pady=10, sticky='nsew')

        self.uturaCard = SpellCard(
            self, context, 'utura', title='Utura')
        self.uturaCard.grid(column=1, row=1, padx=10,
                            pady=10, sticky='nsew')

        self.exuraGranIcoCard = SpellCard(
            self, context, 'exuraGranIco', title='Utura')
        self.exuraGranIcoCard.grid(column=2, row=1, padx=10,
                                   pady=10, sticky='nsew')
