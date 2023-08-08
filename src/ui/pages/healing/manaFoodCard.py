import tkinter as tk


class ManaFoodCard(tk.LabelFrame):
    def __init__(self, parent, context):
        super().__init__(parent, padx=10, pady=10, text='Mana food')
        self.context = context
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=7)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.checkVar = tk.BooleanVar()
        self.checkVar.set(
            self.context.context['healing']['highPriority']['manaFood']['enabled'])
        self.checkbutton = tk.Checkbutton(
            self, text='Enabled', variable=self.checkVar, command=self.onToggleCheckButton)
        self.checkbutton.grid(column=1, row=0, sticky='e')

        self.manaPercentageLessThanOrEqualLabel = tk.Label(
            self, text='HP % less than or equal:')
        self.manaPercentageLessThanOrEqualLabel.grid(
            column=0, row=1, sticky='nsew')

        self.manaPercentageLessThanOrEqualVar = tk.IntVar()
        self.manaPercentageLessThanOrEqualVar.set(
            self.context.context['healing']['highPriority']['manaFood']['manaPercentageLessThanOrEqual'])
        self.manaPercentageLessThanOrEqualSlider = tk.Scale(self, from_=0, to=100,
                                                            resolution=10, orient=tk.HORIZONTAL, variable=self.manaPercentageLessThanOrEqualVar, command=self.onChangeMana)
        self.manaPercentageLessThanOrEqualSlider.grid(
            column=1, row=1, sticky='ew')

    def onToggleCheckButton(self):
        self.context.toggleHealingHighPriorityByKey(
            'manaFood', self.checkVar.get())

    def onChangeMana(self, _):
        self.context.setManaFoodHpPercentageLessThanOrEqual(
            self.manaPercentageLessThanOrEqualVar.get())
