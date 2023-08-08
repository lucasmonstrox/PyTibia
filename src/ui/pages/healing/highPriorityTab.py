import tkinter as tk
from .healthFoodCard import HealthFoodCard
from .manaFoodCard import ManaFoodCard


class HighPriorityTab(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.context = context
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.healthFoodCard = HealthFoodCard(self, context)
        self.healthFoodCard.grid(column=0, row=0, padx=10,
                                 pady=10, sticky='nsew')

        self.manaFoodCard = ManaFoodCard(self, context)
        self.manaFoodCard.grid(column=1, row=0, padx=10,
                               pady=10, sticky='nsew')
