import tkinter as tk


class SwapRingCard(tk.LabelFrame):
    def __init__(self, parent, context):
        super().__init__(parent, padx=10, pady=10, text='Swap ring')
        self.context = context
        self.columnconfigure(0, weight=3)
        self.columnconfigure(1, weight=7)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        self.checkVar = tk.BooleanVar()
        self.checkVar.set(
            self.context.context['healing']['highPriority']['swapRing']['enabled'])
        self.checkbutton = tk.Checkbutton(
            self, text='Enabled', variable=self.checkVar, command=self.onToggleCheckButton)
        self.checkbutton.grid(column=1, row=0, sticky='e')

        self.aaaLabel = tk.Label(self, text='HP % less than or equal:')
        self.aaaLabel.grid(column=0, row=1, sticky='nsew')

        self.hpLessThanOrEqualVar = tk.IntVar()
        self.hpLessThanOrEqualVar.set(
            self.context.context['healing']['highPriority']['swapRing']['tankRing']['hpPercentageLessThanOrEqual'])
        self.hpLessThanOrEqualSlider = tk.Scale(self, from_=10, to=100,
                                                resolution=10, orient=tk.HORIZONTAL, variable=self.hpLessThanOrEqualVar, command=self.onChangeHpLessThanOrEqual)
        self.hpLessThanOrEqualSlider.grid(column=1, row=1, sticky='ew')

        self.bbbLabel = tk.Label(self, text='HP % greater than:')
        self.bbbLabel.grid(column=0, row=2, sticky='nsew')

        self.hpGreaterThanVar = tk.IntVar()
        self.hpGreaterThanVar.set(
            self.context.context['healing']['highPriority']['swapRing']['mainRing']['hpPercentageGreaterThan'])
        self.hpGreaterThanSlider = tk.Scale(self, from_=10, to=100,
                                            resolution=10, orient=tk.HORIZONTAL, variable=self.hpGreaterThanVar, command=self.onChangeHpGreaterThan)
        self.hpGreaterThanSlider.grid(column=1, row=2, sticky='ew')

    def onToggleCheckButton(self):
        self.context.toggleHealingHighPriorityByKey(
            'swapRing', self.checkVar.get())

    def onChangeHpLessThanOrEqual(self, _):
        self.context.setSwapRingHpPercentageLessThanOrEqual(
            self.hpLessThanOrEqualVar.get())

    def onChangeHpGreaterThan(self, _):
        self.context.setSwapRingHpPercentageGreaterThan(
            self.hpGreaterThanVar.get())
