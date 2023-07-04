import tkinter as tk
from .healthPotionCard import HealthPotionCard
from .manaPotionCard import ManaPotionCard


class PotionsTab(tk.Frame):
    def __init__(self, parent, context):
        super().__init__(parent)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.context = context

        self.firstHealthPotionCard = HealthPotionCard(
            self, context, 'firstHealthPotion')
        self.firstHealthPotionCard.grid(column=0, row=0, padx=10,
                                        pady=10, sticky='nsew')

        self.secondHealthPotionCard = HealthPotionCard(
            self, context, 'secondHealthPotion')
        self.secondHealthPotionCard.grid(column=0, row=1, padx=10,
                                         pady=10, sticky='nsew')

        self.thirdHealthPotionCard = HealthPotionCard(
            self, context, 'thirdHealthPotion')
        self.thirdHealthPotionCard.grid(column=0, row=2, padx=10,
                                        pady=10, sticky='nsew')

        self.firstManaPotionCard = ManaPotionCard(
            self, context, 'firstManaPotion')
        self.firstManaPotionCard.grid(column=1, row=0, padx=10,
                                      pady=10, sticky='nsew')

        self.secondManaPotionCard = ManaPotionCard(
            self, context, 'secondManaPotion')
        self.secondManaPotionCard.grid(column=1, row=1, padx=10,
                                       pady=10, sticky='nsew')

        self.thirdManaPotionCard = ManaPotionCard(
            self, context, 'thirdManaPotion')
        self.thirdManaPotionCard.grid(column=1, row=2, padx=10,
                                      pady=10, sticky='nsew')
