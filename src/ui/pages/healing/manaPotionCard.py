# import re
import tkinter as tk


class ManaPotionCard(tk.LabelFrame):
    def __init__(self, parent, context, healthPotionType, title=''):
        super().__init__(parent, text=title)
        self.context = context
        self.healthPotionType = healthPotionType
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=7)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.checkVar = tk.BooleanVar()
        self.checkVar.set(self.context.context['healing']
                          ['potions'][healthPotionType]['enabled'])
        self.checkbutton = tk.Checkbutton(
            self, text='Enabled', variable=self.checkVar, command=self.onToggleCheckButton)
        self.checkbutton.grid(column=1, row=0, padx=10,
                              pady=10, sticky='e')

        self.manaPercentageLessThenOrEqualLabel = tk.Label(
            self, text='Mana % less than or equal:')
        self.manaPercentageLessThenOrEqualLabel.grid(column=0, row=1, padx=10,
                                                     pady=10, sticky='e')

        self.manaPercentageLessThenOrEqualVar = tk.IntVar()
        self.manaPercentageLessThenOrEqualVar.set(self.context.context['healing']
                                                  ['potions'][healthPotionType]['manaPercentageLessThanOrEqual'])
        self.manaPercentageLessThenOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                            resolution=10, orient=tk.HORIZONTAL, variable=self.manaPercentageLessThenOrEqualVar, command=self.onChangeMana)
        self.manaPercentageLessThenOrEqualSlider.grid(column=1, row=1, padx=10,
                                                      pady=10, sticky='nsew')

        # self.hotkeyLabel = tk.Label(
        #     self, text='Hotkey:')
        # self.hotkeyLabel.grid(column=0, row=2, padx=10,
        #                       pady=10, sticky='nsew')

        # self.hotkeyEntryVar = tk.StringVar()
        # self.hotkeyEntryVar.set(self.context.context['healing']
        #                         ['potions'][healthPotionType]['hotkey'])
        # self.hotkeyEntry = tk.Entry(self, textvariable=self.hotkeyEntryVar)
        # self.hotkeyEntry.bind('<Key>', self.onChangeHotkey)
        # self.hotkeyEntry.grid(column=1, row=2, padx=10,
        #                       pady=10, sticky='nsew')

    def onToggleCheckButton(self):
        self.context.toggleHealingPotionsByKey(
            self.healthPotionType, self.checkVar.get())

    def onChangeMana(self, _):
        self.context.setHealthPotionManaPercentageLessThanOrEqual(
            self.healthPotionType, self.manaPercentageLessThenOrEqualVar.get())

    # def onChangeHotkey(self, event):
    #     key = event.char
    #     if key == '\b':
    #         return
    #     if re.match(r'^F[1-9]|1[0-2]$', key) or re.match(r'^[0-9]$', key) or re.match(r'^[a-z]$', key):
    #         self.hotkeyEntry.delete(0, tk.END)
    #         self.context.setHealthPotionHotkeyByKey(self.healthPotionType, key)
    #         return
    #     return 'break'
