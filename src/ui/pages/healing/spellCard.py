# import re
import tkinter as tk


class SpellCard(tk.LabelFrame):
    def __init__(self, parent, context, healingType, title=''):
        super().__init__(parent, text=title)
        self.context = context
        self.text = title
        self.healingType = healingType
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=7)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        # self.rowconfigure(3, weight=1)

        self.checkVar = tk.BooleanVar()
        self.checkVar.set(self.context.context['healing']
                          ['spells'][healingType]['enabled'])
        self.checkbutton = tk.Checkbutton(
            self, text='Enabled', variable=self.checkVar, command=self.onToggleCheckButton)
        self.checkbutton.grid(column=1, row=0, padx=10,
                              pady=10, sticky='e')

        self.hpPercentageLessThanOrEqualLabel = tk.Label(
            self, text='HP % less than or equal:')
        self.hpPercentageLessThanOrEqualLabel.grid(column=0, row=1, padx=10,
                                                   pady=10, sticky='e')

        self.hpLessThanOrEqualVar = tk.IntVar()
        self.hpLessThanOrEqualVar.set(self.context.context['healing']
                                      ['spells'][healingType]['hpPercentageLessThanOrEqual'])
        self.hpLessThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                resolution=10, orient=tk.HORIZONTAL, variable=self.hpLessThanOrEqualVar, command=self.onChangeHp)
        self.hpLessThanOrEqualSlider.grid(column=1, row=1, padx=10,
                                          pady=10, sticky='nsew')

        self.manaPercentageGreaterThanOrEqualLabel = tk.Label(
            self, text='Mana % greater than or equal:')
        self.manaPercentageGreaterThanOrEqualLabel.grid(column=0, row=2, padx=10,
                                                        pady=10, sticky='e')

        self.manaPercentageGreaterThanOrEqualVar = tk.IntVar()
        self.manaPercentageGreaterThanOrEqualVar.set(self.context.context['healing']
                                                     ['spells'][healingType]['manaPercentageGreaterThanOrEqual'])
        self.manaPercentageGreaterThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                               resolution=10, orient=tk.HORIZONTAL, variable=self.manaPercentageGreaterThanOrEqualVar, command=self.onChangeMana)
        self.manaPercentageGreaterThanOrEqualSlider.grid(column=1, row=2, padx=10,
                                                         pady=10, sticky='nsew')

        # self.hotkeyLabel = tk.Label(
        #     self, text='Hotkey:')
        # self.hotkeyLabel.grid(column=0, row=3, padx=10,
        #                       pady=10, sticky='nsew')

        # self.hotkeyEntryVar = tk.StringVar()
        # self.hotkeyEntryVar.set(self.context.context['healing']
        #                         ['spells'][healingType]['hotkey'])
        # self.hotkeyEntry = tk.Entry(self, textvariable=self.hotkeyEntryVar)
        # self.hotkeyEntry.bind('<Key>', self.onChangeHotkey)
        # self.hotkeyEntry.grid(column=1, row=3, padx=10,
        #                       pady=10, sticky='nsew')

    def onToggleCheckButton(self):
        self.context.toggleSpellByKey(
            self.healingType, self.checkVar.get())

    def onChangeHp(self, _):
        self.context.setSpellHpPercentageLessThanOrEqual(
            self.healingType, self.hpLessThanOrEqualVar.get())

    def onChangeMana(self, _):
        self.context.setSpellManaPercentageGreaterThanOrEqual(
            self.healingType, self.manaPercentageGreaterThanOrEqualVar.get())

    # def onChangeHotkey(self, event):
    #     key = event.char
    #     if key == '\b':
    #         return
    #     if re.match(r'^F[1-9]|1[0-2]$', key) or re.match(r'^[0-9]$', key) or re.match(r'^[a-z]$', key):
    #         self.hotkeyEntry.delete(0, tk.END)
    #         self.context.setSpellHotkeyByKey(self.healingType, key)
    #         return
    #     return 'break'
