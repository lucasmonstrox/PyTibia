# import re
import tkinter as tk


class UturaCard(tk.LabelFrame):
    def __init__(self, parent, context):
        super().__init__(parent, padx=10, pady=10, text='Utura')
        self.context = context
        self.healingType = 'utura'
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=7)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.checkVar = tk.BooleanVar()
        self.checkVar.set(
            self.context.context['healing']['spells']['utura']['enabled'])
        self.checkbutton = tk.Checkbutton(
            self, text='Enabled', variable=self.checkVar, command=self.onToggleCheckButton)
        self.checkbutton.grid(column=1, row=0, padx=10,
                              pady=10, sticky='e')

        self.hpPercentageLessThanOrEqualLabel = tk.Label(
            self, text='HP % less than or equal:')
        self.hpPercentageLessThanOrEqualLabel.grid(
            column=0, row=2, sticky='nsew')

        self.hpLessThanOrEqualVar = tk.IntVar()
        self.hpLessThanOrEqualVar.set(self.context.context['healing']
                                      ['spells']['utura']['hpPercentageLessThanOrEqual'])
        self.hpLessThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                resolution=10, orient=tk.HORIZONTAL, variable=self.hpLessThanOrEqualVar, command=self.onChangeHp)
        self.hpLessThanOrEqualSlider.grid(column=1, row=2, sticky='nsew')

        self.manaPercentageGreaterThanOrEqualLabel = tk.Label(
            self, text='Mana % greater than or equal:')
        self.manaPercentageGreaterThanOrEqualLabel.grid(
            column=0, row=3, sticky='e')

        self.manaPercentageGreaterThanOrEqualVar = tk.IntVar()
        self.manaPercentageGreaterThanOrEqualVar.set(self.context.context['healing']
                                                     ['spells']['utura']['manaPercentageGreaterThanOrEqual'])
        self.manaPercentageGreaterThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                               resolution=10, orient=tk.HORIZONTAL, variable=self.manaPercentageGreaterThanOrEqualVar, command=self.onChangeMana)
        self.manaPercentageGreaterThanOrEqualSlider.grid(
            column=1, row=3, sticky='nsew')

    def onToggleCheckButton(self):
        self.context.toggleSpellByKey(
            self.healingType, self.checkVar.get())

    def onChangeHp(self, _):
        self.context.setSpellHpPercentageLessThanOrEqual(
            self.healingType, self.hpLessThanOrEqualVar.get())

    def onChangeMana(self, _):
        self.context.setSpellManaPercentageGreaterThanOrEqual(
            self.healingType, self.manaPercentageGreaterThanOrEqualVar.get())
