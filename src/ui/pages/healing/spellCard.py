# import re
import tkinter as tk
from tkinter import ttk


class SpellCard(tk.LabelFrame):
    def __init__(self, parent, context, healingType, title=''):
        super().__init__(parent, padx=10, pady=10, text=title)
        self.context = context
        self.text = title
        self.healingType = healingType
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=7)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.checkVar = tk.BooleanVar()
        self.checkVar.set(self.context.context['healing']
                          ['spells'][healingType]['enabled'])
        self.checkbutton = tk.Checkbutton(
            self, text='Enabled', variable=self.checkVar, command=self.onToggleCheckButton)
        self.checkbutton.grid(column=1, row=0, sticky='e')

        self.spellsLabel = tk.Label(
            self, text='Spell:')
        self.spellsLabel.grid(column=0, row=1, sticky='nsew')

        self.spellsCombobox = ttk.Combobox(
            self, values=['exura infir ico', 'exura ico', 'exura med ico', 'exura gran ico'], state='readonly')
        if self.context.enabledProfile is not None:
            self.spellsCombobox.set(
                self.context.enabledProfile['config']['healing']['spells'][healingType]['spell'])
        self.spellsCombobox.bind(
            "<<ComboboxSelected>>", self.onChangeSpell)
        self.spellsCombobox.grid(column=1, row=1, sticky='ew')

        self.hpPercentageLessThanOrEqualLabel = tk.Label(
            self, text='HP % less than or equal:')
        self.hpPercentageLessThanOrEqualLabel.grid(
            column=0, row=2, sticky='nsew')

        self.hpLessThanOrEqualVar = tk.IntVar()
        self.hpLessThanOrEqualVar.set(self.context.context['healing']
                                      ['spells'][healingType]['hpPercentageLessThanOrEqual'])
        self.hpLessThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                resolution=10, orient=tk.HORIZONTAL, variable=self.hpLessThanOrEqualVar, command=self.onChangeHp)
        self.hpLessThanOrEqualSlider.grid(column=1, row=2, sticky='ew')

        self.manaPercentageGreaterThanOrEqualLabel = tk.Label(
            self, text='Mana % greater than or equal:')
        self.manaPercentageGreaterThanOrEqualLabel.grid(
            column=0, row=3, sticky='nsew')

        self.manaPercentageGreaterThanOrEqualVar = tk.IntVar()
        self.manaPercentageGreaterThanOrEqualVar.set(self.context.context['healing']
                                                     ['spells'][healingType]['manaPercentageGreaterThanOrEqual'])
        self.manaPercentageGreaterThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                               resolution=10, orient=tk.HORIZONTAL, variable=self.manaPercentageGreaterThanOrEqualVar, command=self.onChangeMana)
        self.manaPercentageGreaterThanOrEqualSlider.grid(
            column=1, row=3, sticky='ew')

    def onToggleCheckButton(self):
        self.context.toggleSpellByKey(
            self.healingType, self.checkVar.get())

    def onChangeSpell(self, _):
        self.context.setSpellName(self.healingType, self.spellsCombobox.get())

    def onChangeHp(self, _):
        self.context.setSpellHpPercentageLessThanOrEqual(
            self.healingType, self.hpLessThanOrEqualVar.get())

    def onChangeMana(self, _):
        self.context.setSpellManaPercentageGreaterThanOrEqual(
            self.healingType, self.manaPercentageGreaterThanOrEqualVar.get())
